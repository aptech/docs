bvarForecast
============

Purpose
-------
Generate posterior predictive forecasts with credible bands from a fitted Bayesian VAR model.

Format
------

.. function:: fc = bvarForecast(result, h)
              fc = bvarForecast(result, h, level=0.90)
              fc = bvarForecast(result, h, xreg_future=X_future)

   :param result: an instance of a :class:`bvarResult` structure returned by :func:`bvarFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param level: Optional keyword, central mass of each credible band, strictly between 0 and 1. A vector gives one band per value, in ascending order. Default = ``0.68|0.90``.
   :type level: scalar or vector

   :param levels: Optional keyword, another name for *level*. Pass one or the other, not both.
   :type levels: scalar or vector

   :param n_draws: Optional keyword, number of posterior draws to simulate from: the first *n_draws* draws stored in *result*, at most *result.n_draws*. Default = all stored draws.
   :type n_draws: scalar

   :param seed: Optional keyword, seed of the forecast simulation. Default = 42.
   :type seed: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param xreg_future: Optional keyword, future values of the exogenous regressors: *h* rows and one column per regressor in the fit. Required if the model was fit with *xreg*, and not allowed otherwise. If both have column names, they must match the fit's, in the same order.
   :type xreg_future: hxK matrix

   :return fc: An instance of a :class:`bvarForecastResult` structure containing:

       .. include:: include/bvarforecastresult.rst

   :rtype fc: struct

Examples
--------

Default BVAR Forecast (68% and 90% Credible Bands)
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Four quarterly US series, 1960Q1-2019Q4: GDP growth and inflation
    // (annualized percent changes), unemployment and the funds rate (percent)
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    // Estimate and forecast 12 quarters
    result = bvarFit(y, p=2, lag1_prior_mean=0|1|1|1, quiet=1);

    fc = bvarForecast(result, 12);

Forecast with a 90% Credible Band Only
++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    result = bvarFit(y, p=2, lag1_prior_mean=0|1|1|1, quiet=1);

    fc = bvarForecast(result, 12, level=0.90);

Choose the Prior Tightness, then Forecast
+++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    // Choose the overall tightness by marginal likelihood
    ps = bvarPriorSelect(y, p=4, lag1_prior_mean=0|1|1|1, quiet=1);

    // Estimate with the chosen settings
    result = bvarFit(y, ctl=ps.fit_settings, quiet=1);

    // Forecast
    fc = bvarForecast(result, 24);

Compare Forecasts Across Lag Orders
+++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    r2 = bvarFit(y, p=2, lag1_prior_mean=0|1|1|1, quiet=1);
    r4 = bvarFit(y, p=4, lag1_prior_mean=0|1|1|1, quiet=1);

    fc2 = bvarForecast(r2, 12, quiet=1);
    fc4 = bvarForecast(r4, 12, quiet=1);

    print "GDP growth forecast (p=2):" fc2.forecasts[., 1];
    print "GDP growth forecast (p=4):" fc4.forecasts[., 1];

Remarks
-------

**Posterior predictive distribution:**
For each posterior draw :math:`(B^{(i)}, \Sigma^{(i)})`, the function simulates
an h-step forecast path by iterating the VAR forward with innovations drawn
from :math:`N(0, \Sigma^{(i)})`. The reported *fc.forecasts* is the median of
the resulting predictive distribution and *fc.mean_path* its mean. Each band in
*fc.bands* holds the quantiles at ``(1-level)/2`` and ``(1+level)/2`` of the
same simulated paths, so the bands nest.

**68% and 90% bands:**
By default *fc.bands* holds a 68% and a 90% band. The 68% level corresponds
to approximately :math:`\pm 1` posterior standard deviation and is the
convention in macroeconomic BVAR applications. The printed table shows the
median and the first band only; the other bands stay on *fc*. For a single
band, pass one level, for example ``level=0.95``.

**Posterior draws:**
:func:`bvarFit` draws :math:`(B, \Sigma)` from the conjugate Minnesota
posterior. :func:`bvarForecast` simulates one path from each of the first
*n_draws* stored draws; by default it uses all *result.n_draws* of them.

Model
-----

For each posterior draw :math:`(B^{(s)}, \Sigma^{(s)})`, the h-step forecast path is
generated by iterating the VAR forward:

.. math::

   y_{T+h}^{(s)} = B_1^{(s)} y_{T+h-1}^{(s)} + \cdots + B_p^{(s)} y_{T+h-p}^{(s)} + c^{(s)} + \Gamma^{(s)} x_{T+h} + \varepsilon_{T+h}^{(s)}

where:

- :math:`y_{T+h}^{(s)}` is the mx1 vector of simulated values *h* steps after
  the last observation *T*. For :math:`h \le 0` it is the observed data.
- :math:`B_l^{(s)}` is the mxm matrix of lag-*l* coefficients in draw *s*;
  row *i* holds equation *i*.
- :math:`c^{(s)}` is the mx1 constant term in draw *s*, zero when the fit has
  no constant.
- :math:`\Gamma^{(s)}` is the mxK matrix of coefficients on the exogenous
  regressors in draw *s*, and :math:`x_{T+h}` is row *h* of *xreg_future*.
  Both terms are absent when the fit has no *xreg*.
- :math:`\varepsilon_{T+h}^{(s)} = L^{(s)} z_{T+h}^{(s)} \sim N(0, \Sigma^{(s)})`,
  where :math:`L^{(s)}` is the lower Cholesky factor of :math:`\Sigma^{(s)}` and
  :math:`z_{T+h}^{(s)}` is a vector of *m* independent standard normal draws.

:math:`B^{(s)}` stacks :math:`B_1^{(s)}, \ldots, B_p^{(s)}`, :math:`c^{(s)}`
and :math:`\Gamma^{(s)}`. No trend term is added. The reported point
forecast is the median across all draws; the credible bands are posterior quantiles.

This integrates over both **parameter uncertainty** (different :math:`B, \Sigma` draws)
and **innovation uncertainty** (random :math:`\varepsilon`), giving a proper Bayesian
predictive density.

Algorithm
---------

1. For each of the *n_draws* posterior draws :math:`(B^{(s)}, \Sigma^{(s)})`:

   a. Draw :math:`\varepsilon_{T+1}^{(s)}, \ldots, \varepsilon_{T+h}^{(s)} \sim N(0, \Sigma^{(s)})`.
   b. Iterate the VAR forward using past data and previously generated forecasts.

2. Compute the median and quantiles of :math:`\{\hat{y}_{T+h}^{(s)}\}_{s=1}^{n\_draws}` at each horizon.

**Complexity:** :math:`O(n\_draws \cdot h \cdot m^2 p)`. Sub-second for typical configurations.

Troubleshooting
---------------

**Forecast bands are too wide:**
Tighten the prior (reduce *overall_tightness* in :func:`bvarFit`) or add the
sum-of-coefficients prior (*soc_tightness* > 0). Wide bands often reflect
parameter uncertainty in an over-parameterized model.

**Forecasts revert to the mean immediately:**
Check *lag1_prior_mean*. With ``lag1_prior_mean = 0`` (white noise prior), the
BVAR pulls each series toward its mean. For data in levels, use the default,
``lag1_prior_mean = 1`` (random walk).

**Forecasts explode:**
The posterior mean may be non-stationary. Check *result.is_stationary*, which
:func:`bvarFit` sets only with ``ctl.stability_check = 1``; otherwise it is
missing. Add regularization via the sum-of-coefficients (*soc_tightness*) or
single-unit-root (*sur_tightness*) priors in :func:`bvarFit`.

References
----------

- Banbura, M., D. Giannone, and L. Reichlin (2010). "Large Bayesian vector auto regressions." *Journal of Applied Econometrics*, 25(1), 71-92.
- Kadiyala, K.R. and S. Karlsson (1997). "Numerical methods for estimation and inference in Bayesian VAR-models." *Journal of Applied Econometrics*, 12(2), 99-132.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarFit`, :func:`varForecast`, :func:`bvarSvForecast`, :func:`condForecast`, :func:`fcScore`, :func:`dmTest`
