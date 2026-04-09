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
    ctl.n_chains = 4;
    ctl.parallel = 1;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = bvarSvFit(data, p=4, ssvs=1, n_draws=10000, n_burn=5000, ctl=ctl);

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarSvFit`
