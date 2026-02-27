
Introduction to GAUSS for MATLAB Users
======================================

GAUSS and MATLAB are both matrix-based programming languages. If you're comfortable with MATLAB, you'll find GAUSS syntax familiar—but with important differences. This guide covers the key translations.

.. note::

    This guide is written for GAUSS 26. Some features (such as :func:`repmat`, :func:`findIdx`, :func:`diagmat`, and the colon operator for sequences) require GAUSS 26.0.1 or later.

How GAUSS Differs from MATLAB
-----------------------------

GAUSS shares MATLAB's matrix-first philosophy but is oriented around statistics and econometrics rather than engineering. The practical differences that affect your code:

- **Dataframes are matrices**: Named columns and typed variables, but you can do matrix algebra on them directly — no conversion step between "table" and "matrix" types.
- **Column-wise by default**: Statistical functions operate on columns (``meanc``, ``stdc``, ``sumc``), matching the convention that columns are variables and rows are observations.
- **Formula strings for estimation**: Model specification uses ``"y ~ x1 + x2"`` syntax. Categorical variables are handled automatically.
- **Structures for output**: Estimation results are returned in structures with named members (``out.b``, ``out.stderr``), similar to MATLAB structs.

Key Syntax Differences
----------------------

+-------------------+---------------------------+---------------------------+
| Feature           | MATLAB                    | GAUSS                     |
+===================+===========================+===========================+
| Indexing          | 1-based                   | 1-based (same)            |
+-------------------+---------------------------+---------------------------+
| Matrix delimiter  | ``[ ]``                   | ``{ }``                   |
+-------------------+---------------------------+---------------------------+
| Row separator     | ``;`` or newline          | ``,``                     |
+-------------------+---------------------------+---------------------------+
| String quotes     | ``" "`` or ``' '``        | ``" "`` only              |
+-------------------+---------------------------+---------------------------+
| Statement end     | Optional ``;``            | Required ``;``            |
+-------------------+---------------------------+---------------------------+
| All rows/cols     | ``:``                     | ``.``                     |
+-------------------+---------------------------+---------------------------+
| Concatenate horiz | ``[A B]``                 | ``A~B``                   |
+-------------------+---------------------------+---------------------------+
| Concatenate vert  | ``[A; B]``                | ``A|B``                   |
+-------------------+---------------------------+---------------------------+
| Solve ``Ax = b``  | ``A\b``                   | ``b/A``                   |
+-------------------+---------------------------+---------------------------+

Matrix Creation
---------------

.. code-block:: matlab

    % MATLAB
    A = [1 2 3; 4 5 6; 7 8 9]

::

    // GAUSS
    A = { 1 2 3, 4 5 6, 7 8 9 };

**Note:** GAUSS uses braces ``{ }`` and commas between rows. Semicolons end statements, not rows. Unlike MATLAB, newlines are not row separators—you must use commas.

Special matrices:

.. code-block:: matlab

    % MATLAB
    zeros(3,3)
    ones(3,3)
    eye(3)
    rand(3,3)
    randn(3,3)

::

    // GAUSS
    zeros(3, 3);
    ones(3, 3);
    eye(3);
    rndu(3, 3);    // Uniform [0,1]
    rndn(3, 3);    // Standard normal

Sequences:

.. code-block:: matlab

    % MATLAB
    1:5           % Row vector [1 2 3 4 5]
    1:0.5:3       % [1 1.5 2 2.5 3]
    linspace(0,1,5)

::

    // GAUSS
    1:5;                 // Column vector {1, 2, 3, 4, 5} (NOTE: MATLAB gives a row vector)
    1:0.5:3;             // Column vector {1, 1.5, 2, 2.5, 3}
    seqa(1, 1, 5);       // Column vector, start=1, inc=1, n=5
    seqa(0, 0.25, 5);    // Column vector {0, 0.25, 0.5, 0.75, 1}

**Note:** MATLAB's ``linspace(0, 1, 5)`` takes start, end, and count. GAUSS's ``seqa`` takes start, increment, and count — you must compute the step size yourself: ``seqa(0, (1-0)/(5-1), 5)``.

Indexing
--------

Both languages use 1-based indexing, but the "all elements" syntax differs:

.. code-block:: matlab

    % MATLAB
    A(1,1)        % Element
    A(1,:)        % First row
    A(:,1)        % First column
    A(1:2,:)      % Rows 1-2
    A(end,:)      % Last row

::

    // GAUSS
    A[1,1];       // Element
    A[1,.];       // First row (dot = all)
    A[.,1];       // First column
    A[1:2,.];     // Rows 1-2
    A[rows(A),.]; // Last row
    A[.,cols(A)]; // Last column

GAUSS dataframes also support indexing by column name:

::

    data[., "mpg"];              // One column by name
    data[., "mpg" "weight"];    // Multiple columns by name
    data[1:10, "mpg"];          // First 10 rows of mpg

**Key difference:** MATLAB uses ``:`` for "all", GAUSS uses ``.``. Use ``rows(A)`` and ``cols(A)`` where MATLAB uses ``end``.

Operators
---------

Element-wise vs. matrix operations:

.. code-block:: matlab

    % MATLAB
    A * B         % Matrix multiplication
    A .* B        % Element-wise multiplication
    A .^ 2        % Element-wise power
    A'            % Conjugate transpose
    A.'           % Transpose

::

    // GAUSS
    A * B;        // Matrix multiplication (same)
    A .* B;       // Element-wise multiplication (same)
    A .^ 2;       // Element-wise power (same)
    A';           // Conjugate transpose (same as MATLAB)
    A.';          // Non-conjugate transpose (same as MATLAB .')

**Good news:** Element-wise operators (``.* ./ .^``) and transpose operators (``'`` and ``.``) work the same in both languages. For real-valued data, ``A'`` and ``A.'`` are identical, so most code just uses ``A'``.

Concatenation
-------------

.. code-block:: matlab

    % MATLAB
    [A B]         % Horizontal concatenation
    [A; B]        % Vertical concatenation

::

    // GAUSS
    A ~ B;        // Horizontal concatenation (tilde)
    A | B;        // Vertical concatenation (pipe)

Example:

::

    A = { 1 2, 3 4 };
    B = { 5, 6 };

    print A ~ B;   // [1 2 5; 3 4 6]
    print A | B';  // [1 2; 3 4; 5 6]

Linear Algebra
--------------

.. code-block:: matlab

    % MATLAB
    inv(A)
    det(A)
    eig(A)
    [V,D] = eig(A)
    svd(A)
    chol(A)
    rank(A)
    A \ b          % Solve Ax = b

::

    // GAUSS
    inv(A);
    invpd(A);             // Inverse (positive definite, faster)
    det(A);
    eig(A);               // Returns eigenvalues only
    { val, vec } = eigv(A);  // Eigenvalues and vectors
    { u, s, v } = svdcusv(A);
    chol(A);
    rank(A);
    b / A;                // Solve Ax = b

**Solving linear systems:** GAUSS uses the ``/`` operator: ``b / A`` solves ``Ax = b``. Use ``solpd(b, A)`` for positive definite systems or ``olsqr(b, A)`` for QR-based least squares.

Functions and Procedures
------------------------

.. code-block:: matlab

    % MATLAB
    function y = square(x)
        y = x.^2;
    end

::

    // GAUSS
    proc (1) = square(x);
        local y;        // Must declare local variables (see Gotcha #8)
        y = x.^2;
        retp(y);
    endp;

**Key differences:**

- GAUSS uses ``proc`` / ``endp`` instead of ``function`` / ``end``
- Return values use ``retp()`` not assignment
- Number of outputs declared in ``proc (n) =``

Multiple outputs:

.. code-block:: matlab

    % MATLAB
    function [a, b] = myFunc(x)
        a = x + 1;
        b = x - 1;
    end

::

    // GAUSS
    proc (2) = myFunc(x);
        local a, b;
        a = x + 1;
        b = x - 1;
        retp(a, b);
    endp;

    // Call it
    { result1, result2 } = myFunc(5);

Function pointers:

.. code-block:: matlab

    % MATLAB — anonymous functions capture data via closures
    f = @(beta) sum((Y - X*beta).^2);
    result = fminunc(f, x0);

::

    // GAUSS — no anonymous functions; use & to get a pointer to a named proc
    // Extra data arguments are passed after x0
    proc (1) = myObj(beta, Y, X);
        local resid;
        resid = Y - X * beta;
        retp(resid'resid);
    endp;

    struct minimizeOut out;
    out = minimize(&myObj, x0, Y, X);

Control Flow
------------

Loops and conditionals are similar:

.. code-block:: matlab

    % MATLAB
    for i = 1:10
        disp(i)
    end

    if x > 0
        disp('positive')
    elseif x < 0
        disp('negative')
    else
        disp('zero')
    end

::

    // GAUSS
    for i (1, 10, 1);
        print i;
    endfor;

    if x > 0;
        print "positive";
    elseif x < 0;
        print "negative";
    else;
        print "zero";
    endif;

While loops:

.. code-block:: matlab

    % MATLAB
    while x > 0
        x = x - 1;
    end

::

    // GAUSS
    do while x > 0;
        x = x - 1;
    endo;

**Note:** GAUSS requires semicolons after control statements.

Data Import/Export
------------------

.. code-block:: matlab

    % MATLAB
    data = readtable('file.csv');
    data = xlsread('file.xlsx');
    writetable(data, 'output.csv')

::

    // GAUSS - loadd reads CSV, Excel, Stata, SAS, SPSS, HDF5
    data = loadd("file.csv");
    data = loadd("file.xlsx");
    data = loadd("auto2.dta");           // Stata
    data = loadd("survey.sas7bdat");     // SAS

    // Load specific variables with a formula string
    data = loadd("auto2.dta", "mpg + rep78 + price");

    // Load all variables except one
    data = loadd("auto2.dta", ". -rep78");

    // Export
    saved(data, "output.csv");
    saved(data, "output.xlsx");
    saved(data, "output.gdat");          // GAUSS format

Statistics and Econometrics
---------------------------

Basic statistics:

.. code-block:: matlab

    % MATLAB
    mean(x)       % Column means
    std(x)        % Column std devs
    sum(x)        % Column sums
    cov(x)        % Covariance matrix

::

    // GAUSS
    meanc(x);     // Column means
    stdc(x);      // Column std devs
    sumc(x);      // Column sums
    vcx(x);       // Covariance matrix

OLS regression:

GAUSS estimation functions use **formula strings** to specify models: the ``~`` separates the dependent variable (left) from predictors (right), following R-style notation. Results are returned in **structures** — typed containers with named members that you access with dot notation.

.. code-block:: matlab

    % MATLAB (Statistics Toolbox)
    mdl = fitlm(X, y);
    mdl.Coefficients
    mdl.Residuals.Raw

::

    // GAUSS (included in base package)
    struct olsmtOut out;
    out = olsmt(data, "y ~ x1 + x2");

    // Access results through the output structure
    print out.b;          // Coefficient estimates
    print out.stderr;     // Standard errors

Using ``call olsmt(...)`` prints a summary table without saving the results.

Logistic regression (GLM):

.. code-block:: matlab

    % MATLAB (Statistics Toolbox)
    mdl = fitglm(X, y, 'Distribution', 'binomial');

::

    // GAUSS (included in base package)
    struct glmOut out;
    out = glm(data, "admit ~ gre + gpa + rank", "binomial");

Quantile regression:

.. code-block:: matlab

    % MATLAB — no built-in function

::

    // GAUSS (included in base package)
    struct qfitOut out;
    out = quantileFit(data, "y ~ x1 + x2", 0.25 | 0.5 | 0.75);

Common Function Translations
-----------------------------

**Functions with different names:**

+-------------------------+---------------------------+---------------------------+
| Description             | MATLAB                    | GAUSS                     |
+=========================+===========================+===========================+
| Natural log             | ``log(x)``                | ``ln(x)``                 |
+-------------------------+---------------------------+---------------------------+
| Log base 10             | ``log10(x)``              | ``log(x)``                |
+-------------------------+---------------------------+---------------------------+
| Sort rows by column     | ``sortrows(x, 1)``        | ``sortc(x, 1)``           |
+-------------------------+---------------------------+---------------------------+
| Find indices            | ``find(x > 0)``           | ``findIdx(x .> 0)``       |
+-------------------------+---------------------------+---------------------------+
| Check NaN               | ``isnan(x)``              | ``ismiss(x)``             |
+-------------------------+---------------------------+---------------------------+
| NaN / missing           | ``NaN``                   | ``.`` (dot)               |
+-------------------------+---------------------------+---------------------------+
| Cumulative sum          | ``cumsum(x)``             | ``cumsumc(x)``            |
+-------------------------+---------------------------+---------------------------+
| Flip rows               | ``flipud(x)``             | ``rev(x)``                |
+-------------------------+---------------------------+---------------------------+
| Create diagonal matrix  | ``diag(v)``               | ``diagmat(v)``            |
+-------------------------+---------------------------+---------------------------+
| Full SVD                | ``[U,S,V] = svd(A)``     | ``{u,s,v} = svdcusv(A)`` |
+-------------------------+---------------------------+---------------------------+
| Number to string        | ``num2str(x)``            | ``ntos(x)``               |
+-------------------------+---------------------------+---------------------------+
| String compare          | ``strcmp(a,b)``           | ``a $== b``               |
+-------------------------+---------------------------+---------------------------+
| String concatenation    | ``strcat(a,b)``           | ``a $+ b``                |
+-------------------------+---------------------------+---------------------------+
| Formatted output        | ``fprintf(fmt, x)``       | ``sprintf(fmt, x)``       |
+-------------------------+---------------------------+---------------------------+

**Functions with the same name:** ``repmat``, ``reshape``, ``unique``, ``abs``, ``exp``, ``ceil``, ``floor``, ``round``, ``rank``, ``inv``, ``det``, ``chol``, ``eye``, ``zeros``, ``ones``

.. note::

    **diag vs diagmat**: MATLAB's ``diag`` both creates and extracts diagonal matrices. In GAUSS, ``diag(A)`` only *extracts* the diagonal. To *create* a diagonal matrix from a vector, use ``diagmat(v)``.

.. warning::

    **log vs ln**: In MATLAB, ``log`` is the natural logarithm. In GAUSS, ``log`` is base 10 and ``ln`` is natural. This will silently give wrong results if you don't catch it.

Quick Reference Cheat Sheet
---------------------------

Things that are different (see sections above for details):

+-------------------------+---------------------------+---------------------------+
| Operation               | MATLAB                    | GAUSS                     |
+=========================+===========================+===========================+
| Matrix literal          | ``[1 2; 3 4]``            | ``{ 1 2, 3 4 }``          |
+-------------------------+---------------------------+---------------------------+
| All rows/cols           | ``A(:,j)``                | ``A[.,j]``                |
+-------------------------+---------------------------+---------------------------+
| Last row                | ``A(end,:)``              | ``A[rows(A),.]``          |
+-------------------------+---------------------------+---------------------------+
| Concatenate             | ``[A B]`` / ``[A; B]``    | ``A~B`` / ``A|B``          |
+-------------------------+---------------------------+---------------------------+
| Solve Ax=b              | ``A\b``                   | ``b/A``                   |
+-------------------------+---------------------------+---------------------------+
| Random uniform          | ``rand(m,n)``             | ``rndu(m, n)``            |
+-------------------------+---------------------------+---------------------------+
| Random normal           | ``randn(m,n)``            | ``rndn(m, n)``            |
+-------------------------+---------------------------+---------------------------+
| Column mean/sum         | ``mean(A)`` / ``sum(A)``  | ``meanc(A)`` / ``sumc(A)``|
+-------------------------+---------------------------+---------------------------+
| Natural log             | ``log(x)``                | ``ln(x)``                 |
+-------------------------+---------------------------+---------------------------+
| Print                   | ``disp(x)``               | ``print x;``              |
+-------------------------+---------------------------+---------------------------+
| Comment                 | ``% comment``             | ``// comment``            |
+-------------------------+---------------------------+---------------------------+
| SVD (full)              | ``[U,S,V] = svd(A)``     | ``{u,s,v} = svdcusv(A)`` |
+-------------------------+---------------------------+---------------------------+
| Diagonal from vector    | ``diag(v)``               | ``diagmat(v)``            |
+-------------------------+---------------------------+---------------------------+

Common Gotchas
--------------

1. **Semicolons are required.** Every statement must end with ``;``

2. **Braces not brackets.** Matrices use ``{ }`` not ``[ ]``

3. **Dot not colon for "all".** "All rows" is ``A[.,1]`` not ``A(:,1)``. But ``:`` works for ranges: ``A[1:5, .]``.

4. **Slash not backslash.** Use ``b/A`` instead of ``A\b``

5. **log means base 10.** MATLAB ``log`` = natural log. GAUSS ``log`` = base 10. Use ``ln`` for natural log.

6. **String quotes.** Only double quotes ``"string"`` work

7. **Procedure syntax.** Use ``proc``/``endp``/``retp`` not ``function``/``end``/``return``

8. **Local variables are not automatic.** In MATLAB, function variables are local by default. In GAUSS, you must declare them with ``local`` inside ``proc`` or they become global. Forgetting ``local`` creates hard-to-find bugs where procedures silently read or modify variables from the calling scope.

9. **No ``end`` keyword for indexing.** Use ``rows(A)`` instead of ``end``. For the last 5 rows: ``A[rows(A)-4:rows(A), .]``

Putting It Together
-------------------

Here is a complete, runnable example that loads data, filters it, runs a regression, and prints the results:

::

    // Get full path to dataset in GAUSS examples folder
    fname = getGAUSSHome("examples/auto2.dta");

    // Load specific variables
    data = loadd(fname, "mpg + weight + foreign");

    // Keep only domestic cars
    data = selif(data, data[., "foreign"] .== 0);

    // Run OLS
    struct olsmtOut out;
    out = olsmt(data, "mpg ~ weight");

    print out.b;

What's Next?
------------

- :doc:`../getting-started/quickstart` — 10-minute introduction to GAUSS basics
- :doc:`../getting-started/running-existing-code` — If you inherited GAUSS code and need to get it running
- :doc:`../data-management` — Loading, cleaning, and reshaping data
- :doc:`../textbook-examples/index` — Worked examples from Greene (*Econometric Analysis*) and Brooks (*Introductory Econometrics for Finance*)
- `Command Reference <../command-reference.html>`__ — Browse all 1,000+ built-in functions
- `Econometrics blog <https://www.aptech.com/blog/category/econometrics/>`__ — Fully worked examples covering regression, panel data, hypothesis testing, and more
- `Time series blog <https://www.aptech.com/blog/category/time-series/>`__ — ARIMA, VAR, GARCH, cointegration, and forecasting tutorials with complete code
- `Panel data blog <https://www.aptech.com/blog/category/panel-data/>`__ — Fixed effects, random effects, and dynamic panel models
- `Programming blog <https://www.aptech.com/blog/category/programming/>`__ — Loops, string handling, data manipulation, and general GAUSS programming
- `Formatted output with sprintf <https://www.aptech.com/blog/how-to-create-a-simple-table-with-sprintf-in-gauss/>`__ — Creating tables and formatted output

.. seealso::

    :func:`loadd`, :func:`olsmt`, :func:`glm`, :func:`quantileFit`, :func:`minimize`
