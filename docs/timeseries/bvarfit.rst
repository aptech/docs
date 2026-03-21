bvarFit
=======

Purpose
-------
Fit a Bayesian VAR with conjugate Minnesota prior.

Format
------

.. function:: result = bvarFit(y)
              result = bvarFit(y, ctl)

   :param y: endogenous variables. If a dataframe, column names are used as variable labels in output. If a matrix, variables are labeled "Y1", "Y2", etc.
   :type y: TxM matrix or dataframe

   :param ctl: Optional input, an instance of a :class:`bvarControl` structure. An instance is initialized by calling :func:`bvarControlCreate` and the following members can be set:

       .. include:: include/bvarcontrol.rst

   :type ctl: struct

   :return result: An instance of a :class:`bvarResult` structure containing:

       .. include:: include/bvarresult.rst

   :rtype result: struct

Model
-----

The BVAR(p) model is:

.. math::

   y_t = B_1 y_{t-1} + B_2 y_{t-2} + \cdots + B_p y_{t-p} + u + \varepsilon_t, \quad \varepsilon_t \sim N(0, \Sigma)

where :math:`y_t` is an :math:`m \times 1` vector, each :math:`B_\ell` is :math:`m \times m`,
:math:`u` is an :math:`m \times 1` intercept, and :math:`\Sigma` is the :math:`m \times m`
error covariance matrix.

Stacking all coefficients, :math:`B = [B_1 \; B_2 \; \cdots \; B_p \; u]'` is :math:`K \times m`
where :math:`K = mp + 1`.

**Prior:**
The default Minnesota prior (Kadiyala & Karlsson 1997) places a conjugate
Normal-Inverse-Wishart prior on :math:`(B, \Sigma)`:

.. math::

   \text{vec}(B) | \Sigma &\sim N\bigl(\text{vec}(B_0),\; \Sigma \otimes \Omega\bigr) \\
   \Sigma &\sim IW(S_0, \alpha_0)

The prior mean :math:`B_0` encodes the belief that each variable follows a random walk
(when *ar* = 1) or white noise (when *ar* = 0). Cross-variable coefficients are
centered at zero.

The diagonal prior covariance :math:`\Omega` is governed by the :math:`\lambda` hyperparameters:

.. math::

   \Omega_{j,\ell} = \begin{cases}
     (\lambda_1 / \ell^{\lambda_3})^2 & \text{own lag } \ell \\
     (\lambda_1 \lambda_2 / \ell^{\lambda_3})^2 \cdot (\hat\sigma_j^2 / \hat\sigma_i^2) & \text{cross lag from variable } j \text{ to equation } i \\
     (\lambda_1 \lambda_4)^2 & \text{constant}
   \end{cases}

where :math:`\hat\sigma_i^2` are residual variances from univariate AR(p) regressions.

The prior scale :math:`S_0 = (\alpha_0 - m - 1) \cdot \text{diag}(\hat\sigma_1^2, \ldots, \hat\sigma_m^2)`
centers the prior on the univariate residual variances.

**Posterior:**
The conjugate prior yields a closed-form posterior:

.. math::

   \Sigma | Y &\sim IW(\bar{S}, \bar{\alpha}) \\
   \text{vec}(B) | \Sigma, Y &\sim N\bigl(\text{vec}(\bar{B}),\; \Sigma \otimes \bar{\Phi}\bigr)

Draws are exact — no MCMC iteration, no burn-in, no convergence diagnostics needed.
The log marginal likelihood is available in closed form for formal Bayesian model comparison.
Algorithm
---------

1. **OLS pre-estimation:** Fit univariate AR(p) models to each variable to obtain :math:`\hat\sigma_i^2`, used to scale the prior.

2. **Prior construction:** Build :math:`B_0`, :math:`\Omega`, :math:`S_0`, :math:`\alpha_0` from the hyperparameters and AR residual variances.

3. **Posterior update:** Apply the Normal-Inverse-Wishart conjugate update (Kadiyala & Karlsson 1997, Eqs. 12-14):

   .. math::

      \bar{\Phi} &= (X'X + \Omega^{-1})^{-1} \\
      \bar{B} &= \bar{\Phi}(X'Y + \Omega^{-1} B_0) \\
      \bar{S} &= S_0 + \hat{S} + (B_0 - \hat{B})' (\Omega + (X'X)^{-1})^{-1} (B_0 - \hat{B}) \\
      \bar{\alpha} &= \alpha_0 + T

4. **Draw from posterior:** Sample :math:`\Sigma \sim IW(\bar{S}, \bar{\alpha})` then :math:`B | \Sigma \sim N(\bar{B}, \Sigma \otimes \bar{\Phi})`. Each draw is independent (no Markov chain).

5. **Sum-of-coefficients and single-unit-root priors** (when *lambda6* > 0 or *lambda7* > 0): Implemented via dummy observations appended to the data before the posterior update (Doan, Litterman & Sims 1984; Sims 1993).

**Complexity:** :math:`O(K^2 m)` for the posterior update, plus :math:`O(K^3)` per draw for the Cholesky factorization. With 5,000 draws on a 3-variable VAR(4), typical wall-clock time is 0.05–0.10 seconds.
Hyperparameter Guide
--------------------

.. list-table::
   :widths: 15 15 70
   :header-rows: 1

   * - Parameter
     - Default
     - Guidance
   * - *lambda1*
     - 0.2
     - Overall tightness. Smaller = prior dominates. For a small system (m=3), 0.1–0.2 works well. For large systems (m > 10), tighter values (0.01–0.05) prevent overfitting. Use :func:`bvarHyperopt` to optimize automatically (Giannone, Lenza & Primiceri 2015).
   * - *lambda2*
     - 0.5
     - Cross-variable shrinkage. A value of 0.5 means other variables' lags are shrunk twice as much as own lags. Range: 0.1–1.0.
   * - *lambda3*
     - 1.0
     - Lag decay exponent. Higher lags are shrunk by :math:`\ell^{-\lambda_3}`. Default of 1.0 is standard. Values above 2 aggressively penalize distant lags.
   * - *lambda4*
     - 1e5
     - Constant tightness. Default is effectively uninformative. Set to 100 if you want the prior to also regularize the intercept (as in BEAR Toolbox).
   * - *lambda6*
     - 0 (off)
     - Sum-of-coefficients prior (Doan, Litterman & Sims 1984). Pulls lag coefficient sums toward the identity, preventing explosive long-horizon forecasts. Typical values: 1–10. Essential for levels data when forecasting beyond 4 steps.
   * - *lambda7*
     - 0 (off)
     - Single-unit-root prior (Sims 1993). Pulls all variables toward a common stochastic trend, stabilizing cointegrated systems. Typical values: 1–10.
   * - *ar*
     - 1.0
     - Prior mean for own first lag. **Set to 1 for levels data** (random walk prior). **Set to 0 for growth rates or stationary data** (white noise prior). Set to 0.8 for "mostly persistent" data. See the :ref:`choosing-a-var-model` guide.
   * - *alpha0*
     - 0 (= m+2)
     - Inverse-Wishart degrees of freedom. Default of m+2 is the least informative proper prior. Increase for stronger prior on :math:`\Sigma`.
Examples
--------

Monetary Policy VAR on US Macro Data
+++++++++++++++++++++++++++++++++++++

Estimate a 3-variable BVAR(4) on GDP growth, CPI inflation, and the federal funds rate:

::

    new;
    library timeseries;

    // Load US macro quarterly data
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;               // Growth rates → white noise prior

    struct bvarResult result;
    result = bvarFit(data, ctl);

Output:

::

    ================================================================================
    BVAR(4) with Conjugate Minnesota Prior    Variables:             3
    Draws: 5000                               Observations:        200
    Prior: minnesota (conjugate NIW)          Effective obs:       196
    ================================================================================

    Posterior Mean of B (68% Credible Intervals)
    Equation: GDP
                                    Mean    Std.Dev      [16%      84%]
    -----------------------------------------------------------------------
    GDP(-1)                       0.2414     0.0724    0.1695    0.3126
    CPI(-1)                       0.0312     0.0485   -0.0170    0.0798
    FFR(-1)                      -0.0031     0.0074   -0.0105    0.0043
    ...

    Log marginal likelihood: -812.34
    ================================================================================

Compare Lag Orders with Bayes Factors
+++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarResult r1, r2, r4;
    ctl = bvarControlCreate();
    ctl.quiet = 1;

    ctl.p = 1;
    r1 = bvarFit(data, ctl);

    ctl.p = 2;
    r2 = bvarFit(data, ctl);

    ctl.p = 4;
    r4 = bvarFit(data, ctl);

    print "Log ML(p=1):" r1.log_ml;
    print "Log ML(p=2):" r2.log_ml;
    print "Log ML(p=4):" r4.log_ml;

    // Bayes factor: p=4 vs p=2
    print "BF(4 vs 2):" exp(r4.log_ml - r2.log_ml);

A Bayes factor above 3 is "substantial evidence" (Kass & Raftery 1995); above 20 is "strong."

Forecasting GDP with SOC/SUR Priors
++++++++++++++++++++++++++++++++++++

Sum-of-coefficients and single-unit-root priors stabilize long-horizon forecasts for levels data:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.lambda6 = 5;          // Sum-of-coefficients
    ctl.lambda7 = 5;          // Single-unit-root

    struct bvarResult result;
    result = bvarFit(data, ctl);

    // 8-step-ahead forecast
    struct forecastResult fc;
    fc = bvarForecast(result, 8);

Data-Driven Hyperparameters (GLP 2015)
+++++++++++++++++++++++++++++++++++++++

Let the marginal likelihood choose all :math:`\lambda` values:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Optimize lambda1, lambda6, lambda7 jointly
    ctl_opt = bvarHyperopt(data);

    print "Optimal lambda1:" ctl_opt.lambda1;
    print "Optimal lambda6:" ctl_opt.lambda6;
    print "Optimal lambda7:" ctl_opt.lambda7;

    // Fit with optimized hyperparameters
    result = bvarFit(data, ctl_opt);

This implements Algorithm 1 of Giannone, Lenza & Primiceri (2015), which maximizes the
log marginal likelihood over a grid of hyperparameter values.
Troubleshooting
---------------

**Non-stationary posterior mean:**
The largest eigenvalue of the companion matrix exceeds 1. This means the posterior
mean coefficients imply explosive dynamics. Common fixes:

- Set ``ar = 0`` if your data is in growth rates (you may be using the wrong prior).
- Increase ``lambda6`` (sum-of-coefficients) to pull lag sums toward unity.
- Tighten the prior (reduce ``lambda1``).

**Prior too tight / too loose:**
If all coefficients are near zero, the prior is too tight — increase ``lambda1`` or use :func:`bvarHyperopt`. If the posterior equals OLS (credible bands match frequentist confidence intervals), the prior is too loose — decrease ``lambda1``.

**"Log ML is missing":**
The log marginal likelihood is only available for the conjugate Minnesota prior (``prior = "minnesota"``). For flat priors, consider using the DIC or WAIC instead.

**Levels vs growth rates:**
This is the single most common specification error. If your data is in levels (GDP, not GDP growth), set ``ar = 1`` (random walk prior). If in growth rates, set ``ar = 0``. Using the wrong setting will produce either explosive forecasts (ar=0 on levels) or excessive shrinkage (ar=1 on growth rates). See the :ref:`choosing-a-var-model` guide.
Verification
------------

``bvarFit`` has been verified against two independent reference implementations:

**R ``vars`` package (OLS component):**
22 tests at :math:`10^{-6}` tolerance against R 4.5.2 ``vars::VAR()``, covering
coefficients, :math:`\Sigma`, IRF, FEVD, Granger causality, and forecasts on identical
data. See ``gausslib-var/tests/r_benchmark.rs``.

**R ``BVAR`` package (Bayesian posterior):**
7 structural validation tests against the R ``BVAR`` package (Kuschnig & Vashold 2021)
using 200,000-draw ground truth. Validates:

- Conjugate posterior RMSE < Gibbs RMSE < 1.0 vs R reference
- :math:`\Sigma` elements within 50% relative error across three prior forms
- Shrinkage toward :math:`B_0` exceeds 60% for all methods

See ``gausslib-var/tests/gibbs_crossval.rs``.

**ECB BEAR Toolbox:**
45 matched-prior coefficient tests (``lambda1=0.1``, ``ar=0.8``, ``lambda4=100``)
and 17 IRF tests at horizons 0, 10, and 20 against BEAR v5.0. OLS components match
to :math:`10^{-8}`. BVAR posterior means agree within 0.06 (prior-form difference
between conjugate and independent Normal-Wishart).

See ``crossval/bear_matched_prior.e`` and ``crossval/bear_matched_irf.e``.
Remarks
-------

**Conjugate draws are exact:**
With ``prior = "minnesota"`` (default), the posterior is available in closed form.
All draws are independent (no MCMC chain, no burn-in, no thinning needed).
For stochastic volatility or non-conjugate priors, use :func:`bvarSvFit`.

**Log marginal likelihood:**
*result.log_ml* is only available for the conjugate Minnesota prior (closed-form
computation). It can be used for formal Bayesian model comparison — the model
with the highest log ML is preferred. The Bayes factor between models A and B is
:math:`\exp(\log ML_A - \log ML_B)`. See Kass & Raftery (1995) for interpretation guidelines.

**When to use BVAR instead of OLS VAR:**
A BVAR with Minnesota prior always weakly dominates an OLS VAR in forecast
accuracy (Banbura, Giannone & Reichlin 2010). The prior acts as regularization,
reducing out-of-sample forecast error by shrinking small, noisy coefficients
toward zero. This benefit grows with the number of variables. For m > 5, BVAR
is strongly preferred.
References
----------

- Banbura, M., D. Giannone, and L. Reichlin (2010). "Large Bayesian vector auto regressions." *Journal of Applied Econometrics*, 25(1), 71-92.
- Doan, T., R. Litterman, and C. Sims (1984). "Forecasting and conditional projection using realistic prior distributions." *Econometric Reviews*, 3, 1-100.
- Giannone, D., M. Lenza, and G. E. Primiceri (2015). "Prior selection for vector autoregressions." *Review of Economics and Statistics*, 97(2), 436-451.
- Kadiyala, K.R. and S. Karlsson (1997). "Numerical methods for estimation and inference in Bayesian VAR-models." *Journal of Applied Econometrics*, 12(2), 99-132.
- Kass, R.E. and A.E. Raftery (1995). "Bayes factors." *Journal of the American Statistical Association*, 90(430), 773-795.
- Sims, C. (1993). "A nine-variable probabilistic macroeconomic forecasting model." In *Business Cycles, Indicators, and Forecasting*, 179-212. NBER.

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarControlCreate`, :func:`bvarSvFit`, :func:`bvarHyperopt`, :func:`bvarForecast`, :func:`irfCompute`, :func:`varFit`

.. seealso:: Guides :ref:`choosing-a-var-model`, :ref:`var-verification`
