fcScore
=======

Purpose
-------
Compute forecast scoring rules for point and density forecasts.

Format
------

.. function:: sc = fcScore(actual, fc)
              sc = fcScore(actual, fc, train=y_train)
              sc = fcScore(actual, draws=D)

   :param actual: realized values.
   :type actual: hx1 or hxm matrix

   :param fc: Optional, a :class:`forecastResult` struct or hxm matrix of point forecasts.
   :type fc: struct or matrix

   :param train: Optional keyword, training data for MASE normalization.
   :type train: Nx1 or Nxm matrix

   :param season: Optional keyword, seasonality for MASE. Default = 1.
   :type season: scalar

   :param draws: Optional keyword, raw forecast draws for density scores (CRPS, LPS). From *dfc.draws* of :func:`bvarSvForecast` with ``store_draws = 1``.
   :type draws: (n_draws)x(h*m) matrix

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return sc: An instance of a :class:`scoreResult` structure containing RMSE, MASE, SMAPE, CRPS, LPS, energy score, PI coverage, and PI width.
   :rtype sc: struct

Examples
--------

Point Forecast Scores
+++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, quiet=1);
    fc = varForecast(result, 12, quiet=1);

    sc = fcScore(actual, fc, train=data);
    print "RMSE:" sc.rmse;
    print "MASE:" sc.mase;
    print "sMAPE:" sc.smape;

Density Forecast Scores
+++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = bvarSvFit(data, quiet=1);

    fctl = svForecastControlCreate();
    fctl.mode = "simulate";
    fctl.store_draws = 1;
    dfc = bvarSvForecast(result, 12, fctl, quiet=1);

    sc = fcScore(actual, draws=dfc.draws);
    print "CRPS:" sc.crps;
    print "LPS:" sc.lps;

Remarks
-------

**Point scores** (RMSE, MASE, SMAPE) require point forecasts. **Density scores**
(CRPS, LPS) require the raw draw matrix. **Interval scores** (PI coverage, PI
width) require a :class:`forecastResult` with lower/upper bounds.

MASE requires training data for the naive-forecast normalization. If *train*
is not provided, *sc.mase* is missing.

Model
-----

**Point scores:**

.. math::

   \text{RMSE} &= \sqrt{\frac{1}{T} \sum_{t=1}^{T} (y_t - \hat{y}_t)^2} \\
   \text{MASE} &= \frac{\sum |y_t - \hat{y}_t|}{\frac{T}{T_{\text{train}} - s} \sum |y_{t}^{\text{train}} - y_{t-s}^{\text{train}}|}

**Density scores:**

.. math::

   \text{CRPS} &= \frac{1}{T} \sum_{t=1}^{T} \left(\frac{1}{S} \sum_{s=1}^{S} |\hat{y}_t^{(s)} - y_t| - \frac{1}{2S^2} \sum_{s,s'} |\hat{y}_t^{(s)} - \hat{y}_t^{(s')}|\right) \\
   \text{LPS}  &= -\frac{1}{T} \sum_{t=1}^{T} \log \hat{f}_t(y_t)

where CRPS (Continuous Ranked Probability Score) is a proper scoring rule for density
forecasts and LPS (Log Predictive Score) is the negative log predictive likelihood
evaluated at the realized value.
References
----------

- Gneiting, T. and A.E. Raftery (2007). "Strictly proper scoring rules, prediction, and estimation." *Journal of the American Statistical Association*, 102(477), 359-378.
- Hyndman, R.J. and A.B. Koehler (2006). "Another look at measures of forecast accuracy." *International Journal of Forecasting*, 22(4), 679-688.
Library
-------
timeseries

Source
------
scoring.src

.. seealso:: Functions :func:`dmTest`, :func:`pitTest`, :func:`fcMetrics`
