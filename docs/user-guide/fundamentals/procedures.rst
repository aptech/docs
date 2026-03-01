
Procedures and Keywords
===============================================

As your GAUSS programs grow, you will find yourself repeating the same
calculations — standardizing columns, computing test statistics, or
formatting output. Procedures let you package a computation into a
reusable, self-contained unit that you write once and call wherever you
need it. They keep programs organized, make code easier to test, and let
you build on your own (and others') previous work.

::

    // Define a procedure that standardizes a column vector
    proc (1) = standardize(x);
        local mu, sd;

        mu = meanc(x);
        sd = stdc(x);

        retp((x - mu) ./ sd);
    endp;

    // Use it like a built-in function
    income = loadd(getGAUSSHome("examples/credit.dat"), "Income");
    income_std = standardize(income);

    head(income_std);

This page covers everything you need to write, call, and compose
procedures in GAUSS, including the function pointer pattern used
throughout the GAUSS runtime library and the related ``keyword``
construct.


Defining Procedures
-----------------------------------------

A procedure definition has four parts:

1. **Declaration** -- the ``proc`` statement that names the procedure,
   its return count, and its parameters.
2. **Local variables** -- optional ``local`` statements that create
   variables visible only inside the procedure.
3. **Body** -- any GAUSS statements needed to do the work.
4. **Return** -- the :func:`retp` statement that sends results back to
   the caller, followed by ``endp`` to close the definition.

The simplest possible procedure
+++++++++++++++++++++++++++++++++

::

    proc (1) = square(a);
        retp(a .* a);
    endp;

    // Call it
    print square(5);

::

    25.000000

The ``(1)`` after ``proc`` tells GAUSS this procedure returns one value.
The name follows the ``=`` sign, and the parameter list is in
parentheses.

The proc statement
+++++++++++++++++++++++++++++++++

The general form is:

::

    proc (rets) = name(arg1, arg2, ..., argN);

- **rets** -- number of values returned (0 to 1023). Default is 1.
  Use ``(0)`` for side-effect-only procedures.
- **name** -- up to 32 characters, starting with a letter or underscore.
- **arg1 ... argN** -- parameter names, local to this procedure. Up to
  1023 parameters are allowed.

.. note::

    Procedure definitions cannot be nested. You cannot define a ``proc``
    inside another ``proc``.


Local Variables
-----------------------------------------

The ``local`` statement declares variables that exist only while the
procedure is executing. Once the procedure returns, its locals disappear.

::

    proc (1) = hypotenuse(a, b);
        local c;

        c = sqrt(a^2 + b^2);

        retp(c);
    endp;

    print hypotenuse(3, 4);

::

    5.0000000

Why local variables matter
+++++++++++++++++++++++++++++++++

Without ``local``, any variable you assign inside a procedure becomes
a **global** variable, visible everywhere. This leads to subtle bugs
when two procedures accidentally share the same variable name. Always
declare intermediates as ``local``:

::

    proc (1) = ols_beta(x, y);
        local xpx_inv, b;

        xpx_inv = invpd(x'x);
        b = xpx_inv * (x'y);

        retp(b);
    endp;

.. warning::

    ``local`` can only be used inside a procedure. It is not valid at
    global scope.

Key rules for locals
+++++++++++++++++++++++++++++++++

- The ``local`` statement does **not** initialize variables. You must
  assign a value before reading them, or GAUSS will raise a
  ``Variable not initialized`` error.
- Parameters listed in the ``proc`` statement are automatically local.
  You do not need to redeclare them.
- Local variables are dynamically sized. They can change dimensions
  during execution.
- You can have multiple ``local`` statements in the same procedure.


Returning Values
-----------------------------------------

The :func:`retp` statement sends results back to the caller. The number
of values in the :func:`retp` must match the return count declared in
the ``proc`` statement.

Single return
+++++++++++++++++++++++++++++++++

::

    proc (1) = cube(x);
        retp(x .* x .* x);
    endp;

    y = cube(3);
    print y;

::

    27.000000

Multiple returns
+++++++++++++++++++++++++++++++++

Procedures can return up to 1023 values. Declare the count in
``proc (N)`` and return all values in a single :func:`retp`:

::

    proc (3) = summary_stats(x);
        local mu, sd, n;

        mu = meanc(x);
        sd = stdc(x);
        n = rows(x);

        retp(mu, sd, n);
    endp;

    // Capture all three returns with braces
    { mu, sd, n } = summary_stats(rndn(100, 1));

    print "Mean:" mu;
    print "Std Dev:" sd;
    print "N:" n;

The caller uses curly braces ``{ ... }`` to capture multiple returns.

.. tip::

    The return values of one procedure can be passed directly as
    arguments to another procedure. For example, if ``procA`` returns
    two values and ``procB`` takes two arguments:

    ::

        y = procB(procA(x));

No return value
+++++++++++++++++++++++++++++++++

If the procedure performs only side effects (printing, writing files),
declare ``(0)`` returns. The ``endp`` statement generates an implicit
:func:`retp` with no arguments, so you can omit the :func:`retp`
entirely:

::

    proc (0) = print_header(title);
        print "============================";
        print title;
        print "============================";
    endp;

    print_header("Regression Results");

Multiple retp statements
+++++++++++++++++++++++++++++++++

A procedure can have more than one :func:`retp`, for example inside
conditional branches. Every :func:`retp` must return the same number
of items declared in the ``proc`` statement:

::

    proc (1) = safe_log(x);
        if x <= 0;
            retp(miss());
        endif;

        retp(ln(x));
    endp;


Calling Procedures
-----------------------------------------

Procedures are called exactly like built-in functions:

::

    // No return -- side-effect only
    print_header("My Report");

    // One return
    y = square(5);

    // Multiple returns
    { mu, sd, n } = summary_stats(x);

Arguments can be expressions of any complexity, including calls to
other procedures:

::

    y = cube(square(2) + 1);   // cube(4 + 1) = 125

The call statement
+++++++++++++++++++++++++++++++++

If a procedure returns values but you want to discard them, use
``call``:

::

    // Run a regression but discard the output structure
    call olsmt(getGAUSSHome("examples/credit.dat"), "Limit ~ Income + Rating");

This works for any procedure, including those that return multiple
values.


Optional Arguments
-----------------------------------------

GAUSS supports optional arguments through the ``...`` (ellipsis) syntax
and the :func:`dynargsGet` function. This is the standard pattern for
writing procedures that accept both required and optional inputs with
sensible defaults.

Basic pattern
+++++++++++++++++++++++++++++++++

Add ``...`` as the last parameter. Inside the procedure, call
:func:`dynargsGet` with an index range and default values:

::

    proc (1) = compute_area(length, ...);
        local width;

        // If a second argument was passed, use it.
        // Otherwise, default to 'length' (a square).
        width = dynargsGet(1, length);

        retp(length * width);
    endp;

    print compute_area(5);      // Square: 25
    print compute_area(5, 3);   // Rectangle: 15

::

    25.000000
    15.000000

Multiple optional arguments
+++++++++++++++++++++++++++++++++

Use a 2x1 index vector in :func:`dynargsGet` to request a range of
optional arguments. Provide one default for each:

::

    proc (1) = weighted_mean(x, ...);
        local w, trim_pct;

        // Dynamic arguments 1 and 2, with defaults
        { w, trim_pct } = dynargsGet(1|2, ones(rows(x), 1), 0);

        if trim_pct > 0;
            // Trim extreme values
            local lo, hi, mask;
            lo = quantile(x, trim_pct / 2);
            hi = quantile(x, 1 - trim_pct / 2);
            mask = (x .>= lo) .and (x .<= hi);
            x = selif(x, mask);
            w = selif(w, mask);
        endif;

        retp(sumc(w .* x) / sumc(w));
    endp;

    data = rndn(100, 1);

    // Use all defaults
    m1 = weighted_mean(data);

    // Custom weights, default trim
    m2 = weighted_mean(data, ones(100, 1) * 2);

    // Custom weights and 10% trim
    m3 = weighted_mean(data, ones(100, 1), 0.10);

Real-world example from the GAUSS runtime library
++++++++++++++++++++++++++++++++++++++++++++++++++++

The built-in :func:`lag` function uses this pattern:

::

    proc lag(x, ...);
        local n_lags, fill;

        { n_lags, fill } = dynargsGet(1|2, 1, miss());

        retp(shiftc(x, n_lags, fill));
    endp;

This lets users call ``lag(x)`` (lag by 1, fill with missing),
``lag(x, 3)`` (lag by 3, fill with missing), or
``lag(x, 3, 0)`` (lag by 3, fill with zero).

Checking the argument count
+++++++++++++++++++++++++++++++++

Use :func:`dynargsCount` when you need to branch based on how many
optional arguments were provided, rather than using defaults:

::

    proc (1) = flexible_stat(x, ...);
        local n_args;

        n_args = dynargsCount();

        if n_args == 1;
            // One optional arg: interpret as quantile level
            local q;
            q = dynargsGet(1);
            retp(quantile(x, q));
        endif;

        // Default: return the mean
        retp(meanc(x));
    endp;


Function Pointers
-----------------------------------------

GAUSS lets you pass procedures as arguments to other procedures. This
is essential for optimization, numerical integration, and any routine
that needs to call a user-supplied function.

The pattern has three steps:

1. Prefix the procedure name with ``&`` when passing it.
2. Inside the receiving procedure, declare the local variable first
   as a plain local (to receive the pointer), then redeclare it with
   ``:proc`` (to call it as a procedure).
3. Call the local as if it were a regular procedure.

Basic example
+++++++++++++++++++++++++++++++++

::

    // A procedure that applies any function to data, then sums
    proc (1) = apply_and_sum(&f, x);
        local f:proc;

        retp(sumc(f(x)));
    endp;

    // Wrap a built-in function so it can be passed with &
    proc (1) = mySqrt(x);
        retp(sqrt(x));
    endp;

    x = { 4, 9, 16, 25 };
    result = apply_and_sum(&mySqrt, x);
    print result;

::

    14.000000

.. warning::

    The ``&`` operator only works with **user-defined GAUSS procedures**.
    It does not work with built-in C-level functions such as ``sqrt``,
    ``ln``, or ``abs``. To pass a built-in, wrap it in a one-line
    procedure as shown in the ``mySqrt`` example above.

.. note::

    **Why** ``local f:proc;`` **is needed:** GAUSS compiles code before
    running it. When the compiler sees ``f(x)`` inside the procedure, it
    needs to know that ``f`` is a callable procedure, not a matrix. The
    ``:proc`` declaration provides that information.

    When a procedure receives a function pointer through its ``&``
    parameter, you only need ``local f:proc;``. The two-step pattern
    is needed when loading a pointer from a variable or array at runtime:

    ::

        // Case 1: & parameter -- just declare :proc
        proc (1) = my_func(&f, x);
            local f:proc;
            retp(f(x));
        endp;

        // Case 2: pointer from a variable or array
        proc (1) = dispatch(func_array, i, x);
            local f;
            f = func_array[i];
            local f:proc;
            retp(f(x));
        endp;

Passing user-defined procedures
+++++++++++++++++++++++++++++++++

You can pass any procedure, not just built-ins:

::

    proc (1) = myMax(x, y);
        if x > y;
            retp(x);
        else;
            retp(y);
        endif;
    endp;

    proc (1) = myMin(x, y);
        if x < y;
            retp(x);
        else;
            retp(y);
        endif;
    endp;

    // A procedure that takes a comparison function
    proc (1) = reduce(&op, x);
        local op:proc;

        local result, i;
        result = x[1];

        for i(2, rows(x), 1);
            result = op(result, x[i]);
        endfor;

        retp(result);
    endp;

    data = { 3, 7, 2, 9, 1 };

    print "Max:" reduce(&myMax, data);
    print "Min:" reduce(&myMin, data);

::

    Max:       9.0000000
    Min:       1.0000000

Indexing into a vector of function pointers
++++++++++++++++++++++++++++++++++++++++++++++

You can store multiple function pointers in a vector and select one
at runtime:

::

    // Assume f1, f2, f3 are already defined
    procVec = &f1 ~ &f2 ~ &f3;

    proc (1) = dispatch(x, i);
        local f;
        f = procVec[i];
        local f:proc;

        retp(f(x));
    endp;

The double ``local`` pattern -- first as a matrix to do the indexing,
then as ``:proc`` to make it callable -- is the key to this technique.


Keywords
-----------------------------------------

A **keyword** is a special type of subroutine that takes exactly one
string argument and returns nothing. Keywords are defined with the
``keyword`` statement instead of ``proc``.

::

    keyword show_file(s);
        local fname;

        if s $== "";
            print "Usage: show_file <filename>";
            retp;
        endif;

        fname = strtriml(strtrimr(s));
        print "Showing: " fname;

        // Load and preview the file
        print head(loadd(fname));
    endp;

Calling a keyword
+++++++++++++++++++++++++++++++++

Keywords are called without parentheses. Everything after the keyword
name up to the semicolon is passed as one string:

::

    show_file mydata.csv;

If called with nothing, the argument is a null string:

::

    show_file;

Keywords vs. procedures
+++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 30 35 35
    :header-rows: 1

    * - Feature
      - ``proc``
      - ``keyword``

    * - Arguments
      - 0 to 1023, typed
      - Exactly 1, always a string

    * - Return values
      - 0 to 1023
      - None

    * - Call syntax
      - ``name(arg1, arg2)``
      - ``name text here;``

    * - Typical use
      - Computation, transformations
      - Interactive commands, utilities

.. note::

    Keywords are uncommon in modern GAUSS code. For most new work,
    procedures with ``...`` optional arguments are more flexible.


Practical Examples
-----------------------------------------

Example 1: Descriptive statistics procedure
+++++++++++++++++++++++++++++++++++++++++++++

A complete procedure that computes descriptive statistics for a
dataframe column:

::

    proc (1) = describe(x);
        local n, mu, sd, lo, hi;

        n  = rows(x);
        mu = meanc(x);
        sd = stdc(x);
        lo = minc(x);
        hi = maxc(x);

        print "  N:      " n;
        print "  Mean:   " mu;
        print "  Std:    " sd;
        print "  Min:    " lo;
        print "  Max:    " hi;

        retp(mu);
    endp;

    // Use with real data
    df = loadd(getGAUSSHome("examples/credit.dat"), "Income");
    mu = describe(df);

Example 2: Procedure with optional arguments
+++++++++++++++++++++++++++++++++++++++++++++

A moving average function with configurable window size:

::

    proc (1) = moving_avg(x, ...);
        local window;

        window = dynargsGet(1, 5);   // Default window = 5

        local n, result, i, start_idx;
        n = rows(x);
        result = zeros(n, 1);

        for i(1, n, 1);
            start_idx = maxc(1 | (i - window + 1));
            result[i] = meanc(x[start_idx:i]);
        endfor;

        retp(result);
    endp;

    // Use defaults
    data = rndn(20, 1);
    ma5 = moving_avg(data);

    // Custom 10-period window
    ma10 = moving_avg(data, 10);

Example 3: Function pointers with optional arguments
++++++++++++++++++++++++++++++++++++++++++++++++++++++

A procedure that applies a user-supplied function element-by-element,
with an optional scaling factor:

::

    proc (1) = apply_scaled(&f, x, ...);
        local f:proc;

        local scale;
        scale = dynargsGet(1, 1);   // Default scale = 1

        retp(scale * f(x));
    endp;

    // Wrappers for built-in functions (& requires user-defined procs)
    proc (1) = mySqrt(x);  retp(sqrt(x));  endp;
    proc (1) = myLn(x);    retp(ln(x));    endp;

    x = { 1, 4, 9, 16 };

    result = apply_scaled(&mySqrt, x);
    print "sqrt:" result';

    result = apply_scaled(&myLn, x, 100);
    print "100*ln:" result';

Example 4: Multiple returns with real data
+++++++++++++++++++++++++++++++++++++++++++++

::

    proc (2) = regression_summary(fname, formula);
        struct olsmtOut result;
        result = olsmt(fname, formula);

        retp(result.b, result.stderr);
    endp;

    fname = getGAUSSHome("examples/credit.dat");

    { b, se } = regression_summary(fname, "Limit ~ Income + Rating");

    print "Coefficients:";
    print b;
    print "Standard errors:";
    print se;


Rules and Tips
-----------------------------------------

- **Always declare locals.** Without ``local``, any variable you assign
  inside a procedure becomes global and can collide with variables in
  other procedures or at the top level.

- **local is only valid inside proc/keyword.** You cannot use ``local``
  at global scope. It will produce a compile error.

- **Parameter names are local by default.** The names in the ``proc``
  argument list do not need to be redeclared with ``local``.

- **The return count must match.** If ``proc (2)`` is declared, every
  :func:`retp` must provide exactly 2 values.

- **Procedures are recursive.** A procedure can call itself, but make
  sure there is a base case to prevent infinite recursion.

- **Naming conventions.** GAUSS procedure names are case-insensitive.
  ``MyProc`` and ``myproc`` refer to the same procedure. Use descriptive
  names: ``compute_returns`` is clearer than ``cr``.

- **Procedure definitions cannot be nested.** You cannot define a
  ``proc`` inside another ``proc``.

- **Use dynargsGet for optional arguments.** Rather than checking
  argument counts manually, use :func:`dynargsGet` with defaults. This
  is the standard pattern in the GAUSS runtime library.

- **Use call to discard returns.** If you call a procedure for its
  side effects and want to ignore the return value, prefix the call
  with ``call``.

- **Function pointer order.** When using the ``local fn; fn = &proc;
  local fn:proc;`` pattern, the assignment must come **before** the
  ``:proc`` declaration.

.. tip::

    If you are writing a procedure that might be used inside a formula
    string (for example, as a data transformation in :func:`olsmt`),
    it must accept a single column vector and return a column vector
    of the same length. If GAUSS reports ``Undefined proc``, add
    ``external proc myProc;`` before the formula string call so the
    compiler includes it.


What's Next
-----------------------------------------

- Learn how to organize procedures into reusable library files
  with ``#include``.
- Explore :func:`olsmt`, :func:`glm`, and other estimation functions
  that accept formula strings referencing user-defined procedures.
- Use :func:`dynargsGet` and :func:`dynargsCount` to write flexible
  interfaces.

.. seealso:: Functions :func:`retp`, :func:`dynargsGet`, :func:`dynargsCount`, :func:`dynargsTypes`, :func:`local`, :func:`call`, :func:`olsmt`, :func:`loadd`, :func:`head`
