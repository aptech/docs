bvarSvForecast
==============

Purpose
-------
Generate density forecasts from a fitted SV-BVAR model with time-varying volatility propagation.

Format
------

.. function:: dfc = bvarSvForecast(result, h, mode={}, n_paths={}, seed={}, level={}, quiet=0, ctl={})

   :param result: an instance of a :class:`bvarSvResult` structure returned by :func:`bvarSvFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param mode: Optional keyword, ``"simulate"`` (default) or ``"mean_path"``. Overrides the control. Simulation bands include parameter uncertainty, future volatility changes and future shocks.
   :type mode: string

   :param n_paths: Optional keyword, simulation paths per posterior draw. Default = 100; overrides the control.
   :type n_paths: scalar

   :param seed: Optional keyword, simulation seed. Default = 42; overrides the control.
   :type seed: scalar

   :param level: Optional keyword, central band masses in ascending order: 0.68, 0.90, or both. Default = ``{ 0.68, 0.90 }``; overrides the control. The headline interval uses *level[1]*.
   :type level: scalar or vector

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of an :class:`svForecastControl` structure. An instance is initialized by calling :func:`svForecastControlCreate` and the following members can be set:

       .. include:: include/svforecastcontrol.rst

   :type ctl: struct

   *ctl* must be a ``svForecastControl`` structure or ``{}`` (omitted).
   Other values or structure types are refused.

   :return dfc: An instance of a :class:`densityForecastResult` structure containing:

       .. include:: include/densityforecastresult.rst

   :rtype dfc: struct

Examples
--------

Default Simulation Forecast
+++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    result = bvarSvFit(data, p=1, lag1_prior_mean={ 0, 1, 1 }, quiet=1);

    dfc = bvarSvForecast(result, 12);

    print "Mean forecast:";
    print dfc.mean;

    print "Median forecast:";
    print dfc.median;

Full Density Forecast (Simulate Mode)
+++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    result = bvarSvFit(data, p=1, lag1_prior_mean={ 0, 1, 1 }, quiet=1);

    // Simulate mode for proper predictive density
    fctl = svForecastControlCreate();
    fctl.mode = "simulate";
    fctl.n_paths = 200;

    dfc = bvarSvForecast(result, 24, ctl=fctl);

Choose a Central Band
+++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    // GDP growth is centered at 0; inflation and the funds rate at 1.
    data = data[., "date" "gdp_growth" "inflation" "fed_funds"];
    result = bvarSvFit(data, p=2, lag1_prior_mean={ 0, 1, 1 }, quiet=1);

    dfc = bvarSvForecast(result, 12, level=0.90);
    print dfc.bands[1].lower;
    print dfc.bands[1].upper;

Forecast Log-Volatility Path
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    ctl = bvarSvControlCreate();
    ctl.p = 4;
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    ctl.lag1_prior_mean = { 0, 1, 1 };
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    result = bvarSvFit(data, p=ctl.p, ctl=ctl, quiet=1);

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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    result = bvarSvFit(data, p=1, lag1_prior_mean={ 0, 1, 1 }, quiet=1);

    fctl = svForecastControlCreate();
    fctl.mode = "simulate";
    fctl.store_draws = 1;
    // Ten paths per draw keep the stored example compact.
    fctl.n_paths = 10;

    dfc = bvarSvForecast(result, 12, ctl=fctl);

    // Each path occupies h consecutive rows, with variables in columns.
    print "Draw matrix:" rows(dfc.draws) "x" cols(dfc.draws);

    // GDP is the first fitted variable. Take horizon 1 from every path.
    h1_rows = 1:dfc.h:rows(dfc.draws);
    gdp_h1_draws = dfc.draws[h1_rows, 1];
    print "Mean GDP growth at horizon 1:" meanc(gdp_h1_draws);

Remarks
-------

**Forecast modes:**

With no mode keyword, an empty *ctl.mode* resolves to ``"simulate"``.
This default also applies when a freshly created control is supplied.
Simulation bands include parameter uncertainty, future volatility changes
and future shocks. The default bands have central masses 68% and 90%.

``"mean_path"`` uses the posterior mean innovation variance at each
forecast horizon. This is fast but underestimates forecast uncertainty due to
Jensen's inequality — the mean of convex functions exceeds the function of
the mean. Use this for quick point forecasts.

``"simulate"`` (default) draws *n_paths* innovation paths per posterior draw from the
SV-implied time-varying covariance. The log-volatility :math:`h_{i,t}` is
propagated forward:

.. math::

   h_{i,T+s} = \mu_i + \phi_i (h_{i,T+s-1} - \mu_i) + \sigma_i \eta_{i,T+s}

and innovations are drawn from :math:`N(0, \text{diag}(\exp(h_{T+s})))`.
This gives a proper predictive density that captures volatility clustering
and parameter uncertainty. Required for density forecast evaluation.

**Ordering of the variables:**

The forecasts come from the model :func:`bvarSvFit` fitted, which orders its
shocks from the last column of *y* to the first; the ordering can change the
forecasts. For the usual ordering, in which the first column's shock comes
first, fit with the columns of *y* reversed (``y[., cols(y):1]``) and read
the forecasts in the reversed column order. :func:`tvpSvFit` orders its
shocks from the first column to the last.

**Memory considerations:**

Setting ``store_draws = 1`` stores a (dfc.n_draws * h) x m matrix.
Each path occupies h consecutive rows; variables are in columns.
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
