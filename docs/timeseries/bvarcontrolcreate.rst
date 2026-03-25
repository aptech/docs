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

    ctl = bvarControlCreate();

    // Minnesota BVAR(4) with tighter prior
    ctl.p = 4;
    ctl.lambda1 = 0.1;
    ctl.n_draws = 10000;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = bvarFit(data, ctl);

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarHyperopt`
