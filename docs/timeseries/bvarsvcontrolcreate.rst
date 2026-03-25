bvarSvControlCreate
===================

Purpose
-------
Create a :class:`bvarSvControl` structure with default values.

Format
------

.. function:: ctl = bvarSvControlCreate()

   :return ctl: An instance of a :class:`bvarSvControl` structure with the following default values:

       .. include:: include/bvarsvcontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    ctl = bvarSvControlCreate();

    // 4-chain SV-BVAR with SSVS
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    ctl.n_chains = 4;
    ctl.parallel = 1;
    ctl.ssvs = 1;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = bvarSvFit(data, ctl);

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarSvFit`
