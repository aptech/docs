forecastEval
============

Purpose
-------
Pseudo out-of-sample forecast evaluation: refit each model at repeated start dates, forecast ahead, and compare the forecasts with what happened. Reports RMSE relative to a benchmark with Diebold-Mariano tests, bias, and band coverage.

Format
------

.. function:: fe = forecastEval(y, models, train_end="1920", h=5)
              fe = forecastEval(y, models, train_end="2019-Q4", h=8, benchmark="AR(bic)", window="rolling", step=1, period=4)
              fe = forecastEval(y, models, target="defl", train_end="2009-Q4", h=4, benchmark="AR(bic)", periods=P)
              fe = forecastEval(y, forecasts=F, names="My model", train_end="1920", h=5)

   :param y: the data: one series, or a dataframe with named columns and an optional date column. Fitted VAR and BVAR models find their variables in *y* by name.
   :type y: Nx1 vector or dataframe

   :param models: the models to evaluate: a string array of model specifications, each refitted on every target variable alone (see Remarks); a :func:`varFit` or :func:`bvarFit` result; or several models made by :func:`forecastModel` and joined with ``|``.
   :type models: string array or struct

   :param target: Optional keyword, name of the variable to score, or a string array of names. Default = the variables of the first fitted model, or the series when *y* has one column.
   :type target: string or string array

   :param train_end: end of the first estimation sample. For dated data, a GAUSS date string read as a point in time: ``"1920"`` is 1920-01-01, ``"2019-12"`` is 2019-12-01, ``"2019-Q4"`` is 2019-10-01, ``"2019-12-31"``. The first fit uses every observation dated on or before it. For undated data, a row number.
   :type train_end: string or scalar

   :param origins: Optional keyword, start dates given one by one instead of *train_end* and *step*: date strings for dated data, row numbers otherwise. Each is the last observation used.
   :type origins: string array or vector

   :param h: largest forecast horizon.
   :type h: scalar

   :param benchmark: Optional keyword, specification of the benchmark model, or the name of a model in the list. A specification is fitted to each target variable alone and added to *models* if not already listed. Default = ``"naive"``, or ``"snaive"`` when *period* > 1.
   :type benchmark: string

   :param window: Optional keyword, ``"expanding"`` (refit on all data up to each origin) or ``"rolling"`` (keep the first sample's length). Default = ``"expanding"``.
   :type window: string

   :param step: Optional keyword, periods between start dates. Default = 1.
   :type step: scalar

   :param period: Optional keyword, seasonal period for ``"snaive"``, seasonal ARIMA and ETS. Default = 1.
   :type period: scalar

   :param levels: Optional keyword, band levels whose coverage is reported. Default = ``0.68|0.90``.
   :type levels: vector

   :param dm: Optional keyword, Diebold-Mariano variant passed to :func:`dmTest`: ``"hln"``, ``"hac_hln_t"`` or ``"asymptotic"``. Default = ``"hln"``.
   :type dm: string

   :param periods: Optional keyword, sub-period reports: one row per period giving the first and last date forecast, for example ``{ "2010-Q1" "2014-Q4", "2015-Q1" "2019-Q4" }`` (row numbers for undated data). The RMSE and bias tables are repeated for the dates forecast inside each period.
   :type periods: Qx2 string array or matrix

   :param seed: Optional keyword, random seed for BVAR draws; start date *i* uses *seed* + *i* - 1. Default = 42.
   :type seed: scalar

   :param forecasts: Optional keyword, forecasts made elsewhere for one target: one row per start date and *h* columns per model. The start dates must be those implied by *train_end* and *step* (or *origins*). Benchmark forecasts are still made by the function.
   :type forecasts: matrix

   :param names: Optional keyword, names of the *forecasts* models.
   :type names: string array

   :param quiet: Optional keyword, 1 to suppress printing. Default = 0.
   :type quiet: scalar

   :return fe: An instance of a :class:`forecastEvalResult` structure (see below).
   :rtype fe: struct

Examples
--------

::

    new;
    library timeseries;

    nile = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));

    // Stand at every year from 1920 to 1969, refit both models on the
    // data up to that year, forecast 1-5 years ahead, and compare with
    // the naive forecast (added automatically)
    fe = forecastEval(nile, { "ARIMA(0,1,1)", "ARIMA(1,1,1)" }, train_end="1920", h=5);

The output is:

::

    Pseudo out-of-sample forecast evaluation: Flow
    ================================================================================
    Estimation samples: 1871-1920 (first), expanding to 1871-1969; 50 start dates
    RMSE relative to naive (below 1 is better).
    Diebold-Mariano test vs naive: * 10%  ** 5%  *** 1%

    Horizon  naive RMSE  ARIMA(0,1,1)  ARIMA(1,1,1)  Obs
    ----------------------------------------------------
    1             138.1       0.83**        0.82***   50
    2             150.9       0.79***       0.77***   49
    3             140.1       0.87**        0.83**    48
    4             159.2       0.81***       0.77***   47
    5             164.7       0.79***       0.75***   46

    Bias: average of forecast minus outcome (positive: forecasts too high).
    Test of zero bias (Newey-West): * 10%  ** 5%  *** 1%

    Horizon  naive  ARIMA(0,1,1)  ARIMA(1,1,1)
    ------------------------------------------
    1          1.6           3.2           1.7
    2          2.8           2.1           0.1
    3          5.5           1.7          -0.7
    4          4.4           0.7          -1.8
    5          7.0          -0.3          -2.7

    Share of outcomes inside the 68% band (%)

    Horizon  ARIMA(0,1,1)  ARIMA(1,1,1)
    -----------------------------------
    1                  82            80
    2                  82            82
    3                  77            79
    4                  77            79
    5                  80            80

    Share of outcomes inside the 90% band (%)

    Horizon  ARIMA(0,1,1)  ARIMA(1,1,1)
    -----------------------------------
    1                  96            98
    2                  98            98
    3                 100            98
    4                  96            98
    5                 100            98

    Failed fits: none

VAR and BVAR models are set up as you would fit them on the full sample; their
settings are kept and their coefficients re-estimated at every start date:

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium_dated.csv"));
    y = y[., "date" "gdp" "defl" "ffr"];

    // Set the models up as you would fit them on the full sample
    v = varFit(y, p=2, quiet=1);
    b = bvarFit(y, p=2, overall_tightness=0.2, lag1_prior_mean="zero", quiet=1);

    // Refit both at every quarter from 2009Q4, forecast inflation (defl)
    // 1-4 quarters ahead, and compare with an autoregression
    models = forecastModel(v) | forecastModel(b, name="Minnesota BVAR");
    fe = forecastEval(y, models, target="defl", train_end="2009-Q4", h=4,
        benchmark="AR(bic)");

The output is:

::

    Pseudo out-of-sample forecast evaluation: defl
    ================================================================================
    Estimation samples: 1960Q1-2009Q4 (first), expanding to 1960Q1-2019Q3; 40 start dates
    Models refitted at every start date; lag order and prior settings held as given.
    BVAR forecasts scored at the mean of the predictive draws.
    RMSE relative to AR(bic) (below 1 is better).
    Diebold-Mariano test vs AR(bic): * 10%  ** 5%  *** 1%

    Horizon  AR(bic) RMSE   VAR(2)  Minnesota BVAR  Obs
    ---------------------------------------------------
    1              0.2291  0.99               0.98   40
    2              0.2386  1.04               1.02   39
    3              0.2367  1.02               0.97   38
    4              0.2366  1.06**             0.97   37

    Bias: average of forecast minus outcome (positive: forecasts too high).
    Test of zero bias (Newey-West): * 10%  ** 5%  *** 1%

    Horizon  AR(bic)     VAR(2)  Minnesota BVAR
    -------------------------------------------
    1         0.0243  0.0265             0.0157
    2         0.0374  0.0502             0.0298
    3         0.0555  0.0786*            0.0489
    4         0.0723  0.1086**           0.0695

    Share of outcomes inside the 68% band (%)

    Horizon  AR(bic)  VAR(2)  Minnesota BVAR
    ----------------------------------------
    1             78      78              85
    2             82      79              82
    3             84      84              84
    4             89      92              92

    Share of outcomes inside the 90% band (%)

    Horizon  AR(bic)  VAR(2)  Minnesota BVAR
    ----------------------------------------
    1             90      90              90
    2             92      90              92
    3             97      97              97
    4            100     100             100

    Failed fits: none

Model specifications are strings, so a list can also be kept in a variable:

::

    string models = { "auto", "ETS", "AR(bic)" };
    fe = forecastEval(nile, models, train_end="1920", h=5);

Remarks
-------

**Model specifications.** Each string is a recipe that is refitted at every
start date with only the data available then, on each target variable alone:

.. list-table::
   :widths: auto

   * - ``"ARIMA(p,d,q)"``, ``"ARIMA(p,d,q)(P,D,Q)[m]"``
     - Fixed orders, fitted by :func:`arimaFit`.
   * - ``"auto"``
     - :func:`autoArima`, rerun at every start date.
   * - ``"ETS"``, ``"ETS(A,N,N)"``
     - Automatic or fixed ETS (error A/M, trend N/A/Ad, season N/A/M).
   * - ``"naive"``
     - Last observed value (random walk).
   * - ``"drift"``
     - Last observed value plus *h* times the average change over the estimation sample (random walk with drift).
   * - ``"snaive"``
     - Value one season earlier (needs *period*).
   * - ``"mean"``
     - Mean of the estimation sample.
   * - ``"AR(bic)"``, ``"AR(p)"``
     - Autoregression with a constant; lag order by BIC (0 to max(4, 2 *period*)) or fixed.

**Fitted VAR and BVAR models.** A :func:`varFit` or :func:`bvarFit` result
passed directly or through :func:`forecastModel` is a recipe: its lag order
and constant, a VAR's trend and residual covariance choice, and a BVAR's
prior and prior settings are kept, and the model is refitted on its own
variables at every start date. These are not re-chosen at each start date. Models with exogenous regressors are not
supported yet.

**No look-ahead.** Every fit, including the automatic ARIMA and ETS searches,
the BIC lag choice and a BVAR's prior residual scales, uses only observations
up to its start date.

**Common sample.** At each horizon all models are scored on the same start
dates: those where every model produced a forecast and the outcome exists.
The *Obs* column reports how many.

**What is scored.** Errors are forecast minus outcome. RMSE, bias and the
Diebold-Mariano test use the point forecast that minimises expected squared
error: the mean of the predictive draws for a BVAR, the point forecast
otherwise. MAE uses the predictive median.

A BVAR made by :func:`forecastModel` with ``point="posterior_mean"`` is
instead forecast from its posterior-mean coefficients, iterated forward,
without draws (Banbura, Giannone and Reichlin 2010). RMSE, bias and MAE all
use that forecast, and the model has no bands. Its memory and time do not
grow with the number of draws, which suits systems too large to simulate at
every start date.

**Bias.** The average error at each horizon, with a test that it is zero:
the errors are regressed on a constant with a Newey-West standard error
(Bartlett weights, *h* - 1 lags) and a normal reference, as in the Bank of
England's forecast evaluation (Abiry et al. 2026).

**Band coverage.** The share of outcomes inside each band; an outcome on a
band edge counts as inside. BVAR bands are quantiles of the predictive
draws; VAR, ARIMA and ETS bands are the models' own intervals (VAR intervals
leave out coefficient uncertainty). Naive, snaive, drift and mean forecasts
have no band, nor does a BVAR with ``point="posterior_mean"``.

**Failed fits** are recorded in *status* and *status_messages*, excluded, and
counted in the printout; they do not stop the run.

**Diebold-Mariano test.** Stars compare each model with the benchmark using
:func:`dmTest` on squared errors, two-sided, with the horizon as *h*; the
default variant has the Harvey-Leybourne-Newbold correction.

Central banks call this exercise pseudo out-of-sample forecast evaluation with
a recursive (expanding) or rolling window; Hyndman & Athanasopoulos
(*Forecasting: Principles and Practice*, 3rd ed., section 5.10) call it time
series cross-validation.

forecastEvalResult
++++++++++++++++++

Models are indexed 1..M in the order of *model_names* and targets 1..T in the
order of *targets*. Forecasts and errors are stored per model in blocks of *h*
columns: model *j* uses columns (j-1)h+1 to jh. Rows are stacked by target:
target *t* uses rows (t-1)O+1 to tO, one per start date. Summary tables have
one row per horizon, stacked by target the same way (rows (t-1)h+1 to th).
With one target the rows are just the start dates or horizons.

.. list-table::
   :widths: auto

   * - model_names
     - Mx1 string array, display names.
   * - specs
     - Mx1 string array, specifications ("" for fitted and *forecasts* models).
   * - model_kinds
     - Mx1 string array, ``"spec"``, ``"var"``, ``"bvar"`` or ``"user"``.
   * - benchmark
     - String, benchmark name.
   * - benchmark_index
     - Scalar, row of the benchmark in *model_names*.
   * - series_name
     - String, the first target ("" if *y* has no column names).
   * - targets
     - Tx1 string array, the variables scored.
   * - origins
     - Ox1, row of the last observation used at each start date.
   * - origin_dates
     - Ox1 POSIX dates of those observations (empty if undated).
   * - freq
     - String, frequency of the date index ("" if undated).
   * - h, window, step, period, levels, dm_variant, seed
     - The settings used (*step* is 0 when *origins* gave the start dates).
   * - actual
     - (TO) x h outcomes (missing beyond the data).
   * - forecasts, errors
     - (TO) x (hM) point forecasts scored by RMSE and bias, and forecast minus outcome.
   * - medians
     - (TO) x (hM) predictive medians, scored by MAE (equal to *forecasts* except for a BVAR).
   * - lower, upper
     - (TO) x (hML) band bounds; level *l* uses columns (l-1)hM+1 to lhM (missing: no band).
   * - status
     - O x M: 0 fitted, 2 fitted but not converged, other values failed.
   * - status_messages
     - O x M failure messages ("" when fitted).
   * - n_used
     - (Th) x 1, start dates in the common sample at each horizon.
   * - rmse, mae
     - (Th) x M accuracy by horizon and model.
   * - ratio
     - (Th) x M RMSE relative to the benchmark.
   * - dm_stat, dm_pvalue
     - (Th) x M Diebold-Mariano statistic and two-sided p-value against the benchmark (missing for the benchmark itself).
   * - bias, bias_pvalue
     - (Th) x M average of forecast minus outcome and the two-sided p-value of zero bias.
   * - coverage
     - (Th) x (ML) share of outcomes inside the band; level *l* uses columns (l-1)M+1 to lM (missing: no band).
   * - period_bounds, period_labels
     - Qx2 first and last date forecast in each sub-period, and Qx1 labels (empty without *periods*).
   * - period_n_used, period_rmse, period_ratio, period_dm_pvalue, period_bias, period_bias_pvalue
     - The same tables on each sub-period, stacked by period, then target, then horizon: row ((q-1)T+(t-1))h+k.

References
----------

- Banbura, M., D. Giannone and L. Reichlin (2010). "Large Bayesian vector auto regressions." *Journal of Applied Econometrics*, 25(1), 71-92.
- Diebold, F.X. and R.S. Mariano (1995). "Comparing predictive accuracy." *Journal of Business & Economic Statistics*, 13(3), 253-263.
- Abiry, R., J. Hurley, P. Labonne, D. Latto, H. Li, A. Moreira, J. Oyegoke and S. Singh (2026). "Learning from forecast errors: the Bank's enhanced approach to forecast evaluation." Bank of England Macro Technical Paper No. 6.
- Harvey, D., S. Leybourne, and P. Newbold (1997). "Testing the equality of prediction mean squared errors." *International Journal of Forecasting*, 13(2), 281-291.
- Hyndman, R.J. and G. Athanasopoulos (2021). *Forecasting: Principles and Practice*, 3rd ed. OTexts.
- Newey, W.K. and K.D. West (1987). "A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix." *Econometrica*, 55(3), 703-708.

Library
-------
timeseries

Source
------
forecast_eval.src

.. seealso:: Functions :func:`forecastModel`, :func:`dmTest`, :func:`fcScore`, :func:`varFit`, :func:`bvarFit`, :func:`arimaFit`, :func:`autoArima`, :func:`etsFit`
