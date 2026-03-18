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

    struct varControl ctl;
    ctl = varControlCreate();

    // Remove the constant
    ctl.p = 4;
    ctl.include_const = 0;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, ctl);

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`
