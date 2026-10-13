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

   :param season: Optional keyword, number of seasons per year (4 for quarterly data, 12 for monthly). Adds ``season-1`` centered seasonal dummies. 0 or 1 = none. Default = 0.
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

    ================================================================================
    VECM(2)     Rank: 1                                     Variables:             4
    Method: Johansen ML                                  Observations:            84
    Det. case 3: Unrestricted constant                                            82
    ================================================================================
    AIC:            -6.056          BIC:            -5.264          HQ:             -5.738
    Log-Lik:       -190.12
    ================================================================================

    Cointegrating vectors (beta, Johansen normalization):

        1.0000
        0.1503
       -0.2465
        3.6128

    Adjustment coefficients (alpha):
    CE1:
      e               0.0132
      prod            0.0666
      rw             -0.1817
      U              -0.0438

    ================================================================================
    Short-run dynamics (Gamma):

        0.7656     0.1651    -0.0236     0.1421
       -0.2986     0.1479     0.1232    -0.8435
       -0.1962    -0.0437    -0.0570     0.4351
       -0.5846    -0.0731    -0.0291    -0.1331

    Companion eigenvalues: max modulus =  1.000
    ================================================================================

The header shows 84 rows of data and 82 rows used in estimation (84 minus
*p*). The cointegrating relation is ``e + 0.150 prod - 0.247 rw + 3.613 U``.
The last line reports the largest modulus among the eigenvalues of the
companion matrix of the model written as a VAR in levels; a model with rank
*r* has at least *M-r* of them equal to 1.

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
used in estimation, *T - p*, must be at least the larger of *Mp + 1* and the
following sum: the number of lagged differences, unrestricted deterministic
terms, seasonal dummies and your own regressors in one equation, plus the
number of rows of ``vr.beta``.
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
