condForecast
============

Purpose
-------
Generate conditional (scenario) forecasts with hard constraints on variable paths.

Format
------

.. function:: cfc = condForecast(result, path)
              cfc = condForecast(result, path, xreg=X_future)
              cfc = condForecast(result, path, level=0.90)

   :param result: an instance of a :class:`bvarResult` or :class:`bvarSvResult` structure.
   :type result: struct

   :param path: constraint matrix. Finite values impose hard constraints; missing values (via :func:`miss`) indicate unconstrained cells. At least one variable must be unconstrained at each horizon.
   :type path: hxm matrix

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxK matrix

   :param level: Optional keyword, credible level for bands on free variables. Default = 0.68.
   :type level: scalar

   :param n_draws: Optional keyword, number of posterior draws for computing bands. Default = 1000.
   :type n_draws: scalar

   :param seed: Optional keyword, RNG seed for reproducibility. Default = 42.
   :type seed: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return cfc: An instance of a :class:`condForecastResult` structure containing:

       .. include:: include/condforecastresult.rst

   :rtype cfc: struct

Examples
--------

Fix One Variable, Forecast the Rest
++++++++++++++++++++++++++++++++++++

Fix the federal funds rate at 5.0% for 12 quarters and forecast GDP and CPI:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    result = bvarFit(data, ctl, quiet=1);

    // Build constraint path: 12 horizons, 3 variables (GDP, CPI, FFR)
    // miss() = unconstrained, finite = fixed
    path = miss(zeros(12, 3), 0);

    // Fix FFR (column 3) at 5.0 for all horizons
    path[., 3] = 5.0 * ones(12, 1);

    struct condForecastResult cfc;
    cfc = condForecast(result, path);

The conditional forecast table is printed:

::

    ================================================================================
    Conditional Forecast: 12 steps               Level: 68%
    Constraints: FFR fixed (all 12 horizons)     Draws: 1000
    ================================================================================
             GDP (free)             CPI (free)             FFR (fixed)
    h    Median [Lower Upper]     Median [Lower Upper]    Path
    ---------------------------------------------------------------------------
     1    2.103 [ 1.89  2.31]      3.214 [ 3.01  3.42]    5.000
     2    2.087 [ 1.78  2.39]      3.198 [ 2.89  3.51]    5.000
    ...
    ================================================================================

Compare Policy Scenarios
++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    result = bvarFit(data, ctl, quiet=1);

    // Scenario 1: FFR holds at 5.0
    path1 = miss(zeros(12, 3), 0);
    path1[., 3] = 5.0;

    // Scenario 2: FFR cut from 5.0 to 3.5 over 4 quarters, then hold
    path2 = miss(zeros(12, 3), 0);
    path2[., 3] = 5.0|4.5|4.0|3.5|3.5|3.5|3.5|3.5|3.5|3.5|3.5|3.5;

    cfc1 = condForecast(result, path1, quiet=1);
    cfc2 = condForecast(result, path2, quiet=1);

    print "GDP under rate hold:" cfc1.median[., 1];
    print "GDP under rate cut: " cfc2.median[., 1];
    print "Difference:         " cfc2.median[., 1] - cfc1.median[., 1];

Constrain Multiple Variables
++++++++++++++++++++++++++++

Fix both GDP growth and the FFR path, let CPI adjust:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    result = bvarFit(data, ctl, quiet=1);

    path = miss(zeros(8, 3), 0);

    // Fix GDP (column 1) at 2.0 for all horizons
    path[., 1] = 2.0;

    // Fix FFR (column 3) with a cutting path
    path[., 3] = 4.5|4.0|3.5|3.0|3.0|3.0|3.0|3.0;

    // CPI (column 2) is free
    cfc = condForecast(result, path);

    print "CPI under GDP=2%, FFR cutting:";
    print cfc.median[., 2];

Conditional Forecast from SV-BVAR
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarSvControl svctl;
    svctl = bvarSvControlCreate();
    svctl.p = 4;
    result = bvarSvFit(data, svctl, quiet=1);

    path = miss(zeros(12, 3), 0);
    path[., 3] = 5.0;

    // Works with bvarSvResult too
    cfc = condForecast(result, path, level=0.90);

Remarks
-------

**Algorithm:**
Implements the Waggoner & Zha (1999) conditional forecasting algorithm. For
each posterior draw :math:`(B^{(i)}, \Sigma^{(i)})`, the constrained variable
paths are imposed exactly and the free variables are drawn from their
conditional distribution. The reported bands reflect posterior uncertainty
in the free variables given the constraints.

**Building the constraint path:**

The *path* matrix has *h* rows and *m* columns (same number of variables as
the model). Use :func:`miss` to mark unconstrained cells:

::

    // Start with all-missing matrix (nothing constrained)
    path = miss(zeros(h, m), 0);

    // Fix variable j at value v for all horizons
    path[., j] = v * ones(h, 1);

    // Fix variable j at specific path
    path[., j] = v1|v2|v3|v4;

    // Fix at specific horizons only
    path[1:4, j] = v1|v2|v3|v4;    // Fix first 4, free after

**At least one variable must be unconstrained** at each horizon. Constraining
all variables leaves no degrees of freedom for the model.

**Credible bands** on free variables come from the posterior distribution of
:math:`(B, \Sigma)`. With more posterior draws (*n_draws*), the bands are
smoother but computation takes longer. Default of 1000 is typically sufficient.

Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarSvFit`, :func:`bvarForecast`, :func:`bvarSvForecast`
