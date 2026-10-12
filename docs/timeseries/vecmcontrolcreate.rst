vecmControlCreate
=================

Purpose
-------
Create a :class:`vecmControl` structure with default settings. It is needed only to pass your own regressors to :func:`vecmFit`.

Format
------

.. function:: ctl = vecmControlCreate()

   :return ctl: An instance of a :class:`vecmControl` structure with the members:

       .. include:: include/vecmcontrol.rst

   :rtype ctl: struct

Examples
--------

Add a step dummy that is 1 from 1990Q1 (data row 41) to every equation:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmControl ctl;
    ctl = vecmControlCreate();
    ctl.p = 2;
    ctl.det_case = 3;
    ctl.xreg = zeros(40, 1) | ones(44, 1);

    struct vecmResult vr;
    vr = vecmFit(y, 1, ctl=ctl);

    // Coefficients of the dummy, one row per equation
    print vr.phi_exo;

Remarks
-------

When a control structure is passed to :func:`vecmFit`, the lag order, the
deterministic terms and the print switch are read from it; set ``ctl.p``,
``ctl.det_case`` and ``ctl.quiet`` instead of the keywords. ``season`` is
not a member of the structure; pass it as a keyword together with *ctl*.

A fit with regressors can be passed to :func:`vecmIrf`,
:func:`vecmDiagnostics` and :func:`vecmToVar`. :func:`vecmForecast` does not
accept it, because a forecast would need future values of the regressors, and
neither do :func:`vecmBetaTest`, :func:`vecmAlphaTest` and
:func:`vecmBootstrap`.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`
