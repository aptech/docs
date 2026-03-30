varForecast
===========

Purpose
-------
Generate h-step-ahead forecasts with confidence intervals from a fitted VAR model.

Format
------

.. function:: fc = varForecast(result, h)
              fc = varForecast(result, h, xreg=X_future)
              fc = varForecast(result, h, level=0.99)

   :param result: an instance of a :class:`varResult` structure returned by :func:`varFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxK matrix

   :param level: Optional keyword, confidence level for prediction intervals. Default = 0.95.
   :type level: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return fc: An instance of a :class:`forecastResult` structure containing:

       .. include:: include/forecastresult.rst

   :rtype fc: struct

Examples
--------

Basic VAR Forecast
++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

    // Fit VAR(4) and forecast 12 steps
    result = varFit(data, 4, quiet=1);

    fc = varForecast(result, 12);

The forecast table is printed to the **Command Window**:

::

    ================================================================================
    VAR(4) Forecast: 12 steps ahead              Level: 95%
    ================================================================================
             GDP                    CPI                    FFR
    h    Forecast  [Lower  Upper]  Forecast  [Lower  Upper]  Forecast  [Lower  Upper]
    ----------------------------------------------------------------------------------
     1     2.103  [ 1.82   2.39]    3.214  [ 2.91   3.52]    4.812  [ 4.21   5.41]
     2     2.087  [ 1.71   2.46]    3.198  [ 2.78   3.62]    4.795  [ 3.98   5.61]
       ⋮
    11     2.018  [ 1.12   2.92]    3.130  [ 2.13   4.13]    4.724  [ 2.98   6.47]
    12     2.011  [ 1.09   2.93]    3.122  [ 2.11   4.13]    4.718  [ 2.94   6.50]
    ================================================================================

Forecast with 99% Confidence Intervals
+++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4, quiet=1);

    // Wider intervals
    fc = varForecast(result, 24, level=0.99);

Forecast with Future Exogenous Regressors
+++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    y = loadd(fname, "gdp + cpi + ffr");
    X = loadd(fname, "oil");

    result = varFit(y, 2, xreg=X, quiet=1);

    // Future oil prices for 12 periods
    X_future = seqa(80, 2, 12);    // 80, 82, 84, ...
    fc = varForecast(result, 12, xreg=X_future);

Accessing Individual Variables
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4, quiet=1);
    fc = varForecast(result, 12, quiet=1);

    // GDP forecast (column 1)
    gdp_fc = fc.forecasts[., 1];
    gdp_lo = fc.lower[., 1];
    gdp_hi = fc.upper[., 1];

    print "GDP forecast with 95% CI:";
    print gdp_fc~gdp_lo~gdp_hi;

Remarks
-------

**Confidence intervals** are computed from the MSE matrix of the h-step-ahead
forecast error, assuming Gaussian innovations. Intervals widen with the forecast
horizon as uncertainty accumulates.

**Exogenous regressors:** If the model was fit with *xreg*, the *xreg* keyword
is required for forecasting. The matrix must have *h* rows and the same number
of columns as the original regressors. An error is raised if omitted.

**Non-stationary models:** Forecasts from non-stationary VARs (explosive
eigenvalues) may diverge rapidly. Check *result.is_stationary* before forecasting.

Model
-----

The h-step-ahead point forecast from a VAR(p) is:

.. math::

   \hat{y}_{T+h|T} = \hat{B}_1 \hat{y}_{T+h-1|T} + \cdots + \hat{B}_p \hat{y}_{T+h-p|T} + \hat{u}

where :math:`\hat{y}_{T+j|T} = y_{T+j}` for :math:`j \leq 0` (observed data) and
:math:`\hat{y}_{T+j|T}` is the forecast for :math:`j \geq 1`.

The confidence interval at horizon :math:`h` is:

.. math::

   \hat{y}_{T+h|T} \pm z_{\alpha/2} \sqrt{\text{diag}(\text{MSE}_h)}

where the mean squared error matrix is :math:`\text{MSE}_h = \sum_{j=0}^{h-1} \Phi_j \hat\Sigma \Phi_j'`
and :math:`\Phi_j = J F^j J'` are the impulse response matrices. Intervals widen with the
horizon as :math:`\text{MSE}_h` accumulates.


Algorithm
---------

1. **Recursive substitution:** Iterate the estimated VAR equations forward, replacing future observations with their forecasts.
2. **MSE computation:** Accumulate the forecast error covariance via the companion form.
3. **Intervals:** Gaussian quantiles applied to the diagonal of :math:`\text{MSE}_h`.

**Complexity:** :math:`O(h \cdot m^2 p^2)` — sub-millisecond.


Troubleshooting
---------------

**Forecasts diverge rapidly:**
The VAR is non-stationary (explosive eigenvalues). Check *result.is_stationary*.
Consider differencing the data or switching to :func:`bvarFit` with regularization.

**Confidence intervals are unrealistically narrow:**
Frequentist VAR intervals do not account for parameter estimation uncertainty —
they condition on :math:`\hat{B}` as if known. For intervals that reflect parameter
uncertainty, use :func:`bvarForecast` (Bayesian predictive density).


Verification
------------

VAR forecasts verified against R ``vars::predict()`` at :math:`10^{-6}` tolerance
on a 2-variable VAR(1) with known DGP. Point forecasts and forecast standard errors
match across 1-4 step horizons.

See ``gausslib-var/tests/r_benchmark.rs`` and the :ref:`var-verification` page.


References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 3.5.


Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`varFit`, :func:`bvarForecast`, :func:`bvarSvForecast`, :func:`fcScore`, :func:`dmTest`
