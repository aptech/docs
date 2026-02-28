
Introduction to GAUSS for MATLAB Users
======================================

If you work with matrices, optimization, and numerical computing in MATLAB, you'll find GAUSS handles these the same way -- with differences in syntax and a stronger focus on econometrics and statistics. This guide maps MATLAB concepts, syntax, and workflows to their GAUSS equivalents.

.. note::

    This guide is written for GAUSS 26. Some features (such as :func:`repmat`, :func:`findIdx`, :func:`diagmat`, and the colon operator for sequences) require GAUSS 26.0.1 or later.

**Where to type code:** Open GAUSS and create a new program file (File > New > Program File). Type or paste your code, then press F5 (or the Run button) to execute it. You can also type single lines in the command bar at the bottom of the window.

**Debugging:** Errors appear in the Output window with a line number -- click it to jump to the error. Use the Variables panel (View > Variables) to inspect values at runtime. You can set breakpoints by clicking in the left margin of the editor, then step through code with the Debug menu. For quick debugging, insert ``print varname;`` statements.

**Inspecting structures:** To see what fields an output structure contains, use ``print`` -- for example, ``print out;`` displays all members and their values. To see just the field names, check the structure definition in the Command Reference (press F1 on the function name).

How GAUSS Differs from MATLAB
-----------------------------

GAUSS shares MATLAB's matrix-first philosophy but is oriented around statistics and econometrics rather than engineering. Here are the practical differences that affect your daily coding:

- **Dataframes are matrices**: Named columns and typed variables, but you can do matrix algebra on them directly -- no ``table2array`` conversion step.
- **Column-wise by default**: Statistical functions operate on columns (``meanc``, ``stdc``, ``sumc``), matching the convention that columns are variables and rows are observations.
- **Formula strings for estimation**: Model specification uses ``"y ~ x1 + x2"`` syntax (similar to R). Categorical variables are handled automatically.
- **Structures for output**: Estimation results are returned in structures with named members (``out.b``, ``out.stderr``), similar to MATLAB structs.
- **No toolbox fees**: OLS, GLM, quantile regression, optimization, and plotting are all included in the base package -- no extra toolboxes required.

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

.. note::

    Most examples below use the ``auto2`` dataset bundled with GAUSS. To run them, load it first:

    ::

       auto2 = loadd(getGAUSSHome("examples/auto2.dta"));

Matrix Creation
---------------

.. code-block:: matlab

    % MATLAB
    A = [1 2 3; 4 5 6; 7 8 9]

::

    // GAUSS
    A = { 1 2 3, 4 5 6, 7 8 9 };

**Note:** GAUSS uses braces ``{ }`` and commas between rows. Semicolons end statements, not rows. Unlike MATLAB, newlines are not row separators -- you must use commas.

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

**Note:** MATLAB's colon operator produces row vectors; GAUSS produces column vectors. MATLAB's ``linspace(0, 1, 5)`` takes start, end, and count. GAUSS's :func:`seqa` takes start, increment, and count -- you must compute the step size yourself: ``seqa(0, (1-0)/(5-1), 5)``.

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
    A(end-2:end,:)  % Last 3 rows

::

    // GAUSS
    A[1, 1];          // Element
    A[1, .];          // First row (dot = all)
    A[., 1];          // First column
    A[1:2, .];        // Rows 1-2
    A[rows(A), .];    // Last row (no 'end' keyword)
    A[rows(A)-2:rows(A), .];  // Last 3 rows

GAUSS dataframes also support indexing by column name:

::

    auto2[., "mpg"];              // One column by name
    auto2[., "mpg" "weight"];    // Multiple columns (space-separated)
    auto2[1:10, "mpg"];          // First 10 rows of mpg

**Key difference:** MATLAB uses ``:`` for "all", GAUSS uses ``.``. Use ``rows(A)`` and ``cols(A)`` where MATLAB uses ``end``.

Operators
---------

Element-wise vs. matrix operations:

.. code-block:: matlab

    % MATLAB
    A * B         % Matrix multiplication
    A .* B        % Element-wise multiplication
    A .^ 2        % Element-wise power
    A'            % Transpose

::

    // GAUSS
    A * B;        // Matrix multiplication (same)
    A .* B;       // Element-wise multiplication (same)
    A .^ 2;       // Element-wise power (same)
    A';           // Transpose (same)

Element-wise arithmetic operators (``.* ./ .^``) and transpose (``'``) work the same in both languages.

**Comparison operators are different.** GAUSS uses dot-prefixed operators for element-wise comparison:

.. code-block:: matlab

    % MATLAB
    A > 0         % Element-wise comparison
    A == B        % Element-wise equality
    A ~= B        % Element-wise not-equal
    A & B         % Element-wise AND
    A | B         % Element-wise OR (also vertical concat in GAUSS!)

::

    // GAUSS
    A .> 0;       // Element-wise comparison (dot prefix required)
    A .== B;      // Element-wise equality
    A .!= B;      // Element-wise not-equal (.ne also works)
    A .and B;     // Element-wise AND
    A .or B;      // Element-wise OR

.. warning::

    **Comparison operators need dots.** In MATLAB, ``A > 0`` is element-wise. In GAUSS, ``A > 0`` without the dot tests whether *all* elements satisfy the condition (returns a scalar). Use ``.>`` for element-wise results. This is the most common source of bugs for MATLAB migrants.

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

For strings, use ``$~`` (horizontal) and ``$|`` (vertical): ``"Domestic" $| "Foreign"`` creates a 2x1 string array.

Example:

::

    A = { 1 2, 3 4 };
    B = { 5, 6 };

    print A ~ B;   // [1 2 5; 3 4 6]
    print A | B';  // [1 2; 3 4; 5 6]

Filtering and Selection
-----------------------

MATLAB uses logical indexing directly. GAUSS uses :func:`selif` with element-wise comparison operators:

.. code-block:: matlab

    % MATLAB
    A(A(:,1) > 5, :)              % Rows where column 1 > 5
    data(data.price > 10000, :)   % Filter table by condition

::

    // GAUSS
    selif(A, A[., 1] .> 5);                      // Rows where column 1 > 5
    selif(auto2, auto2[., "price"] .> 10000);    // Filter by condition

    // Combine conditions
    mask = auto2[., "mpg"] .> 20 .and auto2[., "price"] .< 8000;
    cheap_efficient = selif(auto2, mask);

Note the ``.>`` operator: GAUSS requires the dot prefix for element-wise comparison (see `Operators`_ above).

**Missing values:** MATLAB uses ``NaN`` and ``isnan``; GAUSS uses ``.`` (dot) and provides several tools:

.. code-block:: matlab

    % MATLAB
    clean = rmmissing(data);           % Drop rows with any NaN
    data(isnan(data)) = 0;             % Replace NaN with 0
    mask = ~isnan(data(:,3));          % Rows where column 3 is not NaN

::

    // GAUSS
    clean = packr(data);               // Drop rows with any missing value
    data = missrv(data, 0);            // Replace missings with 0
    mask = data[., 3] .!= miss(1, 1); // Rows where column 3 is not missing

:func:`packr` is the workhorse -- it removes any row containing a missing value. Use :func:`missrv` to replace missings with a specific value. For element-wise missing detection, use ``x .== miss(1, 1)`` (see the `Common Function Translations`_ table).

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

:func:`getGAUSSHome` returns the path to GAUSS's installation directory. Use it to access bundled example datasets: ``loadd(getGAUSSHome("examples/auto2.dta"))``.

**Formula string quick reference:** GAUSS uses formula strings in several contexts with slightly different syntax:

+--------------------------+----------------------------+--------------------------------+
| Context                  | Example                    | Separator                      |
+==========================+============================+================================+
| :func:`loadd` (loading)  | ``"mpg + weight + price"`` | ``+`` lists variables          |
+--------------------------+----------------------------+--------------------------------+
| :func:`olsmt` (models)   | ``"price ~ mpg + weight"`` | ``~`` separates y from X       |
+--------------------------+----------------------------+--------------------------------+
| Bracket indexing          | ``auto2[., "mpg" "wt"]``   | Space separates names          |
+--------------------------+----------------------------+--------------------------------+
| Type overrides            | ``"date($Date) + cat(x)"`` | Keywords wrap variable names   |
+--------------------------+----------------------------+--------------------------------+

Statistics and Econometrics
---------------------------

Unlike MATLAB, where ``fitlm``, ``fitglm``, and optimization functions require the Statistics or Optimization Toolbox, GAUSS includes all of these in the base package.

Basic statistics:

.. code-block:: matlab

    % MATLAB
    mean(x)       % Column means
    std(x)        % Column std devs
    sum(x)        % Column sums
    cov(x)        % Covariance matrix

::

    // GAUSS
    meanc(x);     // Column means (the 'c' suffix = column-wise)
    stdc(x);      // Column std devs
    sumc(x);      // Column sums
    vcx(x);       // Covariance matrix

OLS regression:

.. code-block:: matlab

    % MATLAB (Statistics Toolbox)
    mdl = fitlm(X, y);
    mdl.Coefficients
    mdl.Residuals.Raw

::

    // GAUSS
    struct olsmtOut out;
    out = olsmt(auto2, "price ~ mpg + weight");

    // Access results through the output structure
    print out.b;          // Coefficient estimates
    print out.stderr;     // Standard errors
    print out.rsq;        // R-squared

Key :class:`olsmtOut` members: ``b`` (coefficients), ``stderr`` (standard errors), ``vc`` (variance-covariance matrix), ``rsq`` (R-squared), ``resid`` (residuals), ``dwstat`` (Durbin-Watson), ``sigma`` (residual std dev), ``stb`` (standardized coefficients). To compute t-statistics and p-values: ``t = out.b ./ out.stderr``. See the :func:`olsmt` reference for the full list.

.. tip::

    Use ``call olsmt(...)`` (with ``call``) to print a formatted summary table to the screen without saving results to a variable. The ``call`` keyword discards return values.

Logistic regression (GLM):

.. code-block:: matlab

    % MATLAB (Statistics Toolbox)
    mdl = fitglm(X, y, 'Distribution', 'binomial');

::

    // GAUSS
    struct glmOut out;
    out = glm(data, "admit ~ gre + gpa + rank", "binomial");

Quantile regression:

::

    // GAUSS (no MATLAB built-in equivalent)
    struct qfitOut out;
    out = quantileFit(data, "y ~ x1 + x2", 0.25 | 0.5 | 0.75);

For robust or clustered standard errors, pass an :class:`olsmtControl` structure -- see the :func:`olsmt` reference for details.

Plotting
--------

MATLAB users expect rich plotting. GAUSS has a full graphics library:

.. code-block:: matlab

    % MATLAB
    plot(x, y)
    scatter(x, y)
    histogram(x, 20)
    bar(labels, heights)
    surf(X, Y, Z)
    subplot(2, 1, 1)
    title('My Plot')
    xlabel('X axis')
    saveas(fig, 'plot.png')

::

    // GAUSS
    plotXY(x, y);
    plotScatter(x, y);
    plotHist(x, 20);
    plotBar(labels, heights);
    plotSurface(x, y, z);
    plotLayout(2, 1, 1);
    // Title and labels use a plotControl structure (see below)
    plotSave("plot.png");

**Setting titles, labels, and legends** uses a :class:`plotControl` structure:

::

    // Create a plot with title, labels, and legend
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");

    plotSetTitle(&myPlot, "MPG vs Weight");
    plotSetXLabel(&myPlot, "Weight (lbs)");
    plotSetYLabel(&myPlot, "Miles per gallon");
    plotSetLegend(&myPlot, "Domestic" $| "Foreign");

    plotXY(myPlot, auto2[., "weight"], auto2[., "mpg"]);

Quick plotting example:

::

    // Sine wave -- no plotControl needed for simple plots
    x = seqa(0, 0.1, 63);   // 0 to ~2*pi
    plotXY(x, sin(x));

Optimization
------------

GAUSS includes unconstrained and constrained optimization in the base package.

+-------------------------------+-----------------------------------+
| MATLAB                        | GAUSS                             |
+===============================+===================================+
| ``fminunc(f, x0)``           | ``minimize(&f, x0)``              |
+-------------------------------+-----------------------------------+
| ``fmincon(f, x0, ...)``      | ``sqpSolve(&f, x0)``             |
+-------------------------------+-----------------------------------+
| ``fsolve(f, x0)``            | ``eqSolve(&f, x0)``              |
+-------------------------------+-----------------------------------+

**Key difference:** MATLAB uses anonymous functions (``@(x) ...``) to pass objectives. GAUSS uses the ``&`` operator to pass a pointer to a named procedure. Extra data arguments are passed after the starting values:

.. code-block:: matlab

    % MATLAB -- anonymous function captures Y, X via closure
    f = @(beta) sum((Y - X*beta).^2);
    result = fminunc(f, x0);

::

    // GAUSS -- named procedure; extra data passed as arguments
    proc (1) = myObj(beta, Y, X);
        local resid;
        resid = Y - X * beta;
        retp(resid'resid);    // resid' * resid = sum of squared residuals
    endp;

    struct minimizeOut out;
    out = minimize(&myObj, x0, Y, X);

For constrained optimization with linear or nonlinear constraints, see :func:`sqpSolve`. For systems of nonlinear equations, see :func:`eqSolve`.

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

**Solving linear systems:** GAUSS uses the ``/`` operator: ``b / A`` solves ``Ax = b``. Use :func:`solpd` for positive definite systems or :func:`olsqr` for QR-based least squares.

.. warning::

    **eigv return order is reversed.** MATLAB's ``[V, D] = eig(A)`` returns eigenvectors first, then eigenvalues. GAUSS's ``{ val, vec } = eigv(A)`` returns eigenvalues first, then eigenvectors. Swapping these produces wrong results silently.

.. note::

    **svdcusv returns a diagonal matrix.** Both MATLAB's ``svd`` and GAUSS's :func:`svdcusv` return ``S``/``s`` as a diagonal matrix. GAUSS's plain :func:`svd` (no ``cusv``) returns only a vector of singular values.

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

**Note:** GAUSS requires semicolons after control statements (``if``, ``for``, ``else``, etc.). Inside a ``proc``, remember to declare loop variables with ``local`` (see Gotcha #9) or they become globals: ``local i; for i (1, 10, 1); ... endfor;``

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
| Check NaN (any)         | ``any(isnan(x),'all')``   | ``ismiss(x)``             |
+-------------------------+---------------------------+---------------------------+
| Check NaN (element)     | ``isnan(x)``              | ``x .== miss(1,1)``       |
+-------------------------+---------------------------+---------------------------+
| NaN / missing value     | ``NaN``                   | ``.`` (dot)               |
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
| Formatted output        | ``fprintf(fmt, x)``       | ``print sprintf(fmt, x)`` |
+-------------------------+---------------------------+---------------------------+
| Random uniform          | ``rand(m,n)``             | ``rndu(m, n)``            |
+-------------------------+---------------------------+---------------------------+
| Random normal           | ``randn(m,n)``            | ``rndn(m, n)``            |
+-------------------------+---------------------------+---------------------------+
| Print to console        | ``disp(x)``               | ``print x;``              |
+-------------------------+---------------------------+---------------------------+
| Comment                 | ``% comment``             | ``// comment``            |
+-------------------------+---------------------------+---------------------------+
| FFT                     | ``fft(x)``                | ``fft(x)``                |
+-------------------------+---------------------------+---------------------------+
| Inverse FFT             | ``ifft(x)``               | ``ffti(x)``               |
+-------------------------+---------------------------+---------------------------+

**Functions with the same name:** ``repmat``, ``unique``, ``abs``, ``exp``, ``ceil``, ``floor``, ``round``, ``rank``, ``inv``, ``det``, ``chol``, ``eye``, ``zeros``, ``ones``, ``fft``

.. warning::

    **reshape fill order differs.** MATLAB's ``reshape`` fills column-major (down columns first). GAUSS's ``reshape`` fills row-major (across rows first). The same input will produce different matrix layouts -- silently, with no error.

.. note::

    **diag vs diagmat**: MATLAB's ``diag`` both creates and extracts diagonal matrices. In GAUSS, ``diag(A)`` only *extracts* the diagonal. To *create* a diagonal matrix from a vector, use ``diagmat(v)``.

.. warning::

    **log vs ln**: In MATLAB, ``log`` is the natural logarithm. In GAUSS, ``log`` is base 10 and ``ln`` is natural. This will silently give wrong results if you don't catch it.

Toolbox-to-Package Mapping
---------------------------

MATLAB functionality is split across paid toolboxes. GAUSS includes most of it in the base package:

+-------------------------------------+-----------------------------------------------+
| MATLAB Toolbox                      | GAUSS Equivalent                              |
+=====================================+===============================================+
| Statistics & Machine Learning       | Base GAUSS (OLS, GLM, quantile reg, etc.)     |
+-------------------------------------+-----------------------------------------------+
| Optimization Toolbox                | Base GAUSS (``minimize``, ``sqpSolve``)       |
+-------------------------------------+-----------------------------------------------+
| Econometrics Toolbox                | Base GAUSS + TSMT (time series add-on)        |
+-------------------------------------+-----------------------------------------------+
| Signal Processing Toolbox           | ``fft``, ``ffti``, ``rfft`` (built-in)        |
+-------------------------------------+-----------------------------------------------+
| Financial Toolbox                   | Fanpac (add-on)                               |
+-------------------------------------+-----------------------------------------------+

**Time series users:** If your work involves ARIMA, VAR, GARCH, impulse response functions, or forecasting, you will use the **TSMT** add-on. Key functions: :func:`arimaFit`, :func:`svarFit` (structural VAR), :func:`varmaFit`, :func:`varmaPredict`. For maximum likelihood estimation, see :func:`maxlikmt`. See the `time series blog <https://www.aptech.com/blog/category/time-series/>`__ for complete worked examples.

Common Gotchas
--------------

1. **Semicolons are required.** Every statement must end with ``;``

2. **Braces not brackets.** Matrices use ``{ }`` not ``[ ]``

3. **Dot not colon for "all".** "All rows" is ``A[.,1]`` not ``A(:,1)``. But ``:`` works for ranges: ``A[1:5, .]``.

4. **Comparison operators need dots.** Element-wise comparison uses ``.>``, ``.<``, ``.==``, ``.!=``. Without the dot, ``>`` tests if *all* elements satisfy the condition. This is the most common bug for MATLAB migrants.

5. **Slash not backslash.** Use ``b/A`` instead of ``A\b``

6. **log means base 10.** MATLAB ``log`` = natural log. GAUSS ``log`` = base 10. Use ``ln`` for natural log.

7. **String quotes.** Only double quotes ``"string"`` work

8. **Procedure syntax.** Use ``proc``/``endp``/``retp`` not ``function``/``end``/``return``

9. **Local variables are not automatic.** In MATLAB, function variables are local by default. In GAUSS, you must declare them with ``local`` inside ``proc`` or they become global. Forgetting ``local`` creates hard-to-find bugs where procedures silently read or modify variables from the calling scope.

10. **No ``end`` keyword for indexing.** Use ``rows(A)`` instead of ``end``. For the last 5 rows: ``A[rows(A)-4:rows(A), .]``

11. **The ``call`` keyword.** Use ``call functionName(...)`` to run a function and discard its return value. This is common for estimation functions: ``call olsmt(data, "y ~ x")`` prints the summary table without saving results.

Putting It Together
-------------------

Here is a complete, runnable example that loads data, filters it, plots it, runs a regression, and prints the results:

::

    // Load the auto2 dataset bundled with GAUSS
    auto2 = loadd(getGAUSSHome("examples/auto2.dta"));

    // Keep only domestic cars (foreign == 0)
    domestic = selif(auto2, auto2[., "foreign"] .== 0);

    // Quick scatter plot
    plotScatter(domestic[., "weight"], domestic[., "mpg"]);

    // Run OLS: how does weight affect fuel efficiency?
    struct olsmtOut out;
    out = olsmt(domestic, "mpg ~ weight");

    print out.b;         // Coefficient estimates
    print out.stderr;    // Standard errors
    print out.rsq;       // R-squared

What's Next?
------------

- :doc:`../getting-started/quickstart` -- 10-minute introduction to GAUSS basics
- :doc:`../getting-started/running-existing-code` -- If you inherited GAUSS code and need to get it running
- :doc:`../data-management` -- Loading, cleaning, and reshaping data
- :doc:`../textbook-examples/index` -- Worked examples from Greene (*Econometric Analysis*) and Brooks (*Introductory Econometrics for Finance*)
- `Command Reference <../command-reference.html>`__ -- Browse all 1,000+ built-in functions
- `Graphics documentation <../graphics.html>`__ -- Plotting functions, customization, and export
- :func:`saved` -- Export data to CSV, Excel, or other formats
- `User Guide <https://docs.aptech.com/gauss/getting-started/installing-modules.html>`__ -- Installing and managing add-on modules
- `Econometrics blog <https://www.aptech.com/blog/category/econometrics/>`__ -- Fully worked examples covering regression, panel data, hypothesis testing, and more
- `Time series blog <https://www.aptech.com/blog/category/time-series/>`__ -- ARIMA, VAR, GARCH, cointegration, and forecasting tutorials with complete code
- `Programming blog <https://www.aptech.com/blog/category/programming/>`__ -- Loops, string handling, data manipulation, and general GAUSS programming

.. seealso::

    :func:`loadd`, :func:`olsmt`, :func:`glm`, :func:`quantileFit`, :func:`minimize`, :func:`plotXY`, :func:`fft`
