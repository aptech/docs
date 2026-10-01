forecastEval
============

Purpose
-------
Pseudo out-of-sample forecast evaluation: refit each model at repeated forecast origins, forecast ahead, and compare the forecasts with what happened.

Format
------

.. function:: fe = forecastEval(y, models, train_end="1920", h=5)
              fe = forecastEval(y, models, train_end="2019-Q4", h=8, benchmark="AR(bic)", window="rolling", step=1, period=4)
              fe = forecastEval(y, forecasts=F, names="My model", train_end="1920", h=5)

   :param y: the series. A dataframe with one numeric column and an optional date column is also accepted.
   :type y: Nx1 vector or dataframe

   :param models: model specifications, each refitted at every origin (see Remarks).
   :type models: string array

   :param train_end: end of the first estimation sample. For dated data, a GAUSS date string read as a point in time: ``"1920"`` is 1920-01-01, ``"2019-12"`` is 2019-12-01, ``"2019-Q4"`` is 2019-10-01, ``"2019-12-31"``. The first fit uses every observation dated on or before it. For undated data, a row number.
   :type train_end: string or scalar

   :param h: largest forecast horizon.
   :type h: scalar

   :param benchmark: Optional keyword, specification of the benchmark model. It is added to *models* if not already listed. Default = ``"naive"``, or ``"snaive"`` when *period* > 1.
   :type benchmark: string

   :param window: Optional keyword, ``"expanding"`` (refit on all data up to each origin) or ``"rolling"`` (keep the first sample's length). Default = ``"expanding"``.
   :type window: string

   :param step: Optional keyword, periods between origins. Default = 1.
   :type step: scalar

   :param period: Optional keyword, seasonal period for ``"snaive"``, seasonal ARIMA and ETS. Default = 1.
   :type period: scalar

   :param forecasts: Optional keyword, forecasts made elsewhere: one row per origin and *h* columns per model. The origins must be those implied by *train_end* and *step*. Benchmark forecasts are still made by the function.
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
    Estimation samples: 1871-1920 (first), expanding to 1871-1969; 50 origins
    RMSE relative to naive (below 1 is better).
    Diebold-Mariano test vs naive: * 10%  ** 5%  *** 1%

    Horizon  naive RMSE  ARIMA(0,1,1)  ARIMA(1,1,1)  Obs
    ----------------------------------------------------
    1             138.1       0.83**        0.82***   50
    2             150.9       0.79***       0.77***   49
    3             140.1       0.87**        0.83**    48
    4             159.2       0.81***       0.77***   47
    5             164.7       0.79***       0.75***   46

    Failed fits: none

Model specifications are strings, so a list can also be kept in a variable:

::

    string models = { "auto", "ETS", "AR(bic)" };
    fe = forecastEval(nile, models, train_end="1920", h=5);

Remarks
-------

**Model specifications.** Each string is a recipe that is refitted at every
origin with only the data available then:

.. list-table::
   :widths: auto

   * - ``"ARIMA(p,d,q)"``, ``"ARIMA(p,d,q)(P,D,Q)[m]"``
     - Fixed orders, fitted by :func:`arimaFit`.
   * - ``"auto"``
     - :func:`autoArima`, rerun at every origin.
   * - ``"ETS"``, ``"ETS(A,N,N)"``
     - Automatic or fixed ETS (error A/M, trend N/A/Ad, season N/A/M).
   * - ``"naive"``
     - Last observed value (random walk).
   * - ``"snaive"``
     - Value one season earlier (needs *period*).
   * - ``"mean"``
     - Mean of the estimation sample.
   * - ``"AR(bic)"``, ``"AR(p)"``
     - Autoregression with a constant; lag order by BIC (0 to max(4, 2 *period*)) or fixed.

**No look-ahead.** Every fit, including the automatic ARIMA and ETS searches and
the BIC lag choice, uses only observations up to its origin.

**Common sample.** At each horizon all models are scored on the same origins:
those where every model produced a forecast and the actual value exists. The
*Obs* column reports how many.

**Failed fits** are recorded in *status* and *status_messages*, excluded, and
counted in the printout; they do not stop the run.

**Diebold-Mariano test.** Stars compare each model with the benchmark using
:func:`dmTest` on squared errors with the Harvey-Leybourne-Newbold correction
(two-sided).

Central banks call this exercise pseudo out-of-sample forecast evaluation with
a recursive (expanding) or rolling window; Hyndman & Athanasopoulos
(*Forecasting: Principles and Practice*, 3rd ed., section 5.10) call it time
series cross-validation.

forecastEvalResult
++++++++++++++++++

Models are indexed 1..M in the order of *model_names*. Forecasts and errors
are stored per model in blocks of *h* columns: model *j* uses columns
(j-1)h+1 to jh.

.. list-table::
   :widths: auto

   * - model_names
     - Mx1 string array, display names.
   * - specs
     - Mx1 string array, specifications ("" for *forecasts* models).
   * - benchmark
     - String, benchmark name.
   * - benchmark_index
     - Scalar, row of the benchmark in *model_names*.
   * - series_name
     - String, column name of *y* ("" if none).
   * - origins
     - Ox1, row of the last observation used at each origin.
   * - origin_dates
     - Ox1 POSIX dates of those observations (empty if undated).
   * - freq
     - String, frequency of the date index ("" if undated).
   * - h, window, step, period
     - The settings used.
   * - actual
     - O x h realised values (missing beyond the data).
   * - forecasts, errors
     - O x (hM) point forecasts and actual minus forecast.
   * - status
     - O x M: 0 fitted, 2 fitted but not converged, other values failed.
   * - status_messages
     - O x M failure messages ("" when fitted).
   * - n_used
     - hx1, origins in the common sample at each horizon.
   * - rmse, mae
     - h x M accuracy by horizon and model.
   * - ratio
     - h x M RMSE relative to the benchmark.
   * - dm_stat, dm_pvalue
     - h x M Diebold-Mariano statistic and two-sided p-value against the benchmark (missing for the benchmark itself).

References
----------

- Diebold, F.X. and R.S. Mariano (1995). "Comparing predictive accuracy." *Journal of Business & Economic Statistics*, 13(3), 253-263.
- Harvey, D., S. Leybourne, and P. Newbold (1997). "Testing the equality of prediction mean squared errors." *International Journal of Forecasting*, 13(2), 281-291.
- Hyndman, R.J. and G. Athanasopoulos (2021). *Forecasting: Principles and Practice*, 3rd ed. OTexts.

Library
-------
timeseries

Source
------
forecast_eval.src

.. seealso:: Functions :func:`dmTest`, :func:`fcScore`, :func:`arimaFit`, :func:`autoArima`, :func:`etsFit`
