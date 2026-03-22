fevdCompute
===========

Purpose
-------
Compute forecast error variance decomposition.

Format
------

.. function:: fevd = fevdCompute(irf)
              fevd = fevdCompute(result, n_ahead)

   :param irf: an instance of an :class:`irfResult` structure from :func:`irfCompute`.
   :type irf: struct

   :param result: alternatively, a :class:`varResult` or :class:`bvarResult` structure (IRF is computed internally).
   :type result: struct

   :param n_ahead: number of horizons (required when passing *result*).
   :type n_ahead: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return fevd: An instance of a :class:`fevdResult` structure containing:

       .. include:: include/fevdresult.rst

   :rtype fevd: struct

Examples
--------

From Pre-Computed IRF
+++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4);

    irf = irfCompute(result, 20, quiet=1);

    fevd = fevdCompute(irf);

Direct from Estimation Result
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4);

    // Skip the explicit IRF step
    fevd = fevdCompute(result, 20);

Accessing Decomposition
+++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4);
    fevd = fevdCompute(result, 20, quiet=1);

    // Fraction of GDP variance explained by each shock at h=20
    print "GDP variance decomposition at h=20:";
    print fevd.var_names';
    print fevd.fevd[21, 1, .];

    // Verify rows sum to 1
    print "Sum:" sumc(fevd.fevd[21, 1, .]');

    // Track how FFR's contribution to GDP evolves over horizons
    print "FFR contribution to GDP over time:";
    for h (0, 20, 1);
        print h;; print "  ";; print fevd.fevd[h+1, 1, 3];
    endfor;

Remarks
-------

**The FEVD partitions** the h-step-ahead forecast error variance of each
variable into contributions from each orthogonal shock. At horizon h, row i
of ``fevd.fevd[h+1, i, .]`` gives the fraction of variable i's forecast uncertainty
attributable to each shock. Each row sums to 1.0.

**At h=0 (impact),** the decomposition reflects the contemporaneous Cholesky
structure: variable 1's variance is 100% from its own shock, other variables'
variance includes contributions from earlier-ordered variables.

**As h increases,** the decomposition typically converges to long-run shares
that reflect the relative importance of each shock in driving each variable.

**This function accepts either** a pre-computed :class:`irfResult` (if you
already computed IRFs) or an estimation result (computes IRFs internally).
Both produce identical results.

Model
-----

The FEVD partitions the h-step forecast error variance of variable :math:`i` into
contributions from each orthogonal shock :math:`j`:

.. math::

   \text{FEVD}_{i,j}(h) = \frac{\sum_{\ell=0}^{h-1} (\Theta_\ell[i,j])^2}{\sum_{\ell=0}^{h-1} \sum_{k=1}^{m} (\Theta_\ell[i,k])^2}

where :math:`\Theta_\ell` is the structural IRF at horizon :math:`\ell`. Each row sums to 1.

At :math:`h \to \infty`, the FEVD converges to the long-run variance shares.


Algorithm
---------

1. Compute Cholesky IRF matrices :math:`\Theta_0, \ldots, \Theta_{h-1}` (from :func:`irfCompute` or internally).
2. For each horizon, compute cumulative squared responses and normalize.

**Complexity:** :math:`O(h \cdot m^2)` on top of the IRF computation.


Troubleshooting
---------------

**FEVD shares don't change much across horizons:**
The model has weak dynamic interactions — shocks are mostly absorbed within
the first few periods. This is common in growth-rate data.

**One shock dominates everything:**
Check the variable ordering. With Cholesky identification, the first variable's
shock can absorb variance that should be attributed to other shocks.
Try :func:`girfCompute` or :func:`svarIdentify` for alternative decompositions.


Verification
------------

FEVD verified against R ``vars::fevd()`` at :math:`10^{-6}` tolerance on a
2-variable VAR(1), confirming row-sum-to-one property and individual shares
at h=1 and h=10.

See ``gausslib-var/tests/r_benchmark.rs``.


References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 2.3.3.


Library
-------
timeseries

Source
------
fevd.src

.. seealso:: Functions :func:`irfCompute`, :func:`hdCompute`, :func:`irfPlotData`
