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
    ctl.const = 0;
    ctl.trend = 1;
    ctl.resid_cov = "ml";

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"));
    result = varFit(data, ctl=ctl);

Remarks
-------

Pass the control with ``ctl=ctl``. Its *p*, *const*, *trend*, *xreg*,
*quiet* and *resid_cov* replace the corresponding keywords. *dates* and
*freq* remain separate keywords. The covariance choice follows the
uncertainty and structural outputs described in :func:`varFit`; likelihood
and information criteria always use ML. The same input checks apply.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`
