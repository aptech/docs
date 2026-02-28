
Introduction to GAUSS for EViews Users
======================================

This guide helps EViews users do the same things in GAUSS. If you're comfortable with workfiles, VAR models, IRFs, and ARIMA estimation, you'll find equivalent tools in GAUSS -- with more flexibility for custom models and reproducible workflows.

.. note::

    This guide is written for GAUSS 26. Time series functions (ARIMA, VAR, GARCH) require the **TSMT** add-on.

How GAUSS Differs from EViews
------------------------------

- **Your analysis is code.** EViews blends GUI dialogs, command window entries, and program files. In GAUSS, your entire workflow is a program file -- reproducible, version-controlled, and shareable. No clicking through dialogs to re-estimate.
- **No workfile -- load data directly.** EViews requires creating a workfile first, then importing series into it. GAUSS loads data directly into a dataframe with :func:`loadd` -- no workfile setup step.
- **Multiple datasets at once.** EViews ties your analysis to one workfile at a time. GAUSS can hold many datasets in memory simultaneously.
- **Results in structures, not object views.** EViews stores results in "equation" and "VAR" objects that you view in windows. GAUSS returns results in structures with named members (``out.b``, ``out.sigma``) that you access in code.
- **Full programming language.** EViews handles loops and basic logic. GAUSS is a complete matrix programming language -- you can write custom estimators, simulation studies, and bootstrap procedures.

**Where to type code:** Open GAUSS and create a new program file (File > New > Program File). Type or paste your code, then press F5 (or the Run button) to execute it. You can also type single lines in the command bar at the bottom of the window.

**Debugging:** Errors appear in the Output window with a line number -- click it to jump to the error. Use the Variables panel (View > Variables) to inspect values at runtime. You can set breakpoints by clicking in the left margin of the editor, then step through code with the Debug menu. For quick debugging, insert ``print varname;`` statements.

Key Syntax Differences
-----------------------

+-------------------+---------------------------+---------------------------+
| Feature           | EViews                    | GAUSS                     |
+===================+===========================+===========================+
| Statement end     | Newline                   | Required ``;``            |
+-------------------+---------------------------+---------------------------+
| Indexing          | 1-based (series obs)      | 1-based                   |
+-------------------+---------------------------+---------------------------+
| String quotes     | ``" "``                   | ``" "`` only              |
+-------------------+---------------------------+---------------------------+
| Assignment        | ``=``                     | ``=`` (same)              |
+-------------------+---------------------------+---------------------------+
| All rows/cols     | (implicit in series)      | ``.``                     |
+-------------------+---------------------------+---------------------------+
| Comments          | ``' comment``             | ``// comment``            |
+-------------------+---------------------------+---------------------------+
| String concat     | ``+``                     | ``$+``                    |
+-------------------+---------------------------+---------------------------+
| String equality   | ``=``                     | ``$==``                   |
+-------------------+---------------------------+---------------------------+

Operators
---------

**Matrix vs element-wise multiplication:**

::

    // GAUSS
    A * B;            // Matrix multiplication
    A .* B;           // Element-wise multiplication
    A .^ 2;           // Element-wise power
    A ./ B;           // Element-wise division
    A';               // Transpose

.. warning::

    **``*`` is matrix multiplication in GAUSS.** EViews handles this behind the scenes. In GAUSS, ``A * B`` is matrix multiplication and ``A .* B`` is element-wise. Using the wrong one produces wrong results silently.

**Comparison operators have two forms.** Without a dot, ``A > 0`` returns a scalar -- true only if ALL elements satisfy the condition. With a dot, ``A .> 0`` tests each element individually:

::

    // GAUSS
    A .> 0;           // Element-wise: returns 1/0 for each element
    A .== B;          // Element-wise equality
    A .and B;         // Element-wise AND
    A .or B;          // Element-wise OR

.. warning::

    ``A > 0`` is true only if every element is positive (like EViews's ``@all``). ``A .> 0`` tests each element. Both forms exist for: ``>``/``.>``, ``<``/``.<``, ``>=``/``.>=``, ``<=``/``.<=``, ``==``/``.==``, ``!=``/``.!=``.

Concatenation
-------------

::

    // GAUSS
    A ~ B;            // Horizontal concatenation (tilde)
    A | B;            // Vertical concatenation (pipe)
    a $+ b;           // String concatenation

.. warning::

    **``|`` is vertical concatenation, not logical OR.** ``condition1 | condition2`` stacks two vectors vertically. Use ``.or`` for logical OR and ``.and`` for logical AND.

For string arrays, use ``$~`` (horizontal) and ``$|`` (vertical): ``"Domestic" $| "Foreign"`` creates a 2x1 string array.

**String operators use the ``$`` prefix.** In EViews, ``+`` concatenates strings and ``=`` compares them. In GAUSS: ``$+`` (concatenation), ``$==`` (equality), ``$~`` (horizontal join), ``$|`` (vertical join).

Indexing
--------

EViews manages series by name within a workfile. In GAUSS, you index dataframes directly by row and column:

::

    // GAUSS
    data = loadd("gdp_data.xlsx");

    data[., "gdp"];           // Column by name (dot = all rows)
    data[., "gdp" "cpi"];     // Multiple columns (space-separated names)
    data[., 1];               // Column by position
    data[1, 1];               // First row, first column
    data[1:10, .];            // Rows 1 through 10 (inclusive)
    data[rows(data), .];      // Last row (no negative indexing)

**Key points:**

- GAUSS uses ``.`` for "all rows" or "all columns"
- Slices are inclusive: ``data[1:5, .]`` gets rows 1 through 5
- No negative indexing. Use ``rows(data)`` for the last row.

.. note::

    Most examples below use the ``auto2`` dataset bundled with GAUSS. To run them, load it first:

    ::

       auto2 = loadd(getGAUSSHome("examples/auto2.dta"));

Data: Workfiles vs. Dataframes
------------------------------

In EViews, you create a workfile and import series:

.. code-block:: none

    ' EViews
    wfcreate q 1960Q1 2020Q4
    import "gdp_data.xlsx"

In GAUSS, you load data directly into a dataframe -- no workfile setup:

::

    // GAUSS - one function reads CSV, Excel, Stata, SAS, SPSS, HDF5
    data = loadd("gdp_data.xlsx");

    // Check what you loaded
    print getcolnames(data)';      // Column names
    print rows(data) "observations";
    head(data);                     // First 5 rows (like EViews's spreadsheet view)

**Loading specific variables** uses a formula string with ``+``:

::

    // Load only these variables
    data = loadd("macro_data.csv", "gdp + cpi + unrate");

    // Load all variables except one
    data = loadd("macro_data.csv", ". -date_str");

**Accessing variables:**

.. code-block:: none

    ' EViews - reference by name
    show gdp

::

    // GAUSS - index by column name
    gdp = data[., "gdp"];

**Creating new variables:**

.. code-block:: none

    ' EViews
    series gdp_growth = dlog(gdp)
    series lgdp = log(gdp)

::

    // GAUSS - use lagn() for lags, ln() for natural log
    lgdp = ln(data[., "gdp"]);
    gdp_growth = lgdp - lagn(lgdp, 1);    // lagn fills the first obs with missing

.. warning::

    **log vs ln**: EViews's ``log()`` is the natural logarithm. GAUSS's ``log()`` is **base 10**. Use ``ln()`` in GAUSS. Forgetting this will silently corrupt every model that uses logged variables.

**Generating lags and differences:**

.. code-block:: none

    ' EViews
    series y_lag1 = y(-1)
    series y_lag2 = y(-2)
    series dy = d(y)

::

    // GAUSS
    y_lag1 = lagn(y, 1);                  // Lag 1 (first obs becomes missing)
    y_lag2 = lagn(y, 2);                  // Lag 2 (first two obs become missing)
    dy = y - lagn(y, 1);                  // First difference
    dlog_y = ln(y) - lagn(ln(y), 1);      // Log difference (like EViews's dlog)

.. note::

    :func:`lagn` fills lagged observations with ``miss()``. Use :func:`packr` to drop rows with missing values after creating lags or differences.

Data Import/Export
------------------

::

    // GAUSS - loadd handles all formats
    data = loadd("data.csv");
    data = loadd("data.dta");             // Stata
    data = loadd("data.sas7bdat");        // SAS
    data = loadd("data.xlsx");            // Excel

    // Export
    saved(data, "output.csv");
    saved(data, "output.xlsx");

**Formula string quick reference:** GAUSS uses formula strings in several contexts:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Context
      - Example
      - Separator
    * - :func:`loadd` (loading)
      - ``"gdp + cpi + unrate"``
      - ``+`` lists variables
    * - :func:`olsmt` (models)
      - ``"price ~ mpg + weight"``
      - ``~`` separates y from X
    * - Bracket indexing
      - ``data[., "gdp" "cpi"]``
      - Space separates names
    * - Type overrides
      - ``"date($Date) + cat(x)"``
      - Keywords wrap variable names

Data Manipulation
-----------------

.. code-block:: none

    ' EViews
    smpl if foreign = 0
    sort mpg

::

    // GAUSS
    domestic = selif(auto2, auto2[., "foreign"] .== 0);   // Filter rows
    sorted = sortc(auto2, "mpg");                          // Sort by column

.. warning::

    **GAUSS does not support boolean indexing.** Use :func:`selif` to filter rows: ``selif(df, condition)``. Passing a boolean vector to brackets will not filter -- it interprets the 0s and 1s as row numbers.

**Common operations:**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - EViews
      - GAUSS
    * - ``smpl if x > 5``
      - ``selif(df, df[., "x"] .> 5)``
    * - ``sort x``
      - ``sortc(df, "x")``
    * - ``series z = x + y``
      - ``dfaddcol(df, "z", df[., "x"] + df[., "y"])``
    * - ``group mygrp x y``
      - ``df[., "x" "y"]``
    * - (manual in EViews)
      - ``aggregate(df, "mean", "group_var")``

Missing Values
--------------

EViews handles missing values within the workfile automatically. In GAUSS, you manage them explicitly:

.. code-block:: none

    ' EViews
    series y_clean = @nan(y, 0)
    smpl if y <> NA

::

    // GAUSS
    miss();                       // Creates a missing value (like EViews's NA)
    ismiss(x);                    // Returns 1 if ANY element is missing (scalar)
    x .== miss();                 // Element-wise check (returns 1/0 vector)
    packr(data);                  // Drop rows with any missing value
    missrv(x, 0);                // Replace missing with 0

.. warning::

    **ismiss is NOT element-wise.** ``ismiss(x)`` returns a **scalar** (1 if any element is missing, 0 otherwise). For element-wise missing detection, use ``x .== miss()``.

Descriptive Statistics
----------------------

.. code-block:: none

    ' EViews
    gdp.stats

::

    // GAUSS - dstatmt prints a summary table (like EViews's stats view)
    call dstatmt(auto2[., "price" "mpg" "weight"]);

Output::

    ------------------------------------------------------------------------------------------
    Variable        Mean    Std Dev    Variance    Minimum    Maximum    Valid  Missing
    ------------------------------------------------------------------------------------------
    price       6165.26    2949.50   8699530.9      3291      15906       74        0
    mpg           21.30       5.79       33.47        12         41       74        0
    weight      3019.46     777.19    604021.4      1760       4840       74        0

**Column-wise statistics:**

::

    // GAUSS
    meanc(x);     // Column mean (the 'c' suffix = column-wise)
    stdc(x);      // Column standard deviation (uses N-1)
    sumc(x);      // Column sum
    minc(x);      // Column min
    maxc(x);      // Column max
    median(x);    // Median

    // Row-wise
    meanr(X);     // Row mean (the 'r' suffix = row-wise)
    sumr(X);      // Row sum

OLS Regression
--------------

.. code-block:: none

    ' EViews
    equation eq1.ls price c mpg weight

::

    // GAUSS - print formatted summary (like EViews's equation view)
    call olsmt(auto2, "price ~ mpg + weight");

Output::

    Valid cases:                    74     Dependent variable:           price
    Missing cases:                   0     Deletion method:                  None
    Total SS:                634007042     Degrees of freedom:                 71
    R-squared:                  0.2926     Rbar-squared:                   0.2727
    Residual SS:              448544672     Std error of est:          2514.3269
    F(2,71):                   14.6874     Probability of F:              0.0000

                          Standard                    Prob     Standardized   Cor with
    Variable   Estimate     Error    t-value     >|t|      Estimate    Dep Var
    -------------------------------------------------------------------------------
    CONSTANT   1946.069  3597.0496   0.54101    0.5902       ---         ---
    mpg        -49.5122   86.1560   -0.57464    0.5674   -0.09717     -0.4559
    weight       1.7466    0.3712    4.70402    0.0000    0.46030      0.5386

.. tip::

    Use ``call olsmt(...)`` to print a formatted summary without saving results. The ``call`` keyword discards return values -- useful for quick exploration.

**Accessing results:**

.. code-block:: none

    ' EViews
    eq1.@coefs
    eq1.@se
    eq1.@r2

::

    // GAUSS
    struct olsmtOut out;
    out = olsmt(auto2, "price ~ mpg + weight");

    print out.b;          // Coefficient estimates
    print out.stderr;     // Standard errors
    print out.rsq;        // R-squared
    print out.resid;      // Residuals
    print out.vc;         // Variance-covariance of estimates

Key :class:`olsmtOut` members: ``b`` (coefficients), ``stderr`` (standard errors), ``vc`` (variance-covariance matrix), ``rsq`` (R-squared), ``resid`` (residuals), ``dwstat`` (Durbin-Watson), ``sigma`` (residual std dev).

Time Series Analysis (TSMT)
----------------------------

GAUSS's time series tools are in the **TSMT** add-on. Add this line at the top of your script:

::

    library tsmt;

If this produces an error, contact Aptech to add TSMT to your license. All examples in this section require TSMT.

ARIMA
^^^^^

.. code-block:: none

    ' EViews
    equation eq1.ls d(gdp) c ar(1) ma(1)

::

    // GAUSS
    library tsmt;

    // Load unemployment rate data
    data = loadd(getGAUSSHome("examples/UNRATE.csv"));
    y = data[., "UNRATE"];

    // Fit ARIMA(1,1,1)
    struct arimamtOut aOut;
    aOut = arimaFit(y, 1, 1, 1);

Output::

    ================================================================================
    Coefficient                Estimate      Std. Err.        T-Ratio     Prob |>| t
    ================================================================================

    AR[1,1]                      -0.722          0.167         -4.333          0.000
    MA[1,1]                      -0.798          0.143         -5.580          0.000
    Constant                     -0.001          0.695         -0.001          0.999
    ================================================================================

VAR Estimation
^^^^^^^^^^^^^^

.. code-block:: none

    ' EViews
    var myvar.ls 1 2 dln_inv dln_inc dln_consump

::

    // GAUSS
    library tsmt;

    // Load Lutkepohl data (included with TSMT)
    data = loadd(getGAUSSHome("pkgs/tsmt/examples/lutkepohl2.gdat"));

    // Select variables and estimate VAR
    y = data[., "dln_inv" "dln_inc" "dln_consump"];

    struct svarOut sout;
    sout = svarFit(y);

**Accessing VAR results:**

.. code-block:: none

    ' EViews
    myvar.@coefs
    myvar.@residcov

::

    // GAUSS - results stored in structure members
    print sout.coefficients;  // Coefficient matrix
    print sout.residuals;     // Residuals
    print sout.aic;           // Information criteria
    print sout.sbc;

Impulse Response Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

    ' EViews
    myvar.impulse(10, a, m) dln_inv dln_inc dln_consump

::

    // GAUSS - IRF computed as part of svarFit, just plot it
    plotIRF(sout);

    // Access the IRF matrices directly
    print sout.irf;

Forecast Error Variance Decomposition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

    ' EViews
    myvar.decomp(10) dln_inv dln_inc dln_consump

::

    // GAUSS
    plotFEVD(sout);       // Plot variance decomposition

    // Historical decomposition
    plotHD(sout);

GARCH
^^^^^

.. code-block:: none

    ' EViews
    equation eq1.arch(1,1) y c

::

    // GAUSS
    library tsmt;

    y = loadd(getGAUSSHome("pkgs/tsmt/examples/garch.dat"));

    struct garchEstimation gOut;
    gOut = garchFit(y, 1, 1);

Output::

    ================================================================================
    Model:                   GARCH(1,1)          Dependent variable:               Y
    Time Span:                  Unknown          Valid cases:                    300
    ================================================================================
                                 Coefficient            Upper CI            Lower CI

              beta0[1,1]             0.01208            -0.00351             0.02768
              garch[1,1]             0.15215            -0.46226             0.76655
              arch[1,1]              0.18499             0.01761             0.35236
              omega[1,1]             0.01429             0.00182             0.02675
    ================================================================================

                    AIC:                                                   315.54085
                    LRS:                                                   307.54085

For GJR-GARCH (asymmetric), use :func:`garchGJRFit`. For IGARCH, use :func:`igarchFit`.

Unit Root Tests
^^^^^^^^^^^^^^^

.. code-block:: none

    ' EViews
    y.uroot(adf, 4)
    y.uroot(kpss)

::

    // GAUSS (TSMT)
    library tsmt;

    // DF-GLS test (Elliott, Rothenberg, Stock 1996)
    { tstat, crit } = dfgls(y, 4);       // max 4 lags

    // KPSS stationarity test
    { tstat, crit } = kpss(y, 4);        // max 4 lags

TSMT includes :func:`dfgls` (DF-GLS), :func:`kpss` (KPSS stationarity test), and the Zivot-Andrews structural break test. Results include test statistics and critical values at standard significance levels.

Forecasting
^^^^^^^^^^^

.. code-block:: none

    ' EViews
    myvar.forecast(e) 12

::

    // GAUSS - forecast from a VARMA model
    library tsmt;

    // Estimate and forecast
    struct varmamtOut vOut;
    vOut = varmaFit(y, 2, 0);         // VAR(2)
    fcast = varmaPredict(vOut, y, 0, 12);   // 12 periods ahead (y=data, 0=no exog)

Plotting
--------

EViews has rich graph objects. GAUSS's graphics library covers the same ground:

::

    // GAUSS
    plotXY(x, y);                     // Line plot
    plotScatter(x, y);                // Scatter plot
    plotHist(x, 20);                  // Histogram with 20 bins
    plotBox(data, "val ~ group");     // Box plot
    plotBar(labels, heights);         // Bar chart
    plotTS(1960, 4, data[., "gdp"]);  // Time series plot (start year, frequency, data)

**Customizing plots** uses a :class:`plotControl` structure -- think of it as configuring chart options before drawing:

::

    // Create a scatter plot with title and labels
    struct plotControl myPlot;
    myPlot = plotGetDefaults("scatter");

    plotSetTitle(&myPlot, "MPG vs Weight");
    plotSetXLabel(&myPlot, "Weight (lbs)");
    plotSetYLabel(&myPlot, "Miles per gallon");
    plotSetLegend(&myPlot, "Domestic" $| "Foreign");

    plotScatter(myPlot, auto2[., "weight"], auto2[., "mpg"]);

**Subplots and saving:**

::

    plotLayout(2, 1, 1);            // 2 rows, 1 col, position 1
    plotSave("plot.png", 640|480);  // Save with size (width|height in pixels)

Functions and Procedures
------------------------

EViews subroutines are limited to basic operations. GAUSS has a full procedure system:

.. code-block:: none

    ' EViews
    subroutine my_func(scalar x, scalar y)
        %result = x + y
    endsub

::

    // GAUSS
    proc (1) = my_func(x, y);
        local result;
        result = x + y;
        retp(result);
    endp;

    answer = my_func(3, 4);   // answer = 7

**Key points:**

- ``proc (n) =`` declares the number of return values
- ``local`` declares variables scoped to this procedure (see warning below)
- ``retp()`` returns values
- ``endp`` ends the procedure
- Procedures can be defined anywhere in the file -- before or after the code that calls them

**Multiple outputs:**

::

    proc (2) = stats(x);
        local mn, sd;
        mn = meanc(x);
        sd = stdc(x);
        retp(mn, sd);
    endp;

    { my_mean, my_std } = stats(rndn(100, 1));

.. warning::

    **Variables are global by default.** In GAUSS, you must declare variables with ``local`` inside ``proc`` or they become globals that persist after the procedure returns. Forgetting ``local`` creates hard-to-find bugs where procedures silently modify variables in the calling scope. Make it a habit to declare ``local`` for every variable inside a ``proc``.

Control Flow
------------

.. code-block:: none

    ' EViews
    for !i = 1 to 10
        ' do something
    next

    if condition then
        ' do something
    endif

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

    do while x > 0;
        x = x - 1;
    endo;

**Note:** GAUSS requires semicolons after control statements (``if``, ``for``, ``else``, etc.). Inside a ``proc``, remember to declare loop variables with ``local``.

Common Operations: Quick Reference
-----------------------------------

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Task
      - EViews
      - GAUSS
    * - Load file
      - ``import "file.xlsx"``
      - ``loadd("file.xlsx")``
    * - Natural log
      - ``log(y)``
      - ``ln(y)``
    * - Log base 10
      - ``@log10(y)``
      - ``log(y)``
    * - First difference
      - ``d(y)``
      - ``y - lagn(y, 1)``
    * - Lag
      - ``y(-1)``
      - ``lagn(y, 1)``
    * - OLS
      - ``equation.ls y c x1 x2``
      - ``olsmt(data, "y ~ x1 + x2")``
    * - ARIMA
      - ``eq.ls y c ar(1) ma(1)``
      - ``arimaFit(y, 1, 0, 1)``
    * - VAR
      - ``var.ls 1 2 y1 y2``
      - ``svarFit(data[., "y1" "y2"])``
    * - GARCH(1,1)
      - ``eq.arch(1,1) y c``
      - ``garchFit(y, 1, 1)``
    * - Unit root test
      - ``y.uroot(adf, 4)``
      - ``dfgls(y, 4)``
    * - Stationarity test
      - ``y.uroot(kpss)``
      - ``kpss(y, 4)``
    * - IRF plot
      - ``var.impulse(10)``
      - ``plotIRF(sout)``
    * - Descriptive stats
      - ``y.stats``
      - ``call dstatmt(y)``
    * - Scatter plot
      - ``scat x y``
      - ``plotScatter(x, y)``
    * - Export
      - ``write "output.xlsx"``
      - ``saved(data, "output.xlsx")``
    * - Sort
      - ``sort x``
      - ``sortc(df, "x")``
    * - Filter
      - ``smpl if x > 5``
      - ``selif(df, df[., "x"] .> 5)``
    * - Drop missing
      - ``smpl if y <> NA``
      - ``packr(df)``
    * - Print
      - ``show x``
      - ``print x;``
    * - Comment
      - ``' comment``
      - ``// comment``

.. note::

    **Reminder:** EViews's ``log()`` is natural log. GAUSS's ``log()`` is base 10. Use ``ln()``. See the full warning in the `Data <#data-workfiles-vs-dataframes>`__ section above.

Common Gotchas
--------------

1. **Semicolons required.** Every statement ends with ``;``. This is the first thing EViews users forget.

2. **log() is base 10, ln() is natural log.** EViews's ``log`` = GAUSS's ``ln``.

3. **Operators are explicit.** ``*`` is matrix multiply, ``.*`` is element-wise. ``>`` is a scalar test, ``.>`` is element-wise.

4. **``|`` is concatenation, not OR.** Use ``.or`` for logical OR, ``.and`` for AND.

5. **No boolean indexing.** ``df[condition, .]`` does not filter. Use ``selif(df, condition)``.

6. **Declare ``local`` in procedures.** Without ``local``, variables leak to the global scope.

7. **String operators need ``$``.** Use ``$+`` for concatenation, ``$==`` for equality.

8. **The ``call`` keyword.** Use ``call functionName(...)`` to run a function and discard its return value. This is useful for printing summaries: ``call olsmt(data, "y ~ x1");`` prints without saving.

9. **No negative indexing.** Use ``rows(x)`` for the last row, ``cols(x)`` for the last column.

Putting It Together
-------------------

Here is a complete, runnable example that loads data, creates variables, plots, and runs a regression. Press F5 to run it.

::

    // Load the auto2 dataset bundled with GAUSS
    auto2 = loadd(getGAUSSHome("examples/auto2.dta"));

    // Summary statistics
    call dstatmt(auto2[., "price" "mpg" "weight"]);

    // Keep only domestic cars
    domestic = selif(auto2, auto2[., "foreign"] .== 0);

    // Add a new variable
    domestic = dfaddcol(domestic, "price_k", domestic[., "price"] ./ 1000);

    // Scatter plot with title
    struct plotControl myPlot;
    myPlot = plotGetDefaults("scatter");
    plotSetTitle(&myPlot, "Weight vs MPG (Domestic Cars)");
    plotSetXLabel(&myPlot, "Weight (lbs)");
    plotSetYLabel(&myPlot, "Miles per gallon");
    plotScatter(myPlot, domestic[., "weight"], domestic[., "mpg"]);

    // OLS regression: how does weight affect fuel efficiency?
    struct olsmtOut out;
    out = olsmt(domestic, "mpg ~ weight");

    // Print key results
    print "Coefficients:"; print out.b;
    print "Standard errors:"; print out.stderr;
    print "R-squared:"; print out.rsq;

What's Next?
------------

- :doc:`../getting-started/quickstart` -- 10-minute introduction to GAUSS basics
- :doc:`../getting-started/running-existing-code` -- If you inherited GAUSS code and need to get it running
- :doc:`../data-management` -- Loading, cleaning, and reshaping data
- :doc:`../textbook-examples/index` -- Worked examples from Greene (*Econometric Analysis*) and Brooks (*Introductory Econometrics for Finance*)
- `Command Reference <../command-reference.html>`__ -- Browse all 1,000+ built-in functions
- `Econometrics blog <https://www.aptech.com/blog/category/econometrics/>`__ -- Fully worked examples covering regression, panel data, hypothesis testing, and more
- `Time series blog <https://www.aptech.com/blog/category/time-series/>`__ -- ARIMA, VAR, GARCH, cointegration, and forecasting tutorials with complete code

.. seealso::

    :func:`loadd`, :func:`olsmt`, :func:`selif`, :func:`plotXY`, :func:`packr`, :func:`arimaFit`, :func:`svarFit`, :func:`garchFit`, :func:`dfgls`, :func:`kpss`, :func:`plotIRF`
