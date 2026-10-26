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

   :param arch_lags: Optional keyword, number of lags of residual products in the ARCH-LM tests. Default = 4.
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

    struct vecmResult vr;
    struct diagResult d;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);
    d = vecmDiagnostics(vr);

The printout:

::

    VECM Residual Diagnostics
    ================================================================================
    Test                                     Statistic      df     p-value
    ----------------------------------------------------------------------
    Portmanteau (Ljung-Box), 12 lags           160.860     172      0.7184
    Breusch-Godfrey LM, 5 lags                  89.176      80      0.2261
    Jarque-Bera (normality)                      4.721       8      0.7870
    ARCH-LM, multivariate, 4 lags              478.648     400      0.0041

    ARCH-LM per equation, 4 lags
    Equation                   Statistic      df     p-value
    --------------------------------------------------------
    e                               6.91       4      0.1405
    prod                            3.77       4      0.4378
    rw                              1.72       4      0.7879
    U                               8.39       4      0.0782

The installed example gives the following multivariate ARCH-LM results.
The default remains *arch_lags* = 4.

.. list-table:: Canada VECM, rank 1 and two lags in levels
   :header-rows: 1

   * - arch_lags
     - Auxiliary observations (*n*)
     - Statistic
     - df
     - p-value
   * - 1
     - 81
     - 119.791837
     - 100
     - 0.086444
   * - 2
     - 80
     - 235.342802
     - 200
     - 0.044052
   * - 3
     - 79
     - 367.488101
     - 300
     - 0.004677
   * - 4
     - 78
     - 478.647715
     - 400
     - 0.004145

At four lags, the separate equation tests each have four degrees of freedom:

.. list-table:: Separate equation tests, arch_lags = 4
   :header-rows: 1

   * - Equation
     - Statistic
     - p-value
   * - e
     - 6.913911
     - 0.140508
   * - prod
     - 3.771291
     - 0.437842
   * - rw
     - 1.715304
     - 0.787936
   * - U
     - 8.392944
     - 0.078200

The four-lag multivariate test rejects at 5%, while none of these separate
equation tests does. The multivariate result depends on the lag count and
uses a chi-square approximation with 400 degrees of freedom for 78 auxiliary
observations, so interpret it with the finite-sample caveat below.

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
trend), the lagged differences, the unrestricted constant (cases 3 to 5),
the seasonal dummies, and, when the fit has them, the unrestricted trend and
exogenous columns. This is the auxiliary regression of Bruggemann, Lutkepohl and
Saikkonen (2006, eq. 4.4 and Remarks 1 and 2; numbers from their working
paper of January 2004) without their additional score terms, the version
their simulations favour. Their model has no unrestricted trend or
exogenous columns; these enter with the model's other regressors. The
residuals are used as they are, not demeaned, as in Kilian and Lutkepohl
(2017, eq. 2.6.2). In
a model without an unrestricted constant their mean is not zero, so
implementations that demean them can report different values. With
:math:`\hat\Sigma_u` and :math:`\hat\Sigma_e` the residual covariances of
the VECM and of this regression (both divided by *T*),

.. math::

   Q_{LM} = T\left(m - \operatorname{tr}\left(\hat\Sigma_u^{-1}\hat\Sigma_e\right)\right),

compared with a chi-square on :math:`h m^2` degrees of freedom. Unlike the
portmanteau test, it needs no adjustment for the cointegrating rank
(Kilian and Lutkepohl 2017, section 3.4). Only this chi-square form is
reported, the form Bruggemann, Lutkepohl and Saikkonen study for VECMs
(together with LR and Wald forms, which reject too often in their
simulations).
When *lm_lags* leaves fewer residual degrees of freedom in the regression
than equations, the LM test is shown as missing with a note giving the
largest *lm_lags* that works; the other tests are still reported.

**Normality.** Multivariate Jarque-Bera test on the residuals standardized
by the Cholesky factor of their covariance, chi-square on :math:`2m`
degrees of freedom. The result depends on the order of the variables.

**Multivariate ARCH-LM.** Demean each residual over all *T* observations.
Form :math:`v_t=\operatorname{vech}(u_tu_t')`, stacking columns from the
main diagonal down, and regress it on a constant and *q* = *arch_lags*
lags of itself. Drop the first *q* rows, so :math:`n=T-q`. With
:math:`d=m(m+1)/2`, the statistic is

.. math::

   LM_{ARCH}(q)=n\left[d-\operatorname{tr}(\hat\Omega_0^{-1}\hat\Omega)\right],
   \qquad df=q d^2= q m^2(m+1)^2/4.

Here :math:`\hat\Omega` is the covariance of the auxiliary residuals and
:math:`\hat\Omega_0` is the covariance from a constant-only regression
on the same *n* rows, with the same divisor. The p-value uses a chi-square
with *df* degrees of freedom. No adjustment is made for the estimated
cointegrating vectors. This tests changes in variances and
cross-equation covariances (Kilian and Lutkepohl 2017, section 2.7.3;
Lutkepohl 2005, section 16.5.1; Doornik and Hendry 1997, section 10.9.2.4).

TSMT requires at least *d* residual degrees of freedom after the
:math:`1+qd` regressors. This is TSMT's sample guard, not a requirement
stated by the textbook. The multivariate statistic and p-value are missing
when :math:`n-(1+qd)<d`, the auxiliary regression is singular, or
:math:`\hat\Omega_0` is not positive definite. The nominal degrees of
freedom remain available. For too few observations, *arch_note* gives the
largest *arch_lags* allowed by the sample guard,
:math:`\max(0,\lfloor(T-1-d)/(d+1)\rfloor)`; the design and covariance must
also be nonsingular.

The test can have low power in finite samples, and the chi-square with
:math:`qd^2` degrees of freedom can be a poor approximation when that number
is large relative to the sample. Bootstrap critical values are an alternative
(Kilian and Lutkepohl 2017, section 2.7.3).

**Per-equation ARCH-LM.** Each demeaned residual squared is regressed on
a constant and *q* own lags, also dropping the first *q* rows.
The separate Engle (1982) statistics are :math:`nR_i^2`, each compared
with chi-square(*q*). They are retained when the multivariate test is
unavailable. A constant squared residual or a singular regression gives
a missing result for that equation and an *arch_eq_reason* code.
Each equation needs at least :math:`q+2` auxiliary observations, leaving
at least one residual degree of freedom; a saturated fit is missing with
reason 1. These are separate tests, each at its own significance level,
not a joint test: testing *m* equations at 5% rejects more often than 5%
overall. Their statistics are not added together for joint inference.

References
----------

- Bruggemann, R., H. Lutkepohl and P. Saikkonen (2006). "Residual autocorrelation testing for vector error correction models." *Journal of Econometrics*, 134(2), 579-604.
- Engle, R.F. (1982). "Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation." *Econometrica*, 50(4), 987-1007.
- Kilian, L. and H. Lutkepohl (2017). *Structural Vector Autoregressive Analysis*. Cambridge University Press.

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.

- Doornik, J.A. and D.F. Hendry (1997). *Modelling Dynamic Systems Using PcFiml 9.0 for Windows*. International Thomson Business Press.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`varDiagnostics`, :func:`ljungBoxTest`
