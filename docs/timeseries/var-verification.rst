.. _var-verification:

Verification and Cross-Validation
=================================

VAR reference checks compare numerical values with independent calculations
on fixed data. The covariance divisor, lag order and deterministic terms
must match. The default residual covariance divides by T - p - K;
``resid_cov="ml"`` divides by T - p. Likelihood and information criteria
use ML in both cases.

Current VAR checks cover coefficient inference, covariance choices, common-sample
lag criteria including FPE, one-effect Granger tests, responses, forecasts and
historical decomposition. Deterministic agreement is within each check's
stated tolerance, rather than bit-for-bit equality.

The historical summary below describes earlier fixture checks. It is not a
count of the current test suite or a general guarantee for every model.

Historical Test Summary
-----------------------

.. list-table::
   :widths: 35 15 20 30
   :header-rows: 1

   * - Test Suite
     - Tests
     - Tolerance
     - What it verifies
   * - OLS VAR reference fixture
     - 22
     - :math:`10^{-6}`
     - Coefficients, :math:`\Sigma`, IRF, FEVD, Granger, forecasts
   * - BVAR Gibbs reference fixture, 200K draws
     - 7
     - Structural
     - Posterior mean RMSE ordering, :math:`\Sigma` magnitude, shrinkage behavior
   * - SV-BVAR reference fixtures
     - 30
     - Structural
     - KSC sampler, SV parameters, canonical DGPs (Clark, CCM, GLP), FRED-MD
   * - BVAR compared-prior fixture
     - 45
     - 0.06
     - All 39 B coefficients + 6 :math:`\Sigma` elements, identical hyperparameters
   * - IRF compared-prior fixture
     - 17
     - 0.04-0.25
     - Cholesky IRF at h=0, 10, 20 for all shock-response pairs
   * - OLS deterministic reference fixture
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

    Least-squares reference fixture
        │
        ├── OLS: 22 historical checks, agreement within 1e-6
        │
        └── BVAR: 7 tests, structural properties against a 200K-draw reference
                │
                └── Conjugate RMSE < Gibbs RMSE < 1.0
                    Sigma within 50% relative error
                    Shrinkage > 60%

    Stochastic-volatility reference fixtures
        │
        └── SV-BVAR: 30 tests
            ├── KSC mixture sampler against a mixture-sampler reference
            ├── Canonical DGPs: Clark (2011), CCM (2019), GLP (2015)
            ├── Real FRED-MD data
            └── ASIS interweaving, permutation correctness

    Separate estimation reference fixtures
        │
        ├── OLS: agreement within 1e-8 on same data (T_eff=195)
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

- **SV-BVAR (structural):** Different reference calculations use different samplers, priors,
  and parameterizations. We validate structural properties (convergence, shrinkage,
  parameter recovery on known DGPs) rather than expecting exact draws to match.

**The conjugate vs independent NW prior-form difference:**

GAUSS uses the conjugate Normal-Inverse-Wishart prior (exact posterior draws).
The reference uses the independent Normal-Wishart prior (Gibbs sampling required). With
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

**Installed VAR reference checks:**

::

    library timeseries;
    run test_var_reference.e;
    run test_var_invariance.e;
    run test_kl2017_ch2.e;
    run test_kl2017_ch4.e;

The reference checks use full-precision constants with per-output tolerances.
The invariance checks cover covariance scaling, deterministic terms and input
errors. The published-example checks use Kilian and Lutkepohl (2017),
chapters 2 and 4. Passing these fixtures does not establish forecast coverage
in new data or validate every prior and sampler setting.

References
----------

- Kadiyala, K.R. and S. Karlsson (1997). "Numerical methods for estimation and inference in Bayesian VAR-models." *Journal of Applied Econometrics*, 12(2), 99-132.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer, chapters 3 and 4.
- Kilian, L. and H. Lutkepohl (2017). *Structural Vector Autoregressive Analysis*. Cambridge University Press, chapters 2 and 4.
