varFit
======

Purpose
-------
Fit a VAR(p) model by ordinary least squares.

Format
------

.. function:: result = varFit(y)
              result = varFit(y, p)
              result = varFit(y, ctl)

   :param y: endogenous variables. If a dataframe, column names are used as variable labels in output. If a matrix, variables are labeled "Y1", "Y2", etc.
   :type y: TxM matrix or dataframe

   :param p: Optional input, lag order. Default = 1.
   :type p: scalar

   :param ctl: Optional input, an instance of a :class:`varControl` structure. Overrides *p* if provided. Set *ctl.xreg* for exogenous regressors. An instance is initialized by calling :func:`varControlCreate` and the following members can be set:

       .. include:: include/varcontrol.rst

   :type ctl: struct

   :return result: An instance of a :class:`varResult` structure containing:

       .. include:: include/varresult.rst

   :rtype result: struct

Model
-----

The reduced-form VAR(p) is:

.. math::

   y_t = B_1 y_{t-1} + B_2 y_{t-2} + \cdots + B_p y_{t-p} + \Phi x_t + u + \varepsilon_t, \quad \varepsilon_t \sim N(0, \Sigma)

where :math:`y_t` is :math:`m \times 1`, each :math:`B_\ell` is :math:`m \times m`,
:math:`x_t` are optional exogenous regressors, :math:`u` is the intercept, and
:math:`\Sigma` is the :math:`m \times m` error covariance.

Stacking the regressors into :math:`X = [Y_{-1} \; Y_{-2} \; \cdots \; Y_{-p} \; X_{\text{exo}} \; \mathbf{1}]`
(a :math:`T_{\text{eff}} \times K` matrix where :math:`K = mp + n_{\text{exo}} + 1`), the
system is estimated equation-by-equation by OLS:

.. math::

   \hat{B} = (X'X)^{-1} X'Y, \qquad \hat{\Sigma} = \frac{1}{T_{\text{eff}}} (Y - X\hat{B})'(Y - X\hat{B})

Standard errors, t-statistics, and information criteria (AIC, BIC, HQ) are computed from
the OLS residuals.


Algorithm
---------

1. **Construct lag matrices:** Build :math:`Y` (dependent) and :math:`X` (regressors with lags, exogenous, constant) from the raw data, consuming the first :math:`p` rows as initial conditions.

2. **OLS estimation:** Solve the normal equations via QR decomposition for numerical stability. Complexity: :math:`O(T K^2 m)`.

3. **Residual covariance:** ML estimate :math:`\hat\Sigma = (Y - X\hat{B})'(Y - X\hat{B}) / T_{\text{eff}}`.

4. **Companion form:** Construct the :math:`mp \times mp` companion matrix and compute its eigenvalues to assess stability.

5. **Information criteria:**

   .. math::

      \text{AIC} &= \log|\hat\Sigma| + \frac{2 K m}{T_{\text{eff}}} \\
      \text{BIC} &= \log|\hat\Sigma| + \frac{K m \log T_{\text{eff}}}{T_{\text{eff}}} \\
      \text{HQ}  &= \log|\hat\Sigma| + \frac{2 K m \log \log T_{\text{eff}}}{T_{\text{eff}}}

**Complexity:** Sub-millisecond for typical macro systems (m < 10, T < 500).


Examples
--------

Monetary Policy VAR
+++++++++++++++++++

::

    new;
    library timeseries;

    // Load US macro quarterly data
    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

    // Fit VAR(4)
    result = varFit(data, 4);

Output:

::

    ================================================================================
    VAR(4)                                  Variables:             3
    Method: OLS                             Observations:        200
    Constant: Yes                           Effective obs:       196
    ================================================================================
    AIC:       -12.384          BIC:       -11.927          HQ:        -12.198
    Log-Lik:    1232.86         |Sigma|:    2.41e-08
    ================================================================================
    Companion eigenvalues: 0.981  0.854  0.723  (all inside unit circle)
    ================================================================================

    Equation 1: GDP
                        Coef      Std.Err.     t-stat    p-value
    --------------------------------------------------------------------------------
    GDP(-1)            0.8731      0.0543     16.076      0.000
    CPI(-1)           -0.0218      0.0437     -0.499      0.618
    FFR(-1)            0.0012      0.0089      0.135      0.893
    Constant           0.0080      0.0012      6.588      0.000
    ================================================================================
        ⋮  (Equations 2-3: CPI and FFR follow the same format)

Lag Order Selection
+++++++++++++++++++

Compare AIC across lag orders to choose p:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

    // Automatic selection
    best = varLagSelect(data, 8);   // Test p = 1..8

    print "Selected lag order:" best.p;

    // Or compare manually
    for p (1, 8, 1);
        result = varFit(data, p, quiet=1);
        print "p=" p "  AIC=" result.aic "  BIC=" result.bic;
    endfor;

VAR with Exogenous Regressors
+++++++++++++++++++++++++++++

Include oil price as an exogenous variable:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    y = loadd(fname, "gdp + cpi + ffr");
    X = loadd(fname, "oil");

    ctl = varControlCreate();
    ctl.p = 2;
    ctl.xreg = X;

    result = varFit(y, ctl);

Troubleshooting
---------------

**Non-stationary VAR:**
If the companion matrix has eigenvalues outside the unit circle, the model implies
explosive dynamics. This does not necessarily indicate an error — it may reflect
unit roots in the data. Consider:

- Differencing the data or using growth rates.
- Using a BVAR (:func:`bvarFit`) where the prior regularizes toward stationarity.
- If the data is cointegrated, a VECM may be more appropriate.

**Singular X'X matrix:**
This occurs when the regressor matrix is rank-deficient, typically from collinear
variables or too many lags relative to the sample size. Reduce p, remove collinear
variables, or use :func:`bvarFit` where the prior regularizes the problem.

**Choosing p:**
Use :func:`varLagSelect` to compare information criteria. BIC tends to select
parsimonious models (smaller p), AIC selects larger p. In quarterly macro data,
p = 4 (one year of lags) is a common starting point (Lutkepohl 2005, Section 4.3).


Remarks
-------

**Coefficient layout in result.b:**

The coefficient matrix *result.b* is Kxm where K = m*p + n_exo + include_const
and m is the number of endogenous variables:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Rows
     - Content
   * - 1 to m
     - Lag 1 coefficients (mxm block)
   * - m+1 to 2m
     - Lag 2 coefficients
   * - ...
     - ...
   * - (p-1)*m+1 to pm
     - Lag p coefficients
   * - pm+1 to pm+n_exo
     - Exogenous coefficients (if any)
   * - K
     - Constant (if *include_const* = 1)

Column j corresponds to equation j (variable j as dependent variable).
This layout matches the standard convention in Lutkepohl (2005, Section 3.2.1).

**Stability:**

The companion form eigenvalues are computed automatically and printed in the
summary. A VAR is stable (stationary) if all eigenvalues of the companion
matrix have modulus strictly less than 1. Non-stationary models produce a
warning but are not rejected — they may be appropriate for cointegrated systems.

**When to use VAR vs BVAR:**
For estimation and hypothesis testing with standard inference (t-stats, p-values,
Granger causality), use ``varFit``. For forecasting, especially with m > 3 variables,
:func:`bvarFit` dominates in out-of-sample accuracy because the Minnesota prior
regularizes noisy cross-variable coefficients (Banbura, Giannone & Reichlin 2010).


Verification
------------

Verified against R ``vars`` 1.6-1 (R 4.5.2) with 22 tests at :math:`10^{-6}` tolerance,
covering coefficients, :math:`\Sigma`, residuals, log-likelihood, companion eigenvalues,
IRF, FEVD, Granger causality, and forecasts on identical data (2-variable VAR(1),
300 observations, known DGP).

Additionally, verified against ECB BEAR Toolbox OLS output at :math:`10^{-8}` tolerance
on the 3-variable ECB default dataset (YER, HICSA, STN), confirming all 13 coefficients,
6 :math:`\Sigma` elements, and companion eigenvalues match.

See ``gausslib-var/tests/r_benchmark.rs`` and the :ref:`var-verification` page.


References
----------

- Banbura, M., D. Giannone, and L. Reichlin (2010). "Large Bayesian vector auto regressions." *Journal of Applied Econometrics*, 25(1), 71-92.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.
- Sims, C.A. (1980). "Macroeconomics and reality." *Econometrica*, 48(1), 1-48.


Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varLagSelect`, :func:`bvarFit`, :func:`irfCompute`, :func:`grangerTest`, :func:`varCompanion`, :func:`varCoefTable`

.. seealso:: Guides :ref:`choosing-a-var-model`, :ref:`var-verification`
