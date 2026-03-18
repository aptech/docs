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
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    irf = irfCompute(result, 20, quiet=1);

    struct fevdResult fevd;
    fevd = fevdCompute(irf);

Direct from Estimation Result
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    // Skip the explicit IRF step
    fevd = fevdCompute(result, 20);

Accessing Decomposition
+++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);
    fevd = fevdCompute(result, 20, quiet=1);

    // Fraction of GDP variance explained by each shock at h=20
    print "GDP variance decomposition at h=20:";
    print fevd.var_names';
    print fevd.fevd[21][1, .];

    // Verify rows sum to 1
    print "Sum:" sumc(fevd.fevd[21][1, .]');

    // Track how FFR's contribution to GDP evolves over horizons
    print "FFR contribution to GDP over time:";
    for h (0, 20, 1);
        print h;; print "  ";; print fevd.fevd[h+1][1, 3];
    endfor;

Remarks
-------

**The FEVD partitions** the h-step-ahead forecast error variance of each
variable into contributions from each orthogonal shock. At horizon h, row i
of ``fevd.fevd[h+1]`` gives the fraction of variable i's forecast uncertainty
attributable to each shock. Each row sums to 1.0.

**At h=0 (impact),** the decomposition reflects the contemporaneous Cholesky
structure: variable 1's variance is 100% from its own shock, other variables'
variance includes contributions from earlier-ordered variables.

**As h increases,** the decomposition typically converges to long-run shares
that reflect the relative importance of each shock in driving each variable.

**This function accepts either** a pre-computed :class:`irfResult` (if you
already computed IRFs) or an estimation result (computes IRFs internally).
Both produce identical results.

Library
-------
timeseries

Source
------
fevd.src

.. seealso:: Functions :func:`irfCompute`, :func:`hdCompute`, :func:`irfPlotData`
