tvpSvFit
========

Estimate a Time-Varying Parameter VAR with Stochastic Volatility (Primiceri 2005).

Format
------

.. function:: result = tvpSvFit(y[, ctl])

   :param y: T x m matrix of endogenous variables.
   :type y: matrix or dataframe

   :param ctl: Optional. Control structure with estimation settings. Created by :func:`tvpSvControlCreate`.
   :type ctl: struct tvpSvControl

   :return result: Estimation results including posterior draws of terminal B_T, SV parameters, and acceptance diagnostics.
   :rtype result: struct tvpSvResult

Model
-----

The full Primiceri (2005) TVP-VAR-SV:

.. math::

   y_t &= X_t B_t + \varepsilon_t, \quad \varepsilon_t \sim N(0, \Sigma_t) \\
   \Sigma_t &= U_t'^{-1} D_t U_t^{-1}, \quad D_t = \text{diag}(e^{h_{1,t}}, \ldots, e^{h_{m,t}}) \\
   B_t &= B_{t-1} + \eta_t, \quad \eta_t \sim N(0, Q_B) \\
   u_t &= u_{t-1} + \zeta_t, \quad \zeta_t \sim N(0, Q_U) \\
   h_{i,t} &= \mu_i + \phi_i(h_{i,t-1} - \mu_i) + \nu_{i,t}, \quad \nu_{i,t} \sim N(0, \sigma^2_i)

Three time-varying components: coefficients B_t (random walk), Cholesky off-diagonals U_t (random walk), and log-volatilities h_t (AR(1) stochastic volatility).

Example
-------

::

   new;
   library timeseries;

   // US macro data
   fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
   y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

   // Estimate with defaults
   result = tvpSvFit(y);

   // Print terminal coefficients
   print result.b_mean;

   // With custom settings
   ctl = tvpSvControlCreate();
   ctl.p = 2;
   ctl.n_draws = 10000;
   ctl.n_burn = 10000;
   result = tvpSvFit(y, ctl);

Control structure
-----------------

.. include:: include/tvpsvcontrol.rst

Result structure
----------------

.. include:: include/tvpsvresult.rst

Remarks
-------

- The sampler uses equation-by-equation Carter-Kohn FFBS for B_t (Primiceri's original approach), reducing the state dimension from K*m to K per equation.
- The observation variance for each equation comes from the stochastic volatility h_{eq,t}, not a constant Sigma.
- Q_B and Q_U have conjugate diagonal Inverse-Gamma posteriors.
- B_0 is initialized from OLS and redrawn each iteration from its full conditional.
- SV updates use the OCSN 10-component mixture approximation with optional ASIS interweaving.
- Set ``ctl.u_bandwidth`` > 0 for large systems (m > 15) to reduce U parameters.

See also
--------

- :func:`tvpSvControlCreate` — create control structure with defaults
- :func:`bvarSvFit` — SV-BVAR with constant coefficients (simpler model)
- :func:`varFit` — OLS VAR (simplest model)

References
----------

- Primiceri, G. E. (2005). Time varying structural vector autoregressions and monetary policy. *Review of Economic Studies*, 72(3), 821-852.
- Carter, C. K. & Kohn, R. (1994). On Gibbs sampling for state space models. *Biometrika*, 81(3), 541-553.
- Del Negro, M. & Primiceri, G. E. (2015). Time varying structural vector autoregressions and monetary policy: A corrigendum. *Review of Economic Studies*, 82(4), 1342-1345.
