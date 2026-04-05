.. _var-comparison:

GAUSS vs R vs BEAR: Side-by-Side
================================

This page compares the same BVAR analysis implemented in GAUSS, R, and
MATLAB (ECB BEAR Toolbox). All code is copy-paste runnable.

The Task
--------

Estimate a Bayesian VAR(4) on 200 quarters of US macroeconomic data
(GDP growth, CPI inflation, federal funds rate), compute impulse responses,
and forecast 8 quarters ahead.

GAUSS
-----

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    // BVAR(4)
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;

    result = bvarFit(data, ctl);

    // IRF
    rv = varFit(data, 4, quiet=1);
    irf = irfCompute(rv, 20);

    // Forecast
    fc = bvarForecast(result, 8);

Estimation, IRF, and forecast in one script using the ``timeseries`` library.

R (vars + BVAR packages)
------------------------

::

    library(vars)
    library(BVAR)

    y <- as.matrix(read.csv("us_macro_quarterly.csv"))

    # BVAR(4)
    set.seed(42)
    bv <- bvar(y, lags = 4, n_draw = 6000, n_burn = 1000,
               n_thin = 1, verbose = FALSE)

    # IRF (from OLS VAR — BVAR package doesn't do Cholesky IRF directly)
    v <- VAR(y, p = 4, type = "const")
    ir <- irf(v, n.ahead = 20, boot = FALSE)

    # Forecast
    fc <- predict(bv, horizon = 8, conf_bands = 0.68)

Requires two packages: ``vars`` for OLS/IRF and ``BVAR`` for
Bayesian estimation. The ``BVAR`` package uses Gibbs sampling with hierarchical
hyperparameter tuning — a different algorithm than both GAUSS and BEAR.

MATLAB (ECB BEAR Toolbox)
-------------------------

::

    addpath(genpath('tbx'));

    opts = BEARsettings(2);
    opts.frequency  = 2;
    opts.startdate  = '1970q2';
    opts.enddate    = '2019q4';
    opts.varendo    = 'YER HICSA STN';
    opts.lags       = 4;
    opts.prior      = 21;
    opts.It         = 10000;
    opts.Bu         = 5000;
    opts.IRF        = 1;
    opts.IRFperiods = 20;
    opts.F          = 1;
    opts.Fendsmpl   = 1;
    opts.Fstartdate = '2020q1';
    opts.Fenddate   = '2021q4';

    BEARmain(opts);

Data path, date range, and variable names are configured as strings.
Output is saved to Excel and .mat files rather than returned to the workspace.
Applications (IRF, forecast) must be enabled via flags. Each ``BEARmain()`` call
re-estimates the model from scratch.

Timing Comparison
-----------------

All timings on the same 200-quarter, 3-variable dataset. GAUSS and R timed on
Apple M-series. BEAR on MATLAB R2025b.

.. list-table::
   :widths: 30 15 15 15
   :header-rows: 1

   * - Task
     - GAUSS
     - R
     - BEAR
   * - OLS VAR(4)
     - 0.003s
     - 0.004s
     - 0.058s
   * - BVAR(4), 5K draws
     - **0.08s**
     - 0.66s
     - 3.69s
   * - 8-step forecast
     - 0.02s
     - 0.12s
     - 4.34s :sup:`1`
   * - Cholesky IRF (20h)
     - 0.001s
     - 0.003s
     - 4.23s :sup:`1`

:sup:`1` BEAR re-estimates the full model for each application. Marginal IRF/forecast
time is ~0.5s after subtracting re-estimation.

Implementation Differences
++++++++++++++++++++++++++

**GAUSS vs R:** GAUSS uses the conjugate Normal-Inverse-Wishart posterior, which
produces exact draws without MCMC. R's ``BVAR`` package uses a Gibbs sampler.
Both are correct Bayesian inference — the conjugate form avoids iterative sampling.

**GAUSS vs BEAR:** BEAR uses an independent Normal-Wishart prior with Gibbs
sampling (MATLAB interpreted loops). GAUSS uses conjugate posterior draws
(compiled backend). The difference compounds with draw count: at 50K draws,
BEAR takes approximately 4 minutes vs approximately 1 second for GAUSS.

Numerical Agreement
-------------------

GAUSS matches BEAR to :math:`10^{-8}` on OLS coefficients (same data, same model).
BVAR posterior means agree within 0.06 with matched hyperparameters (conjugate vs
independent NW prior form). R's ``BVAR`` package uses a different prior (hierarchical
hyperparameter tuning), so posterior means differ by design.

Full verification details: :ref:`var-verification`.

What You Get With Each Platform
-------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * -
     - GAUSS
     - R
     - BEAR
   * - OLS VAR
     - :func:`varFit`
     - ``vars::VAR``
     - VARtype=1
   * - Bayesian VAR
     - :func:`bvarFit`
     - ``BVAR::bvar``
     - VARtype=2
   * - Stochastic volatility
     - :func:`bvarSvFit`
     - ``bsvars``
     - VARtype=5
   * - Cholesky IRF
     - :func:`irfCompute`
     - ``vars::irf``
     - opts.IRF=1
   * - Sign restrictions
     - :func:`svarIdentify`
     - ``bayesianVARs``
     - opts.IRFt=4
   * - Conditional forecast
     - :func:`condForecast`
     - (manual)
     - opts.CF=1
   * - Density forecast
     - :func:`bvarSvForecast`
     - ``bayesianVARs``
     - (manual)
   * - Hyperparameter opt
     - :func:`bvarHyperopt`
     - Built-in
     - opts.hogs=1
   * - MCMC diagnostics
     - :func:`varDiagnose`
     - ``coda``
     - (manual)
   * - Forecast evaluation
     - :func:`dmTest` :func:`pitTest`
     - ``forecast``
     - (not included)
   * - FRED data access
     - ``fred_load``
     - ``fredr``
     - (not included)
   * - Verified against
     - R + BEAR (428 tests)
     - —
     - —

Multi-Run Timing (5 runs, median)
---------------------------------

GAUSS timing variability is minimal — the compiled Rust backend produces deterministic
execution times:

.. list-table::
   :widths: 30 15 15 15 15
   :header-rows: 1

   * - Task
     - Median
     - Min
     - Max
     - IQR
   * - OLS VAR(4)
     - 0.0001s
     - 0.0001s
     - 0.0023s
     - 0.0000s
   * - BVAR(4), 5K draws
     - 0.077s
     - 0.076s
     - 0.082s
     - 0.000s
   * - SV-BVAR(4), 10K draws
     - 1.161s
     - 1.154s
     - 1.166s
     - 0.006s
   * - Cholesky IRF
     - 0.0005s
     - 0.0005s
     - 0.0011s
     - 0.0000s
   * - BVAR Forecast
     - 0.024s
     - 0.024s
     - 0.024s
     - 0.000s

All measurements on 3-variable, 200-quarter data. 5 runs each, Apple M-series.
GAUSS runs under Rosetta 2 (x86_64 on ARM) — native arm64 GAUSS will be faster.

Scaling: Large Systems
----------------------

GAUSS handles large BVAR systems efficiently. Memory scales with :math:`n_{draws} \times K \times m`:

.. list-table::
   :widths: 10 10 10 15 15 15
   :header-rows: 1

   * - m
     - p
     - K
     - BVAR (5K draws)
     - SV (2K draws)
     - Memory (B draws)
   * - 3
     - 4
     - 13
     - 0.08s
     - 0.34s
     - 1.5 MB
   * - 5
     - 4
     - 21
     - 0.19s
     - 0.66s
     - 4.0 MB
   * - 10
     - 4
     - 41
     - 0.71s
     - 2.0s
     - 15.6 MB
   * - 20
     - 4
     - 81
     - 2.9s
     - 7.8s
     - 61.8 MB
   * - 50
     - 4
     - 201
     - 18.0s
     - —
     - 383 MB

For systems above m=10, use :func:`bvarSvFit` with ``sv_keep = "online"`` to
reduce memory from O(n_draws * T * m) to O(reservoir_size * m).
.. seealso:: Guides :ref:`getting-started`, :ref:`choosing-a-var-model`, :ref:`var-verification`
