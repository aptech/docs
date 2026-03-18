bvarForecast
============

Purpose
-------
Generate posterior predictive forecasts with credible bands from a fitted Bayesian VAR model.

Format
------

.. function:: fc = bvarForecast(result, h)
              fc = bvarForecast(result, h, xreg=X_future)
              fc = bvarForecast(result, h, level=0.90)

   :param result: an instance of a :class:`bvarResult` structure returned by :func:`bvarFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param xreg: Optional keyword, future values of exogenous regressors. Required if the model was fit with *xreg*.
   :type xreg: hxK matrix

   :param level: Optional keyword, credible level for prediction bands. Default = 0.68.
   :type level: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return fc: An instance of a :class:`forecastResult` structure containing:

       .. include:: include/forecastresult.rst

   :rtype fc: struct

Examples
--------

Default BVAR Forecast (68% Credible Bands)
++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Estimate and forecast
    result = bvarFit(data, quiet=1);

    struct forecastResult fc;
    fc = bvarForecast(result, 12);

Forecast with 90% Credible Bands
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = bvarFit(data, quiet=1);

    fc = bvarForecast(result, 12, level=0.90);

Optimal Hyperparameters to Forecast Pipeline
+++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Optimize hyperparameters
    ho = bvarHyperopt(data);

    // Estimate with optimal lambdas
    result = bvarFit(data, ho.ctl, quiet=1);

    // Forecast
    fc = bvarForecast(result, 24);

Compare Forecasts Across Lag Orders
+++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();

    ctl.p = 2;
    r2 = bvarFit(data, ctl, quiet=1);

    ctl.p = 4;
    r4 = bvarFit(data, ctl, quiet=1);

    fc2 = bvarForecast(r2, 12, quiet=1);
    fc4 = bvarForecast(r4, 12, quiet=1);

    print "GDP forecast (p=2):" fc2.forecasts[., 1];
    print "GDP forecast (p=4):" fc4.forecasts[., 1];

Remarks
-------

**Posterior predictive distribution:**
For each posterior draw :math:`(B^{(i)}, \Sigma^{(i)})`, the function simulates
an h-step forecast path by iterating the VAR forward with innovations drawn
from :math:`N(0, \Sigma^{(i)})`. The reported *fc.forecasts* is the median of
the resulting predictive distribution. The *fc.lower* and *fc.upper* bands are
quantiles at ``(1-level)/2`` and ``(1+level)/2``.

**68% vs 95% bands:**
The default credible level of 0.68 corresponds to approximately :math:`\pm 1`
posterior standard deviation and is the convention in macroeconomic BVAR
applications. For publication or comparison with frequentist intervals, use
``level=0.90`` or ``level=0.95``.

**Conjugate vs Gibbs:**
For models fit with ``prior="minnesota"`` (conjugate), exact posterior draws are
used. For ``prior="flat"`` (Gibbs), the retained MCMC draws are used. In both
cases, the number of forecast draws equals *result.n_draws*.

Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`bvarFit`, :func:`varForecast`, :func:`bvarSvForecast`, :func:`condForecast`
