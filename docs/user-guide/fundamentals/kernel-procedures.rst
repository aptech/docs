
Kernel Procedures
===============================================

Some calculations cannot be vectorized: a recursion where each value
depends on the one before it, a filter, a simulation, or a likelihood
that updates one observation at a time. In an ordinary procedure, such a
loop runs one GAUSS statement at a time.

Write ``kernel proc`` in place of ``proc``, and GAUSS compiles the
procedure to native code, so loops like these run much faster. You call
a kernel proc exactly as you call any other procedure, and it gives the
same results.

::

    kernel proc (1) = arFilter(e, rho);
        local n, y, t;

        n = rows(e);
        y = zeros(n, 1);
        y[1] = e[1];

        for t(2, n, 1);
            y[t] = rho * y[t-1] + e[t];
        endfor;

        retp(y);
    endp;

    print arFilter(ones(4, 1), 0.5);

::

       1.0000000
       1.5000000
       1.7500000
       1.8750000


A First Example
-----------------------------------------

The conditional variance of a GARCH(1,1) model is a recursion: each
variance depends on the previous variance and the previous residual.
Here is the same procedure written as an ordinary procedure and as a
kernel proc. The only difference is the word ``kernel``.

::

    // An ordinary procedure: GARCH(1,1) conditional variances
    proc (1) = garchVar(e, omega, alpha, beta);
        local n, h, t;
        n = rows(e);
        h = zeros(n, 1);
        h[1] = omega / (1 - alpha - beta);
        for t(2, n, 1);
            h[t] = omega + alpha * e[t-1]^2 + beta * h[t-1];
        endfor;
        retp(h);
    endp;

    // The same procedure as a kernel proc
    kernel proc (1) = garchVarK(e, omega, alpha, beta);
        local n, h, t;
        n = rows(e);
        h = zeros(n, 1);
        h[1] = omega / (1 - alpha - beta);
        for t(2, n, 1);
            h[t] = omega + alpha * e[t-1]^2 + beta * h[t-1];
        endfor;
        retp(h);
    endp;

    rndseed 7365;
    e = rndn(1000, 1);

    h1 = garchVar(e, 0.05, 0.1, 0.85);
    h2 = garchVarK(e, 0.05, 0.1, 0.85);

    print h2[1:5];
    print "Largest difference: " maxc(abs(h1 - h2));

::

       1.0000000
      0.90149385
       1.0552942
       1.0154693
       1.2017871
    Largest difference:        0.0000000

The kernel proc is called the same way, with the same arguments, and
returns the same variances.


When to Use a Kernel Proc
-----------------------------------------

Use ``kernel proc`` for code built around loops. For code that is
already vectorized, an ordinary proc is usually as fast or faster.

Good candidates are procedures that:

- compute each value from the previous ones, such as filters, ARMA and
  GARCH recursions, and Kalman filters;
- loop over observations to build a likelihood;
- run simulations element by element;
- are called many times, for example by an optimizer.

A procedure whose work is done by a few large matrix operations, such as
``inv(x'x) * x'y``, already runs in optimized code and does not need to
be a kernel proc.


When GAUSS Compiles a Kernel Proc
-----------------------------------------

GAUSS compiles a kernel proc when it reads the definition, before your
program starts running.

GAUSS keeps the compiled code. When you run the program again, in the
same session or a later one, GAUSS reuses it and starts sooner. When
you change the procedure, GAUSS compiles it again.

There is nothing to set up, and GAUSS shows no messages unless
something in the procedure is not supported (see
`When Something Is Not Supported`_).


Dataframe Arguments
-----------------------------------------

A kernel proc takes dataframes, such as data loaded with :func:`loadd`,
and returns the same values, column names, types and labels as the
same procedure written with ``proc``.

::

    kernel proc (1) = demean(x);
        retp(x - meanc(x)');
    endp;

    kernel proc (1) = garchVarK(e, omega, alpha, beta);
        local n, h, t;
        n = rows(e);
        h = zeros(n, 1);
        h[1] = omega / (1 - alpha - beta);
        for t(2, n, 1);
            h[t] = omega + alpha * e[t-1]^2 + beta * h[t-1];
        endfor;
        retp(h);
    endp;

    // Load inflation and wage growth as a dataframe
    d = loadd(getGAUSSHome("examples/df_returns.gdat"));

    // The result is a dataframe with the same column names
    r = demean(d);
    head(r);

    // A dataframe column can be passed directly
    h = garchVarK(r[., "rcpi"], 1e-5, 0.1, 0.85);
    print h[1:3];

::

                rcpi             rcoe
       -0.0055190058    -0.0049884150
         0.024692194    -0.0058924150
         0.015501194      0.015061585
       -0.0053117058     0.0097415850
         0.018135194    -0.0044594150
       0.00020000000
       0.00018304594
       0.00022655950

``demean`` returns a dataframe because ``x - meanc(x)'`` keeps the
column names of ``x``, as it does in an ordinary procedure.
``garchVarK`` builds its result with :func:`zeros`, so it returns a
plain matrix, again as an ordinary procedure would.


What a Kernel Proc Can Contain
-----------------------------------------

A kernel proc is written like any other procedure, using the parts of
the language listed below.

Arguments and results
+++++++++++++++++++++++++++++++++

- Arguments can be real matrices, real scalars and dataframes, up to
  32 of them.
- A kernel proc returns 1 to 32 real matrices or scalars, or a
  dataframe as described in `Dataframe Arguments`_.
- Both forms of the ``proc`` statement work:
  ``kernel proc (2) = f(x, y);`` and ``kernel proc f(x);``.

Variables
+++++++++++++++++++++++++++++++++

Every variable must be an argument or be declared with ``local``.
A kernel proc cannot read or set global variables; pass the value as an
argument instead.

Statements
+++++++++++++++++++++++++++++++++

- Assignments, including ``{ a, b } = f(x);`` for procedures that
  return more than one value.
- ``for``, ``do while``, ``do until``, ``break`` and ``continue``.
- ``if``, ``elseif`` and ``else``.
- ``retp`` and ``call``.

Operators
+++++++++++++++++++++++++++++++++

- Arithmetic: ``+``, ``-``, ``*``, ``/``, ``%``, ``^``, ``.*``, ``./``,
  ``.^``, transpose ``'``, and concatenation ``~`` and ``|``.
- Comparisons: ``==``, ``/=``, ``!=``, ``<``, ``<=``, ``>``, ``>=``,
  ``eq``, ``ne``, ``lt``, ``le``, ``gt``, ``ge``, and their dot forms
  such as ``.<`` and ``.ge``.
- Logical: ``and``, ``or``, ``not``, ``.and``, ``.or``, ``.not``,
  ``.xor`` and ``.eqv``.

Indexing
+++++++++++++++++++++++++++++++++

- ``x[i]``, ``x[i, j]``, ``x[., j]`` and ``x[i, .]``.
- Ranges such as ``x[2:5, .]`` and ``x[1:2:9, .]``.
- An index vector held in a variable, such as ``x[idx, .]``.
- Assignment to any of these forms, such as ``y[t] = ...``.

Use ``.`` for all rows or columns. An index of 0 is not supported.

Built-in functions
+++++++++++++++++++++++++++++++++

A kernel proc can call these GAUSS functions:

:func:`abs`, ``acos``, ``asin``, :func:`atan`, :func:`cdfbvn`, :func:`cdfchic`, :func:`cdfn`, :func:`cdftvn`, :func:`ceil`, :func:`chol`, :func:`cols`, :func:`cos`, :func:`cumsumc`, :func:`delif`, :func:`det`, :func:`diag`, :func:`diagrv`, :func:`exp`, :func:`eye`, :func:`floor`, :func:`inv`, :func:`invpd`, :func:`ismiss`, :func:`lag1`, :func:`lagn`, :func:`ln`, :func:`lnsumexp`, :func:`log`, :func:`maxc`, :func:`maxindc`, :func:`meanc`, :func:`median`, :func:`minc`, :func:`minindc`, :func:`miss`, :func:`missrv`, :func:`moment`, :func:`ones`, :func:`pdfn`, :func:`prodc`, :func:`recserar`, :func:`reshape`, :func:`rev`, :func:`round`, :func:`rows`, :func:`scalmiss`, :func:`selif`, :func:`seqa`, :func:`shiftc`, :func:`sin`, :func:`sortc`, :func:`sqrt`, :func:`stdc`, :func:`submat`, :func:`substute`, :func:`sumc`, :func:`sumr`, :func:`tan`, :func:`trimr`, :func:`trunc`, :func:`vec`, :func:`zeros`.

Calling other procedures
+++++++++++++++++++++++++++++++++

- A kernel proc can call other kernel procs, including itself. These
  calls run as native code too.
- A kernel proc can call ordinary procedures and procedures from the
  GAUSS libraries, which run as usual. Their results must be real
  matrices or scalars.


When Something Is Not Supported
-----------------------------------------

When GAUSS reads the definition
+++++++++++++++++++++++++++++++++

If a kernel proc uses something not listed above, GAUSS runs it as an
ordinary procedure and prints a warning that says why. Your
program still runs and gives the same results, without the speed-up.

::

    scale = 2;

    kernel proc (1) = scaled(x);
        retp(scale * x);
    endp;

    print scaled(3);

::

    Warning: kernel proc compiled as regular proc (JIT unavailable: validation error: line 4: undeclared variable 'scale'
    )
           6.0000000

Here ``scale`` is a global variable. Pass it as an argument, as in
``scaled(x, scale)``, and the procedure is compiled to native code.

Common reasons for this warning are:

- a global variable;
- a string, or a ``print`` statement;
- a matrix written out in braces, such as ``{ 1 2, 3 4 }``, or an
  index list such as ``x[1 3, .]``;
- a built-in GAUSS function that is not in the list above;
- a function pointer argument (``local f:proc;``);
- ``...`` in the kernel proc's own argument list;
- ``kernel proc (0)``: a kernel proc must return at least one value.

When the procedure runs
+++++++++++++++++++++++++++++++++

A few cases can only be found when the procedure is called. The call
stops with an error that says what is not supported. For example:

::

    kernel proc (1) = firstCol(x);
        retp(x[0, 1]);
    endp;

    x = { 1 2, 3 4 };
    print firstCol(x);

::

    error G0745 : Kernel proc runtime error 'kernel proc firstCol, line 2: index 0 (all elements) is not supported in kernel procs; use . for all'

The cases are:

- **An index of 0.** Use ``.`` for all rows or columns:
  ``x[., 1]``.
- **A call to a procedure that returns a structure.** For example, a
  procedure declared ``proc (struct myResults) = f(x);`` stops with
  ``the ordinary proc f returns a structure as result 1, which a kernel
  proc does not take back``. Call it from ordinary code and pass the
  members you need to the kernel proc.
- **A call to a procedure with named options**, such as
  ``proc f(x, scale=1, ...);``. Call it from ordinary code.
- **An argument that is not a real matrix, scalar or dataframe**, such
  as a string or a structure:
  ``error G0165 : Type mismatch or missing arguments 'kernel proc: expected a real matrix or real scalar'``.
- **An empty matrix** (``{}``) as an argument.
- **A call from a thread** started with :doc:`threadBegin </threadbegin>` or ``threadfor``.

Saved programs
+++++++++++++++++++++++++++++++++

A kernel proc saved with ``compile`` or :doc:`saveall </saveall>` does not keep its
native code. After :doc:`use </use>`, calling it stops with
``error G0293 : Procedure has no definition``. Run or ``#include`` the
source file that defines it instead.


Results
-----------------------------------------

A kernel proc gives the same results as the same procedure written with
``proc``, with the same missing values and the same shapes. In some
calculations, the last one or two digits can differ, as they can
between two computers.


Libraries
-----------------------------------------

Kernel procs can be kept in library source files and listed in a library
with :doc:`lib </lib>`, like any other procedure. ``library mylib;`` makes
them available, and they run as native code.

.. seealso:: :doc:`/user-guide/fundamentals/procedures`, :doc:`proc </proc>`, :doc:`/user-guide/advanced/performance`, :func:`loadd`, :doc:`retp </retp>`, :doc:`local </local>`
