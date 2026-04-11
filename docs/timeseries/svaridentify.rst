svarIdentify
============

Purpose
-------
Find a structural rotation satisfying sign restrictions for a single VAR or BVAR estimate.

Format
------

.. function:: sr = svarIdentify(result, sign_restr)
              sr = svarIdentify(result, sign_restr, n_ahead=20, max_tries=10000, seed=42, quiet=0)

   :param result: an instance of a :class:`varResult` or :class:`bvarResult` structure.
   :type result: struct

   :param sign_restr: Nx4 matrix of sign restrictions on impulse responses. Each row specifies one restriction:

       === ==================================================================
       1   Variable index (1 to m) -- the responding variable.
       2   Shock index (1 to m) -- the structural shock.
       3   Horizon (0 = impact, 1 = one step ahead, etc.).
       4   Sign: 1 for positive response, -1 for negative response.
       === ==================================================================

   :type sign_restr: Nx4 matrix

   :param n_ahead: Optional keyword, number of IRF horizons to compute. Default = 20.
   :type n_ahead: scalar

   :param max_tries: Optional keyword, maximum number of rotation attempts before giving up. Default = 10000.
   :type max_tries: scalar

   :param seed: Optional keyword, RNG seed for reproducible rotation draws. Default = 42.
   :type seed: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return sr: An instance of an :class:`svarResult` structure containing:

       .. list-table::
          :widths: auto

          * - sr.p
            - mxm matrix, structural impact matrix P such that :math:`\Sigma = PP'`.

          * - sr.irf
            - :class:`irfResult` struct, identified impulse responses under this rotation.

          * - sr.n_tries
            - Scalar, number of rotation attempts needed to find a valid rotation.

          * - sr.m
            - Scalar, number of variables.

          * - sr.var_names
            - Mx1 string array, variable names.

          * - sr.shock_names
            - Mx1 string array, shock labels.

   :rtype sr: struct

Examples
--------

Monetary Policy SVAR
++++++++++++++++++++

::

    new;
    library timeseries;

    // Load data — ordering determines Cholesky structure
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = varFit(y, 4);

    // Sign restrictions: [variable, shock, horizon, sign]
    // Monetary shock (shock 3): FFR up, GDP down, CPI down at impact
    sign_restr = { 3 3 0  1,       // FFR positive
                   1 3 0 -1,       // GDP negative
                   2 3 0 -1 };     // CPI negative

    sr = svarIdentify(result, sign_restr);

    print "Structural impact matrix P:";
    print sr.p;
    print "Rotations tried:" sr.n_tries;

Remarks
-------

**Algorithm:**
Draws random orthogonal matrices Q from the Haar measure on O(m) via QR
decomposition of N(0,1) matrices with sign correction (Mezzadri 2007). For
each candidate Q, forms :math:`P = \text{chol}(\Sigma) \cdot Q` and checks
all sign restrictions on the implied IRFs. Returns the first accepted rotation.

**This function finds a single rotation,** which is useful for point estimation
(e.g., from an OLS VAR). For posterior inference with credible bands, use
:func:`svarIrfCompute` with a :class:`bvarResult` or :class:`bvarSvResult`.

**Zero restrictions** are not currently supported in :func:`svarIdentify`.
Zero restrictions require the ARW2018 null-space algorithm; use
:func:`svarIrfCompute` with an :class:`svarControl` struct for zero restrictions.

Model
-----

Sign-restricted SVAR decomposes the error covariance as :math:`\Sigma = PP'` where
:math:`P` is not unique. The set of valid decompositions is :math:`\{PQ : Q \in O(m),\; PQ \text{ satisfies sign restrictions}\}` where :math:`O(m)` is the group of orthogonal matrices.

Given a set of sign restrictions :math:`\Theta_h[i,j] \gtrless 0` (the IRF of variable
:math:`i` to shock :math:`j` at horizon :math:`h` is positive or negative), the
function finds a :math:`Q^*` such that :math:`P^* = \text{chol}(\Sigma)' \cdot Q^*`
produces IRFs satisfying all restrictions.

Algorithm
---------

1. Compute :math:`L = \text{chol}(\Sigma)'`.
2. Draw :math:`Z \sim N(0, I_{m \times m})` and compute :math:`Q, R = \text{QR}(Z)` with sign correction (Mezzadri 2007 algorithm for Haar-uniform orthogonal matrices).
3. Form candidate :math:`P = L \cdot Q`.
4. Compute IRFs :math:`\Theta_h = J F^h J' P` at all restricted horizons.
5. Check all sign restrictions. If satisfied, return :math:`P`. Otherwise, go to step 2.
6. Repeat up to *max_tries* times.

**Complexity:** :math:`O(\text{max\_tries} \cdot h_{\max} \cdot m^2 p^2)` worst case. Acceptance rates depend on how restrictive the sign constraints are.

Troubleshooting
---------------

**No valid rotation found (max_tries exceeded):**
The sign restrictions may be too numerous, contradictory, or implausible for this data.
Relax some restrictions or increase *max_tries*.

**Low acceptance rate (< 1%):**
Many restrictions at long horizons are hard to satisfy. Start with impact-only
restrictions and add horizons incrementally.

Verification
------------

Sign restriction algorithm verified against the Rubio-Ramirez, Waggoner & Zha (2010)
analytical examples for 2-variable and 3-variable systems.


References
----------

- Mezzadri, F. (2007). "How to generate random matrices from the classical compact groups." *Notices of the AMS*, 54(5), 592-604.
- Rubio-Ramirez, J.F., D.F. Waggoner, and T. Zha (2010). "Structural vector autoregressions: Theory of identification and algorithms for inference." *Review of Economic Studies*, 77(2), 665-696.
- Uhlig, H. (2005). "What are the effects of monetary policy on output? Results from an agnostic identification procedure." *Journal of Monetary Economics*, 52(2), 381-419.

Library
-------
timeseries

Source
------
svar.src

.. seealso:: Functions :func:`svarIrfCompute`, :func:`svarControlCreate`, :func:`irfCompute`
