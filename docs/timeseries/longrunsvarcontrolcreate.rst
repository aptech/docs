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

    adv = longRunSvarControlCreate();

    // Remove the constant and suppress output
    adv.include_const = 0;
    adv.quiet = 1;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation");

    lr = longRunSvar(y, 20, 4, adv);

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`longRunSvar`
