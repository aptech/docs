longRunSvarControlCreate
=========================

Purpose
-------
Create a :class:`longRunSvarControl` structure with default values.

Format
------

.. function:: adv = longRunSvarControlCreate()

   :return adv: An instance of a :class:`longRunSvarControl` structure with the following default values:

       .. include:: include/longrunsvarcontrol.rst

   :rtype adv: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation");

    // Remove the constant — use struct for non-keyword settings
    adv = longRunSvarControlCreate();
    adv.const = 0;

    lr = longRunSvar(y, 20, p=4, quiet=1, ctl=adv);

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`longRunSvar`
