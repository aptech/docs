arimaControlCreate
==================

Purpose
-------
Create an :class:`arimaControl` structure with default values.

Format
------

.. function:: ctl = arimaControlCreate()

   :return ctl: An instance of an :class:`arimaControl` structure with the following default values:

       .. include:: include/arimacontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    // Create control structure with defaults
    ctl = arimaControlCreate();

    // Customize: BIC selection, ML estimation
    ctl.ic = "bic";
    ctl.method = "ml";

    // Use with arimaFit
    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline.dat");
    y = loadd(fname, "passengers");
    result = arimaFit(y, ctl, season=12);

Remarks
-------

All members of the :class:`arimaControl` structure apply only to auto-selection.
When a fixed *order* is passed to :func:`arimaFit`, the search-related members
(*max_p*, *max_q*, *max_d*, *ic*, *stepwise*, etc.) are ignored.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`
