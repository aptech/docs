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

Model
-----

The conditional forecast solves: given that certain variables follow a prescribed
path, what is the posterior predictive distribution of the remaining (free) variables?

For a VAR with structural form :math:`\varepsilon_t = P^{-1} u_t` where
:math:`u_t = y_t - B_1 y_{t-1} - \cdots - B_p y_{t-p} - c`, the Waggoner & Zha (1999)
algorithm finds the structural shocks :math:`\varepsilon_{T+1}, \ldots, \varepsilon_{T+h}`
that satisfy the constraints exactly while being drawn from the correct conditional
distribution for the free variables.

The constrained forecast at horizon :math:`s` is:

.. math::

   y_{T+s} = B_1 y_{T+s-1} + \cdots + B_p y_{T+s-p} + c + P \varepsilon_{T+s}

where :math:`\varepsilon_{T+s}` is partitioned into constrained and free components,
and the free components are drawn from their conditional posterior.
Algorithm
---------

For each posterior draw :math:`(B^{(i)}, \Sigma^{(i)})`:

1. Compute :math:`P = \text{chol}(\Sigma^{(i)})'`.
2. Compute unconditional forecasts :math:`\tilde{y}_{T+1}, \ldots, \tilde{y}_{T+h}`.
3. For each constrained horizon, solve for the structural shocks that enforce the constraint: :math:`y_{T+s}^{\text{constrained}} - \tilde{y}_{T+s} = R \varepsilon_{T+s}^*` where :math:`R` selects the constrained variables.
4. Draw the free-variable shocks from :math:`N(0, I)`.
5. Combine constrained and free shocks, propagate through the VAR.

**Complexity:** :math:`O(n\_draws \cdot h \cdot m^3)`.
Troubleshooting
---------------

**"All variables constrained" error:**
At least one variable must be free at each horizon. The model needs degrees of
freedom to satisfy the constraints. If you need to fix all variables, you don't
need a forecast — you already know the answer.

**Free variable bands are very wide:**
This is expected when the constrained path is far from the unconditional forecast.
The model is telling you the scenario requires large structural shocks, which
create uncertainty in the free variables. Tighter priors help.

**Constraints are not exactly satisfied in output:**
Check for rounding in the print output. Internally, constraints are satisfied
to machine precision. The printed table rounds for display.
Verification
------------

Conditional forecasts verified against the ECB BEAR Toolbox conditional forecast
module on the 3-variable ECB dataset with FFR path constraints. Free-variable
forecasts agree within Monte Carlo noise.

See the :ref:`var-verification` page.
References
----------

- Waggoner, D.F. and T. Zha (1999). "Conditional forecasts in dynamic multivariate models." *Review of Economics and Statistics*, 81(4), 639-651.
- Banbura, M., D. Giannone, and M. Lenza (2015). "Conditional forecasts and scenario analysis with vector autoregressions for large cross-sections." *International Journal of Forecasting*, 31(3), 739-756.
Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarSvFit`, :func:`bvarForecast`, :func:`bvarSvForecast`
