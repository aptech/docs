bvarMacroForecast
=================

Purpose
-------
Forecast a set of macroeconomic series with a Bayesian VAR in one call: choose
the lags, choose the prior's overall tightness, fit a Minnesota-prior BVAR,
forecast with bands and, if asked, check the model on a holdout sample against
a least-squares VAR.

Format
------

.. function:: wf = bvarMacroForecast(y)
              wf = bvarMacroForecast(y, h=8, holdout=20)
              wf = bvarMacroForecast(y, lag1_prior_mean="zero", overall_tightness=0.2)
              wf = bvarMacroForecast(y, overall_tightness=bvarChoose(0.1), residual_variances=bvarChoose())
              wf = bvarMacroForecast(y, spec=spec)

   :param y: The series to forecast, one column per variable, with no missing
       values. A dataframe supplies the variable names used in the tables and
       plots; one date column, if present, is used as the time index and left
       out of the model. A matrix is labelled ``Y1``, ``Y2``, and so on.
   :type y: TxM matrix or dataframe

   :param h: Optional keyword, number of periods to forecast.
       Default = 8.
   :type h: scalar

   :param holdout: Optional keyword, number of final observations set aside to
       check the model. The lag order, and the tightness when it is chosen,
       are chosen and the model is fitted without them, they are forecast
       from one start date and the errors are reported; then the model is
       fitted again on all the data for the forecast returned in
       *wf.forecast*. Default = 0 (no check).
   :type holdout: scalar

   :param lag1_prior_mean: Optional keyword, prior mean of each variable's
       coefficient on its own first lag: ``"random_walk"`` (1, for
       persistent series such as levels and rates), ``"zero"`` (for growth
       rates and other series that move around a stable mean), one value for
       every variable, or a vector with one value per variable, each in
       [0,1]. Default = ``"random_walk"``.
   :type lag1_prior_mean: string, scalar or Mx1 vector

   :param max_lags: Optional keyword, largest lag order considered.
       Default = 8.
   :type max_lags: scalar

   :param lag_ic: Optional keyword, criterion that chooses the lag order
       between 1 and *max_lags*: ``"aic"``, ``"bic"`` or ``"hq"``.
       Default = ``"bic"``.
   :type lag_ic: string

   :param overall_tightness: Optional keyword, how strongly the prior pulls
       the coefficients toward their prior means; smaller values pull harder.
       A positive number holds the tightness at that value. ``bvarChoose()``
       chooses it from the training rows with :func:`bvarPriorSelect` (the
       value with the highest marginal likelihood times a weak prior on the
       tightness, between 0.001 and 5), starting at the *overall_tightness*
       of *spec*; ``bvarChoose(x)`` starts the search at *x*. Default: held
       at the *overall_tightness* of *spec*, 0.2 unless changed, with no
       search.
   :type overall_tightness: scalar or struct

   :param residual_variances: Optional keyword, ``bvarChoose()`` to choose
       the residual variance of each series that the prior is built on
       together with the tightness, starting at their autoregression values;
       see the Remarks. It needs ``overall_tightness=bvarChoose()`` too.
       Default: not chosen.
   :type residual_variances: struct

   :param baseline: Optional keyword, the model the holdout check compares
       with: ``"ols_var"`` for a least-squares VAR with the same lags, or
       ``"none"``. Used only when *holdout* is positive.
       Default = ``"ols_var"``.
   :type baseline: string

   :param level: Optional keyword, one or more band levels, each between 0 and
       1, in ascending order. All are stored; printed tables show the first.
       Default = 0.68|0.90.
   :type level: scalar or vector

   :param dates: Optional keyword, dates of the observations (POSIX), for
       matrix input. Default = {} (none, or the dataframe's date column).
   :type dates: Tx1 vector

   :param freq: Optional keyword, frequency of the dates, when it should not
       be inferred from them: ``"annual"``, ``"quarterly"``, ``"monthly"``,
       ``"weekly"`` or ``"daily"``. Needs dates. Default = "" (inferred).
   :type freq: string

   :param n_draws: Optional keyword, number of posterior draws, each giving
       one simulated future path. Default = 5000.
   :type n_draws: scalar

   :param seed: Optional keyword, random number seed. Default = 42.
   :type seed: scalar

   :param const: Optional keyword, 1 to include a constant, 0 to leave it
       out. Default = 1.
   :type const: scalar

   :param quiet: Optional keyword, 1 to print nothing. Default = 0.
   :type quiet: scalar

   :param spec: Optional keyword, a :class:`bvarMacroForecastSpec` structure
       from ``bvarMacroForecastSpecCreate`` holding the settings above. A
       keyword given in the call replaces the value in *spec*. A spec holds
       values only: what is chosen is set in the call.
       *spec.overall_tightness* is the tightness held, or where
       ``bvarChoose()`` starts the search.
   :type spec: struct

   :return wf: An instance of a :class:`bvarMacroForecastResult` structure
       containing:

       .. list-table::
          :widths: auto

          * - wf.forecast
            - :class:`bvarForecastResult` structure, the forecast from the model fitted on all the data: *wf.forecast.forecasts* (medians, horizon x M), *wf.forecast.bands* (one lower and upper matrix per level) and *wf.forecast.forecast_dates*.

          * - wf.fit
            - :class:`bvarResult` structure, the model fitted on all the data.

          * - wf.selected_p
            - Scalar, the lag order chosen.

          * - wf.lag_selection
            - Structure returned by :func:`varLagSelect`.

          * - wf.prior_search
            - :class:`priorSelectResult` structure. *wf.prior_search.overall_tightness* is the tightness used; *wf.prior_search.status* is "converged", "not_converged" or "at_bound" after a search and "not_run" when the tightness was held; *wf.prior_search.choose* lists what was chosen (``""`` when nothing was); *wf.prior_search.residual_variances* holds the chosen residual variances when they were chosen.

          * - wf.spec
            - :class:`bvarMacroForecastSpec` structure, every setting as used.

          * - wf.used_holdout
            - Scalar, 1 if a holdout check was made.

          * - wf.holdout_rmse_by_variable
            - Mx1 vector, the BVAR's root mean squared error on the holdout, by variable; empty without a holdout.

          * - wf.baseline_rmse_by_variable
            - Mx1 vector, the same for the least-squares VAR; empty without a holdout or a baseline.

          * - wf.holdout_coverage
            - M x (number of levels) matrix, share of holdout outcomes inside each band; empty without a holdout.

          * - wf.holdout_forecast, wf.backtest_fit, wf.baseline_fit, wf.baseline_forecast
            - The forecasts and fits behind the holdout check.

          * - wf.holdout_actual
            - holdout x M matrix, the holdout observations.

          * - wf.train_rows, wf.total_rows
            - Scalars, observations used before the holdout and in all.

          * - wf.dates, wf.freq
            - The dates of the sample (POSIX) and their frequency; empty without dates.

   :rtype wf: struct

Examples
--------

One Call, with a Holdout Check
++++++++++++++++++++++++++++++

Four quarterly US series, with the last five years held out to check the
model.

::

    new;
    library timeseries;

    // Four quarterly US series, 1960Q1-2019Q4.
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    // Prior centre of each variable's own first lag: 0 for GDP growth, 1 for
    // inflation, unemployment and the funds rate. The tightness is chosen
    // by marginal likelihood.
    wf = bvarMacroForecast(y, h=8, holdout=20, lag1_prior_mean=0|1|1|1,
        overall_tightness=bvarChoose());

::

    BVAR macro forecast: 4 variables, 240 quarters (1960Q1-2019Q4)
    ================================================================================
    Model:        BVAR(2), conjugate Minnesota prior, constant, 5,000 draws, seed 42
    Lag order:    2, selected by BIC over 1-8 (training sample)
    Tightness:    lambda1 = 0.2581 MAP (log ML + Gamma hyperprior); converged, 52 evaluations
    Prior centre: own first lag 0, 1, 1, 1; constant variance 1e+07
    Sample:       training 1960Q1-2014Q4, holdout 2015Q1-2019Q4

    Trust checks
    Optimizer:    converged (52 evaluations); log ML (train) -1307.44
    Stability:    largest companion root 0.9664 (below 1: stationary)

    Residuals at the posterior centre
    Variable      Variance  Max |ACF|
    ---------------------------------
    gdp_growth      8.4169      0.102
    inflation       3.3233      0.177
    unemployment    0.0518      0.192
    fed_funds       0.6489      0.262

    Variance: posterior mean of Sigma (inverse-Wishart). Max |ACF|: over lags 1-8.

    Holdout: 20 quarters from one origin; RMSE (lower is better) and band coverage
    Variable      BVAR RMSE  OLS VAR RMSE  68% coverage  90% coverage
    -----------------------------------------------------------------
    gdp_growth        1.520         1.536         1.000         1.000
    inflation         1.274         1.353         0.950         1.000
    unemployment      0.670         0.742         1.000         1.000
    fed_funds         1.019         1.307         1.000         1.000

    BVAR forecast, 8 quarters ahead
    ================================================================================
    Point: predictive median of 5,000 simulated paths.
    Band: 68% equal-tailed quantiles of the same paths.

    Period  gdp_growth  Lower 68%  Upper 68%  inflation  Lower 68%  Upper 68%
    -------------------------------------------------------------------------
    2020Q1       2.772     -0.111      5.746      2.126      0.252      3.979
    2020Q2       2.681     -0.386      5.627      2.239      0.008      4.482
    2020Q3       2.486     -0.476      5.600      2.353     -0.182      4.757
    2020Q4       2.483     -0.625      5.486      2.337     -0.292      4.873
    2021Q1       2.400     -0.792      5.617      2.383     -0.435      5.099
    2021Q2       2.403     -0.755      5.634      2.434     -0.456      5.238
    2021Q3       2.569     -0.668      5.764      2.508     -0.483      5.319
    2021Q4       2.503     -0.732      5.585      2.513     -0.467      5.409

    Period  unemployment  Lower 68%  Upper 68%  fed_funds  Lower 68%  Upper 68%
    ---------------------------------------------------------------------------
    2020Q1         3.616      3.398      3.847      1.667      0.855      2.473
    2020Q2         3.654      3.244      4.075      1.864      0.638      3.093
    2020Q3         3.715      3.116      4.321      1.964      0.372      3.564
    2020Q4         3.787      3.022      4.522      2.045      0.119      3.976
    2021Q1         3.864      2.961      4.720      2.099     -0.121      4.339
    2021Q2         3.940      2.910      4.905      2.216     -0.351      4.731
    2021Q3         4.005      2.897      5.099      2.282     -0.481      4.982
    2021Q4         4.070      2.915      5.253      2.327     -0.653      5.292

    Forecasts from the full-sample refit.
    More: bvarReport(wf) for the full report, plotForecast(wf), bvarExport(wf, dir).

BIC chose two lags and the search chose a tightness of 0.2581, both on the
training sample 1960Q1-2014Q4. On the five held-out years the BVAR's errors
were smaller than the least-squares VAR's for all four series. That is one
start date and 20 overlapping forecasts: a sanity check, not a ranking. Every
held-out value of GDP growth, unemployment and the funds rate fell inside the
68% band, so for those five years the bands were wider than they needed to
be. To compare models over many start dates, use :func:`forecastEval`.

A Fixed Tightness and a Table for Two Variables
+++++++++++++++++++++++++++++++++++++++++++++++

Give *overall_tightness* a number to hold the tightness at that value. With
``quiet=1`` the call prints nothing and :func:`printForecast` prints the
forecast for the variables you name.

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    // Tightness fixed at 0.2, lags chosen by AIC from 1 to 4, a 90% band, and
    // nothing printed by the call itself.
    wf = bvarMacroForecast(y, h=4, lag1_prior_mean=0|1|1|1, max_lags=4, lag_ic="aic",
        overall_tightness=0.2, level=0.90, quiet=1);

    print "Lags chosen: " $+ ntos(wf.selected_p);
    print "Tightness:   " $+ ntos(wf.prior_search.overall_tightness) $+ " (" $+ wf.prior_search.status $+ ")";
    print "";

    // The forecast for two of the variables.
    string two_series = { "inflation", "fed_funds" };
    printForecast(wf, vars=two_series);

::

    Lags chosen: 3
    Tightness:   0.2 (not_run)

    ================================================================================
    Workflow summary
    ================================================================================
    Selected lag order:                    3
    Overall tightness:                0.2000
    Full-sample log ML:           -1377.7566

    Forecast (median and 90% band), all horizons for selected variables
    Period     inflation                        fed_funds
    2020Q1     2.4169  [ -0.6329,   5.4786]     1.7780  [  0.4563,   3.0929]
    2020Q2     2.3539  [ -1.2540,   6.0066]     2.0236  [  0.0038,   3.9926]
    2020Q3     2.5834  [ -1.3411,   6.5813]     2.1904  [ -0.3785,   4.7217]
    2020Q4     2.6674  [ -1.5928,   6.9032]     2.2764  [ -0.7610,   5.1753]

    Point: predictive median of 5,000 simulated paths.
    Band: 90% equal-tailed quantiles of the same paths. Full-sample refit.

Settings Kept in One Place
++++++++++++++++++++++++++

A :class:`bvarMacroForecastSpec` structure holds the settings so that several
calls can share them. A keyword given in the call replaces the value in the
structure.

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    // Settings kept in one place and reused. What is chosen is marked in
    // each call.
    struct bvarMacroForecastSpec spec;
    spec = bvarMacroForecastSpecCreate();
    spec.h = 12;
    spec.max_lags = 4;
    spec.lag_ic = "aic";
    spec.n_draws = 2000;
    spec.quiet = 1;

    struct bvarMacroForecastResult wf_a, wf_b;
    wf_a = bvarMacroForecast(y, lag1_prior_mean=0|1|1|1,
        overall_tightness=bvarChoose(), spec=spec);
    // A keyword given in the call replaces the value in spec.
    wf_b = bvarMacroForecast(y, lag1_prior_mean=0|1|1|1, h=4,
        overall_tightness=bvarChoose(), spec=spec);

    print "Forecast rows: " $+ ntos(rows(wf_a.forecast.forecasts)) $+ " and " $+ ntos(rows(wf_b.forecast.forecasts));
    print "Lags: " $+ ntos(wf_a.selected_p) $+ "; tightness chosen: " $+ sprintf("%.4f", wf_a.prior_search.overall_tightness);

::

    Forecast rows: 12 and 4
    Lags: 3; tightness chosen: 0.2736

Remarks
-------

**What the call does.** In order: :func:`varLagSelect` chooses the lag order;
with ``overall_tightness=bvarChoose()``, :func:`bvarPriorSelect` chooses the
tightness; :func:`bvarFit` fits the model; :func:`bvarForecast` simulates
the forecast.
With a holdout, these steps run first on the sample without the held-out
observations, the held-out observations are forecast and scored, and the
model is then fitted on all the data with the same lag order and tightness
(and the same residual variances, when they were chosen).
The function makes forecasts that do not condition on a future path of any
variable. For impulse responses use :func:`irfCompute`, for forecasts given an
assumed path :func:`condForecast`, for changing volatility :func:`bvarSvFit`.

**Prior means.** *lag1_prior_mean* is the centre of the prior for each
variable's coefficient on its own first lag; every other coefficient is
centred on zero. Use 1 for series that drift (levels, rates) and 0 for growth
rates. The default, ``"random_walk"``, suits data that are all levels or
rates; data that are all growth rates take ``"zero"``. With one value per
variable the printed summary lists them. The prior means are a
fixed part of the prior: the search chooses the tightness, not the means.

**The tightness search.** Left out, the overall tightness is held at
*spec.overall_tightness*, 0.2 unless changed, and nothing is searched.
``overall_tightness=bvarChoose()`` looks for the overall tightness alone, with
the Minnesota prior's lag decay at 1 and without the sum-of-coefficients
and single-unit-root priors. Only the overall tightness and the residual
variances can be chosen here. To choose the others as well, call
:func:`bvarPriorSelect` and :func:`bvarFit` yourself.

**Choosing the residual variances.** The prior is built on one residual
variance per series, by default the residual variance of an autoregression
of that series. With ``residual_variances=bvarChoose()``
the search chooses them together with the tightness, each between 1/100 and
100 times its autoregression value, with the priors of Giannone, Lenza and
Primiceri (2015); the tightness is then looked for between 0.0001 and 5. A
tightness chosen this way cannot be compared with one chosen with fixed
residual variances, and it belongs with them: to fit that prior again use
``bvarFit(y, ctl=wf.prior_search.fit_settings)``, not the tightness alone. The
paper's prior on the residual variances has its peak near 0.02 squared and
is written for data in logs multiplied by four and rates in decimals. This
function always uses it, so put the data in those units before choosing the
residual variances here; for data in other units call
:func:`bvarPriorSelect` yourself (its Remarks explain the choice, and say
when the setting has helped).

**Tightness search stopped at the edge of its range.**
When the overall tightness is chosen by the search, it is looked for between
0.001 and 5 (between 0.0001 and 5 when the residual variances are chosen
too). If the search stops at either end, no peak was found: the value
is the edge of the range, not a value chosen by the data. The workflow prints
a note saying so as soon as the search ends, before the model is fitted, and
then fits and forecasts with the edge value. At the lower edge the prior holds
the coefficients close to their prior means; at the upper edge the prior barely
restrains them. The result records the case in ``wf.prior_search.status``
(``"at_bound"``) and ``wf.prior_search.at_bound`` (``"overall_tightness"``). When
the residual variances are chosen and one of them stops at an edge of its
range, the note names the series and *at_bound* contains
``"residual_variances"``. The note is not printed with ``quiet=1``. To set
the tightness yourself, pass a number as ``overall_tightness``.

**The holdout check.** The held-out observations are forecast once, from the
end of the training sample, so the errors at different horizons come from one
start date. The BVAR's errors use its median forecast and the least-squares
VAR's use its point forecast. For an evaluation over many start dates, with
tests, use :func:`forecastEval`.

**Variable names.** Pass a dataframe. Converting it to a matrix first drops
the names, and the tables and plots then show ``Y1``, ``Y2``, and so on.

**Draws.** The forecast is simulated, so its medians and bands change a
little with *seed*; more draws (*n_draws*) make them steadier.

Source Examples
---------------

See the shipped examples:

- ``pkgs/timeseries/examples/workflows/bvar_macro_forecast_3var_holdout.e``
- ``pkgs/timeseries/examples/workflows/bvar_macro_forecast_fred_qd.e``
- ``pkgs/timeseries/examples/workflows/bvar_macro_forecast_plot.e``

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarChoose`, :func:`printForecast`, :func:`plotForecast`, :func:`bvarMacroForecastPrint`, :func:`bvarMacroForecastPlot`, :func:`bvarForecast`, :func:`bvarFit`, :func:`varLagSelect`, :func:`bvarPriorSelect`, :func:`forecastEval`
