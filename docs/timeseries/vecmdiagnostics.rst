vecmDiagnostics
===============

Purpose
-------
Check the residuals of a fitted VECM: autocorrelation, normality and changing variance.

Format
------

.. function:: d = vecmDiagnostics(result)
              d = vecmDiagnostics(result, port_lags=12, lm_lags=5, arch_lags=4, quiet=1)

   :param result: An instance of a :class:`vecmResult` structure returned by :func:`vecmFit`.
   :type result: struct

   :param port_lags: Optional keyword, number of autocorrelation lags in the portmanteau test. :math:`m^2 \cdot` *port_lags* must exceed :math:`(p-1)m^2 + mr`. Default = 12.
   :type port_lags: scalar

   :param lm_lags: Optional keyword, number of lagged residuals in the LM test. Default = 5.
   :type lm_lags: scalar

   :param arch_lags: Optional keyword, number of lags of squared residuals in the ARCH-LM test. Default = 4.
   :type arch_lags: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return d: An instance of a :class:`diagResult` structure containing:

       .. include:: include/diagresult.rst

   :rtype d: struct

Examples
--------

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);
    d = vecmDiagnostics(vr);

The printout:

::

    ================================================================================
    VECM Residual Diagnostics
    ================================================================================

    Portmanteau (Ljung-Box), lags=12:
      Q statistic:     160.860   df:   172   p-value:    0.7184

    Breusch-Godfrey LM, lags=5:
      LM statistic:      89.176   df:    80   p-value:    0.2261

    Jarque-Bera (normality):
      JB statistic:       4.721   df:     8   p-value:    0.7870

    ARCH-LM, lags=4:
      LM statistic:      20.793   df:    16   p-value:    0.1866

    ================================================================================

Remarks
-------

In the formulas below *m* is the number of variables, *p* the lag order in
levels, *r* the cointegrating rank and *T* the number of residuals.

**Portmanteau.** Tests whether the residuals of all equations, taken
together, still have autocorrelation at lags 1 to :math:`h` = *port_lags*.
The statistic is the modified portmanteau of Kilian and Lutkepohl (2017,
section 2.6.2),

.. math::

   \bar Q_h = T^2 \sum_{j=1}^{h} \frac{1}{T-j}\,
   \operatorname{tr}\!\left(\hat C_j' \hat C_0^{-1} \hat C_j \hat C_0^{-1}\right),
   \qquad \hat C_j = \frac{1}{T}\sum_{t=j+1}^{T} \hat u_t \hat u_{t-j}',

compared with a chi-square on :math:`m^2 h - m^2(p-1) - mr` degrees of
freedom (Kilian and Lutkepohl 2017, section 3.4). That reference assumes
the cointegrating rank is correct.

**LM test.** Tests whether the residuals have autocorrelation at lags 1 to
:math:`h` = *lm_lags*. The residuals are regressed on the VECM's own
regressors and on their own lags 1 to *h*, with residuals before the
sample set to zero. The VECM's regressors are the estimated cointegrating
relations :math:`\hat\beta' y_{t-1}` (including a restricted constant or
trend), the lagged differences, the unrestricted constant, the seasonal
dummies, and, when the fit has them, the unrestricted trend and exogenous
columns. This is the auxiliary regression of Bruggemann, Lutkepohl and
Saikkonen (2006, eq. 4.4 and Remarks 1 and 2; numbers from their working
paper of January 2004) without their additional score terms, the version
their simulations favour; their model has no unrestricted trend or
exogenous columns, and these enter as the model's own regressors, as in
Kilian and Lutkepohl (2017, eq. 2.6.2). The residuals are used as they
are, not demeaned (Kilian and Lutkepohl 2017, eq. 2.6.2). In a model
without an unrestricted constant their mean is not zero, and
implementations that demean them report larger values. With
:math:`\hat\Sigma_u` and :math:`\hat\Sigma_e` the residual covariances of
the VECM and of this regression (both divided by *T*),

.. math::

   Q_{LM} = T\left(m - \operatorname{tr}\left(\hat\Sigma_u^{-1}\hat\Sigma_e\right)\right),

compared with a chi-square on :math:`h m^2` degrees of freedom. Unlike the
portmanteau test, it needs no adjustment for the cointegrating rank
(Kilian and Lutkepohl 2017, section 3.4). Only this chi-square form is
reported. Bruggemann, Lutkepohl and Saikkonen study it (and LR and Wald
forms, which reject too often) for VECMs and leave small-sample F
corrections aside; the F approximation that :func:`varDiagnostics` prints
(Doornik 1996) is derived for multivariate regressions in general but has
not been evaluated for VECMs.
When *lm_lags* leaves fewer residual degrees of freedom in the regression
than equations, the LM test is shown as missing with a note giving the
largest *lm_lags* that works; the other tests are still reported.

**Normality.** Multivariate Jarque-Bera test on the residuals standardized
by the Cholesky factor of their covariance, chi-square on :math:`2m`
degrees of freedom. The result depends on the order of the variables.

**ARCH-LM.** For each equation, the squared residual is regressed on a
constant and its own *arch_lags* lags; the statistic is the sum over
equations of :math:`(T - q)R^2` (Engle 1982), chi-square on
:math:`m \cdot q` degrees of freedom with :math:`q` = *arch_lags*. It is
not the full multivariate ARCH test.

References
----------

- Bruggemann, R., H. Lutkepohl and P. Saikkonen (2006). "Residual autocorrelation testing for vector error correction models." *Journal of Econometrics*, 134(2), 579-604.
- Doornik, J.A. (1996). "Testing vector error autocorrelation and heteroscedasticity." Working paper, Nuffield College, Oxford.
- Engle, R.F. (1982). "Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation." *Econometrica*, 50(4), 987-1007.
- Kilian, L. and H. Lutkepohl (2017). *Structural Vector Autoregressive Analysis*. Cambridge University Press.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`varDiagnostics`, :func:`ljungBoxTest`
