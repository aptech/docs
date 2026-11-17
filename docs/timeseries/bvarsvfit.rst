bvarSvFit
=========

Purpose
-------
Fit a Bayesian VAR with stochastic volatility and optional SSVS variable selection.

Format
------

.. function:: result = bvarSvFit(y, p={}, const={}, xreg={}, quiet={}, ctl={}, lag1_prior_mean={}, overall_tightness={}, prior={}, ssvs={}, n_draws={}, n_burn={}, seed={})

   :param y: endogenous variables. If a dataframe, column names are used as variable names.
   :type y: TxM matrix or dataframe

   :param p: Required lag order, supplied as ``p=`` or in *ctl.p*. There is no default.
   :type p: scalar

   :param const: Optional keyword, 1 to include a constant, 0 to omit it. Overrides *ctl.const* for this call. Default = 1. Must be a scalar 0 or 1; the same rule applies to *ctl.const*.
   :type const: scalar

   :param xreg: Optional keyword, exogenous regressors.
   :type xreg: TxK matrix

   :param quiet: Optional keyword, set to 1 to suppress printed output. Overrides *ctl.quiet*. Must be a scalar 0 or 1; the same rule applies to *ctl.quiet*.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of a :class:`bvarSvControl` structure. An instance is initialized by calling :func:`bvarSvControlCreate` and the following members can be set:

       .. include:: include/bvarsvcontrol.rst

   :type ctl: struct

   *ctl* must be a ``bvarSvControl`` structure or ``{}`` (omitted).
   Other values or structure types are refused.

   :param lag1_prior_mean: Optional keyword, numeric own-first-lag prior mean: one value or one per variable in [0,1]. Default = 1; overrides the control. Values outside [0,1] are refused. With ``prior="horseshoe"`` or SSVS enabled, only the default mean 1 is accepted (every entry must be 1 for a vector).
   :type lag1_prior_mean: scalar or vector

   :param overall_tightness: Optional keyword, Minnesota prior tightness. Default = 0.2; overrides the control.
   :type overall_tightness: scalar

   :param prior: Optional keyword, coefficient prior: ``"minnesota"``, ``"flat"`` or ``"horseshoe"``. Default = ``"minnesota"``; overrides *ctl.prior*.
   :type prior: string

   :param ssvs: Optional keyword, 1 to enable variable selection, 0 to disable it. Default = 0; overrides the control.
   :type ssvs: scalar

   :param n_draws: Optional keyword, posterior draws. Default = 5000; overrides the control.
   :type n_draws: scalar

   :param n_burn: Optional keyword, burn-in draws. Default = 5000; overrides the control.
   :type n_burn: scalar

   :param seed: Optional keyword, random seed. Default = 42; overrides the control.
   :type seed: scalar

   :return result: An instance of a :class:`bvarSvResult` structure containing:

       .. include:: include/bvarsvresult.rst

   :rtype result: struct

Examples
--------

Minnesota SV-BVAR
+++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    result = bvarSvFit(data, p=1, lag1_prior_mean={ 0, 1, 1 });

The summary includes stochastic volatility parameters:

::

    BVAR-SV(1), minnesota prior on the coefficients
    ================================================================================
    Variables:                         3    Observations:                        240
    Lags:                              1    Effective obs.:                      239
    Constant:                        Yes    Posterior draws:                   5,000
    SSVS:                            Off    Burn-in draws:                     5,000

    Stochastic volatility parameters (posterior means)
    Variable        mu    phi  sigma2  phi acceptance
    -------------------------------------------------
    gdp_growth   1.805  0.896   0.173           0.862
    inflation    0.709  0.843   0.248           0.917
    fed_funds   -2.015  0.918   0.946           0.861

    Equation 1: gdp_growth
    Regressor        Center      SD  Lower 68%  Upper 68%
    -----------------------------------------------------
    Constant         2.5559  0.3519     2.2158     2.9084
    gdp_growth(-1)   0.2005  0.0654     0.1363     0.2653
    inflation(-1)   -0.1844  0.0786    -0.2613    -0.1054
    fed_funds(-1)    0.0994  0.0588     0.0411     0.1574

    Equation 2: inflation
    Regressor       Center      SD  Lower 68%  Upper 68%
    ----------------------------------------------------
    Constant        0.3501  0.2219     0.1279     0.5707
    gdp_growth(-1)  0.0066  0.0296    -0.0225     0.0360
    inflation(-1)   0.6351  0.0585     0.5768     0.6918
    fed_funds(-1)   0.1740  0.0402     0.1338     0.2135

    Equation 3: fed_funds
    Regressor        Center      SD  Lower 68%  Upper 68%
    -----------------------------------------------------
    Constant        -0.0187  0.0151    -0.0338    -0.0037
    gdp_growth(-1)   0.0087  0.0045     0.0042     0.0132
    inflation(-1)    0.0002  0.0045    -0.0039     0.0046
    fed_funds(-1)    1.0004  0.0060     0.9946     1.0061

    Center: posterior draw mean.
    SD and 68% interval: equal-tailed quantiles of 5,000 posterior draws.

Independent SV-BVAR Fits
++++++++++++++++++++++++

Run four seeds sequentially and inspect diagnostics for each fit. The API does
not pool chains or calculate between-fit R-hat:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    ctl.lag1_prior_mean = { 0, 1, 1 };

    // Run four independent seeds sequentially. Diagnostics describe each fit;
    // these are not pooled, between-chain convergence statistics.
    for chain (1, 4, 1);
        ctl.seed = 41 + chain;
        result = bvarSvFit(data, p=ctl.p, ctl=ctl, quiet=1);
        print sprintf("Fit %d (seed %d)", chain, ctl.seed);
        dx = mcmcDiagnostics(result);
    endfor;

SV-BVAR with SSVS Variable Selection
++++++++++++++++++++++++++++++++++++

Enable stochastic search variable selection to identify which coefficients are nonzero:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.ssvs = 1;
    // SSVS requires the default own-first-lag prior mean of 1.
    result = bvarSvFit(data, p=ctl.p, ctl=ctl);

    print "B inclusion probabilities:";
    print result.pip_b;
    mask = result.pip_b .> 0.5;
    print "Number of coefficients with PIP > 0.5:" sumc(vecr(mask));

Larger System and Coefficient Summaries
+++++++++++++++++++++++++++++++++++++++

Fit twenty quarterly series from 1960Q1-2019Q4 and inspect the public coefficient means. The
backend retains sampler draws; there is no public online-storage control:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_large.csv");
    data = loadd(
        fname,
        "gdp + cons + inv + defl + cpi + pce_core + payroll + unemp + hours + wage + indpro + caputil + housing + m2 + ffr + gs10 + tbill + sp500 + spread + exrate"
    );

    struct bvarSvControl ctl;
    ctl = bvarSvControlCreate();
    ctl.p = 2;
    // Growth series are centered at 0. Unemployment, capacity utilization,
    // interest-rate levels and the yield spread are centered at 1.
    prior_means = { 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0 };
    ctl.lag1_prior_mean = prior_means;
    // More shrinkage for the larger system.
    ctl.overall_tightness = 0.1;

    result = bvarSvFit(data, p=ctl.p, ctl=ctl);

    // Public coefficient summaries; no raw draws are copied into this matrix.
    print result.b_mean;

SV-BVAR with Exogenous Regressors
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds + unemployment");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    y = data[., "date" "gdp_growth" "inflation" "fed_funds"];
    X = data[., "unemployment"];

    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    result = bvarSvFit(y, p=4, xreg=X, lag1_prior_mean={ 0, 1, 1 });

Remarks
-------

**Stochastic volatility model:**
The residuals are built from *m* uncorrelated structural shocks with a
recursive (triangular) model. Each shock :math:`i` has a time-varying
log-variance :math:`h_{i,t}` that follows an AR(1) process:

.. math::

   h_{i,t} = \mu_i + \phi_i (h_{i,t-1} - \mu_i) + \sigma_i \eta_{i,t}, \quad \eta_{i,t} \sim N(0, 1)

The SV parameters :math:`(\mu_i, \phi_i, \sigma_i^2)` are estimated per
structural shock, in the order described next.

**Ordering of the shocks:**
:func:`bvarSvFit` orders the shocks from the last column of *y* to the first.
The last column's shock comes first: that variable's residual is its own
shock. Shock *i* moves variable *i* and the variables in the columns before
it within the period, but not the variables after it. Element *i* of
*result.sv_mu*, *result.sv_phi* and *result.sv_sigma2* belongs to shock *i*
in this order. The ordering can change the estimates and the forecasts.

For the usual ordering, in which the first column's shock comes first,
reverse the columns of *y* before fitting, ``y = y[., cols(y):1];``, and
read every result in the reversed order. :func:`tvpSvFit` orders its shocks
from the first column to the last.
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

**Repeated fits and storage:**
Use distinct seeds for independent fits. :func:`mcmcDiagnostics` reports
within-fit split-chain diagnostics, not a pooled diagnostic across those fits.
The independent-seed example can print diagnostic warnings because its minimum
bulk effective sample size is below the default threshold. Running without a
GAUSS error does not establish convergence; extend the runs and recheck the
diagnostics before using their estimates for inference.

The public result exposes coefficient summaries and a process-local sampler
handle. It has no online-storage or multi-chain controls.

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarSvControlCreate`, :func:`bvarFit`, :func:`varResults`, :func:`varCoefTable`
