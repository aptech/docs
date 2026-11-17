bvarSvControlCreate
===================

Purpose
-------
Create a :class:`bvarSvControl` structure with default values.

The lag order starts empty. Set ``ctl.p`` or pass ``p=`` when fitting.
Saved structures with renamed fields must be recreated under the current schema.

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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.ssvs = 1;
    // SSVS requires the default own-first-lag prior mean of 1.

    result = bvarSvFit(data, p=ctl.p, ctl=ctl);

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarSvFit`
