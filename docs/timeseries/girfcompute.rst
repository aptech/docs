girfCompute
===========

Purpose
-------
Compute generalized impulse response functions (Pesaran & Shin 1998).

Format
------

.. function:: girf = girfCompute(result, n_ahead)

   :param result: an instance of a :class:`varResult` or :class:`bvarResult` structure.
   :type result: struct

   :param n_ahead: number of horizons to compute.
   :type n_ahead: scalar

   :param var_names: Optional keyword, override variable names.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return girf: An instance of an :class:`irfResult` structure with ``ident = "generalized"`` containing:

       .. include:: include/irfresult.rst

   :rtype girf: struct

Examples
--------

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    // Generalized IRF — invariant to variable ordering
    girf = girfCompute(result, 20);

Compare Cholesky and Generalized
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    irf = irfCompute(result, 20, quiet=1);
    girf = girfCompute(result, 20, quiet=1);

    // For variable 1's own shock, Cholesky and GIRF are identical
    print "Cholesky GDP→GDP h=5:" irf.irf[6][1, 1];
    print "GIRF    GDP→GDP h=5:" girf.irf[6][1, 1];

    // For cross-variable responses, they differ
    print "Cholesky FFR→GDP h=5:" irf.irf[6][1, 3];
    print "GIRF    FFR→GDP h=5:" girf.irf[6][1, 3];

Remarks
-------

**Generalized IRFs** do not require a causal ordering and are invariant to the
ordering of variables in the data. They measure the response to a shock of
one standard deviation to variable j, integrating out the effects of other
shocks using the historical error covariance.

**Key difference from Cholesky IRF:** GIRF shocks are *not orthogonal*. The
GIRF to a shock in variable j accounts for the typical contemporaneous
correlation with other variables, rather than isolating a pure structural
shock. This means GIRF variance decompositions do not sum to 1.

**When to use GIRF vs Cholesky:**

- Use **Cholesky** when you have a defensible recursive ordering (e.g.,
  monetary policy VAR with slow/fast variable classification).
- Use **GIRF** when no ordering is defensible, or as a robustness check
  against ordering sensitivity.
- Use **sign/zero restrictions** (SVAR) for theory-driven non-recursive
  identification.

Library
-------
timeseries

Source
------
irf.src

.. seealso:: Functions :func:`irfCompute`, :func:`fevdCompute`
