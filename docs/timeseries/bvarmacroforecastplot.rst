bvarMacroForecastPlot
=====================

Purpose
-------
Plot the forecast fan chart from a W1 macro BVAR workflow result.

Format
------

.. function:: bvarMacroForecastPlot(wf)
              bvarMacroForecastPlot(wf, history=24)

   :param wf: Workflow result returned by :func:`bvarMacroForecast`.
   :type wf: struct bvarMacroForecastResult

   :param history: Optional keyword, number of final historical observations to
       show before the forecast begins. If omitted, the plot shows the last 20%
       of the sample or 40 observations, whichever is larger, capped at the
       sample length.
   :type history: scalar

Examples
--------

Plot a Compact History Window
+++++++++++++++++++++++++++++

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

    call printForecast(wf, horizons=8);
    plotForecast(wf, history=24);

Default History Window
++++++++++++++++++++++

::

    plotForecast(wf);

Remarks
-------

:func:`bvarMacroForecastPlot` remains available as a compatibility alias. New
code can call :func:`plotForecast` directly with the workflow result. Both forms
plot ``wf.fit`` and ``wf.forecast``, which are the final full-sample BVAR fit
and forecast returned by :func:`bvarMacroForecast`.

``history`` follows the same rules as :func:`plotForecast`:

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

For multivariate BVARs, each variable is shown in its own stacked panel. Variable
names are taken from the dataframe labels stored in the workflow forecast
metadata when available.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarMacroForecast`, :func:`printForecast`, :func:`bvarMacroForecastPrint`, :func:`plotForecast`
