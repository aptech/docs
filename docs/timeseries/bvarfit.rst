bvarFit
=======

Purpose
-------
Fit a Bayesian VAR with Minnesota or flat prior.

Format
------

.. function:: result = bvarFit(y)
              result = bvarFit(y, ctl)
              result = bvarFit(y, ctl, xreg=X)

   :param y: endogenous variables. If a dataframe, column names are used as variable names.
   :type y: TxM matrix or dataframe

   :param ctl: Optional input, an instance of a :class:`bvarControl` structure. An instance is initialized by calling :func:`bvarControlCreate` and the following members can be set:

       .. include:: include/bvarcontrol.rst

   :type ctl: struct

   :param xreg: Optional keyword, exogenous regressors.
   :type xreg: TxK matrix

   :param xreg_names: Optional keyword, column names for *xreg*.
   :type xreg_names: Kx1 string array

   :param var_names: Optional keyword, endogenous variable names.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Overrides *ctl.quiet*.
   :type quiet: scalar

   :return result: An instance of a :class:`bvarResult` structure containing:

       .. include:: include/bvarresult.rst

   :rtype result: struct

Examples
--------

Default Minnesota BVAR
++++++++++++++++++++++

Fit a BVAR(1) with default Minnesota prior settings:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Default Minnesota BVAR(1)
    result = bvarFit(data);

Minnesota BVAR(4) with Custom Tightness
++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.lambda1 = 0.1;        // Tighter prior

    result = bvarFit(data, ctl);

BVAR with Sum-of-Coefficients and Single-Unit-Root Priors
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.lambda6 = 5;          // Sum-of-coefficients
    ctl.lambda7 = 5;          // Single-unit-root

    result = bvarFit(data, ctl);

Stationary Prior for Growth Rate Data
++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.ar = 0;               // White noise prior (not random walk)

    result = bvarFit(data, ctl);

Model Comparison via Marginal Likelihood
++++++++++++++++++++++++++++++++++++++++

Compare lag orders using the log marginal likelihood:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    struct bvarResult r1, r2, r4;

    ctl = bvarControlCreate();

    // Fit with p=1, p=2, p=4
    ctl.p = 1;
    r1 = bvarFit(data, ctl, quiet=1);

    ctl.p = 2;
    r2 = bvarFit(data, ctl, quiet=1);

    ctl.p = 4;
    r4 = bvarFit(data, ctl, quiet=1);

    // Compare
    print "Log ML(p=1):" r1.log_ml;
    print "Log ML(p=2):" r2.log_ml;
    print "Log ML(p=4):" r4.log_ml;

    // Bayes factor for p=4 vs p=2
    print "BF(4 vs 2):" exp(r4.log_ml - r2.log_ml);

BVAR with Exogenous Regressors
+++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "oil");

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;

    result = bvarFit(y, ctl, xreg=X, var_names="GDP"$|"CPI"$|"FFR", xreg_names="Oil");

Remarks
-------

**Minnesota prior:**
The default Minnesota prior (Kadiyala & Karlsson 1997) places a Normal-Inverse-Wishart
conjugate prior on the coefficients B and covariance :math:`\Sigma`. The prior
shrinks coefficients toward a random walk (:math:`ar = 1`) or white noise
(:math:`ar = 0`). Cross-variable coefficients are shrunk more than own-lag
coefficients (controlled by *lambda2*), and higher lags are shrunk more than
lower lags (controlled by *lambda3*).

**Conjugate vs Gibbs:**
With ``prior = "minnesota"`` (default), the posterior is available in closed form
and draws are exact (no MCMC). With ``prior = "flat"``, the posterior is
sampled via Gibbs with *n_draws*, *n_burn*, *n_thin* iterations.

**Log marginal likelihood:**
*result.log_ml* is only available for the conjugate Minnesota prior (closed-form
computation). It can be used for formal Bayesian model comparison — the model
with the highest log ML is preferred. For flat priors, *result.log_ml* is missing.

**Sum-of-coefficients (lambda6) and single-unit-root (lambda7):**
These add "dummy observations" to the data that encode prior beliefs:

- **SOC** pulls the sum of lag coefficients toward the identity, preventing explosive long-horizon forecasts.
- **SUR** pulls all variables toward a common unit root, stabilizing cointegrated systems.

Both are disabled by default (lambda = 0). Typical values range from 1 to 10.
See Giannone, Lenza & Primiceri (2015) for guidance on setting these values,
or use :func:`bvarHyperopt` to optimize them automatically.

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarControlCreate`, :func:`bvarSvFit`, :func:`bvarHyperopt`, :func:`varResults`, :func:`varCoefTable`
