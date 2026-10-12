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

Step 2: Choose the cointegrating rank
-------------------------------------

::

    struct johansenResult jt;
    jt = johansenTest(y, p=2, det_case=3);

::

    ================================================================================
    Johansen Cointegration Test
    Det. case 3: Unrestricted constant
    Lags: 2        Variables: 4        Obs: 84
    ================================================================================
    H0: rank      Eigenvalue    Trace Stat           10%            5%            1%
    --------------------------------------------------------------------------------
    r <= 0            0.4386       75.9321       44.4929       47.8545       54.6815
    r <= 1            0.2128       28.5952       27.0669       29.7961       35.4628
    r <= 2            0.1001        8.9711       13.4294       15.4943       19.9349
    r <= 3            0.0039        0.3227        2.7055        3.8415        6.6349

    H0: rank      Eigenvalue      Max Stat           10%            5%            1%
    --------------------------------------------------------------------------------
    r =  0            0.4386       47.3369       25.1236       27.5858       32.7172
    r =  1            0.2128       19.6241       18.8928       21.1314       25.8650
    r =  2            0.1001        8.6483       12.2971       14.2639       18.5200
    r =  3            0.0039        0.3227        2.7055        3.8415        6.6349

    Selected rank (trace, 5%): 1
    ================================================================================

Read the trace table from the top: rank 0 is rejected at 5% (75.93 is above
47.85), rank at most 1 is not (28.60 is below 29.80). The selected rank,
``jt.rank``, is 1.

With a short sample the critical values can be unreliable.
:func:`vecmBootstrap` gives a bootstrap p-value for the same test:

::

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    struct bootstrapResult boot;
    boot = vecmBootstrap(vr, r0=0, quiet=1);
    print "p-value, rank 0:         " boot.p_value;       // 0.004
    boot = vecmBootstrap(vr, r0=1, quiet=1);
    print "p-value, rank at most 1: " boot.p_value;       // 0.352

It agrees here: rank 0 is rejected, rank 1 is not.

Step 3: Estimate the model
--------------------------

::

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3);

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

- ``vr.beta`` is the long-run relation: ``e + 0.150 prod - 0.247 rw + 3.613 U``
  is stationary.
- ``vr.alpha`` says how each series reacts when that relation is away from
  its mean. The real wage has the largest coefficient (-0.182).
- ``vr.Gamma`` holds the short-run dynamics; ``vr.alpha_se`` and
  ``vr.beta_se`` hold standard errors.

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
    print test.lr_stat test.df test.p_value;      // 5.058  1  0.0245

Does productivity react to the relation at all?

::

    test = vecmAlphaTest(vr, 2);
    print test.lr_stat test.df test.p_value;      // 5.481  1  0.0192

Both hypotheses are rejected at the 5% level.

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

The responses are of the levels of the series to one-standard-deviation
shocks, identified recursively in the order of the columns of *y*. In a
cointegrated system a shock can move the levels permanently, so the
responses need not return to zero.

What Next
---------

- :func:`vecmFit` documents the model, the deterministic cases, seasonal
  dummies and the contents of the result.
- :func:`johansenTest` documents the statistics and critical values.
- :func:`vecmToVar` writes the fitted model as a VAR in levels.

.. seealso:: Functions :func:`johansenTest`, :func:`vecmFit`, :func:`vecmAuto`, :func:`vecmDiagnostics`, :func:`vecmBetaTest`, :func:`vecmAlphaTest`, :func:`vecmBootstrap`, :func:`vecmForecast`, :func:`vecmIrf`, :func:`vecmToVar`
