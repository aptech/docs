vecmFit
=======

Purpose
-------
Estimate a vector error correction model (VECM) with a given number of cointegrating relations by Johansen's maximum likelihood method.

Format
------

.. function:: vr = vecmFit(y, r)
              vr = vecmFit(y, r, p=1, det_case=3, season=0, quiet=0)
              vr = vecmFit(y, r, ctl=ctl)

   :param y: the series in levels, not differences. If a dataframe, the column names label the output.
   :type y: TxM matrix or dataframe

   :param r: cointegrating rank, 1 to M.
   :type r: scalar

   :param p: Optional keyword, lag order of the model written in levels. The VECM has ``p-1`` lagged differences. Default = 1.
   :type p: scalar

   :param det_case: Optional keyword, deterministic terms, 1 to 5 (see Remarks). Default = 3.
   :type det_case: scalar

   :param season: Optional keyword, 0 for no seasonal dummies; otherwise a whole number giving the number of seasons per year, at least 2 (4 for quarterly data, 12 for monthly). Adds ``season-1`` centered seasonal dummies. 1 is refused. Default = 0.
   :type season: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of a :class:`vecmControl` structure, needed only to add your own regressors. When *ctl* is passed, ``p``, ``det_case`` and ``quiet`` are read from it and the keywords of the same name are ignored. ``season`` is not a member of the structure; pass it as a keyword together with *ctl*, as in ``vecmFit(y, r, ctl=ctl, season=4)``. An instance is initialized by calling :func:`vecmControlCreate` and the following members can be set:

       .. include:: include/vecmcontrol.rst

   :type ctl: struct

   :return vr: An instance of a :class:`vecmResult` structure containing:

       .. include:: include/vecmresult.rst

   :rtype vr: struct

Examples
--------

Fit with one cointegrating relation
+++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3);

The printout:

::

    VECM, maximum likelihood
    ================================================================================
    Rank:                              1    Lags:                                  2
    Deterministic:  Unrestricted constant
    Variables:                         4    Observations:                         84
    Usable obs.:       82 (rows 3 to 84)    Log-likelihood:                  -190.12
    AIC:                         -6.0560    BIC:                             -5.2635
    HQ:                          -5.7378
    Largest root (excl. M-r unit roots):              0.8534

    Cointegrating vectors (beta): first r rows set to the identity
    Cointegrating relation CE1
    Coefficient    Coef.  Std. err.       z  p-value
    ------------------------------------------------
    e             1.0000          -       -        -
    prod          0.1503     0.2012   0.747    0.455
    rw           -0.2465     0.0303  -8.127  < 0.001
    U             3.6128     0.3326  10.864  < 0.001

    Equation 1: D.e
    Coefficient     Coef.  Std. err.       z  p-value
    -------------------------------------------------
    CE1            0.0132     0.0158   0.838    0.402
    D.e(-1)        0.7656     0.1412   5.424  < 0.001
    D.prod(-1)     0.1651     0.0638   2.588    0.010
    D.rw(-1)      -0.0236     0.0560  -0.422    0.673
    D.U(-1)        0.1421     0.1934   0.735    0.463
    Constant     -12.2255    14.7387  -0.829    0.407

    Equation 2: D.prod
    Coefficient     Coef.  Std. err.       z  p-value
    -------------------------------------------------
    CE1            0.0666     0.0265   2.512    0.012
    D.e(-1)       -0.2986     0.2372  -1.259    0.208
    D.prod(-1)     0.1479     0.1072   1.379    0.168
    D.rw(-1)       0.1232     0.0940   1.310    0.190
    D.U(-1)       -0.8435     0.3250  -2.595    0.009
    Constant     -61.9059    24.7637  -2.500    0.012

    Equation 3: D.rw
    Coefficient     Coef.  Std. err.       z  p-value
    -------------------------------------------------
    CE1           -0.1817     0.0322  -5.635  < 0.001
    D.e(-1)       -0.1962     0.2883  -0.681    0.496
    D.prod(-1)    -0.0437     0.1303  -0.336    0.737
    D.rw(-1)      -0.0570     0.1143  -0.498    0.618
    D.U(-1)        0.4351     0.3950   1.102    0.271
    Constant     170.2479    30.0977   5.657  < 0.001

    Equation 4: D.U
    Coefficient    Coef.  Std. err.       z  p-value
    ------------------------------------------------
    CE1          -0.0438     0.0119  -3.696  < 0.001
    D.e(-1)      -0.5846     0.1060  -5.514  < 0.001
    D.prod(-1)   -0.0731     0.0479  -1.525    0.127
    D.rw(-1)     -0.0291     0.0420  -0.692    0.489
    D.U(-1)      -0.1331     0.1453  -0.916    0.360
    Constant     41.0526    11.0694   3.709  < 0.001

The header gives the rank, lag order in levels, deterministic terms,
number of series, total data rows, usable observations and the data rows
used in estimation (``p+1`` to ``T``): here 84 rows, of which rows 3 to 84
are used. It also shows the log-likelihood, AIC, BIC and HQ. The
cointegrating relation is ``e + 0.150 prod - 0.247 rw + 3.613 U``.

The largest root is the largest modulus of the companion matrix
eigenvalues after setting aside the *M-r* imposed unit roots. These are
identified as the *M-r* moduli closest to 1, so an explosive root remains
in the comparison. At full rank, all moduli are used.

Each cointegrating relation has a beta table with named rows. The first
*r* rows of beta are fixed to the identity by the normalization; their
standard error, z and p-value are shown as ``-``.

Each differenced equation has its own table. Rows are shown in this order:
loadings on the cointegrating relations, lagged differences, unrestricted
constant and trend, your regressors, then seasonal columns. Only terms
present in the fitted model appear. Regressors use their column names when
available, or numbered labels; seasonal columns have numbered labels.

The columns are coefficient, standard error, z and p-value. The z statistic
is the coefficient divided by its standard error; p-values are two-sided
standard-normal probabilities. Standard errors for the loadings, lagged
differences, unrestricted deterministic terms and regressors are conditional
on the estimated beta. They use ``sigma_u``, with divisor ``n_obs = T-p``
for the residual cross-products, and no degrees-of-freedom correction.

Choose the rank with the Johansen test first
++++++++++++++++++++++++++++++++++++++++++++

::

    struct johansenResult jt;
    jt = johansenTest(y, p=2, det_case=3);

    struct vecmResult vr;
    vr = vecmFit(y, jt.rank, p=2, det_case=3);

Remarks
-------

**Model.** With :math:`y_t` the *M* series in row *t*,

.. math::

   \Delta y_t = \alpha \beta' y_{t-1} + \sum_{i=1}^{p-1} \Gamma_i \Delta y_{t-i}
   + \text{deterministic terms} + u_t .

:math:`\beta` (``vr.beta``) holds the *r* cointegrating relations,
:math:`\alpha` (``vr.alpha``) the speed at which each series adjusts to them,
and :math:`\Gamma_i` (``vr.Gamma``, or :func:`vecmGamma`) the short-run
dynamics. :math:`\beta` is normalized so that its first *r* rows are the
identity matrix.

**Deterministic terms.**

=== ============================================================================
1   No constant and no trend.
2   A constant inside the cointegrating relations only. ``vr.beta`` has M+1 rows; the last row is the constant.
3   An unrestricted constant: the levels can have linear trends. (Default)
4   An unrestricted constant and a linear trend inside the cointegrating relations. ``vr.beta`` has M+1 rows; the last row is the trend coefficient.
5   An unrestricted constant and an unrestricted linear trend.
=== ============================================================================

In case 4 the trend inside the cointegrating relations equals the row number
of the lagged levels: in the equation for data row *t* it is *t-1*, with the
first data row numbered 1. In case 5 the unrestricted trend is the data row
number *t* itself.

``vr.phi_det`` holds the coefficients of the unrestricted constant (cases 3
and 4) or of the unrestricted constant and trend (case 5). The constant of
case 2 and the trend coefficient of case 4 are the last row of ``vr.beta``.

**Seasonal dummies and your own regressors.** The seasonal dummies are
centered: a column equals :math:`1 - 1/s` in its own season and :math:`-1/s`
otherwise, with *s* = *season*. Data row *i* is in season
:math:`((i-1) \bmod s) + 1`. Columns of ``ctl.xreg`` enter every equation
unrestricted. ``vr.phi_exo`` holds the coefficients, your regressors first,
then the seasonal dummies.

A fit with seasonal dummies or your own regressors can be passed to
:func:`vecmIrf`, :func:`vecmDiagnostics` and :func:`vecmToVar`.
:func:`vecmForecast`, :func:`vecmBetaTest`, :func:`vecmAlphaTest` and
:func:`vecmBootstrap` do not accept it.

**Residual covariance.** ``vr.sigma_u`` is the maximum likelihood estimate
:math:`\hat U'\hat U / T`, with *T* the number of rows used in estimation. It
is not divided by the residual degrees of freedom, unlike the default of
:func:`varFit`.

**Information criteria.** With *K* the number of free coefficients of the
model (the covariance matrix is not counted),

.. math::

   \text{AIC} = \ln|\hat\Sigma_u| + \frac{2K}{T}, \qquad
   \text{BIC} = \ln|\hat\Sigma_u| + \frac{K \ln T}{T}, \qquad
   \text{HQ} = \ln|\hat\Sigma_u| + \frac{2K \ln\ln T}{T},

   K = r(2M - r) + r\,d_r + M^2(p-1) + M(d_u + n_x),

where :math:`d_r` is 1 in cases 2 and 4 (the term inside the relations),
:math:`d_u` is the number of unrestricted deterministic terms (0, 0, 1, 1, 2
in cases 1 to 5) and :math:`n_x` the number of seasonal dummies and
regressors. Compare criteria only between fits that use the same rows.

**Full rank.** With *r* = *M* the model is a VAR in levels written in
error-correction form.

**Data requirements.** *y* must have no missing values. The number of rows
used in estimation, *T - p*, must be at least *k + M*, where *k* counts the
coefficients in one equation of the full-rank model: the lagged differences,
unrestricted deterministic terms, seasonal dummies and your own regressors,
plus the number of rows of ``vr.beta``. With fewer rows the error covariance
is singular and the fit is refused, whatever the rank. For example, four
series with *p* = 2 and *det_case* = 3 have *k* = 4 + 1 + 4 = 9, so they need
13 rows in estimation, or 15 rows of data.
A series that is an exact or near-exact linear combination of the others is
refused. The units of the series do not matter: a series in billions next
to one in percent is fine.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`johansenTest`, :func:`vecmAuto`, :func:`vecmForecast`, :func:`vecmIrf`, :func:`vecmDiagnostics`, :func:`vecmBetaTest`, :func:`vecmAlphaTest`
