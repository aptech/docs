GARCH: Moving from TSMT 4.1
===========================

GARCH estimation is now part of the GAUSS Time Series package
(``library timeseries``). This page is for TSMT 4.1 users: it shows how
each TSMT 4.1 call and setting carries over, and how to compare results.

What you gain:

- Orders by keyword, ``garch=`` and ``arch=``, so the two orders cannot be
  mixed up.
- AR terms and regressors in the mean, by keyword or with a formula string.
- :func:`garchForecast` for variance, volatility and mean forecasts, with
  dates.
- Hessian and robust standard errors side by side, with OPG on request.
- A status code and a message for every fit, and ``on_error="return"`` to
  keep going in a loop over many series.
- :func:`garchDiagnostics` for the ARCH-LM and sign-bias tests.

Load one library per program
----------------------------

Change ``library tsmt;`` to ``library timeseries;``. If TSMT 4.1 is also
installed, load only one of the two libraries in a program: :func:`garchFit`,
:func:`garchControlCreate` and the :class:`garchControl` structure have the
same names in both, with different arguments and members.

Procedures
----------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - TSMT 4.1
     - GAUSS 27
   * - ``garchFit(y, p, q)``
     - ``garchFit(y, garch=p, arch=q)`` (``garchFit(y, p, q)`` still works)
   * - ``garchFit(y, x, p, q)``
     - ``garchFit(y, garch=p, arch=q, x=X)``
   * - ``garchFit(dataset, formula, p, q)``
     - ``garchFit(df, formula, garch=p, arch=q)``
   * - ``garchGJRFit(y, 1, 1)``
     - ``garchFit(y, garch=1, arch=1, model="gjr")``
   * - ``garchMFit``, ``igarchFit``
     - Not in GAUSS 27.0
   * - (none)
     - :func:`garchForecast`, :func:`garchDiagnostics`, :func:`garchResults`

GARCH-in-mean, IGARCH, the skewed *t* distribution, GED errors and EGARCH
are planned for a later 27.x release.

Order arguments
---------------

By position, the GARCH order still comes first: ``garchFit(y, 2, 1)`` is
GARCH order 2 and ARCH order 1, as in TSMT 4.1. The examples use the
keywords ``garch=`` and ``arch=``, which say which is which. Give each order
once: ``garchFit(y, 1, 1, garch=1)`` is refused, even though the values
agree.

The second argument is now always the GARCH order. A matrix there, as in the
TSMT 4.1 call ``garchFit(y, x, p, q)``, is refused with a message that says
to give the regressors as ``x=``.

GJR in GAUSS 27 is fitted with ``garch=1, arch=1``.

Control structure
-----------------

Set options as keywords to :func:`garchFit`, or in a :class:`garchControl`
structure from :func:`garchControlCreate`. The members are new:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - TSMT 4.1 member
     - GAUSS 27
   * - ``gctl.density = 0`` (normal), ``1`` (*t*)
     - ``dist="normal"`` (default), ``dist="t"``
   * - ``gctl.density = 3`` (skewed generalized *t*)
     - Planned for 27.x
   * - ``gctl.asymmetry``
     - ``model="gjr"``
   * - ``gctl.inmean``
     - Planned for 27.x (GARCH-in-mean)
   * - ``gctl.stConstraintsType``
     - No setting: the persistence is always kept below 1
   * - ``gctl.cvConstraintsType``
     - No setting: the coefficients are always kept so that the variance is
       positive (for GJR, :math:`\alpha \ge 0` and :math:`\alpha + \gamma \ge 0`)
   * - ``gctl.covType`` (1 ML, 2 QML, 3 none)
     - Hessian (ML) and robust (QML) standard errors are both shown;
       ``covariance="none"`` for none, ``covariance="opg"`` to add OPG
   * - ``gctl.start``
     - No setting: starting values are chosen by :func:`garchFit`
   * - ``gctl.sqpsolvemtControlProc``, ``gctl.cmlmtControlProc``
     - ``ctl.max_iter`` and ``ctl.tol``

The constant mean is still the default. ``mean_model="zero_mean"`` fits
without it.

Results
-------

TSMT 4.1 returned a ``garchEstimation`` structure; GAUSS 27 returns a
:class:`garchResult`. Mind the names: in TSMT 4.1 *beta* was the regression
coefficients and *garch* the GARCH coefficients; in GAUSS 27 *beta* is the
GARCH coefficients.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - TSMT 4.1
     - GAUSS 27
   * - ``beta0`` in ``gOut.par``
     - ``result.mu``
   * - ``beta`` in ``gOut.par`` (regressors)
     - ``result.x_coefs``, named by ``result.x_names``
   * - ``garch`` in ``gOut.par``
     - ``result.beta``
   * - ``arch`` in ``gOut.par``
     - ``result.alpha``
   * - ``omega`` in ``gOut.par``
     - ``result.omega``
   * - ``tau`` in ``gOut.par`` (GJR)
     - ``result.gamma``
   * - *t* degrees of freedom in ``gOut.par``
     - ``result.nu``
   * - ``gOut.lrs``
     - ``result.loglik`` (the log likelihood itself, not twice it)
   * - ``gOut.aic``, ``gOut.bic``
     - ``result.aic``, ``result.bic``, with :math:`-2 \log L + 2k` and
       :math:`-2 \log L + k \ln n`
   * - ``gOut.moment``
     - ``result.covariance_hessian``, ``result.covariance_robust`` and
       ``result.covariance_opg``
   * - ``gOut.climits``
     - The limit columns of ``result.parameter_table``
   * - ``gOut.retcode``
     - ``result.status`` and ``result.status_message``
   * - ``gOut.numObs``
     - ``result.n``; ``result.effective_nobs`` is the number in the likelihood

``result.parameter_table`` is a dataframe with one row per parameter:
estimate, both standard errors, robust p-value and limits.

Start-up rule and how to compare with TSMT 4.1
----------------------------------------------

The recursion for the conditional variance needs values before the first
observation. The GAUSS 27 default, ``init_policy="sample_variance_presample"``,
sets the pre-sample variance and squared residual to the mean squared
residual. TSMT 4.1 instead set the first conditional variance to the mean
squared residual; ``init_policy="sample_variance"`` does the same. TSMT 4.1
also left the first observation out of the log likelihood it maximized and
printed, while GAUSS 27 includes every observation. So with
``init_policy="sample_variance"`` the estimates are close to those of TSMT
4.1 but not identical. :func:`garchFit` lists every start-up rule.

TSMT 4.1 printed *LRS*, twice the log likelihood, and *AIC* as
:math:`2 \log L + 2k`; GAUSS 27 prints the log likelihood and
:math:`\text{AIC} = -2 \log L + 2k`. To compare a TSMT 4.1 fit with a GAUSS 27 fit,
compare log likelihoods (*LRS*/2 in TSMT 4.1), not the printed AIC.

Standard errors
---------------

TSMT 4.1 computed one covariance matrix, chosen by ``gctl.covType``, and
printed confidence limits. GAUSS 27 prints two standard errors for each
parameter: from the Hessian (*SE_Hessian*, the maximum-likelihood standard
errors) and robust (*SE_Robust*, the quasi-maximum-likelihood sandwich), and
computes the p-values and limits from the robust
ones. See :func:`garchFit` for the cases where standard errors are shown with
a warning or not at all.

Example: the same GARCH(1,1) in both
------------------------------------

The 1,974 daily DM/£ returns shipped with the Time Series package
(``dmbp.csv``). In TSMT 4.1.1 (run on GAUSS 26, with a copy of the same
file in the working folder):

::

    new;
    library tsmt;

    dm = loadd("dmbp.csv", "return_pct");

    struct garchEstimation gOut;
    gOut = garchFit(dm, 1, 1);
    print "Log likelihood (LRS/2): " gOut.lrs/2;

::

    ================================================================================
    Model:                   GARCH(1,1)          Dependent variable:      return_pct
    Time Span:                  Unknown          Valid cases:                   1974
    ================================================================================
                                 Coefficient            Upper CI            Lower CI

              beta0[1,1]            -0.00622            -0.02265             0.01020
              garch[1,1]             0.80589             0.73988             0.87190
               arch[1,1]             0.15340             0.10115             0.20565
              omega[1,1]             0.01076             0.00515             0.01637
    ================================================================================

                    AIC:                                                 -2204.76608
                    LRS:                                                 -2212.76608
    Log likelihood (LRS/2):       -1106.3830

In GAUSS 27, with the TSMT 4.1 start-up rule:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/dmbp.csv");
    dm = loadd(fname, "return_pct");

    struct garchResult fit;
    fit = garchFit(dm, garch=1, arch=1, init_policy="sample_variance");

::

    ================================================================================
    GARCH Family Model Results
    ================================================================================
    Model:        GARCH(1,0,1)
    Mean model:   constant_mean
    Distribution: normal
    Observations: 1974
    Log likelihood: -1106.59
    AIC: 2221.17    BIC: 2243.52

    Parameters on the original data scale

           Parameter         Estimate       SE_Hessian        SE_Robust  P_Robust_Normal Lower_95_Robust_ Upper_95_Robust_
                  mu    -0.0061844102     0.0084616074     0.0091876592       0.50087005     -0.024191891      0.011823071
               omega      0.010760272     0.0028530142     0.0064948616      0.097572843    -0.0019694232      0.023489966
              alpha1       0.15340746      0.026581406      0.053659273     0.0042508874      0.048237215       0.25857770
               beta1       0.80587919      0.033566939      0.072501189    1.0558512e-28       0.66377947       0.94797891
    Inference: available; Hessian and unadjusted score sandwich; robust normal p-values and limits
    Initialization: sample_variance
    P-values and limits: robust asymptotic normal, level=0.95

    Optimizer: lbfgsb_tight_repolish; projected_gradient_at_or_below_pgtol
    Iterations: 9; function evaluations: 11
    Projected-gradient norm: 2.79045e-05 (requested 0.0001)
    Persistence: 0.959287 (admissible)

All four estimates agree to four decimals: *mu* -0.0062 (TSMT *beta0*),
*omega* 0.0108, *alpha* 0.1534 (TSMT *arch*) and *beta* 0.8059 (TSMT
*garch*). At the five decimals TSMT 4.1 printed, *omega* is the same, *alpha*
and *beta* differ in the last digit, and *mu* is -0.00622 in TSMT 4.1 against
-0.00618 in GAUSS 27: the first observation, which only GAUSS 27 includes in
the likelihood, moves the estimate of the mean slightly. The first
observation's term is about -0.20, which is most of the difference between
the two printed log likelihoods: -1106.38 over observations 2 to 1,974 in
TSMT 4.1, -1106.59 over all 1,974 in GAUSS 27.

Without ``init_policy``, GAUSS 27 uses its default start-up rule and prints
log likelihood -1106.61 for this model (see the first example on the
:func:`garchFit` page).

.. seealso:: Functions :func:`garchFit`, :func:`garchForecast`, :func:`garchControlCreate`, :func:`garchResults`, :func:`garchDiagnostics`
