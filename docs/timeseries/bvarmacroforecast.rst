bvarMacroForecast
=================

Purpose
-------
Run the Workflow 1 (W1) standard reduced-form macro BVAR forecasting path.

Format
------

.. function:: wf = bvarMacroForecast(y)
              wf = bvarMacroForecast(y, horizon=8, holdout=20)
              wf = bvarMacroForecast(y, h=8, max_lags=4, lag_ic="bic")
              wf = bvarMacroForecast(y, tune="glp", data_type="stationary")

   :param y: Endogenous macro variables. If a dataframe, column names are used
       in forecast tables and plot titles. If a matrix, variables are labeled
       ``Y1``, ``Y2``, etc.
   :type y: TxM matrix or dataframe

   :param h: Optional keyword, forward forecast horizon. Alias for
       ``horizon``. Default = 8.
   :type h: scalar

   :param horizon: Optional keyword, forward forecast horizon. Alias for ``h``.
       Default = 8.
   :type horizon: scalar

   :param holdout: Optional keyword, number of final observations reserved for
       holdout scoring before refitting the final model on the full sample.
       Default = 0.
   :type holdout: scalar

   :param data_type: Optional keyword, data persistence type. Use
       ``"stationary"`` for transformed growth-rate data and ``"levels"`` for
       persistent levels data. Default = ``"stationary"``.
   :type data_type: string

   :param max_lag: Optional keyword, maximum lag considered by lag selection.
       Alias for ``max_lags``. Default = 8.
   :type max_lag: scalar

   :param max_lags: Optional keyword, maximum lag considered by lag selection.
       Alias for ``max_lag``. Default = 8.
   :type max_lags: scalar

   :param lag_ic: Optional keyword, information criterion for lag selection:
       ``"aic"``, ``"bic"``, or ``"hq"``. Alias for ``lag_policy``.
       Default = ``"bic"``.
   :type lag_ic: string

   :param tune: Optional keyword, shrinkage policy. Use ``"glp"`` to optimize
       Minnesota prior tightness with :func:`bvarHyperopt` or ``"fixed"`` to use
       default/fixed settings. Alias for ``shrinkage_policy``. Default =
       ``"glp"``.
   :type tune: string

   :param baseline: Optional keyword, holdout baseline. Use ``"ols_var"`` to
       score an OLS VAR baseline when ``holdout`` is positive, or ``"none"``.
       Default = ``"ols_var"``.
   :type baseline: string

   :param level: Optional keyword, credible level for forecast bands.
       Default = 0.68.
   :type level: scalar

   :param n_draws: Optional keyword, posterior draws used by the BVAR forecast.
       Default = 5000.
   :type n_draws: scalar

   :param seed: Optional keyword, random number seed. Default = 42.
   :type seed: scalar

   :param const: Optional keyword, include an intercept. Default = 1.
   :type const: scalar

   :param quiet: Optional keyword, set to 1 to suppress workflow printing.
       Default = 0.
   :type quiet: scalar

   :param spec: Optional keyword, :class:`bvarMacroForecastSpec` structure.
       Explicit keyword arguments override values in ``spec``.
   :type spec: struct

   :return wf: A :class:`bvarMacroForecastResult` structure containing the
       resolved workflow specification, lag selection result, hyperparameter
       result, final full-sample BVAR fit, final forecast, optional holdout
       objects, and summary scores.
   :rtype wf: struct

Examples
--------

Canonical W1 Forecast
+++++++++++++++++++++

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

    call printForecast(wf, horizons=8);

Forecast and Plot
+++++++++++++++++

::

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

    call printForecast(wf, horizons=8);
    plotForecast(wf, history=24);

Remarks
-------

**Workflow scope:**
This W1 helper wraps the standard reduced-form forecast path:
:func:`varLagSelect`, :func:`bvarHyperopt`, :func:`bvarFit`, and
:func:`bvarForecast`. It is for unconditional macro forecasts from a
Minnesota-prior BVAR. It does not do structural identification, IRFs,
conditional forecasts, stochastic volatility, TVP-VAR, or VECM analysis.

**Dataframe labels:**
Load data with :func:`loadd` and keep the dataframe when possible. Do not call
``asmatrix()`` on dataframe input before calling :func:`bvarMacroForecast`;
that conversion drops variable names used by :func:`printForecast` and
:func:`plotForecast`.

**Holdout behavior:**
When ``holdout`` is positive, the workflow estimates and scores on the training
sample and holdout window, then refits the final BVAR on all available data
using the selected lag order and prior settings. The returned ``wf.forecast`` is
the final full-sample forecast.

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

.. seealso:: Functions :func:`printForecast`, :func:`plotForecast`, :func:`bvarMacroForecastPrint`, :func:`bvarMacroForecastPlot`, :func:`bvarForecast`, :func:`bvarFit`, :func:`varLagSelect`, :func:`bvarHyperopt`
