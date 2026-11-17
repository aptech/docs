fcScore
=======

Purpose
-------
Compute RMSE, MASE and sMAPE for point forecasts; related ensemble functions score predictive densities.

Format
------

.. function:: sc = fcScore(actual, predicted={}, train={}, period=1, quiet=0)

   :param actual: Realized values.
   :type actual: Nx1 vector

   :param predicted: Point forecasts, one per realized value.
   :type predicted: Nx1 vector

   :param train: Optional training series for MASE normalization.
   :type train: Tx1 vector

   :param period: Optional seasonal period for the MASE denominator. Default = 1.
   :type period: scalar

   :param quiet: Set to 1 to suppress printing. Default = 0.
   :type quiet: scalar

   :return sc: A :class:`scoreResult` containing RMSE, MASE and sMAPE.
   :rtype sc: struct

Examples
--------

Point Forecast Scores
+++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // Reserve the last 12 quarters for evaluation.
    h = 12;
    n_train = rows(data) - h;
    y_train = data[1:n_train, .];
    actual = asMatrix(data[n_train+1:rows(data), "gdp_growth"]);

    result = varFit(y_train, 4, quiet=1);
    fc = varForecast(result, h, quiet=1);
    sc = fcScore(actual, fc.forecasts[., "gdp_growth"], train=y_train[., "gdp_growth"]);

Density Forecast Scores
+++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // Reserve the last 12 quarters for evaluation.
    h = 12;
    n_train = rows(data) - h;
    y_train = data[1:n_train, .];
    actual = asMatrix(data[n_train+1:rows(data), "gdp_growth"]);

    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    result = bvarSvFit(y_train, p=1, lag1_prior_mean={ 0, 1, 1 }, quiet=1);
    fctl = svForecastControlCreate();
    fctl.store_draws = 1;
    // Keep the stored ensemble compact; each posterior draw gets ten paths.
    fctl.n_paths = 10;
    dfc = bvarSvForecast(result, h, ctl=fctl, quiet=1);

    // Path blocks have h rows; GDP growth is the first fitted variable.
    // Scoring expects one row per path and one column per target quarter.
    gdp_draws = reshape(dfc.draws[., 1], dfc.n_draws, h);
    crps = crpsEnsemble(gdp_draws, actual);
    log_loss = logScoreEnsemble(gdp_draws, actual);
    print "Mean CRPS:" meanc(crps);
    print "Mean negative log predictive density:" meanc(log_loss);

Remarks
-------

``fcScore`` accepts numeric point forecasts, not a forecast structure or a
``draws`` keyword. Score one variable at a time. Without *train*, MASE is missing.
For predictive draws, use :func:`crpsEnsemble` and :func:`logScoreEnsemble`, as in
the density example. Both return losses, so lower values are better.

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
