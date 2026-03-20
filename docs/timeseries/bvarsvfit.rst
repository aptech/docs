bvarSvFit
=========

Purpose
-------
Fit a Bayesian VAR with stochastic volatility and optional SSVS variable selection.

Format
------

.. function:: result = bvarSvFit(y)
              result = bvarSvFit(y, ctl)
              result = bvarSvFit(y, ctl, xreg=X)

   :param y: endogenous variables. If a dataframe, column names are used as variable names.
   :type y: TxM matrix or dataframe

   :param ctl: Optional input, an instance of a :class:`bvarSvControl` structure. An instance is initialized by calling :func:`bvarSvControlCreate` and the following members can be set:

       .. include:: include/bvarsvcontrol.rst

   :type ctl: struct

   :param xreg: Optional keyword, exogenous regressors.
   :type xreg: TxK matrix

   :param xreg_names: Optional keyword, column names for *xreg*.
   :type xreg_names: Kx1 string array

   :param var_names: Optional keyword, endogenous variable names.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Overrides *ctl.quiet*.
   :type quiet: scalar

   :return result: An instance of a :class:`bvarSvResult` structure containing:

       .. include:: include/bvarsvresult.rst

   :rtype result: struct

Examples
--------

Default SV-BVAR
+++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Default SV-BVAR(1)
    result = bvarSvFit(data);

The summary includes stochastic volatility parameters:

::

    ================================================================================
    BVAR-SV(1) with Minnesota Prior         Variables:             3
    Draws: 5000  Burn: 5000  Thin: 1       Observations:        200
    Chains: 1                               Effective obs:       199
    ================================================================================

    Stochastic Volatility Parameters
               mu        phi      sigma2    phi_accept
    ------------------------------------------------------
    GDP      -0.231    0.971     0.0089       0.47
    CPI      -1.842    0.984     0.0052       0.41
    FFR       0.402    0.962     0.0134       0.52
    ================================================================================
    ...

Multi-Chain SV-BVAR
+++++++++++++++++++

Run 4 parallel chains for convergence diagnostics:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    ctl.n_chains = 4;
    ctl.parallel = 1;

    result = bvarSvFit(data, ctl);

SV-BVAR with SSVS Variable Selection
+++++++++++++++++++++++++++++++++++++

Enable stochastic search variable selection to identify which coefficients are nonzero:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.ssvs = 1;

    result = bvarSvFit(data, ctl);

    // Posterior inclusion probabilities
    print "B inclusion probabilities:";
    print result.pip_b;

    // Coefficients with PIP > 0.5
    mask = result.pip_b .> 0.5;
    print "Number of included coefficients:" sumc(vecr(mask));

Large System with Online Storage
++++++++++++++++++++++++++++++++

For large systems where storing all draws is infeasible, use online mode:

::

    new;
    library timeseries;

    // 20-variable system
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/largeMacro.dat"));

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 2;
    ctl.sv_keep = "online";
    ctl.reservoir_size = 1000;
    ctl.n_draws = 50000;
    ctl.n_burn = 10000;

    result = bvarSvFit(data, ctl);

    // Posterior means available via streaming moments
    print result.b_online_mean;

SV-BVAR with Exogenous Regressors
++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "oil");

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;

    result = bvarSvFit(y, ctl, xreg=X,
        var_names="GDP"$|"CPI"$|"FFR", xreg_names="Oil");

Model
-----

The SV-BVAR(p) model extends the standard BVAR by allowing the error covariance
to change over time:

.. math::

   y_t &= B_1 y_{t-1} + \cdots + B_p y_{t-p} + u + \varepsilon_t \\
   \varepsilon_t &= A_t^{-1} D_t^{1/2} e_t, \quad e_t \sim N(0, I_m)

where :math:`A_t` is a lower unitriangular matrix (Cholesky factor of the
contemporaneous relationships) and :math:`D_t = \text{diag}(\exp(h_{1,t}), \ldots, \exp(h_{m,t}))`
contains the time-varying variances.

Each log-variance follows an AR(1) process:

.. math::

   h_{i,t} = \mu_i + \phi_i (h_{i,t-1} - \mu_i) + \sigma_i \eta_{i,t}, \quad \eta_{i,t} \sim N(0, 1)

with stationary initialization :math:`h_{i,0} \sim N(\mu_i, \sigma_i^2 / (1 - \phi_i^2))`.

The SV parameters :math:`(\mu_i, \phi_i, \sigma_i^2)` are estimated per equation:

- :math:`\mu_i`: level of log-volatility (prior: :math:`N(0, 100)`)
- :math:`\phi_i`: persistence (prior: :math:`(\phi_i + 1)/2 \sim \text{Beta}(20, 1.5)`, centering mass near 1)
- :math:`\sigma_i^2`: volatility of volatility (prior: :math:`IG(0.5, 0.5)`)


Algorithm
---------

The sampler is a multi-block Gibbs sampler (Primiceri 2005; Kastner & Fruhwirth-Schnatter 2014):

1. **Draw B | y, A, h:** Equation-by-equation WLS with weights :math:`\exp(-h_{i,t})`.
2. **Draw A | y, B, h:** Column-by-column regression for Cholesky off-diagonals.
3. **Draw h | y, B, A:** Per equation, using the **Kim-Shephard-Chib (2004) 10-component mixture** approximation to :math:`\log \chi^2(1)`, solved via the **precision sampler** (McCausland, Miller & Pelletier 2011) in :math:`O(T)` time.
4. **Draw** :math:`(\mu, \phi, \sigma^2)` **| h:** Conjugate draws for :math:`\mu` and :math:`\sigma^2`; Metropolis-Hastings with Laplace proposal for :math:`\phi`.

When ASIS is enabled (default), steps 3-4 are repeated in the non-centered parameterization,
which improves effective sample size by 4-5x (Kastner & Fruhwirth-Schnatter 2014).

**Complexity:** :math:`O(T m K^2)` per iteration (dominated by the WLS draws for B).
With m=3, p=4, T=200, 10K draws: typical wall-clock time is 1-2 seconds.


Remarks
-------

**Stochastic volatility model:**
Each equation :math:`i` has a time-varying log-variance :math:`h_{i,t}` that
follows an AR(1) process:

.. math::

   h_{i,t} = \mu_i + \phi_i (h_{i,t-1} - \mu_i) + \sigma_i \eta_{i,t}, \quad \eta_{i,t} \sim N(0, 1)

The SV parameters :math:`(\mu_i, \phi_i, \sigma_i^2)` are estimated per equation.
The persistence parameter :math:`\phi_i` is drawn via Metropolis-Hastings; the
acceptance rate is reported in *result.phi_accept_rate*. Rates between 0.2 and
0.6 indicate good mixing.

**ASIS interweaving:**
By default, the sampler uses the Ancillarity-Sufficiency Interweaving Strategy
(Kastner & Fruhwirth-Schnatter 2014) which alternates between centered and
non-centered parameterizations of the SV equation. This dramatically improves
mixing, especially when persistence :math:`\phi_i` is near 1. Disable with
``ctl.use_asis = 0``.

**SSVS variable selection:**
When ``ctl.ssvs = 1``, a spike-and-slab prior (George & McCulloch 1993) is
placed on each coefficient:

.. math::

   b_j | \gamma_j \sim (1-\gamma_j) \cdot N(0, \tau_{0,j}^2) + \gamma_j \cdot N(0, \tau_{1,j}^2)

where :math:`\tau_0` (spike) shrinks coefficients toward zero and :math:`\tau_1`
(slab) allows nonzero values. The posterior inclusion probability (PIP) in
*result.pip_b* indicates which coefficients the data supports. A PIP > 0.5
corresponds to the median probability model.

Scaling is semiautomatic (George, Sun & Ni 2008): the spike and slab widths
are scaled by each coefficient's OLS standard error, making the prior adaptive
to the natural scale.

**Storage modes:**

.. list-table::
   :widths: auto
   :header-rows: 1

   * - sv_keep
     - Memory
     - Use case
   * - ``"full"``
     - O(n_draws * T * m)
     - Small systems (m < 10), need full posterior
   * - ``"last"``
     - O(n_draws * m)
     - Medium systems, need last h for forecasting
   * - ``"online"``
     - O(reservoir * m)
     - Large systems (m > 10), production use

**Multi-chain inference:**
When ``ctl.n_chains > 1``, each chain starts from an independent random state.
Draws from all chains are pooled before computing posterior summaries. Use
multiple chains to assess convergence via split-R-hat (see :func:`varDiagnose`).

Troubleshooting
---------------

**Low phi acceptance rates (< 0.2):**
The Metropolis-Hastings proposal for :math:`\phi_i` is too far from the posterior.
This usually means the data strongly favors either very high or very low
persistence. Solutions: run more burn-in (increase *n_burn*), or increase draws
and thin (set *n_thin* = 5). ASIS (enabled by default) already helps substantially.

**Phi acceptance rates near 1.0 (> 0.95):**
The prior dominates the likelihood — the data has little information about persistence.
This is common with short samples (T < 100) or near-constant volatility series.
Consider whether SV is necessary; a constant-volatility :func:`bvarFit` may suffice.

**R-hat > 1.05 on some parameters:**
The chain has not converged. Increase *n_burn* and *n_draws*. For persistent volatility
(:math:`\phi_i > 0.95`), 20K+ draws may be needed. Running multiple chains
(*n_chains* = 4) helps diagnose the problem.

**SV parameters look unreasonable:**
If :math:`\mu_i` is very large (> 5) or :math:`\sigma_i^2` is very small (< 0.001),
the model may be overfitting volatility to outliers. Check your data for measurement
errors or structural breaks.


Verification
------------

``bvarSvFit`` has been verified through 30 cross-validation tests covering the
core SV sampler and the full SV-BVAR system:

**R ``stochvol`` (univariate KSC sampler):**
The KSC 10-component mixture approximation is the same algorithm used by Kastner's
R ``stochvol`` package. Verified on multiple DGPs with known parameters.

**R ``bayesianVARs`` (Gruber & Kastner 2023):**
The full SV-BVAR sampler validated on multivariate data.

**Canonical test cases:**

- Clark (2011): 3-variable quarterly macro, tests volatility break detection
- CCM (2019): tests posterior concentration around known DGP parameters
- GLP (2015): tests interaction between SV and hierarchical hyperparameters

**Real data:**
FRED-MD large macro dataset, both with and without structural breaks.

All 30 tests pass. See ``gausslib-var/tests/sv_crossval.rs`` and the
:ref:`var-verification` page for the full chain of trust.


References
----------

- George, E.I. and R.E. McCulloch (1993). "Variable selection via Gibbs sampling." *Journal of the American Statistical Association*, 88(423), 881-889.
- George, E.I., D. Sun, and S. Ni (2008). "Bayesian stochastic search for VAR model restrictions." *Journal of Econometrics*, 142(1), 553-580.
- Gruber, L. and G. Kastner (2023). "Forecasting macroeconomic data with Bayesian VARs: Sparse or dense? It depends!" *Journal of Applied Econometrics*, 38(4), 459-482.
- Kastner, G. and S. Fruhwirth-Schnatter (2014). "Ancillarity-sufficiency interweaving strategy (ASIS) for boosting MCMC estimation of stochastic volatility models." *Computational Statistics & Data Analysis*, 76, 408-423.
- Kim, S., N. Shephard, and S. Chib (1998). "Stochastic volatility: Likelihood inference and comparison with ARCH models." *Review of Economic Studies*, 65(3), 361-393.
- McCausland, W.J., S. Miller, and D. Pelletier (2011). "Simulation smoothing for state-space models: A computational efficiency analysis." *Computational Statistics & Data Analysis*, 55(1), 199-212.
- Primiceri, G.E. (2005). "Time varying structural vector autoregressions and monetary policy." *Review of Economic Studies*, 72(3), 821-852.


Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarSvControlCreate`, :func:`bvarFit`, :func:`bvarSvForecast`, :func:`irfSvCompute`, :func:`varDiagnose`

.. seealso:: Guides :ref:`choosing-a-var-model`, :ref:`var-verification`
