irfSvCompute
============

Purpose
-------
Compute posterior impulse response bands from SV-BVAR draws.

Format
------

.. function:: irf = irfSvCompute(result, n_ahead)

   :param result: an instance of a :class:`bvarSvResult` structure returned by :func:`bvarSvFit`.
   :type result: struct

   :param n_ahead: number of horizons to compute.
   :type n_ahead: scalar

   :param var_names: Optional keyword, override variable names.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return irf: An instance of an :class:`svIrfResult` structure containing:

       .. include:: include/svirfresult.rst

   :rtype irf: struct

Examples
--------

SV-BVAR IRF with Credible Bands
++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    result = bvarSvFit(data, ctl, quiet=1);

    struct svIrfResult irf;
    irf = irfSvCompute(result, 20);

Accessing Median and Bands
++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = bvarSvFit(data, quiet=1);
    irf = irfSvCompute(result, 20, quiet=1);

    // Median response of GDP (1) to FFR shock (3) at h=5
    print "Median:" irf.median[6][1, 3];

    // 68% credible band
    print "68% band:" irf.lower_68[6][1, 3] "to" irf.upper_68[6][1, 3];

    // 90% credible band
    print "90% band:" irf.lower_90[6][1, 3] "to" irf.upper_90[6][1, 3];

    // Full path with bands
    print "GDP response to FFR shock:";
    print "  h   Median    68%lo   68%hi   90%lo   90%hi";
    for h (0, 20, 1);
        print h;;
        print irf.median[h+1][1, 3];;
        print irf.lower_68[h+1][1, 3];;
        print irf.upper_68[h+1][1, 3];;
        print irf.lower_90[h+1][1, 3];;
        print irf.upper_90[h+1][1, 3];
    endfor;

Remarks
-------

**Posterior bands:**
For each posterior draw :math:`(B^{(i)}, U^{(i)})`, the function computes the
Cholesky IRF using the time-averaged :math:`U^{(i)}` for the structural rotation.
The reported bands are pointwise quantiles across all draws:

- **68% bands:** 16th and 84th percentiles (approximately :math:`\pm 1\sigma`)
- **90% bands:** 5th and 95th percentiles

**These are pointwise bands,** not simultaneous bands. They capture parameter
uncertainty but do not control joint coverage across all horizons.

**Requires full draws.** The estimation must be run with ``sv_keep = "full"``
(the default) so that the posterior draws of B and U are available. If
``sv_keep = "online"`` was used, an error is raised.

Library
-------
timeseries

Source
------
irf.src

.. seealso:: Functions :func:`bvarSvFit`, :func:`irfCompute`, :func:`irfPlotData`
