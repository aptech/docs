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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

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
        ⋮  (Posterior coefficient tables for each equation follow)

Multi-Chain SV-BVAR
+++++++++++++++++++

Run 4 parallel chains for convergence diagnostics:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

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
    fname = getGAUSSHome("pkgs/timeseries/examples/data/largeMacro.dat");
    data = loadd(fname);

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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    y = loadd(fname, "gdp + cpi + ffr");
    X = loadd(fname, "oil");

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;

    result = bvarSvFit(y, ctl, xreg=X,
        var_names="GDP"$|"CPI"$|"FFR", xreg_names="Oil");

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

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarSvControlCreate`, :func:`bvarFit`, :func:`varResults`, :func:`varCoefTable`
