.. _getting-started-bvar-forecast:

Getting Started: Standard Macro BVAR Forecast
=============================================

This guide shows the Workflow 1 (W1) path for standard reduced-form macro BVAR
forecasting. The workflow loads a dataframe with variable names, runs
:func:`bvarMacroForecast`, prints a forecast summary, and optionally plots the
final forecast fan chart.

Use this workflow for unconditional macro forecasts from a Minnesota-prior BVAR.
It does not perform structural identification, impulse responses, conditional
forecasting, stochastic volatility, TVP-VAR, or VECM analysis.

The Canonical Workflow
----------------------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium.csv");
    y = loadd(fname);

    wf = bvarMacroForecast(y,
        horizon=8,
        holdout=20,
        data_type="stationary",
        max_lags=8,
        lag_ic="bic",
        tune="glp",
        baseline="ols_var",
        level=0.68,
        n_draws=2000,
        seed=42,
        quiet=1);

    call bvarMacroForecastPrint(wf, horizons=8);
    call bvarMacroForecastPlot(wf, history=24);

This is the same W1 pattern used by the shipped
``bvar_macro_forecast_fred_qd.e`` and ``bvar_macro_forecast_plot.e`` examples.

Step 1: Load a Dataframe
------------------------

::

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macrodata_logdiff.csv");
    y = loadd(fname);

Load the input as a dataframe when possible. Dataframe column names are carried
into the BVAR result, forecast tables, and plot titles.

.. warning::

   Do not call ``asmatrix()`` on dataframe input before passing it to
   :func:`bvarMacroForecast`. Converting to a matrix drops the variable names,
   so output labels fall back to ``Y1``, ``Y2``, and so on.

Step 2: Run the W1 Forecast
---------------------------

::

    wf = bvarMacroForecast(y,
        horizon=8,
        holdout=20,
        data_type="stationary",
        max_lags=4,
        lag_ic="bic",
        tune="glp",
        baseline="ols_var",
        level=0.68,
        n_draws=2000,
        seed=42,
        quiet=1);

The workflow runs the reduced-form forecast path:

- select the VAR lag order using :func:`varLagSelect`
- choose Minnesota shrinkage using :func:`bvarHyperopt` when ``tune="glp"``
- fit the conjugate BVAR using :func:`bvarFit`
- generate posterior predictive forecasts using :func:`bvarForecast`
- if ``holdout`` is positive, score the holdout window and then refit on the
  full sample for the final production forecast

For transformed growth-rate or stationary macro data, use
``data_type="stationary"``. For persistent levels data, use
``data_type="levels"``.

Step 3: Print Workflow Output
-----------------------------

::

    call bvarMacroForecastPrint(wf, horizons=8);

The print helper reports the selected lag order, prior tightness, log marginal
likelihoods, optional holdout scores, and forecast mean/lower/upper tables.

To print a subset of variables by name:

::

    string vars = { "gdp", "cons", "inv" };
    call bvarMacroForecastPrint(wf, vars=vars, horizons=8);

To print variables by column index:

::

    call bvarMacroForecastPrint(wf, vars={ 1, 3 }, horizons={ 1, 4, 8 });

``vars`` and ``horizons`` follow these rules:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Argument
     - Behavior
   * - ``vars={}``
     - Print all variables.
   * - numeric ``vars``
     - Select variables by 1-based column index.
   * - string array ``vars``
     - Select variables by dataframe column name.
   * - ``horizons={}``
     - Print all forecast horizons.
   * - scalar ``horizons=N``
     - Print horizons 1 through ``N``, clamped to the forecast horizon.
   * - vector ``horizons``
     - Print exactly the selected 1-based horizons.

Step 4: Plot the Forecast
-------------------------

::

    call bvarMacroForecastPlot(wf, history=24);

The plot helper draws the W1 forecast fan chart from the final full-sample BVAR
fit and forecast stored in ``wf``.

``history`` controls how many final historical observations are shown before the
forecast:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Argument
     - Behavior
   * - omitted
     - Show the last 20% of the sample or 40 observations, whichever is larger,
       capped at the sample length.
   * - ``history=N``
     - Show the last ``N`` historical observations, capped at the sample length.

Concise 3-Variable Example
--------------------------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macrodata_logdiff.csv");
    y = loadd(fname);

    wf = bvarMacroForecast(y,
        horizon=8,
        holdout=20,
        data_type="stationary",
        max_lags=4,
        lag_ic="bic",
        tune="glp",
        baseline="ols_var",
        level=0.68,
        n_draws=2000,
        seed=42,
        quiet=1);

    call bvarMacroForecastPrint(wf, horizons=8);

This matches the compact shipped example
``bvar_macro_forecast_3var_holdout.e``.

Related Functions
-----------------

See :func:`bvarMacroForecast`, :func:`bvarMacroForecastPrint`,
:func:`bvarMacroForecastPlot`, and :func:`plotForecast` for function-level
details.
