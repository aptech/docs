.. _var-verification:

Verification and Cross-Validation
=================================

GAUSS Time Series is verified against two independent reference implementations
(R and MATLAB/BEAR) at multiple levels: exact numerical match for deterministic
computations, structural property validation for stochastic samplers.

Test Summary
------------

.. list-table::
   :widths: 35 15 20 30
   :header-rows: 1

   * - Test Suite
     - Tests
     - Tolerance
     - What it verifies
   * - OLS VAR vs R ``vars``
     - 22
     - :math:`10^{-6}`
     - Coefficients, :math:`\Sigma`, IRF, FEVD, Granger, forecasts
   * - BVAR Gibbs vs R ``BVAR`` 200K
     - 7
     - Structural
     - Posterior mean RMSE ordering, :math:`\Sigma` magnitude, shrinkage behavior
   * - SV-BVAR vs R ``stochvol`` + ``bayesianVARs``
     - 30
     - Structural
     - KSC sampler, SV parameters, canonical DGPs (Clark, CCM, GLP), FRED-MD
   * - BVAR matched-prior vs ECB BEAR
     - 45
     - 0.06
     - All 39 B coefficients + 6 :math:`\Sigma` elements, identical hyperparameters
   * - IRF matched-prior vs BEAR
     - 17
     - 0.04-0.25
     - Cholesky IRF at h=0, 10, 20 for all shock-response pairs
   * - OLS exact vs BEAR
     - 14
     - :math:`10^{-8}`
     - B, :math:`\Sigma`, eigenvalues, Cholesky factors
   * - **Total**
     - **135**
     -
     -


Chain of Trust
--------------

Each level validates against an independent source:

::

    R vars 1.6-1 / R 4.5.2
        │
        ├── OLS: 22 tests, exact match (1e-6)
        │
        └── BVAR: 7 tests, structural properties vs R BVAR 200K reference
                │
                └── Conjugate RMSE < Gibbs RMSE < 1.0
                    Sigma within 50% relative error
                    Shrinkage > 60%

    R stochvol / bayesianVARs
        │
        └── SV-BVAR: 30 tests
            ├── KSC mixture sampler vs stochvol (same algorithm)
            ├── Canonical DGPs: Clark (2011), CCM (2019), GLP (2015)
            ├── Real FRED-MD data
            └── ASIS interweaving, permutation correctness

    ECB BEAR Toolbox v5.0 (MATLAB)
        │
        ├── OLS: exact match (1e-8) on same data (T_eff=195)
        ├── BVAR: matched hyperparameters (lambda1=0.1, ar=0.8)
        │         max coefficient difference: 0.051 / 39 coefficients
        └── IRF: Cholesky at h=0,10,20 across 9 shock-response pairs


Methodology Notes
-----------------

**Why different tolerances?**

- **OLS (1e-6 to 1e-8):** Deterministic — the same linear algebra on the same data
  should produce the same answer to floating point precision.

- **BVAR posteriors (0.06):** Different RNG streams and slightly different prior
  forms (conjugate vs independent Normal-Wishart) produce Monte Carlo variation.
  The tolerance is calibrated to 2 posterior standard deviations.

- **SV-BVAR (structural):** Different R packages use different samplers, priors,
  and parameterizations. We validate structural properties (convergence, shrinkage,
  parameter recovery on known DGPs) rather than expecting exact draws to match.

**The conjugate vs independent NW prior-form difference:**

GAUSS uses the conjugate Normal-Inverse-Wishart prior (exact posterior draws).
BEAR uses the independent Normal-Wishart prior (Gibbs sampling required). With
matched hyperparameters (lambda1=0.1, ar=0.8), posterior means agree within 0.06
on all 39 B coefficients. The largest difference (0.051 on YER lag 2) occurs on a
non-own-lag coefficient where the two prior forms shrink differently:

- OLS: 0.172
- Conjugate NW posterior: 0.036
- Independent NW posterior: -0.015

Both are shrunk toward the prior mean of zero; the conjugate form preserves more
of the OLS signal. This is expected and well-documented behavior.


Running the Tests
-----------------

**Rust-level tests** (R cross-validation):

::

    cd gausslib/crates/gausslib-var
    cargo test --test r_benchmark         # 22 OLS tests
    cargo test --test gibbs_crossval      # 7 BVAR tests
    cargo test --test sv_crossval         # 30 SV-BVAR tests

**GAUSS-level tests** (BEAR cross-validation):

::

    library timeseries;
    run verify_vs_bear.e;             // 14 OLS exact + timing
    run bear_matched_prior.e;         // 45 matched-prior BVAR
    run bear_matched_irf.e;           // 17 matched-prior IRF


References
----------

- Kadiyala, K.R. and S. Karlsson (1997). "Numerical methods for estimation and inference in Bayesian VAR-models." *Journal of Applied Econometrics*, 12(2), 99-132.
- Kastner, G. (2016). "Dealing with stochastic volatility in time series using the R package stochvol." *Journal of Statistical Software*, 69(5).
- Kuschnig, N. and L. Vashold (2021). "BVAR: Bayesian vector autoregressions with hierarchical prior selection in R." *Journal of Statistical Software*, 100(14).
- Dieppe, A., R. Legrand, and B. van Roye (2016). "The BEAR Toolbox." ECB Working Paper No. 1934.
