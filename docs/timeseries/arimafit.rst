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

Model
-----

**ARIMA(p,d,q):**
After differencing :math:`d` times, the series :math:`w_t = (1-L)^d y_t` follows a
stationary ARMA(p,q) process:

.. math::

   w_t = \phi_1 w_{t-1} + \cdots + \phi_p w_{t-p} + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \cdots + \theta_q \varepsilon_{t-q}

where :math:`\varepsilon_t \sim N(0, \sigma^2)`. In backshift operator notation:

.. math::

   \phi(L)(1 - L)^d \, y_t = \theta(L) \, \varepsilon_t

**SARIMA(p,d,q)(P,D,Q)[s]:**
Adds seasonal differencing and seasonal ARMA terms:

.. math::

   \Phi(L^s) \, \phi(L) \, (1 - L)^d (1 - L^s)^D \, y_t = \Theta(L^s) \, \theta(L) \, \varepsilon_t

where :math:`\Phi(L^s) = 1 - \Phi_1 L^s - \cdots - \Phi_P L^{Ps}` and
:math:`\Theta(L^s) = 1 + \Theta_1 L^s + \cdots + \Theta_Q L^{Qs}`.

**ARIMAX (regression with ARIMA errors):**
When exogenous regressors :math:`X_t` are provided:

.. math::

   y_t = X_t' \beta + \eta_t, \qquad \phi(L)(1-L)^d \, \eta_t = \theta(L) \, \varepsilon_t

This is a *regression with ARIMA errors* model (Hyndman & Athanasopoulos 2021, Ch. 10),
not a transfer function model. The distinction matters: the AR/MA structure applies to
the regression residuals, not directly to :math:`y_t`.
Algorithm
---------

**Estimation (CSS-ML):**

1. **Conditional sum of squares (CSS):** Condition on the first :math:`\max(p, s \cdot P)` observations and minimize the sum of squared one-step-ahead prediction errors. This provides fast initial parameter estimates. Complexity: :math:`O(N)`.

2. **Maximum likelihood refinement (ML):** Starting from the CSS estimates, maximize the exact Gaussian log-likelihood via the state-space representation and Kalman filter. The likelihood is:

   .. math::

      \log \mathcal{L} = -\frac{N}{2} \log(2\pi) - \frac{1}{2} \sum_{t=1}^{N} \left( \log f_t + \frac{v_t^2}{f_t} \right)

   where :math:`v_t` and :math:`f_t` are the innovation and its variance from the Kalman filter. Optimization uses L-BFGS-B with parameter transforms to enforce stationarity and invertibility.

**Auto-selection (stepwise):**

When ``order`` is omitted, the Hyndman-Khandakar (2008) stepwise algorithm is used:

1. Determine :math:`d` via KPSS unit root tests (Kwiatkowski et al. 1992).
2. Determine :math:`D` via OCSB seasonal unit root tests (Osborn, Chui, Smith & Birchenhall 1988), if seasonal.
3. Fit an initial model, then search neighboring orders in a stepwise fashion, minimizing AICc (default) or the criterion in *ctl.ic*.
4. Total models evaluated is typically 15-30 (vs. hundreds for exhaustive search).

Set ``ctl.stepwise = 0`` for exhaustive search over all :math:`(p, q, P, Q)` combinations up to *ctl.max_order*.
Examples
--------

Auto ARIMA on Airline Passengers
++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Automatic ARIMA — selects order via AICc
    result = arimaFit(y);

Output:

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
Seasonal ARIMA on Monthly Data
++++++++++++++++++++++++++++++

The classic Box-Jenkins airline model — SARIMA(0,1,1)(0,1,1)[12]:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Auto SARIMA with season=12
    result = arimaFit(y, 12);

Selects SARIMA(0,1,1)(0,1,1)[12] — the same model identified by Box & Jenkins (1970)
on this dataset. The seasonal MA(1) coefficient captures the within-year pattern, while
regular differencing and seasonal differencing handle trend and annual cycles.

Fixed Order with Diagnostics
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Force SARIMA(1,1,1)(0,1,1)[12]
    result = arimaFit(y, 12, 1, 1, 1, 0, 1, 1);

Check the Ljung-Box statistic for residual autocorrelation: p > 0.05 indicates no
remaining serial correlation. Check Jarque-Bera for normality: p > 0.05 indicates
Gaussian residuals.

ARIMAX: GDP with Leading Indicators
++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "cpi + ffr");

    // Regression with ARIMA errors
    result = arimaFit(y, xreg=X, xreg_names="CPI"$|"FFR");

The exogenous coefficients are reported alongside the ARIMA parameters.
Use :func:`arimaForecast` with ``xreg=X_future`` to produce forecasts conditional
on projected regressor values.

Partial Auto-Selection
++++++++++++++++++++++

Fix :math:`d = 1` but auto-select :math:`p` and :math:`q`:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    // Fix d=1, auto-select p and q
    // season=12, fix d=1, auto-select p and q (use -1)
    result = arimaFit(y, 12, -1, 1, -1);

Using BIC for Model Selection
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    ctl = arimaControlCreate();
    ctl.ic = "bic";

    result = arimaFit(y, ctl, season=12);

BIC penalizes model complexity more than AICc, typically selecting more parsimonious models.
Troubleshooting
---------------

**Optimizer did not converge:**
Increase ``ctl.max_iter`` (default 1000) or switch to ``ctl.method = "css"`` for a
quick approximate estimate. Non-convergence often indicates the model is
over-parameterized for the data — try a simpler order.

**Near-unit-root MA coefficient:**
If :math:`|\theta_q|` or :math:`|\Theta_Q|` is close to 1.0, the model is near
the boundary of invertibility. The MA polynomial is nearly non-invertible, which
causes numerical issues. Solutions:

- Increase the differencing order by 1 (replace MA near-unit-root with a difference).
- Use ``ctl.method = "ml"`` instead of ``"css-ml"`` — CSS initialization can sometimes
  find a near-boundary starting point that ML refinement cannot escape.

**CSS and ML give different answers:**
CSS conditions on initial values and optimizes a different objective than exact ML.
Small discrepancies (< 0.02 in coefficients) are normal. Large discrepancies suggest
the likelihood surface has multiple modes — try ``ctl.method = "ml"`` with different
starting values, or simplify the model.

**Auto-selection picks a simple model when you expected a complex one:**
AICc penalizes complexity. If you believe a more complex model is correct, fix the
order explicitly with ``order=p|d|q`` and compare the diagnostic statistics. Remember
that more parsimonious models often forecast better even when the true DGP is complex
(Hyndman & Athanasopoulos 2021, Section 8.6).

**Residual autocorrelation (Ljung-Box p < 0.05):**
The model has not captured all the serial dependence. Try:

- Increasing the AR order (higher p).
- Adding seasonal terms if the data has a seasonal pattern.
- Adding exogenous regressors if there is an omitted variable.
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

This matches the behavior of R's ``auto.arima`` (Hyndman & Khandakar 2008).

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
Verification
------------

Verified against **three** independent reference implementations:

**R ``forecast`` package (Hyndman et al.):**
Cross-validated on 15+ classic time series datasets (Nile, AirPassengers, USAccDeaths,
CO2, LakeHuron, WWWusage, sunspot.year, nottem, UKgas, JohnsonJohnson, austres, lynx)
covering ARIMA, SARIMA, and ARIMAX models. Tests verify coefficients, standard errors,
log-likelihood, information criteria, and forecasts.

**Python ``statsmodels`` SARIMAX:**
Same datasets and model specifications re-verified against Python's state-space SARIMAX
implementation. Coefficients match to :math:`10^{-4}` on most models.

**Julia:**
Additional cross-validation on a subset of datasets against Julia time series packages.

**Unit root tests:**
KPSS test verified against R ``urca::ur.kpss()`` on 5 datasets. OCSB seasonal unit
root test (``nsdiffs``) verified against R ``forecast::nsdiffs()`` on 4 seasonal series.

Total: **65 passing tests** across R, Python, and Julia references.
See ``gausslib-ts/tests/r_regression.rs``.
References
----------

- Box, G.E.P. and G.M. Jenkins (1970). *Time Series Analysis: Forecasting and Control*. Holden-Day.
- Brockwell, P.J. and R.A. Davis (2002). *Introduction to Time Series and Forecasting*. 2nd ed., Springer.
- Hyndman, R.J. and Y. Khandakar (2008). "Automatic time series forecasting: The forecast package for R." *Journal of Statistical Software*, 27(3).
- Hyndman, R.J. and G. Athanasopoulos (2021). *Forecasting: Principles and Practice*. 3rd ed., OTexts.
- Kwiatkowski, D., P.C.B. Phillips, P. Schmidt, and Y. Shin (1992). "Testing the null hypothesis of stationarity against the alternative of a unit root." *Journal of Econometrics*, 54(1-3), 159-178.
Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaForecast`, :func:`arimaControlCreate`, :func:`arimaResults`, :func:`arimaCoefTable`, :func:`stlDecompose`
