irfCompute
==========

Purpose
-------
Compute orthogonalized impulse response functions using Cholesky identification.

Format
------

.. function:: irf = irfCompute(result, n_ahead)

   :param result: an instance of a :class:`varResult` or :class:`bvarResult` structure.
   :type result: struct

   :param n_ahead: number of horizons to compute (e.g., 20).
   :type n_ahead: scalar

   :param var_names: Optional keyword, override variable names from the estimation result.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return irf: An instance of an :class:`irfResult` structure containing:

       .. include:: include/irfresult.rst

   :rtype irf: struct

Model
-----

An impulse response function (IRF) traces the dynamic effect of a one-standard-deviation
structural shock to variable :math:`j` on variable :math:`i` over :math:`h` periods.

For a VAR(p) in companion form :math:`Y_t = F Y_{t-1} + G \varepsilon_t`, the
reduced-form IRF at horizon :math:`h` is:

.. math::

   \Phi_h = J \, F^h \, J'

where :math:`F` is the :math:`mp \times mp` companion matrix and :math:`J = [I_m \; 0 \; \cdots \; 0]`
selects the first :math:`m` rows.

**Cholesky identification:** To give shocks a structural interpretation, the
reduced-form innovations are orthogonalized via the Cholesky factorization
:math:`\Sigma = P P'` where :math:`P` is lower triangular. The structural IRF is:

.. math::

   \Theta_h = \Phi_h \, P

Element :math:`\Theta_h[i, j]` is the response of variable :math:`i` at horizon :math:`h`
to a one-standard-deviation shock to variable :math:`j`.

**Identification assumption:** Cholesky identification imposes a recursive causal ordering.
Variable 1 can affect all others contemporaneously; variable :math:`m` is affected by all
others but affects none contemporaneously. This assumption is appropriate when there is a
natural fast-to-slow ordering (e.g., financial variables respond faster than real activity).

Algorithm
---------

1. **Extract companion matrix** :math:`F` and Cholesky factor :math:`P = \text{chol}(\Sigma)'` from the VAR estimates.

2. **Iterate:** For :math:`h = 0, 1, \ldots, n\_ahead`:

   .. math::

      \Theta_h = J \, F^h \, J' \, P

   The companion power :math:`F^h` is computed iteratively (matrix multiplication, not matrix exponentiation) for numerical stability.

3. **Store** :math:`\Theta_0, \Theta_1, \ldots, \Theta_{n\_ahead}` as an array of :math:`m \times m` matrices.

**Complexity:** :math:`O(n\_ahead \cdot m^2 p^2)` — dominated by the :math:`mp \times mp` matrix
multiplications. Sub-millisecond for typical systems.

Examples
--------

Monetary Policy Shock
+++++++++++++++++++++

Trace the effect of a federal funds rate shock on GDP and CPI:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

    // Variable ordering: GDP (slow), CPI (medium), FFR (fast policy instrument)
    // This ordering means: FFR shocks can affect GDP and CPI contemporaneously,
    // but GDP shocks take one period to reach FFR.
    result = varFit(data, 4);

    irf = irfCompute(result, 20);

Output:

::

    ================================================================================
    Impulse Response Functions (cholesky)
    Horizons: 0-20
    ================================================================================

    Shock to: GDP
      h          GDP       CPI       FFR
    --------------------------------------------------------------------------------
      0     0.5280     0.0456     0.0919
      1     0.1859     0.0810     0.2753
      2     0.1600     0.0612     0.4442
        ⋮
     18     0.0089     0.0031     0.0042
     19     0.0071     0.0025     0.0035
     20     0.0057     0.0020     0.0029
    ================================================================================

The impact response (h=0) shows that a 1-SD GDP shock raises GDP by 0.528,
CPI by 0.046, and FFR by 0.092 — consistent with the central bank responding
to output movements within the quarter.

IRF from BVAR with Shrinkage
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

    ctl = bvarControlCreate();
    ctl.p = 4;

    br = bvarFit(data, ctl, quiet=1);

    // IRF at the posterior mean of B and Sigma
    irf = irfCompute(br, 20);

For posterior IRF bands (credible intervals), use :func:`irfSvCompute` with
an SV-BVAR result.

Plotting IRFs
+++++++++++++

Reshape IRF results into a plot-ready dataframe:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4, quiet=1);
    irf = irfCompute(result, 20, quiet=1);

    // Get plot data: (n_ahead+1) x (m*m) matrix with column names
    struct DataFrame plot_data;
    plot_data = irfPlotData(irf);

    // Plot GDP response to FFR shock
    plotXY(seqa(0, 1, 21), plot_data[., "GDP<-FFR"]);

Troubleshooting
---------------

**IRFs don't decay to zero:**
If the VAR is near-nonstationary (max eigenvalue close to 1), IRFs can be very
persistent. This is not a numerical error — it reflects the model's dynamics.
Check ``result.max_eigenvalue``. For near-unit-root systems, consider:

- Using longer horizons (40-60 periods instead of 20).
- Differencing the data.
- Adding sum-of-coefficients priors (:func:`bvarFit` with lambda6 > 0).

**IRFs are sensitive to variable ordering:**
This is inherent to Cholesky identification — different orderings produce different
structural shocks. If the ordering is uncertain, use :func:`girfCompute` (generalized
IRF, ordering-invariant) or :func:`svarIdentify` (sign restrictions).

**Impact response has wrong sign:**
Check the variable ordering. In Cholesky identification, the first variable's shock
is unrestricted; later variables' shocks are residualized. A monetary policy variable
(FFR) should typically be ordered last so its shock is "purged" of contemporaneous
output and price movements.

Remarks
-------

**Identification:**
The Cholesky decomposition of :math:`\Sigma` is used to orthogonalize the
innovations. The ordering of variables in the data determines the recursive
causal structure: variable 1 can affect all others contemporaneously, variable
2 can affect variables 3, ..., m but not 1, and so on.

**To change the identification ordering,** reorder the columns of the data
before calling :func:`varFit` or :func:`bvarFit`.

**For ordering-invariant responses,** use :func:`girfCompute` (generalized IRF,
Pesaran & Shin 1998). For theory-based identification with sign/zero restrictions,
see :func:`svarIdentify`.

**For BVAR,** the IRF is computed at the posterior mean of B and :math:`\Sigma`.
For posterior IRF bands, use :func:`irfSvCompute` with an :class:`bvarSvResult`.

**Indexing convention:**
``irf.irf[1, ., .]`` is the impact response (h=0). ``irf.irf[h+1, ., .]`` is the response
at horizon h. Element ``irf.irf[h+1, i, j]`` is the response of variable i to
a shock to variable j.

Verification
------------

Verified against R ``vars::irf()`` with ``boot=FALSE`` at :math:`10^{-6}` tolerance
on a 2-variable VAR(1) with known DGP. Tests cover impact values, decay patterns
at h=1 and h=2, and the Cholesky lower-triangularity constraint (zero upper-off-diagonal
at h=0). See ``gausslib-var/tests/r_benchmark.rs``.

Additionally verified against ECB BEAR Cholesky IRFs on matched-prior BVAR(4),
covering all 9 shock-response pairs at horizons 0, 10, and 20 (17 tests).
See ``crossval/bear_matched_irf.e``.

References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Chapter 2.3 (IRF computation), Chapter 9 (structural identification).
- Pesaran, M.H. and Y. Shin (1998). "Generalized impulse response analysis in linear multivariate models." *Economics Letters*, 58(1), 17-29.
- Sims, C.A. (1980). "Macroeconomics and reality." *Econometrica*, 48(1), 1-48.

Library
-------
timeseries

Source
------
irf.src

.. seealso:: Functions :func:`irfSvCompute`, :func:`girfCompute`, :func:`fevdCompute`, :func:`hdCompute`, :func:`irfPlotData`, :func:`svarIdentify`

.. seealso:: Guides :ref:`choosing-a-var-model`, :ref:`var-verification`
