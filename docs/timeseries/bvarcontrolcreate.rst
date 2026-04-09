bvarControlCreate
=================

Purpose
-------
Create a :class:`bvarControl` structure with default values.

Format
------

.. function:: ctl = bvarControlCreate()

   :return ctl: An instance of a :class:`bvarControl` structure with the following default values:

       .. include:: include/bvarcontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    // Minnesota BVAR(4) with tighter prior
    result = bvarFit(data, p=4, overall_tightness=0.1, n_draws=10000);

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarHyperopt`
