printForecast
=============

Purpose
-------
Print forecast output from a BVAR macro workflow result or a lower-level
forecast result.

Format
------

.. function:: printForecast(wf)
              printForecast(wf, vars=vars)
              printForecast(wf, horizons=8)
              printForecast(wf, vars=vars, horizons=horizons)
              printForecast(fc)
              forecastPrint(wf, vars=vars, horizons=horizons)
              forecastPrint(fc)

   :param wf: Workflow result returned by :func:`bvarMacroForecast`.
   :type wf: struct bvarMacroForecastResult

   :param fc: Forecast result from :func:`bvarForecast`. This lower-level form
       prints the standard forecast table and does not support ``vars`` or
       ``horizons`` filters.
   :type fc: struct forecastResult

   :param vars: Optional keyword for workflow input, variables to print. Omit
       or pass ``{}`` to print all variables. Numeric input selects 1-based
       column indices. A GAUSS string array selects variables by name.
   :type vars: scalar, vector, or string array

   :param horizons: Optional keyword for workflow input, forecast horizons to
       print. Omit or pass ``{}`` to print all horizons. A scalar prints
       horizons 1 through ``N``, clamped to the workflow forecast horizon. A
       vector prints exactly the selected 1-based horizons.
   :type horizons: scalar or vector

Examples
--------

Print Workflow Forecast Output
++++++++++++++++++++++++++++++

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

    call printForecast(wf, horizons=8);

Select Variables by Name
++++++++++++++++++++++++

::

    string vars = { "gdp", "cons", "inv" };
    call printForecast(wf, vars=vars, horizons=8);

Select Variables and Horizons by Index
++++++++++++++++++++++++++++++++++++++

::

    call printForecast(wf, vars={ 1, 3 }, horizons={ 1, 4, 8 });

Print a Lower-Level Forecast Result
+++++++++++++++++++++++++++++++++++

::

    result = bvarFit(y, ctl=ctl);
    fc = bvarForecast(result, 8);

    call printForecast(fc);

Remarks
-------

For :class:`bvarMacroForecastResult` input, the printed summary includes the
selected lag order, Minnesota prior tightness, training-sample and full-sample
log marginal likelihoods, and holdout scores when the workflow was run with
``holdout > 0``.

The workflow forecast output includes three tables for the selected variables
and horizons: forecast means, lower forecast bands, and upper forecast bands.

For :class:`forecastResult` input, :func:`printForecast` prints the standard
forecast table. Variable and horizon filters are only available for workflow
input because the workflow result carries the fit, forecast, scoring, and
metadata needed for the compact presentation.

Selection Rules for Workflow Input
----------------------------------

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
     - Select variables by name from workflow forecast metadata.
   * - ``horizons={}``
     - Print all forecast horizons.
   * - scalar ``horizons=N``
     - Print horizons 1 through ``N``, clamped to the workflow forecast horizon.
   * - vector ``horizons``
     - Print exactly the selected 1-based horizons.

.. note::

   Name-based variable selection requires dataframe labels. Load data with
   :func:`loadd` and avoid converting it with ``asmatrix()`` before calling
   :func:`bvarMacroForecast`.

Compatibility Aliases
---------------------

:func:`forecastPrint` is a compatibility alias for :func:`printForecast`.
:func:`bvarMacroForecastPrint` remains available as a workflow-specific
compatibility alias. New examples use :func:`printForecast`.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarMacroForecast`, :func:`bvarMacroForecastPrint`, :func:`plotForecast`, :func:`bvarForecast`, :func:`bvarFit`
