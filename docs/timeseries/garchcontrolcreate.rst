garchControlCreate
==================

Purpose
-------
Create a :class:`garchControl` structure with default values.

Format
------

.. function:: ctl = garchControlCreate()

   :return ctl: An instance of a :class:`garchControl` structure with the following default values:

       .. include:: include/garchcontrol.rst

   :rtype ctl: struct

Examples
--------

Keep shared settings in one structure and change one setting per call with a
keyword:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/dmbp.csv");
    dm = loadd(fname, "return_pct");

    // t errors, OPG standard errors as well, no printed summary
    struct garchControl ctl;
    ctl = garchControlCreate();
    ctl.dist = "t";
    ctl.covariance = "opg";
    ctl.quiet = 1;

    // The same settings for a GARCH and a GJR fit; model= applies to the
    // second call only
    struct garchResult fit_g, fit_j;
    fit_g = garchFit(dm, ctl=ctl);
    fit_j = garchFit(dm, model="gjr", ctl=ctl);

    print "GARCH-t log likelihood:     " fit_g.loglik;
    print "GJR-GARCH-t log likelihood: " fit_j.loglik;
    print "ctl.model is still " ctl.model;

::

    error : garchFit: Warning: persistence is 1 (within 5.9e-08), the edge of the stationary region. Standard errors, p-values and limits assume a fit inside that region and may be unreliable.

    error : garchFit: Warning: persistence is 1 (within 9.8e-08), the edge of the stationary region. Standard errors, p-values and limits assume a fit inside that region and may be unreliable.

    GARCH-t log likelihood:           -989.77437
    GJR-GARCH-t log likelihood:       -988.70269
    ctl.model is still garch

The persistence warnings print even with ``ctl.quiet = 1``; see
:func:`garchFit`.

Remarks
-------

Every member except *max_iter* and *tol* can also be given as a keyword to
:func:`garchFit`, and a keyword overrides the member for that call only. The
orders are *ctl.p* (GARCH) and *ctl.q* (ARCH); the matching keywords are
*garch* and *arch*.

Library
-------
timeseries

Source
------
garch.src

.. seealso:: Functions :func:`garchFit`
