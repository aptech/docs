.. _control-flow:

Control Flow
===============================================

GAUSS provides several control-flow constructs:
``if``/``elseif``/``else`` for conditional branching, ``for`` for
counted loops, ``do while``/``do until`` for condition-based loops,
and ``threadfor`` for parallel execution. Two helper statements —
``break`` and ``continue`` — give you finer control inside any loop.

.. note::

    In GAUSS, **every statement ends with a semicolon** — including
    ``else;``, ``endif;``, ``endfor;``, and ``endo;``. This is different
    from Python, R, and MATLAB where semicolons are optional or absent.

The examples on this page use common GAUSS functions like
:func:`zeros`, :func:`rows`, :func:`cols`, and :func:`abs`. See the
:doc:`/command-reference` for details on any unfamiliar function.

+-------------------------------+-------------------------------------------------------------+
| Statement                     | Description                                                 |
+===============================+=============================================================+
| ``if`` / ``elseif`` / ``else``| Conditional branching based on scalar expressions.          |
+-------------------------------+-------------------------------------------------------------+
| ``for`` / ``endfor``          | Counted loop with start, stop, and step values.             |
+-------------------------------+-------------------------------------------------------------+
| ``do while`` / ``do until``   | Condition-based loop that runs while (or until) an          |
|                               | expression is true.                                         |
+-------------------------------+-------------------------------------------------------------+
| ``break``                     | Exits the innermost loop immediately.                       |
+-------------------------------+-------------------------------------------------------------+
| ``continue``                  | Skips to the next iteration of the innermost loop.          |
+-------------------------------+-------------------------------------------------------------+
| ``threadfor``                 | Parallel ``for`` loop — iterations may run on               |
|                               | different threads.                                          |
+-------------------------------+-------------------------------------------------------------+
| ``goto``                      | Unconditional jump to a label. Rarely needed;               |
|                               | prefer structured constructs.                               |
+-------------------------------+-------------------------------------------------------------+


Conditional Branching: if / elseif / else
--------------------------------------------

::

    if scalar_expression;
        // runs when expression is nonzero (TRUE)
    elseif scalar_expression;
        // runs when this expression is TRUE
    else;
        // runs when no expression above was TRUE
    endif;

- The expression must evaluate to a **scalar**. It is TRUE if nonzero,
  FALSE if zero. Passing a matrix or vector produces the error
  ``Argument must be scalar``.
- ``elseif`` and ``else`` are optional. You can have as many
  ``elseif`` branches as you need, but at most one ``else``.
- One ``endif`` is required per ``if``.

Example: Sign function
+++++++++++++++++++++++++++++++++

::

    x = -3;

    if x < 0;
        y = -1;
    elseif x > 0;
        y = 1;
    else;
        y = 0;
    endif;

    print y;

This prints:

::

          -1.0000000

.. note::

    The ``print`` statement displays one or more expressions separated
    by spaces: ``print "label" x;`` prints the string, then the value
    of *x*. A double semicolon ``;;`` at the end suppresses the newline
    so the next ``print`` continues on the same line.

Example: Classify a numeric grade
+++++++++++++++++++++++++++++++++++++

::

    score = 82;

    if score >= 90;
        grade = "A";
    elseif score >= 80;
        grade = "B";
    elseif score >= 70;
        grade = "C";
    else;
        grade = "F";
    endif;

    print grade;

This prints:

::

    B

GAUSS tests each ``elseif`` in order and executes the **first** branch
whose expression is TRUE, then jumps to ``endif``.


Counted Loops: for
--------------------------------------------

The ``for`` loop runs a counter from a start value to a stop value,
incrementing by a step each iteration:

::

    for i (start, stop, step);
        // body
    endfor;

- *i* — counter variable name, **strictly local** to the loop. It does
  not affect any global variable with the same name, and it is not
  accessible after the loop ends. If you need the final counter value,
  save it to another variable inside the loop.
- *start*, *stop*, *step* — scalar expressions, evaluated **once** when
  the loop initializes.
- The loop terminates when *i* exceeds *stop* (for positive *step*) or
  falls below *stop* (for negative *step*). If *start* already exceeds
  *stop* (or is already below *stop* for negative *step*), the loop body
  never executes.

.. warning::

    Unlike Python and R, the ``for`` counter does not exist outside
    the loop. ``for i (1, 5, 1); endfor; print i;`` will print
    whatever value ``i`` had *before* the loop, not 5.

Example: Basic counting
+++++++++++++++++++++++++++++++++

::

    for i (1, 4, 1);
        print i;
    endfor;

This prints:

::

       1.0000000
       2.0000000
       3.0000000
       4.0000000

Example: Step by 2
+++++++++++++++++++++++++++++++++

::

    for i (1, 10, 2);
        print i;;
    endfor;

This prints:

::

       1.0000000        3.0000000        5.0000000        7.0000000        9.0000000

Example: Counting down
+++++++++++++++++++++++++++++++++

Use a negative step to count backward:

::

    for i (5, 1, -1);
        print i;;
    endfor;

This prints:

::

       5.0000000        4.0000000        3.0000000        2.0000000        1.0000000

Example: Nested loops — building a matrix
++++++++++++++++++++++++++++++++++++++++++++

::

    x = zeros(3, 4);

    for i (1, rows(x), 1);
        for j (1, cols(x), 1);
            x[i,j] = i * j;
        endfor;
    endfor;

    print x;

This prints:

::

       1.0000000        2.0000000        3.0000000        4.0000000
       2.0000000        4.0000000        6.0000000        8.0000000
       3.0000000        6.0000000        9.0000000        12.000000

.. tip::

    The same result can often be computed without loops using
    element-wise operators::

        // seqa(start, step, n) creates a sequence: {1, 2, 3}
        // ' transposes it to a row: {1, 2, 3, 4}
        // .* is element-wise multiply (broadcasts 3x1 .* 1x4 → 3x4)
        x = seqa(1, 1, 3) .* seqa(1, 1, 4)';

    Vectorized operations are typically much faster than explicit loops.
    See :ref:`when-to-use-loops` below.


Condition-Based Loops: do while / do until
--------------------------------------------

A ``do while`` loop repeats as long as its expression is TRUE (nonzero).
A ``do until`` loop repeats until its expression becomes TRUE — that is,
it continues while the expression is FALSE (zero).

Note that ``do`` loops end with ``endo`` (not ``enddo``).
``for`` loops use ``endfor``, and ``if`` blocks use ``endif``.

::

    // Runs while expression is TRUE
    do while expression;
        // body
    endo;

    // Runs until expression becomes TRUE
    do until expression;
        // body
    endo;

- The condition is checked **at the top** of the loop, before each
  iteration. If the condition is not met on entry, the body never
  executes.
- You must update the loop variable yourself — ``do`` loops do not
  auto-increment a counter.

Example: do while
+++++++++++++++++++++++++++++++++

::

    x = 1;

    do while x <= 5;
        print x;;
        x = x + 1;
    endo;

This prints:

::

       1.0000000        2.0000000        3.0000000        4.0000000        5.0000000

Example: do until
+++++++++++++++++++++++++++++++++

The same result, with the condition inverted:

::

    x = 1;

    do until x > 5;
        print x;;
        x = x + 1;
    endo;

This prints:

::

       1.0000000        2.0000000        3.0000000        4.0000000        5.0000000

Example: Convergence check
+++++++++++++++++++++++++++++++++

``do while`` is especially useful when you don't know the number of
iterations in advance — for example, iterating until convergence:

::

    x = 10;
    tol = 1e-6;
    diff = 1;

    do while diff > tol;
        x_new = (x + 2 / x) / 2;   // Babylonian method for sqrt(2)
        diff = abs(x_new - x);
        x = x_new;
    endo;

    print "sqrt(2) =" x;

This prints:

::

    sqrt(2) =       1.4142136

break and continue
--------------------------------------------

``break`` and ``continue`` work inside both ``for`` and ``do`` loops.

- ``break`` — exits the **innermost** loop immediately. Execution
  continues at the statement after ``endfor`` or ``endo``.
- ``continue`` — skips the rest of the current iteration. In a ``for``
  loop, the counter is incremented and the loop resumes at the top. In a
  ``do`` loop, execution returns to the condition check.

Example: break — find the first negative value
+++++++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 3.1, 2.7, 1.2, -0.8, 4.5 };
    found = 0;

    for i (1, rows(x), 1);
        if x[i] < 0;
            found = i;
            break;
        endif;
    endfor;

    print "First negative at row:" found;

This prints:

::

    First negative at row:       4.0000000

Example: continue — skip missing values
++++++++++++++++++++++++++++++++++++++++++

::

    // A bare . denotes a missing value (like NA in R or NaN in Python)
    x = { 1.2, ., 3.4, ., 5.6, 7.8 };
    total = 0;
    count = 0;

    for i (1, rows(x), 1);
        if ismiss(x[i]);
            continue;
        endif;
        total = total + x[i];
        count = count + 1;
    endfor;

    print "Sum:" total;
    print "Count:" count;
    print "Mean:" (total / count);

This prints:

::

    Sum:       18.000000
    Count:       4.0000000
    Mean:       4.5000000


Parallel Loops: threadfor
--------------------------------------------

The ``threadfor`` loop has the same syntax as ``for`` but distributes
iterations across CPU threads:

::

    threadfor i (start, stop, step);
        // body — iterations may run in any order
    threadendfor;

Key rules:

1. **Iterations may execute in any order.** Do not rely on sequential
   execution.
2. **Indexed assignments** to global variables (e.g., ``x[i] = ...``)
   behave the same as in a standard ``for`` loop — the variable persists
   after the loop.
3. **Non-indexed assignments** inside the loop create temporary
   variables that exist only for the current iteration.
4. ``threadfor`` loops **cannot be nested**.
5. ``break`` and ``continue`` are **not supported** in ``threadfor``.

Example: Fill a vector in parallel
+++++++++++++++++++++++++++++++++++++

::

    x = zeros(5, 1);

    threadfor i (1, 5, 1);
        x[i] = i^2;
    threadendfor;

    print x;

This prints:

::

       1.0000000
       4.0000000
       9.0000000
       16.000000
       25.000000

Example: Parallel bootstrap
+++++++++++++++++++++++++++++++++++++

::

    // loadd loads a dataset; x[., 2] selects all rows of column 2
    fname = getGAUSSHome("examples/fueleconomy.dat");
    x = loadd(fname);
    engine_disp = x[., 2];

    iters = 500;
    nobs = rows(engine_disp);      // number of observations

    // zeros(r, c) creates an r x c matrix of zeros
    sample_means = zeros(iters, 1);

    threadfor i (1, iters, 1);
        // rndu draws uniform random numbers; ceil rounds up
        // idx contains random row indices for resampling
        idx = ceil(nobs * rndu(nobs, 1));
        sample = engine_disp[idx];

        // Indexed assignment — persists after the loop
        // meanc computes the column mean
        sample_means[i] = meanc(sample);
    threadendfor;

    print "Bootstrap mean:" meanc(sample_means);
    print "Bootstrap std: " stdc(sample_means);


.. _when-to-use-loops:

When to Use Loops (and When Not To)
--------------------------------------------

GAUSS is a matrix language. Many operations that require loops in
general-purpose languages can be written as a single matrix expression
in GAUSS. Vectorized expressions are almost always **faster** than
equivalent loops because they run in optimized compiled code.

**Prefer vectorized operations when you can:**

::

    // SLOW: element-wise loop
    y = zeros(rows(x), 1);
    for i (1, rows(x), 1);
        y[i] = x[i]^2;
    endfor;

    // FAST: vectorized equivalent
    y = x .^ 2;

**Loops are appropriate when:**

- Each iteration depends on the previous result (e.g., convergence,
  recursive calculations).
- You need to accumulate results conditionally (e.g., skip rows, early
  exit with ``break``).
- You are iterating over model specifications or file names, not over
  data elements.

.. list-table::
    :widths: 25 35 40
    :header-rows: 1

    * - Task
      - Loop approach
      - Vectorized approach

    * - Square each element
      - ``for`` loop over rows
      - ``x .^ 2``

    * - Column sums
      - ``for`` loop accumulating
      - :func:`sumc` (sum of each column)

    * - Element-wise multiply
      - Nested ``for`` loops
      - ``x .* y``

    * - Find rows matching a condition
      - ``for`` with ``if``
      - :func:`selif` (select rows where condition is true)

Choosing the right loop
+++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 30 20 50
    :header-rows: 1

    * - Situation
      - Use
      - Why

    * - Known number of iterations
      - ``for``
      - Fastest loop; counter is automatic and local

    * - Unknown iterations (convergence, EOF)
      - ``do while``
      - Flexible termination condition

    * - Large independent iterations (CPU-bound)
      - ``threadfor``
      - Distributes work across CPU cores

    * - Small loops, or iterations with dependencies
      - ``for``
      - Threading overhead exceeds benefit for small loops

The ``for`` loop has lower per-iteration overhead than ``do`` and should
be preferred when either could be used.


Unconditional Jump: goto
--------------------------------------------

The ``goto`` statement jumps to a labeled location in the program:

::

    goto label;
    // ... skipped code ...

    label:
    // execution continues here

- A label is any valid GAUSS name followed immediately by a colon.
- Labels do not need to be declared before use.

``goto`` is rarely needed in modern GAUSS code — ``if``/``else``,
``break``, and ``continue`` handle nearly all branching. It is
documented here for completeness and for reading legacy code.


Quick Reference
--------------------------------------------

.. list-table::
    :widths: 25 35 40
    :header-rows: 1

    * - Construct
      - Syntax
      - Terminates with

    * - ``if``
      - ``if expr; ... elseif expr; ... else; ... endif;``
      - ``endif``

    * - ``for``
      - ``for i (start, stop, step); ... endfor;``
      - ``endfor``

    * - ``do while``
      - ``do while expr; ... endo;``
      - ``endo``

    * - ``do until``
      - ``do until expr; ... endo;``
      - ``endo``

    * - ``threadfor``
      - ``threadfor i (start, stop, step); ... threadendfor;``
      - ``threadendfor``


.. seealso:: :doc:`/user-guide/fundamentals/procedures`, :func:`selif`, :func:`delif`, :func:`ismiss`, :func:`sumc`, :func:`meanc`
