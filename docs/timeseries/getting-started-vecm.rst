.. _getting-started-vecm:

Getting Started: VECM
=====================

A vector error correction model (VECM) is for series that wander
individually but move together in the long run: they are cointegrated. This
guide goes through one analysis from start to finish: choose the number of
cointegrating relations, estimate the model, check it, test hypotheses on
it, forecast, and compute impulse responses.

The data are four quarterly Canadian series, 1980Q1 to 2000Q4: employment
(``e``), labor productivity (``prod``), the real wage (``rw``) and the
unemployment rate (``U``).

Quick Example
-------------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmAuto(y, p=2);              // choose the rank, then estimate

    struct forecastResult fc;
    fc = vecmForecast(vr, 8);           // 8 quarters ahead, 95% intervals

    struct irfResult ir;
    ir = vecmIrf(vr, 20);               // impulse responses of the levels

Step 1: Load the data in levels
-------------------------------

Pass the series in levels, not in differences. The procedures take the
differences they need.

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

Two settings are yours to choose and are used by every step:

- *p*, the lag order of the model written in levels. The VECM then has
  *p-1* lagged differences. This guide uses ``p=2``.
- *det_case*, the deterministic terms. The default, 3, has an unrestricted
  constant and suits series with linear trends. See :func:`vecmFit` for the
  five cases.

If the input dataframe includes one date-typed column, ``vecmFit`` and
``vecmAuto`` keep that calendar and ``vecmForecast`` supplies the following
periods in ``fc.forecast_dates``. Use ``freq=`` for irregular dates or fewer
than three dates. An undated input keeps empty date members. Dates never
set the seasonal phase: data row 1 remains season 1.

Step 2: Choose the cointegrating rank
-------------------------------------

::

    struct johansenResult jt;
    jt = johansenTest(y, p=2, det_case=3);

::

    Johansen Cointegration Test
    ================================================================================
    Det. case 3: Unrestricted constant
    Lags: 2        Variables: 4        Obs: 82 (84 rows)

    H0: rank      Eigenvalue    Trace Stat           10%            5%            1%       P value
    ----------------------------------------------------------------------------------------------
    r <= 0            0.4386       75.9321       44.4932       47.8564       54.6847       <0.0001
    r <= 1            0.2128       28.5952       27.0660       29.7976       35.4657        0.0683
    r <= 2            0.1001        8.9711       13.4295       15.4948       19.9396        0.3681
    r <= 3            0.0039        0.3227        2.7055        3.8415        6.6349        0.5700

    H0: rank      Eigenvalue      Max Stat           10%            5%            1%       P value
    ----------------------------------------------------------------------------------------------
    r = 0             0.4386       47.3369       25.1238       27.5856       32.7171       <0.0001
    r = 1             0.2128       19.6241       18.8925       21.1323       25.8613        0.0802
    r = 2             0.1001        8.6483       12.2969       14.2644       18.5193        0.3166
    r = 3             0.0039        0.3227        2.7055        3.8415        6.6349        0.5700

    Selected rank (trace, 5%): 1

Read the trace table from the top: reject a rank while its statistic exceeds
the 5% critical value and stop at the first rank that is not rejected. For
these data, ``jt.rank`` is 1.

The critical values describe the asymptotic distribution.
:func:`vecmBootstrap` also gives a bootstrap p-value for the trace test:

::

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    struct bootstrapResult boot;
    boot = vecmBootstrap(vr, r0=0, quiet=1);
    print "p-value, rank 0:         " boot.p_value;
    boot = vecmBootstrap(vr, r0=1, quiet=1);
    print "p-value, rank at most 1: " boot.p_value;

Compare each returned p-value with the chosen significance level. The
bootstrap does not check the roots of the fit under the tested rank; see
:func:`vecmBootstrap` before interpreting it.

Step 3: Estimate the model
--------------------------

::

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3);

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

- ``vr.beta`` estimates the long-run relation, normalized on employment
  (the first series).
- ``vr.alpha`` says how each series reacts when that relation is away from
  its long-run value. The coefficient sign and size depend on the normalization
  and the units of each series.
- ``vr.Gamma`` holds the short-run dynamics; ``vr.alpha_se`` and
  ``vr.beta_se`` hold standard errors. ``vr.Gamma_se`` holds standard errors
  for the lagged differences.

:func:`vecmAuto` does steps 2 and 3 in one call.

Step 4: Check the residuals
---------------------------

::

    struct diagResult d;
    d = vecmDiagnostics(vr);

This tests the residuals for autocorrelation, non-normality and changing
variance. Autocorrelation left in the residuals usually means *p* is too
small. See :func:`vecmDiagnostics`.

Step 5: Test hypotheses
-----------------------

Does unemployment belong in the long-run relation? Under the hypothesis the
relation involves the first three series only:

::

    h_mat = { 1 0 0,
              0 1 0,
              0 0 1,
              0 0 0 };

    struct lrTestResult test;
    test = vecmBetaTest(vr, h_mat);
    print test.lr_stat test.df test.p_value;

Does productivity react to the relation at all?

::

    print "";
    test = vecmAlphaTest(vr, 2);
    print test.lr_stat test.df test.p_value;

Compare ``test.p_value`` with 0.05 for a test at the 5% level.

Step 6: Forecast
----------------

::

    struct forecastResult fc;
    fc = vecmForecast(vr, 8);

::

    VECM forecast
    ================================================================================
    8 steps ahead, 95% prediction intervals

    h      e  Lower 95%  Upper 95%   prod  Lower 95%  Upper 95%     rw  Lower 95%  Upper 95%      U  Lower 95%  Upper 95%
    ---------------------------------------------------------------------------------------------------------------------
    1  962.3      961.6      963.1  417.2      416.0      418.5  470.1      468.6      471.6  6.639      6.088      7.190
    2  962.9      961.4      964.3  417.6      415.7      419.5  470.6      468.5      472.7  6.463      5.499      7.428
    3  963.4      961.2      965.6  418.0      415.5      420.4  471.1      468.4      473.7  6.293      4.923      7.663
    4  964.0      961.1      966.8  418.3      415.4      421.2  471.6      468.4      474.7  6.108      4.366      7.851
    5  964.6      961.1      968.1  418.7      415.4      422.0  472.1      468.5      475.7  5.921      3.854      7.988
    6  965.2      961.1      969.2  419.0      415.4      422.6  472.7      468.5      476.8  5.736      3.397      8.075
    7  965.7      961.2      970.3  419.3      415.4      423.3  473.3      468.6      477.9  5.556      2.996      8.117
    8  966.3      961.4      971.3  419.7      415.4      423.9  473.9      468.6      479.1  5.384      2.648      8.120

    Intervals include shocks only.

The forecasts are of the levels. The intervals reflect future shocks; they
do not include the uncertainty of the estimated coefficients.

Step 7: Impulse responses
-------------------------

::

    struct irfResult ir;
    ir = vecmIrf(vr, 20);

::

    Impulse responses: Cholesky (recursive) identification
    ================================================================================
    Model             VECM, rank 1
    Shock size        one standard deviation
    Horizons          0 to 20

    Responses to e shock (point estimates)
    h              e       prod         rw          U
    -------------------------------------------------
    0         0.3743     0.0020    -0.0726    -0.2000
    1         0.6302     0.0282    -0.1691    -0.3758
    2         0.7987     0.0467    -0.1676    -0.4712
    3         0.9058     0.0228    -0.0876    -0.5209
    4         0.9623    -0.0243     0.0390    -0.5358
    5         0.9797    -0.0858     0.1956    -0.5238
    6         0.9679    -0.1557     0.3681    -0.4929
    7         0.9354    -0.2291     0.5456    -0.4494
    8         0.8890    -0.3023     0.7198    -0.3984
    9         0.8343    -0.3723     0.8848    -0.3439
    10        0.7757    -0.4374     1.0369    -0.2890
    11        0.7165    -0.4965     1.1737    -0.2358
    12        0.6591    -0.5488     1.2940    -0.1860
    13        0.6052    -0.5942     1.3977    -0.1406
    14        0.5561    -0.6328     1.4853    -0.1001
    15        0.5122    -0.6650     1.5577    -0.0648
    16        0.4739    -0.6912     1.6164    -0.0346
    17        0.4411    -0.7122     1.6628    -0.0093
    18        0.4136    -0.7284     1.6984     0.0115
    19        0.3910    -0.7406     1.7248     0.0282
    20        0.3728    -0.7494     1.7434     0.0412

    (The responses to the prod, rw and U shocks follow in three tables of the same form.)

The responses are of the levels of the series to one-standard-deviation
shocks, identified recursively in the order of the columns of *y*. In a
cointegrated system a shock can move the levels permanently, so the
responses need not return to zero.

Quarterly Denmark example
-------------------------

The Denmark data of Johansen and Juselius (1990) contain log real money
(``LRM``), log real income (``LRY``), the bond rate (``IBO``) and the deposit
rate (``IDE``), in that order. This example uses two lags in levels, a
constant inside the cointegrating relation (case 2), and centered quarterly
dummies. The first data row is season 1.

For this specification, the trace test does not reject rank zero at 5%:
the statistic is 49.1444 against a critical value of 54.0779, with P value
0.1282. The maximum-eigenvalue test does reject rank zero: 30.0875 against
28.5876, with P value 0.0319. The two tests therefore give different evidence
at this step. This example uses rank one, the choice of Johansen and
Juselius (1990) for these data. Inspect the rank tests and residual
diagnostics before using the forecasts.

::

    new;
    library timeseries;
    struct johansenResult denmark_rank;
    struct johansenResult denmark_max;
    struct vecmResult denmark_fit;
    struct diagResult denmark_diag;
    struct lrTestResult deposit_test;
    struct lrTestResult income_test;
    struct forecastResult denmark_fc;

    denmark_data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/vecm_family_denmark.csv"));
    denmark_rank = johansenTest(denmark_data, p=2, det_case=2, season=4);
    denmark_max = johansenTest(denmark_data, p=2, det_case=2, season=4, test_type="max");
    denmark_fit = vecmFit(denmark_data, 1, p=2, det_case=2, season=4);
    denmark_diag = vecmDiagnostics(denmark_fit);

    // Exclude IDE while allowing LRM, LRY, IBO and the restricted constant.
    money_h = { 1 0 0 0,
                0 1 0 0,
                0 0 1 0,
                0 0 0 0,
                0 0 0 1 };
    deposit_test = vecmBetaTest(denmark_fit, money_h);

    // Test whether income does not adjust to the cointegrating relation.
    income_test = vecmAlphaTest(denmark_fit, 2);

    denmark_fc = vecmForecast(denmark_fit, 8, level=0.95);

``deposit_test`` tests whether the deposit rate can be excluded from the
relation. ``income_test`` tests whether real income is weakly exogenous for
the cointegrating vector. Compare each returned ``p_value`` with the chosen
significance level; failure to reject does not establish the hypothesis.
The seasonal coefficients remain unrestricted in both tests.

``denmark_fc.forecasts`` contains eight rows of level forecasts, in the
same four-column order as the data. ``denmark_fc.lower`` and
``denmark_fc.upper`` hold the corresponding 95% bounds. The 55 data rows end
in season 3, so the forecast begins in season 4. Future seasonal dummies are
constructed automatically. The intervals include future shocks only.
User regressors in ``ctl.xreg`` remain unavailable in these three procedures;
:func:`vecmBootstrap` also remains unavailable for seasonal fits.

What Next
---------

- :func:`vecmFit` documents the model, the deterministic cases, seasonal
  dummies and the contents of the result.
- :func:`johansenTest` documents the statistics and critical values.
- :func:`vecmToVar` writes the fitted model as a VAR in levels.

.. seealso:: Functions :func:`johansenTest`, :func:`vecmFit`, :func:`vecmAuto`, :func:`vecmDiagnostics`, :func:`vecmBetaTest`, :func:`vecmAlphaTest`, :func:`vecmBootstrap`, :func:`vecmForecast`, :func:`vecmIrf`, :func:`vecmToVar`

References
----------

- Johansen, S. and K. Juselius (1990). Maximum likelihood estimation and
  inference on cointegration, with applications to the demand for money.
  *Oxford Bulletin of Economics and Statistics*, 52(2), 169-210.
  `doi:10.1111/j.1468-0084.1990.mp52002003.x <https://doi.org/10.1111/j.1468-0084.1990.mp52002003.x>`_.
