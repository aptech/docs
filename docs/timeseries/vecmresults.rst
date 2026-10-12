vecmResults
===========

Purpose
-------
Print the summary of a fitted VECM.

Format
------

.. function:: vecmResults(vr)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`.
   :type vr: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    vecmResults(vr);

This prints the table that :func:`vecmFit` prints when *quiet* is 0; see
:func:`vecmFit` for the printout.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmGamma`
