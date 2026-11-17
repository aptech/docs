bvarControlCreate
=================

Purpose
-------
Create a :class:`bvarControl` structure with default values.

The lag order starts empty. Set ``ctl.p`` or pass ``p=`` when fitting.
Saved structures with renamed fields must be recreated under the current schema.

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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    // Tighter shrinkage for the 4-lag quarterly model.
    ctl.overall_tightness = 0.1;
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    ctl.lag1_prior_mean = { 0, 1, 1 };
    ctl.n_draws = 10000;

    result = bvarFit(data, p=ctl.p, ctl=ctl);

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarPriorSelect`
