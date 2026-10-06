varDiagnostics
==============

Purpose
-------
Check the residuals of a fitted VAR or BVAR: autocorrelation, normality and changing variance.

Format
------

.. function:: vd = varDiagnostics(fit)
              vd = varDiagnostics(fit, lags=12, arch_lags=4, quiet=1)

   :param fit: An instance of a :class:`varResult` structure returned by :func:`varFit`, or a :class:`bvarResult` structure returned by :func:`bvarFit`.
   :type fit: struct

   :param lags: Optional keyword, number of autocorrelation lags tested. Must be larger than the fit's lag order. Default = 12.
   :type lags: scalar

   :param arch_lags: Optional keyword, number of lags of squared residuals in the ARCH-LM test. Default = 4.
   :type arch_lags: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return vd: An instance of a :class:`varDiagResult` structure containing:

       .. include:: include/vardiagresult.rst

   :rtype vd: struct

Examples
--------

::

    new;
    library timeseries;

    // Four quarterly US series, 1960Q1-2019Q4
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    data = data[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    ols = varFit(y, p=5, quiet=1);
    bvar = bvarFit(y, p=5, lag1_prior_mean=0|1|1|1, quiet=1);

    diag_ols = varDiagnostics(ols);
    diag_bvar = varDiagnostics(bvar);

The least-squares VAR's printout begins:

::

    Residual diagnostics: VAR(5), least squares
    ================================================================================
    235 residuals per equation; autocorrelation tested over 12 lags.

    Test                             Statistic    df   p-value
    ----------------------------------------------------------
    Portmanteau, all equations          196.86   112   <0.0001
    Normality (Jarque-Bera)            2742.06     8   <0.0001
    ARCH-LM, 4 lags                      59.83    16   <0.0001

Remarks
-------

**Portmanteau.** Tests whether the residuals of all equations, taken
together, still have autocorrelation at lags 1 to *lags*. The statistic is
the adjusted portmanteau of Lutkepohl (2005, section 4.4.3),

.. math::

   \bar Q_h = T^2 \sum_{j=1}^{h} \frac{1}{T-j}\,
   \operatorname{tr}\!\left(\hat C_j' \hat C_0^{-1} \hat C_j \hat C_0^{-1}\right),
   \qquad \hat C_j = \frac{1}{T}\sum_{t=j+1}^{T} \hat u_t \hat u_{t-j}',

compared with a chi-square on :math:`m^2(h-p)` degrees of freedom, where *m*
is the number of equations and *p* the lag order. A BVAR's prior shrinks its
lags instead of estimating them freely, so for a :func:`bvarFit` result the
right reference lies between :math:`m^2(h-p)` and :math:`m^2 h` degrees of
freedom; both p-values are reported. The approximation needs *lags* well
above *p*.

**Ljung-Box by equation.** The Ljung-Box *Q* of each equation's residuals
over the same lags shows where autocorrelation remains. It is reported
without a p-value: in a VAR, one equation's residual autocorrelations do
not have a chi-square reference. For a single series, use
:func:`ljungBoxTest`.

**Normality.** Multivariate Jarque-Bera test on the residuals standardized
by the Cholesky factor of their covariance, chi-square on :math:`2m`
degrees of freedom. The result depends on the order of the variables.

**ARCH-LM.** For each equation, the squared residual is regressed on a
constant and its own *arch_lags* lags; the statistic is the sum over
equations of :math:`(T - q)R^2` (Engle 1982), chi-square on
:math:`m \cdot q` degrees of freedom with :math:`q` = *arch_lags*. It tests
whether the size of the shocks changes over time, equation by equation;
it is not the full multivariate ARCH test.

BVAR residuals are those stored by :func:`bvarFit`, at the analytic posterior mean.

References
----------

- Engle, R.F. (1982). "Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation." *Econometrica*, 50(4), 987-1007.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`ljungBoxTest`, :func:`vecmDiagnostics`, :func:`varFitInspect`, :func:`mcmcDiagnostics`
