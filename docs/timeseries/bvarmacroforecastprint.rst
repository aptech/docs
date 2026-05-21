bvarMacroForecastPrint
======================

Purpose
-------
Compatibility alias for printing W1 macro BVAR workflow forecast output. New
code should use :func:`printForecast`.

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

Preferred Form
++++++++++++++

::

    call printForecast(wf, horizons=8);

Compatibility Form
++++++++++++++++++

::

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

:func:`bvarMacroForecastPrint` remains available for existing workflow code. It
prints the same workflow summary and forecast tables as
``call printForecast(wf, ...)``.

For a lower-level :class:`forecastResult`, use :func:`printForecast` directly.

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

.. seealso:: Functions :func:`printForecast`, :func:`bvarMacroForecast`, :func:`bvarMacroForecastPlot`, :func:`plotForecast`
