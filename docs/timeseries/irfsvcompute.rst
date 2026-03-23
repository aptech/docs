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

    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    result = bvarSvFit(data, ctl, quiet=1);

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
    print "Median:" irf.median[6, 1, 3];

    // 68% credible band
    print "68% band:" irf.bands[1].lower[6, 1, 3] "to" irf.bands[1].upper[6, 1, 3];

    // 90% credible band
    print "90% band:" irf.bands[2].lower[6, 1, 3] "to" irf.bands[2].upper[6, 1, 3];

    // Full path with bands
    print "GDP response to FFR shock:";
    print "  h   Median    68%lo   68%hi   90%lo   90%hi";
    for h (0, 20, 1);
        print h;;
        print irf.median[h+1, 1, 3];;
        print irf.bands[1].lower[h+1, 1, 3];;
        print irf.bands[1].upper[h+1, 1, 3];;
        print irf.bands[2].lower[h+1, 1, 3];;
        print irf.bands[2].upper[h+1, 1, 3];
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

Model
-----

For each posterior draw :math:`(B^{(s)}, U^{(s)})` from the SV-BVAR, the structural
IRF is computed using the time-averaged Cholesky factor:

.. math::

   \Theta_h^{(s)} = J \, (F^{(s)})^h \, J' \, \bar{P}^{(s)}

where :math:`\bar{P}^{(s)}` is derived from the draw-specific :math:`U^{(s)}` and
the mean of the time-varying diagonal :math:`D_t`. The posterior distribution of
:math:`\{\Theta_h^{(s)}\}` yields pointwise credible bands.
Algorithm
---------

1. For each of *n_draws* posterior draws:

   a. Construct companion matrix :math:`F^{(s)}` from :math:`B^{(s)}`.
   b. Construct structural rotation :math:`\bar{P}^{(s)}` from the draw's Cholesky factor.
   c. Compute :math:`\Theta_0^{(s)}, \ldots, \Theta_h^{(s)}` via companion powers.

2. At each horizon, compute pointwise quantiles across all draws.

**Complexity:** :math:`O(n\_draws \cdot h \cdot m^2 p^2)`.
Troubleshooting
---------------

**"Requires full draws" error:**
The SV-BVAR was estimated with ``sv_keep = "online"`` or ``"last"``, which does
not store the individual :math:`(B, U)` draws needed for posterior IRF bands.
Re-estimate with ``sv_keep = "full"`` (the default).

**Bands are asymmetric:**
This is expected — the posterior distribution of IRFs is typically skewed,
especially at longer horizons. Asymmetric bands reflect this correctly.

**Bands include zero at all horizons:**
The shock may not have a statistically significant effect on the response variable.
This is a finding, not a problem.
References
----------

- Primiceri, G.E. (2005). "Time varying structural vector autoregressions and monetary policy." *Review of Economic Studies*, 72(3), 821-852.
- Clark, T.E. (2011). "Real-time density forecasts from Bayesian vector autoregressions with stochastic volatility." *Journal of Business & Economic Statistics*, 29(3), 327-341.
Library
-------
timeseries

Source
------
irf.src

.. seealso:: Functions :func:`bvarSvFit`, :func:`irfCompute`, :func:`irfPlotData`, :func:`svarIdentify`
