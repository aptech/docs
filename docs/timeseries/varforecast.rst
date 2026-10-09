varForecast
===========

Purpose
-------
Generate h-step-ahead forecasts with confidence intervals from a fitted VAR model.

Format
------

.. function:: fc = varForecast(result, h)
              fc = varForecast(result, h, xreg_future=X_future)
              fc = varForecast(result, h, level=0.99)

   :param result: an instance of a :class:`varResult` structure returned by :func:`varFit`.
   :type result: struct

   :param h: positive integer forecast horizon (number of steps ahead).
   :type h: scalar

   :param xreg_future: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg_future: hxK matrix

   :param level: Optional keyword, central mass of each prediction band. Default = 0.95. Multiple masses must be strictly ascending and between 0 and 1. *levels* is an alias; supply only one of them.
   :type level: scalar or vector

   :param coef_uncertainty: Optional keyword, scalar 0 (default) for future shocks only, or 1 to add approximate coefficient estimation uncertainty. Only fits without trend or xreg are supported.
   :type coef_uncertainty: scalar

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

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"),
                 "gdp_growth + cpi_inflation + fed_funds");

    // Fit VAR(4) and forecast 12 steps
    result = varFit(data, 4, quiet=1);

    fc = varForecast(result, 12);

The forecast table and an interval note are printed to the **Command Window**.
The default note is ``Intervals include shocks only.``

Forecast with 99% Confidence Intervals
+++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"),
                 "gdp_growth + cpi_inflation + fed_funds");
    result = varFit(data, 4, quiet=1);

    // Wider intervals
    fc = varForecast(result, 24, level=0.99);

Forecast with Future Exogenous Regressors
+++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"),
              "gdp_growth + cpi_inflation + fed_funds");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"), "unemployment");

    result = varFit(y, 2, trend=1, xreg=X, quiet=1);

    // Assume unemployment stays at 5 for 12 periods
    // Supply only user xreg; the trend is extended automatically
    X_future = 5 * ones(12, 1);
    fc = varForecast(result, 12, xreg_future=X_future);

Adding coefficient uncertainty
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    canada_data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/canada.csv"));
    struct varResult fit_est;
    fit_est = varFit(canada_data, p=2, quiet=1);
    fc_est = varForecast(fit_est, 12, coef_uncertainty=1);

Accessing Individual Variables
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"),
                 "gdp_growth + cpi_inflation + fed_funds");
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

**Covariance and coefficient uncertainty.** Standard errors and bands use
*result.sigma*, following the fit's *resid_cov* choice. The default
``coef_uncertainty=0`` includes only future shocks. With
``coef_uncertainty=1``, the MSE also includes the approximate estimation
term of Lutkepohl (2005, section 3.5.2), divided by T - p. This approximation
assumes a stable VAR; the function does not reject an unstable fit on this
basis, so check *result.is_stationary*. Trend or xreg fits raise an error.
When printing is enabled, the note says ``Intervals include shocks and
approximate coefficient uncertainty.``

**Trend.** A fitted trend continues automatically with values T + 1, T + 2,
..., where T is *result.n_total*. *xreg_future* contains only the user's
exogenous regressors, with matching columns in the fitted order.

A :func:`vecmToVar` result is refused; use :func:`vecmForecast`. A
*varResult* built by hand must supply a valid *sigma* as well as the
coefficients, original data and model settings.

**Confidence intervals** are computed from the MSE matrix of the h-step-ahead
forecast error, assuming Gaussian innovations. With shocks-only covariance,
uncertainty accumulates with the forecast horizon.

**Exogenous regressors:** If the model was fit with *xreg*, the *xreg_future* keyword
is required for forecasting. The matrix must have *h* rows and the same number
of columns as the original regressors. An error is raised if omitted.

**Non-stationary models:** Forecasts from non-stationary VARs (explosive
eigenvalues) may diverge rapidly. Check *result.is_stationary* before forecasting.

Model
-----

The h-step-ahead point forecast from a VAR(p) is:

.. math::

   \hat{y}_{T+h|T} = \hat{B}_1 \hat{y}_{T+h-1|T} + \cdots + \hat{B}_p \hat{y}_{T+h-p|T} + \hat{u}

The displayed recursion is for a constant-only VAR. A trend and *xreg*
add their fitted deterministic terms at each forecast step.

Here :math:`\hat{y}_{T+j|T} = y_{T+j}` for :math:`j \leq 0` (observed data) and
:math:`\hat{y}_{T+j|T}` is the forecast for :math:`j \geq 1`.

The confidence interval at horizon :math:`h` is:

.. math::

   \hat{y}_{T+h|T} \pm z_{\alpha/2} \sqrt{\text{diag}(\text{MSE}_h)}

For ``coef_uncertainty=0``, the mean squared error matrix is :math:`\text{MSE}_h = \sum_{j=0}^{h-1} \Phi_j \hat\Sigma \Phi_j'`
and :math:`\Phi_j = J F^j J'` are the impulse response matrices. Intervals widen with the
horizon as :math:`\text{MSE}_h` accumulates.


Algorithm
---------

1. **Recursive substitution:** Iterate the estimated VAR equations forward, replacing future observations with their forecasts.
2. **MSE computation:** Accumulate the forecast error covariance via the companion form.
3. **Intervals:** Gaussian quantiles applied to the diagonal of :math:`\text{MSE}_h`.

**Computation.** Forecasts and shock covariance are propagated recursively.


Troubleshooting
---------------

**Forecasts diverge rapidly:**
The VAR is non-stationary (explosive eigenvalues). Check *result.is_stationary*.
Consider differencing the data or switching to :func:`bvarFit` with regularization.

**Confidence intervals are unrealistically narrow:**
The default intervals condition on the estimated coefficients. For a stable
fit without trend or xreg, ``coef_uncertainty=1`` adds approximate estimation
uncertainty. :func:`bvarForecast` provides posterior predictive bands for
Bayesian fits.


Verification
------------

Forecast checks compare point forecasts and standard errors with independent
reference calculations using the same residual-covariance divisor. The default
bands include future shocks only. See :ref:`var-verification`.


References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 3.5.


Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`bvarForecast`, :func:`bvarSvForecast`, :func:`fcScore`, :func:`dmTest`
