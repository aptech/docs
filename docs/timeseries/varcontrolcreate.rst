varControlCreate
================

Purpose
-------
Create a :class:`varControl` structure with default values.

Format
------

.. function:: ctl = varControlCreate()

   :return ctl: An instance of a :class:`varControl` structure with the following default values:

       .. include:: include/varcontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    ctl = varControlCreate();

    // Remove the constant
    ctl.p = 4;
    ctl.include_const = 0;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = varFit(data, ctl=ctl);

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`
