
Introduction to GAUSS for EViews Users
======================================

This guide helps EViews users transition to GAUSS. If you're comfortable with VAR models, IRFs, and time series analysis in EViews, you'll find GAUSS handles the same workflows with a code-first approach that offers more flexibility and reproducibility.

What Sets GAUSS Apart
---------------------

- **Reproducibility**: Your entire analysis is code—version-controlled, shareable, auditable.
- **Flexibility**: Custom estimators, non-standard models, simulation studies, bootstrap—anything you can write, you can estimate.
- **Speed**: Compiled code with highly optimized BLAS for computationally intensive work like Monte Carlo and bootstrapping.
- **Extensibility**: Build your own procedures and share them. Full programming language, not a scripting layer on top of a GUI.

Key Conceptual Differences
--------------------------

+-------------------+---------------------------+---------------------------+
| Concept           | EViews                    | GAUSS                     |
+===================+===========================+===========================+
| Data storage      | Workfile with series      | Matrices and dataframes   |
+-------------------+---------------------------+---------------------------+
| Model objects     | Equation, VAR, System     | Output structures         |
+-------------------+---------------------------+---------------------------+
| Workflow          | GUI dialogs + commands    | Code only                 |
+-------------------+---------------------------+---------------------------+
| Results access    | Object views              | Structure members         |
+-------------------+---------------------------+---------------------------+
| Reproducibility   | Program files (.prg)      | All work is code          |
+-------------------+---------------------------+---------------------------+

Data: Workfiles vs. Dataframes
------------------------------

In EViews, you create a workfile and import series:

.. code-block:: none

    ' EViews
    wfcreate q 1960Q1 2020Q4
    import "gdp_data.xlsx"

In GAUSS, you load data directly into a dataframe:

::

    // GAUSS
    data = loadd("gdp_data.xlsx");

    // Check what you loaded
    print getcolnames(data)';
    print rows(data) "observations";

**Accessing variables:**

.. code-block:: none

    ' EViews - reference by name
    show gdp

::

    // GAUSS - index by column name
    gdp = data[., "gdp"];

    // Or by column number
    gdp = data[., 1];

    // View first 10 rows
    print data[1:10, .];

**Creating new variables:**

.. code-block:: none

    ' EViews
    series dlog_gdp = dlog(gdp)

::

    // GAUSS
    dlog_gdp = ln(data[2:rows(data), "gdp"]) - ln(data[1:rows(data)-1, "gdp"]);

    // Or use the diff function
    dlog_gdp = ln(data[., "gdp"]);
    dlog_gdp = dlog_gdp[2:rows(dlog_gdp)] - dlog_gdp[1:rows(dlog_gdp)-1];

Time Series Estimation
----------------------

ARIMA
^^^^^

.. code-block:: none

    ' EViews
    equation eq1.ls d(gdp) c ar(1) ma(1)

::

    // GAUSS
    library tsmt;

    // Load unemployment rate data
    data = loadd(getGAUSSHome() $+ "examples/UNRATE.csv");
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

    // Specify variables
    formula = "dln_inv + dln_inc + dln_consump";

    // Estimate VAR
    struct svarOut sout;
    sout = svarFit(data, formula);

The output displays coefficient estimates, standard errors, and diagnostics for each equation.

**Accessing VAR results:**

.. code-block:: none

    ' EViews
    myvar.@coefs
    myvar.@residcov

::

    // GAUSS - results stored in structure members
    print sout.beta;      // Coefficient matrix
    print sout.sigma;     // Residual covariance
    print sout.aic;       // Information criteria
    print sout.sbc;

Impulse Response Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

    ' EViews
    myvar.impulse(10, a, m) dln_inv dln_inc dln_consump

::

    // GAUSS
    // IRF is computed as part of svarFit
    // Plot the impulse responses
    plotIRF(sout);

    // Access IRF matrices directly
    print sout.irfs;

Forecasting
^^^^^^^^^^^

.. code-block:: none

    ' EViews
    myvar.forecast(e) 12

::

    // GAUSS
    // Forecast 12 periods ahead
    struct varmamtOut vOut;
    vOut = varmaFit(y, 2, 0);  // VAR(2)

    // Get forecasts
    fcast = varmaPredict(vOut, 12);

Granger Causality
^^^^^^^^^^^^^^^^^

.. code-block:: none

    ' EViews
    myvar.testexog dln_inv

::

    // GAUSS
    // Granger causality is part of the standard VAR output
    // Check the printed output from svarFit

Common Operations: Quick Reference
----------------------------------

+-------------------------+---------------------------+---------------------------+
| Task                    | EViews                    | GAUSS                     |
+=========================+===========================+===========================+
| Load Excel file         | ``import "file.xlsx"``    | ``loadd("file.xlsx")``    |
+-------------------------+---------------------------+---------------------------+
| Log transform           | ``series ly = log(y)``    | ``ly = ln(y);``           |
+-------------------------+---------------------------+---------------------------+
| First difference        | ``series dy = d(y)``      | ``dy = y[2:n] - y[1:n-1];``|
+-------------------------+---------------------------+---------------------------+
| OLS regression          | ``equation.ls y c x1 x2`` | ``olsmt(data, "y~x1+x2")``|
+-------------------------+---------------------------+---------------------------+
| Unit root test          | ``y.uroot(adf,4)``        | ``adf(y, 4)``             |
+-------------------------+---------------------------+---------------------------+
| Estimate ARIMA          | ``eq.ls y c ar(1) ma(1)`` | ``arimaFit(y, 1, 0, 1)``  |
+-------------------------+---------------------------+---------------------------+
| Estimate VAR            | ``var.ls 1 2 y1 y2``      | ``svarFit(data, "y1+y2")``|
+-------------------------+---------------------------+---------------------------+
| Compute IRF             | ``var.impulse(10)``       | ``plotIRF(sout)``         |
+-------------------------+---------------------------+---------------------------+
| Export to Excel         | ``write "output.xlsx"``   | ``xlsWrite(data, "f.xlsx")``|
+-------------------------+---------------------------+---------------------------+

TSMT: The Time Series Toolkit
-----------------------------

Most time series functionality in GAUSS comes from **TSMT** (Time Series MT), an add-on package. It includes:

- ARIMA, SARIMA estimation and forecasting
- VAR/VECM models with IRF and FEVD
- Structural VAR with multiple identification schemes
- GARCH family models
- State-space models and Kalman filtering
- Unit root and cointegration tests
- Rolling window estimation

If you're doing serious time series work, TSMT is essential.

**Check if TSMT is installed:**

::

    library tsmt;
    print "TSMT loaded successfully";

If this errors, contact Aptech to add TSMT to your license.

Complete VAR Workflow Example
-----------------------------

Here's a complete VAR analysis workflow, from data loading to results:

::

    new;
    library tsmt;

    // 1. Load data
    data = loadd(getGAUSSHome("pkgs/tsmt/examples/lutkepohl2.gdat"));

    // 2. Check the data
    print "Variables:" getcolnames(data)';
    print "Sample size:" rows(data);

    // 3. Specify model
    formula = "dln_inv + dln_inc + dln_consump";

    // 4. Estimate VAR
    struct svarOut sout;
    sout = svarFit(data, formula);

    // 5. View results (automatic output includes)
    //    - Coefficient estimates with std errors
    //    - Model fit statistics (AIC, SBC)
    //    - Diagnostic tests

    // 6. Plot impulse response functions
    plotIRF(sout);

    // 7. Plot forecast error variance decomposition
    plotFEVD(sout);

    // 8. Historical decomposition
    plotHD(sout);

    // 9. Access specific results
    print "AIC:" sout.aic;
    print "Residual covariance:";
    print sout.sigma;

Tips for EViews Users
---------------------

1. **Everything is code.** There's no way to estimate a VAR by clicking. This is a feature—your analysis is reproducible.

2. **Results go into structures.** EViews creates "objects" you view in windows. GAUSS stores results in structures you access with dot notation (``sout.aic``, ``sout.beta``).

3. **Use the documentation.** Press F1 on any function name in the GAUSS IDE to see its help page.

4. **TSMT is your friend.** For time series work, nearly everything you need is in TSMT.

5. **The learning curve is real.** Budget time to learn GAUSS syntax. The payoff is flexibility and reproducibility you can't get from a GUI.

What's Next?
------------

- :doc:`../getting-started/quickstart` — General GAUSS introduction
- :doc:`../data-management` — Data import, export, manipulation
- TSMT User Guide — Detailed time series documentation (Help → TSMT)

.. seealso::

    :func:`arimaFit`, :func:`svarFit`, :func:`varmaFit`, :func:`adf`, :func:`plotIRF`
