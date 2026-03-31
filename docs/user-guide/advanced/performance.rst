Optimizing GAUSS Code for Speed
===============================================

GAUSS is a matrix language. Code that embraces matrix operations instead
of scalar loops can run **20-400x faster** with no extra effort. This
guide covers the techniques that matter most, ordered by impact.


Find Your Bottleneck First
-----------------------------------------

Before optimizing, measure where the time goes::

    // Time a section of code
    t0 = hsec;

    // ... your slow code here ...

    t1 = hsec;
    print "Elapsed:" ((t1 - t0) / 100) "seconds";

Wrap different sections of your program to find which part is actually
slow. Then use this guide to fix it:

1. **Loop that could be a matrix operation?** → :ref:`vectorize-section`
2. **Loop that grows a matrix with** ``|`` **?** → :ref:`preallocate-section`
3. **Loop with expensive independent iterations?** → :ref:`loop-section` (``threadfor``)
4. **Loading more data than you need?** → :ref:`memory-section`


.. _vectorize-section:

Vectorize Everything
-----------------------------------------

This is the single biggest performance lever in GAUSS. Every built-in
function and element-wise operator runs in optimized C/Fortran under the
hood. A scalar loop doing the same work pays the interpreter overhead on
every iteration.

Counting elements that satisfy a condition
+++++++++++++++++++++++++++++++++++++++++++++

**Slow** -- loop with accumulator::

    // Count values where |x| > 1
    // 1,000,000 elements: ~110 ms
    n = rows(x);
    count = 0;
    for i (1, n, 1);
        if abs(x[i, 1]) > 1;
            count = count + 1;
        endif;
    endfor;

**Fast** -- vectorized::

    // Same result: ~6 ms  (18x faster)
    count = sumc(abs(x) .> 1);

The expression ``abs(x) .> 1`` produces a column of 0s and 1s in one
pass. :func:`sumc` totals them. Two operations, zero loop overhead.


Element-wise math
++++++++++++++++++++++

**Slow** -- loop over every element::

    // 1,000,000 rows: ~410 ms
    z = zeros(n, 1);
    for i (1, n, 1);
        z[i, 1] = x[i, 1] * y[i, 1] + x[i, 1] / (abs(y[i, 1]) + 1);
    endfor;

**Fast** -- element-wise operators::

    // Same result: ~12 ms  (33x faster)
    z = x .* y + x ./ (abs(y) + 1);

Use ``.*``, ``./``, ``.^`` for element-wise operations and ``*``, ``/``
for matrix operations. The dot-prefix convention applies to comparisons
too: ``.>``, ``.<``, ``.==``, ``.!=``.


Filtering rows
++++++++++++++++++++

**Slow** -- loop and concatenate matching rows::

    // 100,000 rows x 3 cols: ~710 ms
    result = {};
    for i (1, rows(x), 1);
        if x[i, 1] > 0;
            result = result | x[i, .];
        endif;
    endfor;

**Fast** -- use :func:`selif`::

    // Same result: ~1.6 ms  (440x faster)
    result = selif(x, x[., 1] .> 0);

:func:`selif` selects rows where the condition vector is non-zero.
:func:`delif` does the opposite (deletes matching rows). Both are
single-pass operations.


Summary statistics
++++++++++++++++++++

Use the column-wise built-in functions instead of writing accumulator loops:

==========================  ========================
Loop pattern                Vectorized replacement
==========================  ========================
Sum in a loop               :func:`sumc`
Mean in a loop              :func:`meanc`
Std dev in a loop           :func:`stdc`
Min/max in a loop           :func:`minc` / :func:`maxc`
Product in a loop           :func:`prodc`
Cumulative sum              :func:`cumsumc`
==========================  ========================


.. note::

   For data that approaches available RAM, a single vectorized expression
   can create multiple temporary matrices. If you see disk paging, break
   the expression into steps or process data in chunks.


.. _loop-section:

Loop Optimization
-----------------------------------------

When a loop is unavoidable -- iterative algorithms, simulations with
state, or row-by-row I/O -- these techniques keep it fast.

Use ``for``, not ``do while``
++++++++++++++++++++++++++++++++

The ``for`` loop has a pre-compiled counter. A ``do while`` loop
re-evaluates its condition expression on every iteration.

::

    // for loop: 1,000,000 iterations in ~62 ms
    x = 0;
    for i (1, 1000000, 1);
        x = x + 1;
    endfor;

    // do while: same work in ~164 ms  (2.6x slower)
    x = 0;
    i = 1;
    do while i <= 1000000;
        x = x + 1;
        i = i + 1;
    endo;

Use ``for`` whenever the iteration count is known in advance. The
difference matters most for tight loops with cheap bodies; with
heavy computation per iteration, the overhead gap is negligible.


Use ``threadfor`` for heavy independent work
++++++++++++++++++++++++++++++++++++++++++++++++

When each iteration is computationally expensive and independent of the
others, ``threadfor`` distributes iterations across CPU cores.

::

    // 8 large matrix operations
    y = zeros(8, 1);

    // threadfor: ~370 ms
    threadfor i(1, 8, 1);
        tmp = rndn(1000, 1000);
        y[i] = det(tmp'tmp);
    threadendfor;

    // for: ~2370 ms (6.4x slower)
    for i (1, 8, 1);
        tmp = rndn(1000, 1000);
        y[i] = det(tmp'tmp);
    endfor;

``threadfor`` is most effective when each iteration does substantial
work (matrix factorizations, simulations, optimization). For simple
element-wise math, vectorized operations are faster than any loop.

.. warning::

   ``threadfor`` iterations must be independent -- no iteration can read
   a value written by another. Each iteration should write to its own
   location (e.g., ``y[i]``). Don't use ``threadfor`` when iterations are
   cheap (simple arithmetic) -- the threading overhead will make it slower
   than a plain ``for`` loop.


Minimize work inside tight loops
++++++++++++++++++++++++++++++++++

Move invariant computations outside the loop::

    // Slow: recomputes inv(X'X) every iteration
    for i (1, n_sims, 1);
        b[i, .] = inv(X'X) * X'y[., i];
    endfor;

    // Fast: compute the fixed part once
    XtX_inv_Xt = inv(X'X) * X';
    for i (1, n_sims, 1);
        b[i, .] = XtX_inv_Xt * y[., i];
    endfor;


.. _preallocate-section:

Preallocate, Don't Concatenate
-----------------------------------------

Appending to a matrix with ``|`` or ``~`` inside a loop copies the
entire matrix on every iteration. For *n* iterations, this means
*n(n+1)/2* element copies -- quadratic cost.

**Slow** -- concatenation in a loop::

    // 100,000 iterations: ~914 ms
    y = {};
    for i (1, 100000, 1);
        y = y | i;
    endfor;

**Fast** -- preallocate and fill::

    // Same result: ~15 ms  (62x faster)
    y = zeros(100000, 1);
    for i (1, 100000, 1);
        y[i, 1] = i;
    endfor;

The fix is simple:

1. Allocate the full output matrix with :func:`zeros` before the loop.
2. Write to ``y[i, .]`` inside the loop.

If you don't know the final size in advance, estimate an upper bound,
fill what you need, and trim at the end::

    y = zeros(max_possible, k);
    count = 0;
    for i (1, n, 1);
        if some_condition;
            count = count + 1;
            y[count, .] = result_row;
        endif;
    endfor;

    // Trim to actual size
    y = y[1:count, .];


.. _memory-section:

Memory-Efficient Data Access
-----------------------------------------

Load only the columns you need
+++++++++++++++++++++++++++++++++

Use a formula string with :func:`loadd` to load a subset of columns
directly from disk::

    // Loads all columns into memory
    data = loadd("big_survey.csv");

    // Loads only the columns you need
    data = loadd("big_survey.csv", "Income + Age + Education");

    // Load all except a few columns
    data = loadd("big_survey.csv", ". - RawText - Notes");

When a file has dozens of columns but you only need a few, this reduces
both load time and memory use.


Free memory when done
++++++++++++++++++++++++

Inside a procedure, local variables are freed automatically when the
procedure returns. At global scope, reassign large matrices once they
are no longer needed::

    // Free a large matrix
    raw_data = 0;

This replaces the large matrix with a 1x1 scalar, releasing the memory
immediately.

Inside procedures, use ``local`` to ensure intermediate matrices are
cleaned up on return::

    proc (1) = myEstimate(data);
        local X, y, XtX;

        X = data[., 2:cols(data)];
        y = data[., 1];
        XtX = X'X;

        retp(inv(XtX) * X'y);
    endp;
    // X, y, XtX are all freed when myEstimate returns


Quick Reference
-----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 40 20

   * - Slow Pattern
     - Fast Pattern
     - Speedup
   * - Loop with counter to count matches
     - ``sumc(condition)``
     - ~18x
   * - Loop with element-wise arithmetic
     - Vectorized ``.*``, ``./``, ``.^``
     - ~33x
   * - Loop and concatenate to filter rows
     - ``selif(x, condition)``
     - ~440x
   * - ``do while`` with known iteration count
     - ``for i (1, n, 1)``
     - ~2.6x
   * - Sequential ``for`` over heavy work
     - ``threadfor``
     - ~6x
   * - Concatenation inside a loop (``y = y | row``)
     - Preallocate with ``zeros``, fill by index
     - ~62x
   * - ``loadd`` all columns, subset later
     - Formula string: ``"col1 + col2"``
     - varies
   * - Invariant computation inside loop
     - Hoist computation before loop
     - varies
