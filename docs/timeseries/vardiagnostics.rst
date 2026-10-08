varDiagnostics
==============

Purpose
-------
Check the residuals of a fitted least-squares VAR: autocorrelation, normality and changing variance.

Format
------

.. function:: vd = varDiagnostics(fit)
              vd = varDiagnostics(fit, port_lags=12, lm_lags=5, arch_lags=4, quiet=1)

   :param fit: An instance of a :class:`varResult` structure returned by :func:`varFit`.
   :type fit: struct

   :param port_lags: Optional keyword, number of autocorrelation lags in the portmanteau test. Must be larger than the fit's lag order. Default = 12.
   :type port_lags: scalar

   :param lm_lags: Optional keyword, number of lagged residuals in the LM test. Default = 5.
   :type lm_lags: scalar

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

    diag_ols = varDiagnostics(ols);

The printout begins:

::

    Residual diagnostics: VAR(5), least squares
    ================================================================================
    235 residuals per equation.

    Test                                   Statistic          df   p-value
    ----------------------------------------------------------------------
    Portmanteau, 12 lags                      196.86         112   <0.0001
    LM (Breusch-Godfrey), 5 lags              137.91          80   <0.0001
    LM, F form (Rao), 5 lags                    1.67     80, 755    0.0004
    Normality (Jarque-Bera)                  2742.06           8   <0.0001
    ARCH-LM, 4 lags                            59.83          16   <0.0001

Remarks
-------

**Portmanteau.** Tests whether the residuals of all equations, taken
together, still have autocorrelation at lags 1 to *port_lags*. The statistic is
the modified portmanteau of Kilian and Lutkepohl (2017, section 2.6.2),

.. math::

   \bar Q_h = T^2 \sum_{j=1}^{h} \frac{1}{T-j}\,
   \operatorname{tr}\!\left(\hat C_j' \hat C_0^{-1} \hat C_j \hat C_0^{-1}\right),
   \qquad \hat C_j = \frac{1}{T}\sum_{t=j+1}^{T} \hat u_t \hat u_{t-j}',

compared with a chi-square on :math:`m^2(h-p)` degrees of freedom, where *m*
is the number of equations, :math:`h` = *port_lags* and *p* the lag
order. The same section asks for *port_lags* considerably larger than *p*,
and notes that the chi-square reference is not reliable when some
variables are nonstationary.

**LM test.** Tests whether the residuals of all equations, taken together,
have autocorrelation at lags 1 to *lm_lags*. Following Kilian and Lutkepohl
(2017, section 2.6.2, eq. 2.6.2), the residuals are regressed on the VAR's
own regressors (its lags, the constant and any *xreg* columns of the fit)
and on their own lags 1 to :math:`h` = *lm_lags*, with residuals before the
sample set to zero. With :math:`\hat\Sigma_u` and :math:`\hat\Sigma_e` the
residual covariances of the VAR and of this regression (both divided by
*T*),

.. math::

   Q_{LM} = T\left(m - \operatorname{tr}\left(\hat\Sigma_u^{-1}\hat\Sigma_e\right)\right),

compared with a chi-square on :math:`h m^2` degrees of freedom. The same
section prefers this test to the portmanteau test for low-order
autocorrelation, and reports, citing Bruggemann, Lutkepohl and Saikkonen
(2006), that its chi-square reference stays valid when some variables are
integrated.

**F form.** Kilian and Lutkepohl (2017, section 2.6.2) note that the LM
statistic's small-sample distribution can differ substantially from its
chi-square, and point to the F version of Edgerton and Shukur (1999).
varDiagnostics computes :math:`F_{Rao}(h)` of Lutkepohl (2005, section
4.4.4), Rao's F approximation from Doornik (1996). With :math:`k`
regressors per equation in the VAR (:math:`k = mp + 1` with a constant),

.. math::

   F_{Rao}(h) = \left[\left(\frac{|\hat\Sigma_u|}{|\hat\Sigma_e|}\right)^{1/s} - 1\right]
   \frac{Ns - \frac{1}{2}m^2 h + 1}{m^2 h},

   s = \left(\frac{m^4 h^2 - 4}{m^2 + m^2 h^2 - 5}\right)^{1/2}, \qquad
   N = T - k - mh - \tfrac{1}{2}(m - mh + 1).

The statistic uses :math:`Ns - \frac{1}{2}m^2 h + 1` as written; its
p-value comes from an F distribution on :math:`hm^2` and
:math:`[Ns - \frac{1}{2}m^2 h + 1]` degrees of freedom, the integer part,
which is the second degrees of freedom Lutkepohl (2005, Table 4.8) prints.
The F form needs :math:`|\hat\Sigma_e| > 0`. When the regression leaves
fewer residual degrees of freedom than equations (:math:`T - k - mh < m`),
both LM rows are shown as "-" (missing values in *vd*) with a note giving
the largest *lm_lags* that works; the other tests are still reported.

On the investment/income/consumption VAR(2) of Lutkepohl (2005, Table
4.8), varDiagnostics gives LM statistics 6.37, 15.52, 32.81 and 46.60 and
:math:`F_{Rao}` values 0.62, 0.76, 1.14 and 1.26, on 148, 164, 161 and 154
second degrees of freedom, for *lm_lags* = 1 to 4, as printed there.

**Normality.** Multivariate Jarque-Bera test on the residuals standardized
by the Cholesky factor of their covariance, chi-square on :math:`2m`
degrees of freedom. The result depends on the order of the variables.

**ARCH-LM.** For each equation, the squared residual is regressed on a
constant and its own *arch_lags* lags; the statistic is the sum over
equations of :math:`(T - q)R^2` (Engle 1982), chi-square on
:math:`m \cdot q` degrees of freedom with :math:`q` = *arch_lags*. It tests
whether the size of the shocks changes over time, equation by equation;
it is not the full multivariate ARCH test.

varDiagnostics takes least-squares fits only: the reference distributions
above are derived for least-squares residuals, and results from
:func:`bvarFit` are refused.

References
----------

- Bruggemann, R., H. Lutkepohl and P. Saikkonen (2006). "Residual autocorrelation testing for vector error correction models." *Journal of Econometrics*, 134(2), 579-604.
- Doornik, J.A. (1996). "Testing vector error autocorrelation and heteroscedasticity." Working paper, Nuffield College, Oxford.
- Edgerton, D. and G. Shukur (1999). "Testing autocorrelation in a system perspective." *Econometric Reviews*, 18(4), 343-386.
- Engle, R.F. (1982). "Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation." *Econometrica*, 50(4), 987-1007.
- Kilian, L. and H. Lutkepohl (2017). *Structural Vector Autoregressive Analysis*. Cambridge University Press.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`ljungBoxTest`, :func:`vecmDiagnostics`, :func:`varFitInspect`, :func:`mcmcDiagnostics`
