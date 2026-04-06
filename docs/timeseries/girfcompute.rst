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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = varFit(data, 4);

    // Generalized IRF — invariant to variable ordering
    girf = girfCompute(result, 20);

Compare Cholesky and Generalized
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = varFit(data, 4);

    irf = irfCompute(result, 20, quiet=1);
    girf = girfCompute(result, 20, quiet=1);

    // For variable 1's own shock, Cholesky and GIRF are identical
    print "Cholesky GDP→GDP h=5:" irf.irf[6, 1, 1];
    print "GIRF    GDP→GDP h=5:" girf.irf[6, 1, 1];

    // For cross-variable responses, they differ
    print "Cholesky FFR→GDP h=5:" irf.irf[6, 1, 3];
    print "GIRF    FFR→GDP h=5:" girf.irf[6, 1, 3];

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

Model
-----

The generalized IRF (Pesaran & Shin 1998) for a shock to variable :math:`j` is:

.. math::

   \text{GIRF}_j(h) = \frac{\Phi_h \Sigma e_j}{\sqrt{\Sigma_{jj}}}

where :math:`\Phi_h = J F^h J'` is the reduced-form IRF, :math:`\Sigma` is the error
covariance, and :math:`e_j` is the j-th unit vector. The denominator normalizes to a
one-standard-deviation shock.

Unlike Cholesky IRF, the GIRF accounts for the typical contemporaneous correlation
structure rather than imposing orthogonality. The result is invariant to variable ordering.

**Important caveat:** GIRF shocks are correlated, so the GIRF-based FEVD does not sum
to 1. Use Cholesky (:func:`irfCompute`) or sign-restricted SVAR (:func:`svarIdentify`)
for a proper variance decomposition.


Algorithm
---------

1. Compute reduced-form IRF matrices :math:`\Phi_0, \ldots, \Phi_h` from the companion form.
2. For each variable :math:`j`, scale by :math:`\Sigma e_j / \sqrt{\Sigma_{jj}}`.

**Complexity:** Same as :func:`irfCompute`.


Verification
------------

GIRF verified against the analytical relationship with Cholesky IRF: for the
first variable, GIRF and Cholesky IRF are identical (both equal
:math:`\Phi_h P e_1`). Tested on the R benchmark data.


References
----------

- Pesaran, M.H. and Y. Shin (1998). "Generalized impulse response analysis in linear multivariate models." *Economics Letters*, 58(1), 17-29.


Library
-------
timeseries

Source
------
irf.src

.. seealso:: Functions :func:`irfCompute`, :func:`fevdCompute`, :func:`svarIdentify`
