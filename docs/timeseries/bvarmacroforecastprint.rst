bvarMacroForecastPrint
======================

Purpose
-------
Print a W1 macro BVAR workflow summary and forecast tables.

Format
------

.. function:: bvarMacroForecastPrint(wf)
              bvarMacroForecastPrint(wf, vars=vars)
              bvarMacroForecastPrint(wf, horizons=8)
              bvarMacroForecastPrint(wf, vars=vars, horizons=horizons)

   :param wf: Workflow result returned by :func:`bvarMacroForecast`.
   :type wf: struct bvarMacroForecastResult

   :param vars: Optional keyword, variables to print. Omit or pass ``{}`` to
       print all variables. Numeric input selects 1-based column indices.
       A GAUSS string array selects variables by name.
   :type vars: scalar, vector, or string array

   :param horizons: Optional keyword, forecast horizons to print. Omit or pass
       ``{}`` to print all horizons. A scalar prints horizons 1 through ``N``,
       clamped to the workflow forecast horizon. A vector prints exactly the
       selected 1-based horizons.
   :type horizons: scalar or vector

Examples
--------

Print the First 8 Horizons
++++++++++++++++++++++++++

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

    call bvarMacroForecastPrint(wf, horizons=8);

Select Variables by Name
++++++++++++++++++++++++

::

    string vars = { "gdp", "cons", "inv" };
    call bvarMacroForecastPrint(wf, vars=vars, horizons=8);

Select Variables and Horizons by Index
++++++++++++++++++++++++++++++++++++++

::

    call bvarMacroForecastPrint(wf, vars={ 1, 3 }, horizons={ 1, 4, 8 });

Remarks
-------

The printed summary includes the selected lag order, Minnesota prior tightness,
training-sample and full-sample log marginal likelihoods, and holdout scores
when the workflow was run with ``holdout > 0``.

The forecast output includes three tables for the selected variables and
horizons: forecast means, lower forecast bands, and upper forecast bands.

Selection Rules
---------------

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

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarMacroForecast`, :func:`bvarMacroForecastPlot`, :func:`plotForecast`
