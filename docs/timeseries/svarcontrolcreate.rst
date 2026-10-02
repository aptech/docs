svarControlCreate
=================

Purpose
-------
Create an :class:`svarControl` structure with narrative restrictions and the
rotation sampler choice for sign identification in :func:`irfCompute`.

Format
------

.. function:: ctl = svarControlCreate()

   :return ctl: An instance of an :class:`svarControl` structure with the following members:

       .. include:: include/svarcontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = bvarFit(y, p=4, quiet=1);

    signs = signRestrictions({ "fed_funds"     "monetary" "0:4" "+",
                               "cpi_inflation" "monetary" "0:4" "-" });

    ctl = svarControlCreate();

    // The monetary shock (shock 1) was positive at observation 95 and was
    // the largest contributor to the funds rate surprise at observations
    // 95 to 96 of the estimation sample.
    ctl.narrative_restr = { 1 0 1 95  0 1,
                            2 3 1 95 96 0 };

    irf = irfCompute(fit, 20, restrictions=signs, ctl=ctl);

Remarks
-------

Sign and zero restrictions are given to :func:`irfCompute` with
``restrictions=`` (see :func:`signRestrictions`). Shocks are numbered in the
order they first appear in the restriction table, and narrative restrictions
use these numbers.

Narrative restrictions follow Antolin-Diaz and Rubio-Ramirez (2018): a draw
is kept only if its structural shocks and historical decomposition agree
with every narrative statement. They are available for :func:`bvarFit`
results.

References
----------

- Antolin-Diaz, J. and J.F. Rubio-Ramirez (2018). "Narrative sign restrictions for SVARs." *American Economic Review*, 108(10), 2802-2829.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`irfCompute`, :func:`signRestrictions`
