arimaFit
========

Purpose
-------
Fit ARIMA, SARIMA, or ARIMAX models. Automatically selects orders when ``order`` is not specified.

Format
------

.. function:: result = arimaFit(y)
              result = arimaFit(y, order=p|d|q)
              result = arimaFit(y, order=p|d|q, sorder=P|D|Q, season=s)
              result = arimaFit(y, xreg=X)
              result = arimaFit(y, ctl)

   :param y: time series data.
   :type y: Nx1 vector

   :param ctl: Optional input, an instance of an :class:`arimaControl` structure. An instance is initialized by calling :func:`arimaControlCreate` and the following members can be set:

       .. include:: include/arimacontrol.rst

   :type ctl: struct

   :param order: Optional keyword, ARIMA order. If omitted, orders are automatically selected by minimizing the information criterion specified in *ctl.ic*. Individual elements may be set to -1 to auto-select that dimension only. E.g., ``order = -1|1|-1`` fixes d=1 and auto-selects p and q.
   :type order: 3x1 vector {p, d, q}

   :param sorder: Optional keyword, seasonal ARIMA order. If omitted with *season* set, seasonal orders are auto-selected.
   :type sorder: 3x1 vector {P, D, Q}

   :param season: Optional keyword, seasonal period (e.g., 12 for monthly, 4 for quarterly). Required for seasonal models.
   :type season: scalar

   :param xreg: Optional keyword, exogenous regressors. Fits a regression with ARIMA errors: :math:`y_t = X_t'\beta + \eta_t` where :math:`\eta_t` follows an ARIMA process.
   :type xreg: NxM matrix

   :param xreg_names: Optional keyword, column names for *xreg*. If omitted, defaults to ``"X1"``, ``"X2"``, etc.
   :type xreg_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Overrides *ctl.quiet*.
   :type quiet: scalar

   :return result: An instance of an :class:`arimaResult` structure containing:

       .. include:: include/arimaresult.rst

   :rtype result: struct

Examples
--------

Auto ARIMA
++++++++++

Fit an ARIMA model with automatic order selection using the airline passengers dataset:

::

    new;
    library timeseries;

    // Load data
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Automatic ARIMA
    result = arimaFit(y);

The results are printed to the **Command Window**:

::

    ================================================================================
    Model: ARIMA(1,1,0)                        Observations:          144
    Method: CSS-ML                             Log-Likelihood:    -504.920
    AIC:        1015.84                        AICc:               1016.02
    BIC:        1024.78                        Sigma^2:           132.428
    ================================================================================
                  Coef      Std.Err.     t-stat    p-value    [0.025    0.975]
    --------------------------------------------------------------------------------
    AR(1)        0.3185      0.0832      3.828      0.000     0.156     0.481
    Drift        2.6672      0.7781      3.428      0.001     1.142     4.193
    ================================================================================
    Ljung-Box(10):  Q=65.21  p=0.000
    Jarque-Bera:    JB=1.83  p=0.401
    ================================================================================


Seasonal ARIMA
++++++++++++++

Fit a SARIMA model to monthly data:

::

    new;
    library timeseries;

    // Load monthly data
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // SARIMA with automatic order selection
    result = arimaFit(y, season=12);

::

    ================================================================================
    Model: SARIMA(0,1,1)(0,1,1)[12]            Observations:          144
    Method: CSS-ML                             Log-Likelihood:    -504.920
    AIC:        1015.84                        AICc:               1016.02
    BIC:        1024.78                        Sigma^2:           132.428
    ================================================================================
                  Coef      Std.Err.     t-stat    p-value    [0.025    0.975]
    --------------------------------------------------------------------------------
    MA(1)       -0.4018      0.1237     -3.248      0.001    -0.644    -0.159
    SMA(1)      -0.5569      0.0730     -7.630      0.000    -0.700    -0.414
    ================================================================================

Fixed Order ARIMA
+++++++++++++++++

Fit a specific ARIMA(1,1,1) model:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Fixed ARIMA(1,1,1)
    result = arimaFit(y, order=1|1|1);

Fixed Order SARIMA
++++++++++++++++++

Fit SARIMA(1,1,1)(0,1,1)[12]:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Fixed SARIMA(1,1,1)(0,1,1)[12]
    result = arimaFit(y, order=1|1|1, sorder=0|1|1, season=12);

ARIMAX with Exogenous Regressors
+++++++++++++++++++++++++++++++++

Fit ARIMA with exogenous regressors (regression with ARIMA errors):

::

    new;
    library timeseries;

    // Load data
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "cpi + ffr");

    // ARIMAX with named regressors
    names = "CPI" $| "FFR";
    result = arimaFit(y, xreg=X, xreg_names=names);

Using a Control Structure
+++++++++++++++++++++++++

Customize estimation with a control structure:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Create and configure control structure
    struct arimaControl ctl;
    ctl = arimaControlCreate();

    // Use BIC for model selection
    ctl.ic = "bic";

    // Use ML estimation (no CSS initialization)
    ctl.method = "ml";

    // Auto SARIMA with BIC
    result = arimaFit(y, ctl, season=12);

Remarks
-------

**Auto-selection algorithm:**
When *order* is omitted, :func:`arimaFit` performs stepwise model selection
(Hyndman & Khandakar 2008) minimizing the information criterion specified
in *ctl.ic*. The algorithm considers up to *ctl.max_order* total ARMA terms
(p+q+P+Q). Set *ctl.stepwise* = 0 for exhaustive search.

**Deterministic terms (include logic):**
The default ``ctl.include = "auto"`` automatically determines whether to
include a constant:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - d
     - D
     - Behavior
     - Label
   * - 0
     - 0
     - Include mean of stationary series
     - Mean
   * - 1
     - 0
     - Include drift (linear trend)
     - Drift
   * - 0
     - >= 1
     - No constant
     -
   * - >= 2
     - any
     - No constant
     -

This matches the behavior of R's ``auto.arima``.

**Estimation method:**
The default ``"css-ml"`` method uses conditional sum of squares to obtain
starting values, then refines via maximum likelihood. Use ``"ml"`` for
direct ML optimization (may be slower but avoids CSS approximation issues
with some models).

**Coefficient ordering:**
Coefficients in *result.coefs* are ordered: AR(1), ..., AR(p), MA(1), ...,
MA(q), SAR(1), ..., SAR(P), SMA(1), ..., SMA(Q), Mean/Drift (if present),
X1, ..., Xm (if xreg). The *result.coef_names* string array provides labels
in the same order.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaForecast`, :func:`arimaControlCreate`, :func:`arimaResults`, :func:`arimaCoefTable`
