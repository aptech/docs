tvpSvControlCreate
===================

Purpose
-------
Create a :class:`tvpSvControl` structure with default values.

Format
------

.. function:: adv = tvpSvControlCreate()

   :return adv: An instance of a :class:`tvpSvControl` structure with the following default values:

       .. include:: include/tvpsvcontrol.rst

   :rtype adv: struct

Examples
--------

::

    new;
    library timeseries;

    struct tvpSvControl adv;
    adv = tvpSvControlCreate();

    // Tighter drift priors (less time variation in coefficients)
    adv.q_b_shape = 10.0;
    adv.q_b_scale = 0.001;

    // Band-limited U for a larger system
    adv.u_bandwidth = 3;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = tvpSvFit(y, 2, 10000, 10000, adv);

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`tvpSvFit`
