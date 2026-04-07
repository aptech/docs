tvpSvFit
========

Purpose
-------
Estimate a Time-Varying Parameter VAR with Stochastic Volatility (Primiceri 2005).

Format
------

.. function:: result = tvpSvFit(y)
              result = tvpSvFit(y, p)
              result = tvpSvFit(y, p, n_draws)
              result = tvpSvFit(y, p, n_draws, n_burn)
              result = tvpSvFit(y, p, n_draws, n_burn, adv)
              result = tvpSvFit(y, adv)

   :param y: endogenous variables. If a dataframe, column names are used as variable names.
   :type y: TxM matrix or dataframe

   :param p: Optional input, lag order. Default = 1.
   :type p: scalar

   :param n_draws: Optional input, number of posterior draws to keep. Default = 5000.
   :type n_draws: scalar

   :param n_burn: Optional input, number of burn-in iterations to discard. Default = 5000.
   :type n_burn: scalar

   :param adv: Optional input, an instance of a :class:`tvpSvControl` structure. An instance is initialized by calling :func:`tvpSvControlCreate` and the following members can be set:

       .. include:: include/tvpsvcontrol.rst

   :type adv: struct

   :return result: An instance of a :class:`tvpSvResult` structure containing:

       .. include:: include/tvpsvresult.rst

   :rtype result: struct

Examples
--------

Default TVP-SV-VAR
+++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    // Default TVP-SV-VAR(1) with 5000 draws
    result = tvpSvFit(y);

The summary includes SV acceptance diagnostics:

::

    ================================================================================
    TVP-VAR-SV (Primiceri 2005)
    Variables: 3, Lags: 1, T: 199
    Draws: 5000, Burn-in: 5000
    ================================================================================
    Phi acceptance rates:
        0.47    0.41    0.52
    ================================================================================

Custom Draws and Lags
+++++++++++++++++++++

Increase the lag order and posterior draws directly:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    // TVP-SV-VAR(2) with 10000 draws and 10000 burn-in
    result = tvpSvFit(y, 2, 10000, 10000);

    // Terminal B_T (coefficients at the last observation)
    print "Terminal B_T posterior mean:";
    print result.b_mean;

Advanced Settings
+++++++++++++++++

Use the :class:`tvpSvControl` structure for fine-grained prior control:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    struct tvpSvControl adv;
    adv = tvpSvControlCreate();

    // Tighter drift priors (less time variation)
    adv.q_b_shape = 10.0;
    adv.q_b_scale = 0.001;

    // Wider diffuse initialization
    adv.p0_b_kappa = 25.0;

    result = tvpSvFit(y, 4, 10000, 10000, adv);

    // SV parameters
    print "SV persistence (phi):";
    print result.sv_phi;

    print "Phi acceptance rates:";
    print result.phi_accept_rate;

Model
-----

The full Primiceri (2005) TVP-VAR-SV with three time-varying components:

.. math::

   y_t &= X_t B_t + \varepsilon_t, \quad \varepsilon_t \sim N(0, \Sigma_t) \\
   \Sigma_t &= U_t'^{-1} D_t U_t^{-1}, \quad D_t = \text{diag}(e^{h_{1,t}}, \ldots, e^{h_{m,t}}) \\
   B_t &= B_{t-1} + \eta_t, \quad \eta_t \sim N(0, Q_B) \\
   u_t &= u_{t-1} + \zeta_t, \quad \zeta_t \sim N(0, Q_U) \\
   h_{i,t} &= \mu_i + \phi_i(h_{i,t-1} - \mu_i) + \nu_{i,t}, \quad \nu_{i,t} \sim N(0, \sigma^2_i)

where:

- :math:`B_t` are the VAR coefficients, following a random walk.
- :math:`U_t` are the lower-triangular Cholesky off-diagonals of the error covariance, following a random walk.
- :math:`h_{i,t}` are the log-volatilities, following independent AR(1) processes.
- :math:`Q_B` and :math:`Q_U` are diagonal drift covariance matrices with Inverse-Gamma priors.

Remarks
-------

**Sampler details:**
The sampler uses equation-by-equation Carter-Kohn forward-filtering backward-sampling
(FFBS) for :math:`B_t`, following Primiceri's original approach. This reduces the
state dimension from :math:`K \times m` to :math:`K` per equation. The observation
variance for each equation comes from the stochastic volatility :math:`h_{i,t}`.

**Priors:**
:math:`Q_B` and :math:`Q_U` have conjugate diagonal Inverse-Gamma posteriors
controlled by ``adv.q_b_shape``, ``adv.q_b_scale``, ``adv.q_u_shape``, and
``adv.q_u_scale``. Smaller scale values (e.g., 0.001) produce tighter drift
priors, favoring slower parameter evolution. Larger scale values (e.g., 0.1)
allow more rapid time variation.

**Initialization:**
:math:`B_0` is initialized from OLS and redrawn each iteration from its full
conditional. The initial state covariance is :math:`P_0 = \kappa I` where
:math:`\kappa` is controlled by ``adv.p0_b_kappa``.

**ASIS interweaving:**
By default, the SV sampler uses the Ancillarity-Sufficiency Interweaving Strategy
(Kastner & Fruhwirth-Schnatter 2014) which alternates between centered and
non-centered parameterizations. This dramatically improves mixing when persistence
:math:`\phi_i` is near 1. Disable with ``adv.use_asis = 0``.

**Band-limited U for large systems:**
For systems with :math:`m > 15`, set ``adv.u_bandwidth`` > 0 to estimate only the
first :math:`k` off-diagonals per column of :math:`U_t`, reducing parameters from
:math:`m(m-1)/2` to :math:`m \cdot k`. This is an approximation that assumes
distant variables have negligible contemporaneous correlation.

**Acceptance rates:**
The persistence parameter :math:`\phi_i` is drawn via Metropolis-Hastings. The
acceptance rate is reported in *result.phi_accept_rate*. Rates between 0.2 and
0.6 indicate good mixing. If rates are outside this range, increase *n_burn*
or adjust the SV prior.

References
----------

- Primiceri, G. E. (2005). "Time varying structural vector autoregressions and monetary policy." *Review of Economic Studies*, 72(3), 821-852.
- Del Negro, M. & G. E. Primiceri (2015). "Time varying structural vector autoregressions and monetary policy: A corrigendum." *Review of Economic Studies*, 82(4), 1342-1345.
- Carter, C. K. & R. Kohn (1994). "On Gibbs sampling for state space models." *Biometrika*, 81(3), 541-553.
- Kastner, G. & S. Fruhwirth-Schnatter (2014). "Ancillarity-sufficiency interweaving strategy (ASIS) for boosting MCMC estimation of stochastic volatility models." *Computational Statistics & Data Analysis*, 76, 408-423.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`tvpSvControlCreate`, :func:`tvpSvForecast`, :func:`bvarSvFit`, :func:`varFit`
