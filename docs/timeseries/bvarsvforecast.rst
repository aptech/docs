bvarSvForecast
==============

Purpose
-------
Generate density forecasts from a fitted SV-BVAR model with time-varying volatility propagation.

Format
------

.. function:: dfc = bvarSvForecast(result, h)
              dfc = bvarSvForecast(result, h, ctl)
              dfc = bvarSvForecast(result, h, ctl, xreg=X_future)

   :param result: an instance of a :class:`bvarSvResult` structure returned by :func:`bvarSvFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param ctl: Optional input, an instance of an :class:`svForecastControl` structure. An instance is initialized by calling :func:`svForecastControlCreate` and the following members can be set:

       .. include:: include/svforecastcontrol.rst

   :type ctl: struct

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxK matrix

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return dfc: An instance of a :class:`densityForecastResult` structure containing:

       .. include:: include/densityforecastresult.rst

   :rtype dfc: struct

Examples
--------

Quick Mean-Path Forecast
++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    result = bvarSvFit(data, quiet=1);

    dfc = bvarSvForecast(result, 12);

    print "Mean forecast:";
    print dfc.fc_mean;

    print "Median forecast:";
    print dfc.fc_median;

Full Density Forecast (Simulate Mode)
+++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = bvarSvFit(data, quiet=1);

    // Simulate mode for proper predictive density
    fctl = svForecastControlCreate();
    fctl.mode = "simulate";
    fctl.n_paths = 500;

    dfc = bvarSvForecast(result, 24, fctl);

Custom Quantiles for VaR
+++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = bvarSvFit(data, quiet=1);

    fctl = svForecastControlCreate();
    fctl.mode = "simulate";
    fctl.n_paths = 1000;
    fctl.quantile_levels = 0.01|0.05|0.10|0.50|0.90|0.95|0.99;

    dfc = bvarSvForecast(result, 12, fctl);

    // 1% VaR forecast (first quantile band)
    var_01 = dfc.quantile_bands[1];
    print "1% quantile forecast (VaR):";
    print var_01;

    // 5% VaR forecast (second quantile band)
    var_05 = dfc.quantile_bands[2];

Forecast Log-Volatility Path
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    result = bvarSvFit(data, ctl, quiet=1);

    dfc = bvarSvForecast(result, 24);

    // Future volatility path
    print "Forecast log-volatility (mean):";
    print dfc.log_vol_mean;

    // Convert to standard deviations
    print "Forecast std dev:";
    print exp(dfc.log_vol_mean / 2);

Store Raw Draws for Custom Analysis
++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = bvarSvFit(data, quiet=1);

    fctl = svForecastControlCreate();
    fctl.mode = "simulate";
    fctl.store_draws = 1;

    dfc = bvarSvForecast(result, 12, fctl);

    // Raw draws: each row is one draw, columns are h1_v1, h1_v2, ..., h1_vm, h2_v1, ...
    print "Draw matrix:" rows(dfc.draws) "x" cols(dfc.draws);

    // Extract GDP (variable 1) draws at horizon 1
    m = dfc.m;
    gdp_h1_draws = dfc.draws[., 1];    // First column = h1, variable 1

Remarks
-------

**Forecast modes:**

``"mean_path"`` (default) uses the posterior mean innovation variance at each
forecast horizon. This is fast but underestimates forecast uncertainty due to
Jensen's inequality — the mean of convex functions exceeds the function of
the mean. Use this for quick point forecasts.

``"simulate"`` draws *n_paths* innovation paths per posterior draw from the
SV-implied time-varying covariance. The log-volatility :math:`h_{i,t}` is
propagated forward:

.. math::

   h_{i,T+s} = \mu_i + \phi_i (h_{i,T+s-1} - \mu_i) + \sigma_i \eta_{i,T+s}

and innovations are drawn from :math:`N(0, \text{diag}(\exp(h_{T+s})))`.
This gives a proper predictive density that captures volatility clustering
and parameter uncertainty. Required for density forecast evaluation.

**h_T initialization:**

``"stochastic"`` draws the initial log-volatility :math:`h_T` from the reservoir
of posterior draws (when ``sv_keep = "online"`` or ``"full"``). This captures
uncertainty about the current volatility state.

``"posterior_mean"`` uses the posterior mean :math:`h_T`. Faster but
underestimates tail risk by ignoring :math:`h_T` uncertainty.

**Memory considerations:**

Setting ``store_draws = 1`` stores an (n_draws * n_paths) x (h * m) matrix.
For large systems or long horizons, this can be substantial. Default is off.

Model
-----

The SV-BVAR density forecast accounts for three sources of uncertainty:

1. **Parameter uncertainty:** different :math:`(B^{(s)}, A^{(s)})` draws.
2. **Volatility uncertainty:** the future path of log-volatilities :math:`h_{T+1}, \ldots, h_{T+h}`.
3. **Innovation uncertainty:** random :math:`\varepsilon_{T+s}` with time-varying variance.

At each forecast horizon :math:`s = 1, \ldots, h`:

.. math::

   h_{i,T+s} &= \mu_i + \phi_i (h_{i,T+s-1} - \mu_i) + \sigma_i \eta_{i,T+s} \\
   \varepsilon_{T+s} &\sim N(0, \Sigma_{T+s}) \quad \text{where } \Sigma_{T+s} = A_{T+s}^{-1} D_{T+s} A_{T+s}^{-\prime} \\
   y_{T+s} &= B_1 y_{T+s-1} + \cdots + B_p y_{T+s-p} + u + \varepsilon_{T+s}

The resulting predictive density is non-Gaussian and potentially fat-tailed due to
volatility clustering — a key advantage over constant-variance BVAR forecasts.

Algorithm
---------

**Simulate mode:**

1. For each posterior draw :math:`(B^{(s)}, A^{(s)}, \mu^{(s)}, \phi^{(s)}, \sigma^{(s)}, h_T^{(s)})`:

   a. For each of *n_paths* simulation paths:
      i. Propagate log-volatilities forward: :math:`h_{T+1}, \ldots, h_{T+h}`.
      ii. Draw innovations from the time-varying covariance.
      iii. Iterate the VAR forward.

2. Collect all forecast paths and compute quantiles.

**Mean-path mode:**
Uses the posterior mean volatility at each horizon (no simulation of :math:`\eta`),
giving a single path per posterior draw. Faster but underestimates tail risk.

**Complexity:** Simulate mode: :math:`O(n\_draws \cdot n\_paths \cdot h \cdot m^2)`.

Troubleshooting
---------------

**Density forecasts are too narrow compared to realized outcomes:**
Use ``mode = "simulate"`` instead of ``"mean_path"``. The mean-path mode
underestimates uncertainty by ignoring future volatility randomness.

**Memory issues with large systems:**
Use ``store_draws = 0`` (default) and rely on the quantile summaries. For systems
with m > 10, use ``sv_keep = "online"`` in :func:`bvarSvFit`.

**Forecast volatility path seems unreasonable:**
If :math:`h_T` is at an extreme value (e.g., a crisis period), forecasts may show
elevated volatility for many periods. This is the model correctly reflecting
persistent volatility. If the persistence :math:`\phi_i` is near 1, volatility
shocks take many periods to decay.

Verification
------------

SV-BVAR forecast density calibration verified via PIT (probability integral transform)
tests on out-of-sample evaluation windows. Forecast paths validated against
R ``bayesianVARs::predict()`` for structural consistency.

See the :ref:`var-verification` page.

References
----------

- Clark, T.E. (2011). "Real-time density forecasts from Bayesian vector autoregressions with stochastic volatility." *Journal of Business & Economic Statistics*, 29(3), 327-341.
- Kastner, G. and S. Fruhwirth-Schnatter (2014). "Ancillarity-sufficiency interweaving strategy (ASIS) for boosting MCMC estimation of stochastic volatility models." *Computational Statistics & Data Analysis*, 76, 408-423.

Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`bvarSvFit`, :func:`svForecastControlCreate`, :func:`bvarForecast`, :func:`condForecast`, :func:`pitTest`
