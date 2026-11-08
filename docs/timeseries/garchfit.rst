garchFit
========

Purpose
-------
Fit a GARCH(p,q) or GJR-GARCH(1,1) model of the conditional variance, with
normal or Student's *t* errors. The mean can be a constant, zero, or a
regression on AR terms and other variables. Use :func:`garchForecast` to
forecast the variance and the mean from the fit.

Format
------

.. function:: result = garchFit(y)
              result = garchFit(y, garch=1, arch=1)
              result = garchFit(y, p, q)
              result = garchFit(y, model="gjr")
              result = garchFit(y, ar=1, x=X)
              result = garchFit(df, formula, ar=1)
              result = garchFit(y, ctl=ctl)

   :param y: the series, for example percentage returns. A dataframe may
             also hold one date column; the dates label the forecasts of
             :func:`garchForecast`. With a *formula*, a dataframe (or the
             name of a dataset) that holds *y*, the regressors and,
             optionally, one date column.
   :type y: Nx1 vector or dataframe

   :param formula: Optional, ``"y ~ x1 + x2"``: *y* on the left of ``~`` and
                   the regressors on the right, read as :func:`loadd` reads a
                   formula string. ``"y ~ ."`` uses every other column,
                   ``"y ~ . - date"`` every other column except *date*, and
                   ``"y ~ ln(x1) + x2"`` a transformed column. The mean has a
                   constant unless the formula drops it with ``- 1``, which is
                   the same as ``mean_model="zero_mean"``. With a formula, give
                   the orders as *garch* and *arch*.
   :type formula: string

   :param garch: Optional keyword, GARCH order: the number of lagged
                 variances (*beta* terms). Default = 1.
   :type garch: positive integer scalar

   :param arch: Optional keyword, ARCH order: the number of lagged squared
                residuals (*alpha* terms). Default = 1.
   :type arch: positive integer scalar

   :param p: Optional, the GARCH order by position. ``garchFit(y, 2, 1)`` is
             GARCH order 2, ARCH order 1. Give each order once, by position
             or by keyword: giving it both ways stops :func:`garchFit`, even
             when the two values agree. Default = 1.
   :type p: positive integer scalar

   :param q: Optional, the ARCH order by position. Default = 1.
   :type q: positive integer scalar

   :param model: Optional keyword, ``"garch"`` or ``"gjr"``. GJR adds a term
                 for negative residuals; it is fitted with
                 ``garch=1, arch=1``. Default = ``"garch"``.
   :type model: string

   :param dist: Optional keyword, error distribution: ``"normal"`` or
                ``"t"`` (Student's *t* scaled to variance 1, with estimated
                degrees of freedom). Default = ``"normal"``.
   :type dist: string

   :param mean_model: Optional keyword, ``"constant_mean"`` or
                      ``"zero_mean"``. Default = ``"constant_mean"``.
   :type mean_model: string

   :param ar: Optional keyword, number of AR terms in the mean,
              :math:`y_{t-1}, \ldots, y_{t-r}`. The first *ar* rows only
              supply lags; the likelihood uses rows *ar* + 1 to N. Default =
              0.
   :type ar: nonnegative integer scalar

   :param x: Optional keyword, regressors in the mean, one row per row of
             *y*. The column names of a dataframe label the coefficients.
             Default = none.
   :type x: NxK matrix or dataframe

   :param init_policy: Optional keyword, start-up rule: how the variance
                       recursion starts before the first observation.
                       Default = ``"default"``, which is
                       ``"sample_variance_presample"``. See `Start-up rules`_.
   :type init_policy: string

   :param presample_residual: Optional keyword, pre-sample residual for
                              ``init_policy="fixed_presample_state"``.
                              Default = 0.
   :type presample_residual: scalar

   :param presample_state: Optional keyword, pre-sample variance for
                           ``"fixed_presample_state"`` and first variance for
                           ``"explicit_backcast_value"``. Must be positive.
                           Default = 1.
   :type presample_state: scalar

   :param leverage_order: Optional keyword, 0 for GARCH and 1 for GJR. The
                          default, -1, follows *model*; any other value is
                          refused.
   :type leverage_order: scalar

   :param covariance: Optional keyword, ``"both"`` (Hessian and robust
                      standard errors), ``"opg"`` (also
                      outer-product-of-gradients standard errors) or
                      ``"none"`` (no standard errors). Default = ``"both"``.
   :type covariance: string

   :param level: Optional keyword, level of the parameter limits. Default =
                 0.95.
   :type level: scalar strictly between 0 and 1

   :param quiet: Optional keyword, 1 to suppress the printed summary.
                 Default = 0.
   :type quiet: scalar

   :param on_error: Optional keyword, ``"stop"`` ends the program when the
                    fit is refused; ``"return"`` returns the result with
                    *status* and *status_message* set. Default = ``"stop"``.
   :type on_error: string

   :param ctl: Optional :class:`garchControl` structure. Create one with
               :func:`garchControlCreate`. A keyword that is given overrides
               the matching member for this call; *ctl* itself is not
               changed. *ctl.max_iter* and *ctl.tol* are set only here.

       .. include:: include/garchcontrol.rst

   :type ctl: struct

   :return result: A :class:`garchResult` structure containing:

       .. include:: include/garchresult.rst

   :rtype result: struct

Model
-----

The mean equation is

.. math::

   y_t = \mu + \phi_1 y_{t-1} + \cdots + \phi_r y_{t-r} + x_t'\delta + \varepsilon_t,
   \qquad \varepsilon_t = \sigma_t z_t,

where :math:`\mu` is left out with ``mean_model="zero_mean"``, the AR terms
are present with ``ar=r``, and :math:`x_t'\delta` with *x* or a formula. The
:math:`z_t` are independent with mean 0 and variance 1: standard normal, or
Student's *t* with :math:`\nu` degrees of freedom scaled to variance 1. The
degrees of freedom are estimated between 2.05 and 500.

A GARCH(p,q) model has the conditional variance

.. math::

   \sigma_t^2 = \omega + \sum_{i=1}^{q} \alpha_i \varepsilon_{t-i}^2
              + \sum_{j=1}^{p} \beta_j \sigma_{t-j}^2 ,

with *p* the GARCH order (*garch*) and *q* the ARCH order (*arch*). The fit
keeps :math:`\omega > 0`, :math:`\alpha_i \ge 0`, :math:`\beta_j \ge 0` and
the persistence :math:`\sum \alpha_i + \sum \beta_j` below 1, so the variance
process is stationary.

GJR-GARCH(1,1) adds a term for negative residuals:

.. math::

   \sigma_t^2 = \omega + (\alpha + \gamma I_{t-1}) \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2,
   \qquad I_{t-1} = 1 \text{ if } \varepsilon_{t-1} < 0, \text{ else } 0.

:math:`\gamma` may be negative. The fit keeps :math:`\alpha \ge 0` and
:math:`\alpha + \gamma \ge 0`, so the variance stays positive after a shock
of either sign, and the persistence :math:`\alpha + \gamma/2 + \beta` below
1.

The printed model name gives the GARCH order, the leverage order and the
ARCH order: GARCH(1,0,1) is a GARCH(1,1) and GJR-GARCH(1,1,1) the GJR model.

The AR coefficients are not constrained. The summary prints the largest
modulus of the AR inverse roots, and :func:`garchFit` prints a warning when
it is 1 or above.

Start-up rules
--------------

The variance recursion needs values for the variance and the squared
residual before the first observation. *init_policy* sets them. With AR
terms, "the first observation" is row *ar* + 1 and the averages below run
over the rows the likelihood uses.

``"sample_variance_presample"`` (the default, also ``"default"``)
   Every pre-sample variance and squared residual equals *v*, the mean
   squared residual at the current mean parameters. For GJR the pre-sample
   negative part is *v*/2. *v* changes with the mean parameters during the
   fit.

``"sample_variance"``
   The first max(*garch*, *arch*) conditional variances are set to *v*,
   and the recursion starts after them. In a GARCH(1,1) the first
   conditional variance is *v* and the recursion starts at the second
   observation, as in TSMT 4.1; see :doc:`garch-from-tsmt`.

``"exponential_backcast"``
   Every pre-sample variance and squared residual equals a weighted average
   of the first 75 squared least-squares residuals, with weights
   proportional to :math:`0.94^j`. It is computed once, before the fit, and
   stays fixed. For GJR the pre-sample negative part is half of it.

Other rules:

``"unconditional_variance"``
   Every pre-sample variance and squared residual equals the unconditional
   variance :math:`\omega / (1 - \text{persistence})` at the current
   parameters (GJR negative part half of it).

``"explicit_backcast_value"``
   The first max(*garch*, *arch*) conditional variances are set to
   *presample_state*, and the recursion starts after them, as
   ``"sample_variance"`` does with *v*. Requires a positive
   *presample_state*.

``"fixed_presample_state"``
   The pre-sample residual is *presample_residual* and the pre-sample
   variance is *presample_state*. Requires a finite *presample_residual*
   and a positive *presample_state*.

The rules give slightly different estimates on the same data, because the
first few variances differ. On the 1,974 daily DM/£ returns of the first
example below, the GARCH(1,1) log likelihood is -1106.6079 under the default
rule, -1106.5866 under ``"sample_variance"`` and -1104.5214 under
``"exponential_backcast"``. :func:`garchForecast` uses the rule of the fit.

Standard errors
---------------

By default the summary shows two standard errors for each parameter: from the
Hessian of the log likelihood (*SE_Hessian*) and robust, from the Hessian
and the scores of each observation (*SE_Robust*, a sandwich estimator
without centering). The p-values and the limits always use the robust
standard errors and the normal distribution. With ``covariance="opg"`` the
table adds outer-product-of-gradients standard errors (*SE_OPG*); the OPG
covariance is stored in *result.covariance_opg* whenever standard errors are
available. No covariance has a small-sample correction.

*result.standard_error_status* says which case applies:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Status
     - Meaning
   * - ``"available"``
     - Standard errors, p-values and limits are computed.
   * - ``"persistence_boundary"``
     - The fitted persistence is within 1e-6 of 1, the edge of the
       stationary region, no other parameter is at a bound, and the Hessian
       can be used. Standard errors, p-values and limits are computed, and a
       warning is printed: they assume a fit inside that region and may be
       unreliable. If the likelihood still rises beyond persistence 1, the
       status is ``"nonregular"`` instead.
   * - ``"nonregular"``
     - The fit is at or very near a bound: :math:`\omega`, an
       :math:`\alpha_i` or a :math:`\beta_j` at 0, :math:`\alpha + \gamma`
       at 0 for GJR, the *t* degrees of freedom at 2.05 or 500, or the
       persistence at 1 when the likelihood still rises beyond it or another
       parameter is also at a bound. The usual standard errors do not apply
       there, so none are given. *result.inference_message* says which case it is: "Persistence
       at 1 and the likelihood still rises beyond it", "alpha1 at 0 and the
       likelihood still rises toward it" (or another parameter, such as
       omega or alpha1 + gamma1), or "Boundary or near-boundary fit" for the
       others.
   * - ``"failed"``
     - The standard errors could not be computed; the fit is kept.
       *result.inference_message* gives the reason: too few observations,
       derivatives that are not finite, a Hessian that is not positive
       definite, a covariance that could not be computed or is not positive
       definite, or a covariance that overflows or underflows on the data
       scale.
   * - ``"skipped"``
     - ``covariance="none"``.
   * - ``"skipped: fit did not converge"``
     - Status 2: no standard errors for a fit that did not converge.
   * - ``"skipped: no fit"``
     - The fit was refused.

With *t* errors, a large fitted *df* (hundreds) means the data say little
about the tails beyond what normal errors describe, and the curvature of the
likelihood in *df* is small and noisy. The *df* standard error is then
unreliable, even though no warning is printed. Consider normal errors for
such a series.

Sample size
-----------

:func:`garchFit` refuses a fit with fewer than 5 observations per estimated
parameter (status 1). A fit on fewer than 100 observations is returned with a
printed warning, even when *quiet* is 1; its status is not changed.

Examples
--------

Fit a GARCH(1,1) and read the table
+++++++++++++++++++++++++++++++++++

The data are 1,974 daily percentage returns of the Deutschmark against the
British pound.

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/dmbp.csv");
    dm = loadd(fname, "return_pct");

    struct garchResult fit;
    fit = garchFit(dm, garch=1, arch=1);

::

    ================================================================================
    GARCH Family Model Results
    ================================================================================
    Model:        GARCH(1,0,1)
    Mean model:   constant_mean
    Distribution: normal
    Observations: 1974
    Log likelihood: -1106.61
    AIC: 2221.22    BIC: 2243.57

    Parameters on the original data scale

           Parameter         Estimate       SE_Hessian        SE_Robust  P_Robust_Normal Lower_95_Robust_ Upper_95_Robust_
                  mu    -0.0061904139     0.0084621193     0.0091893537       0.50053346     -0.024201216      0.011820388
               omega      0.010761404     0.0028527145     0.0064931937      0.097451542    -0.0019650214      0.023487830
              alpha1       0.15313409      0.026522838      0.053531721     0.0042280922      0.048213839       0.25805433
               beta1       0.80597362      0.033552706      0.072461499    9.7190780e-29       0.66395169       0.94799555
    Inference: available; Hessian and unadjusted score sandwich; robust normal p-values and limits
    Initialization: sample_variance_presample
    P-values and limits: robust asymptotic normal, level=0.95

    Optimizer: lbfgsb_tight_repolish; projected_gradient_at_or_below_pgtol
    Iterations: 13; function evaluations: 15
    Projected-gradient norm: 4.01748e-05 (requested 0.0001)
    Persistence: 0.959108 (admissible)

*alpha1* = 0.153 is the response of the variance to yesterday's squared
shock and *beta1* = 0.806 the carry-over of yesterday's variance. Their sum,
the persistence 0.959, sets how slowly a burst of volatility fades. The
robust standard errors are about twice the Hessian ones for *omega*,
*alpha1* and *beta1*, a common sign that the normal distribution does not
describe the tails of the returns. The printed column names are cut to 16
characters; the full names are *Lower_95_Robust_Normal* and
*Upper_95_Robust_Normal*.

Student's t errors
++++++++++++++++++

::

    struct garchResult fit_t;
    fit_t = garchFit(dm, garch=1, arch=1, dist="t");

::

    error : garchFit: Warning: persistence is 1 (within 5.9e-08), the edge of the stationary region. Standard errors, p-values and limits assume a fit inside that region and may be unreliable.

    ...
    Distribution: t
    Observations: 1974
    Log likelihood: -989.774
    AIC: 1989.55    BIC: 2017.49

    Parameters on the original data scale

           Parameter         Estimate       SE_Hessian        SE_Robust  P_Robust_Normal Lower_95_Robust_ Upper_95_Robust_
                  mu     0.0021695146     0.0070002228     0.0068867868       0.75274217     -0.011328340      0.015667369
               omega     0.0027289063     0.0013312932     0.0020056365       0.17363426    -0.0012020691     0.0066598816
              alpha1       0.11708006      0.023961693      0.035825509     0.0010828586      0.046863351       0.18729677
               beta1       0.88291988      0.024493293      0.039377298   2.3986050e-111       0.80574180       0.96009797
                  df        4.3334421       0.41261735       0.41191692    6.9736870e-26        3.5260997        5.1407844
    Inference: persistence_boundary; Persistence at 1 (within 5.9e-08): standard errors, p-values and limits assume a fit inside the stationary region and may be unreliable
    ...
    Persistence: 1 (boundary)

The log likelihood rises by 116.8 for one more parameter, and *df* = 4.3: the
returns have fat tails. Under *t* errors the fitted persistence is 1 to within
6e-8, so the standard errors come with the persistence warning. The
estimates are the highest likelihood the fit finds in the stationary
region, at its edge. The *df* p-value tests *df* = 0, which is outside the
allowed range, so it is not a standard test (see `Remarks`_).

GJR-GARCH
+++++++++

::

    struct garchResult fit_gjr;
    fit_gjr = garchFit(dm, garch=1, arch=1, model="gjr");

The parameter table adds *gamma1*:

::

           Parameter         Estimate       SE_Hessian        SE_Robust  P_Robust_Normal Lower_95_Robust_ Upper_95_Robust_
                  mu    -0.0079045414     0.0086254846     0.0088911853       0.37398629     -0.025330944     0.0095218615
               omega      0.011233224     0.0030186682     0.0070693007       0.11205703    -0.0026223508      0.025088799
              alpha1       0.14049661      0.027771159      0.049551010     0.0045769266      0.043378419       0.23761481
              gamma1      0.028350751      0.028966292      0.043494293       0.51451283     -0.056896496       0.11359800
               beta1       0.80144124      0.034858456      0.077064835    2.4905114e-25       0.65039694       0.95248554

For this exchange rate *gamma1* is small (robust p-value 0.51): there is no
evidence that falls of the Deutschmark move its volatility more than rises. Use
:func:`garchDiagnostics` to test for this asymmetry after a GARCH fit.

AR terms and regressors with a formula
++++++++++++++++++++++++++++++++++++++

The monthly S&P 500 return is regressed on its own lag and two lagged
macroeconomic variables, with GARCH(1,1) errors. The file has a date
column, which :func:`garchFit` stores for :func:`garchForecast`.

::

    fname = getGAUSSHome("pkgs/timeseries/examples/data/garch_sp500_monthly.csv");
    sp = loadd(fname);

    struct garchResult fit_x;
    fit_x = garchFit(sp, "y ~ x1_spread_lag1 + x2_ipgrowth_lag1", ar=1, garch=1, arch=1);

::

    ================================================================================
    GARCH Family Model Results
    ================================================================================
    Model:        GARCH(1,0,1)
    Mean model:   constant_mean
    Mean terms:   AR(1), 2 regressors
    AR inverse roots: largest modulus 0.201978 (below 1, stationary)
    Distribution: normal
    Observations: 802
    Log likelihood: -2114.32
    AIC: 4242.64    BIC: 4275.45

    Parameters on the original data scale

           Parameter         Estimate       SE_Hessian        SE_Robust  P_Robust_Normal Lower_95_Robust_ Upper_95_Robust_
                  mu       0.37893964       0.14724014       0.19464608      0.051557077    -0.0025596571       0.76043894
                 ar1       0.20197845      0.039326237      0.039741250    3.7281777e-07       0.12408704       0.27986987
      x1_spread_lag1       0.17513280      0.077098630      0.092282478      0.057723698    -0.0057375321       0.35600313
    x2_ipgrowth_lag1     -0.029014878       0.14030933       0.13905858       0.83471976      -0.30156469       0.24353493
               omega        1.7095014       0.57211585       0.61838353     0.0057015735       0.49749191        2.9215108
              alpha1       0.14636684      0.039082537      0.068005221      0.031374653      0.013079059       0.27965463
               beta1       0.72389090      0.064741431      0.076324664    2.4386528e-21       0.57429731       0.87348450
    Inference: available; Hessian and unadjusted score sandwich; robust normal p-values and limits
    Initialization: sample_variance_presample
    P-values and limits: robust asymptotic normal, level=0.95

    Optimizer: lbfgsb_tight_repolish; projected_gradient_at_or_below_pgtol
    Iterations: 15; function evaluations: 19
    Projected-gradient norm: 5.54024e-05 (requested 0.0001)
    Persistence: 0.870258 (admissible)

The file has 803 months; the first supplies the lag, so 802 enter the
likelihood. *mu* is the intercept of the mean equation, not the mean return:
with the AR term the mean is *mu* / (1 - *ar1*) when the regressors are 0.

Keep a refused fit and read its message
+++++++++++++++++++++++++++++++++++++++

With ``on_error="return"`` a refusal returns the result with *status* and
*status_message* set, so a loop over many series can record it and go on.

::

    struct garchResult fit_s;
    fit_s = garchFit(dm[1:15], garch=1, arch=1, on_error="return");
    print "status: " fit_s.status;
    print fit_s.status_message;

::

    status:        1.0000000
    garchFit: the series has 15 observations; this model needs at least 20 (5 per estimated parameter, 4 parameters).

Remarks
-------

:func:`garchFit` stores the data of the fit in *result.y*, *result.x* and
*result.dates*. :func:`garchForecast` forecasts from them, so it needs only
the result, the horizon and, for a model with regressors, their future
values.

When the data is a dataframe, one date column is taken as the dates of *y*
and is not part of the series; two or more date columns are refused. With
``"y ~ ."`` the date column must be dropped in the formula
(``"y ~ . - date"``). The dates must increase from row to row.

Each p-value tests whether its parameter is 0. For *df*, 0 is outside the
allowed range, and for *omega*, the *alpha* and the *beta*, 0 is the lower
bound, so these p-values are not standard tests; read them as a rough guide.

Each fit leaves out its first *ar* rows, so fits with different *ar* use
different rows. To compare their AIC and BIC, fit them on a common sample:
with *r_max* the largest *ar*, give the model with ``ar=r`` the rows
*r_max* - *r* + 1 to *N*. Every likelihood then covers rows *r_max* + 1 to
*N*. For AR(0), AR(1) and AR(2) on the monthly S&P 500 returns:

::

    fname = getGAUSSHome("pkgs/timeseries/examples/data/garch_sp500_monthly.csv");
    sp = loadd(fname);
    y = sp[., "y"];
    n = rows(y);

    // The largest ar is 2. The model with ar=r gets rows r_max-r+1 to n,
    // so every likelihood covers rows 3 to n.
    r_max = 2;
    struct garchResult f0, f1, f2;
    f0 = garchFit(y[r_max+1:n], garch=1, arch=1, quiet=1);
    f1 = garchFit(y[r_max:n], ar=1, garch=1, arch=1, quiet=1);
    f2 = garchFit(y[r_max-1:n], ar=2, garch=1, arch=1, quiet=1);

    print sprintf("%-6s %8s %12s %12s %12s", "", "Obs.", "Log lik.", "AIC", "BIC");
    print sprintf("%-6s %8d %12.4f %12.4f %12.4f", "AR(0)" $| "AR(1)" $| "AR(2)",
        f0.effective_nobs | f1.effective_nobs | f2.effective_nobs,
        f0.loglik | f1.loglik | f2.loglik, f0.aic | f1.aic | f2.aic, f0.bic | f1.bic | f2.bic);

::

               Obs.     Log lik.          AIC          BIC

    AR(0)       801   -2127.5959    4263.1918    4281.9352
    AR(1)       801   -2114.7468    4239.4935    4262.9228
    AR(2)       801   -2112.6943    4237.3885    4265.5037

All three likelihoods cover the same 801 months. AIC prefers AR(2) and BIC
prefers AR(1).

``model="gjr_garch"`` is accepted for ``"gjr"`` and ``dist="student_t"`` for
``"t"``. EGARCH, skewed *t*, GED, GARCH-in-mean and IGARCH are planned for a
later release; ``model="egarch"`` is refused with a message that says so.

Refusals and Messages
---------------------

By default a refusal ends the program with its message. With
``on_error="return"`` the result is returned with *status* and
*status_message*:

.. list-table::
   :header-rows: 1
   :widths: 8 37 55

   * - Status
     - Condition
     - Message
   * - 0
     - Converged fit
     - (empty)
   * - 1
     - Fewer than 5 observations per estimated parameter
     - ``garchFit: the series has 15 observations; this model needs at least
       20 (5 per estimated parameter, 4 parameters).`` With AR terms:
       ``garchFit: the series has 28 usable observations after the first 2 (AR
       lags); this model needs at least 35 (5 per estimated parameter, 7
       parameters).``
   * - 2
     - The optimizer did not converge. The estimates are returned, with no
       standard errors. With ``on_error="stop"`` the message is printed as a
       warning; with ``on_error="return"`` it is only stored in
       *status_message*. Unless *quiet* is 1, the printed summary ends with a
       warning either way. The advice
       at the end depends on why the optimizer stopped. The message shown is
       from a run with ``dist="t"``, ``ctl.max_iter = 1`` and
       ``ctl.tol = 1e-14``.
     - ``garchFit: Warning: the optimizer did not converge (L-BFGS-B task 31,
       projected gradient 1.55204e-06, requested 1e-14). The estimates are the
       best finite run and have no standard errors. Try a larger
       ctl.max_iter.``
   * - 6
     - A missing or non-finite value in *y* or *x*
     - ``garchFit: y has a missing or non-finite value at row 7. Remove or
       fill missing values before fitting.`` or ``garchFit: regressor
       return_pct (x column 1) has a missing or non-finite value at row 1.
       Remove or fill missing values before fitting.``
   * - 7
     - An invalid argument. The message names it, for example:
     - ``garchFit: the GARCH order (garch) must be a positive integer.``,
       ``garchFit: the GARCH order is given twice (p and garch=). Give it once,
       as garch=.``, ``garchFit: the second argument is the GARCH order, not
       the regressors. Give regressors as x=, for example garchFit(y,
       x=X).``, ``garchFit: x has 10 rows; it needs one row per observation of
       y (1974).``, ``garchFit: dist must be "normal" or "t".``,
       ``garchFit: covariance must be both, opg or none.``,
       ``garchFit: level must be a finite scalar strictly between 0 and 1.``,
       ``garchFit: presample_state must be finite and positive for the
       selected init_policy.``, ``garchFit: ctl.max_iter must be a positive
       integer.``
   * - 9
     - No starting value gives a finite likelihood
     - ``garchFit: no starting value gave a finite likelihood. Check the scale
       of y and the model.``
   * - 11
     - A refusal by the estimator itself
     - ``garchFit: the estimator refused this request (category n).``
   * - 17
     - A model or setting not offered
     - ``garchFit: GJR fitting supports garch=1, arch=1, leverage_order=1.``,
       ``garchFit: model="garch" requires leverage_order=0.``,
       ``garchFit: model="egarch" is planned for a later release. Use
       model="garch" or model="gjr".``
   * - 18
     - *y* is constant, or with ``mean_model="zero_mean"`` every value has
       the same absolute value
     - ``garchFit: y is constant; there is no volatility to model.`` or
       ``garchFit: with mean_model="zero_mean", every value of y has the same
       absolute value; there is no volatility to model.``
   * - 19
     - A mean term cannot be estimated: constant, zero in every row, or a
       linear combination of the terms before it
     - ``garchFit: regressor x1 is constant, so it duplicates the constant
       mean. Remove it or use mean_model="zero_mean".``,
       ``garchFit: regressor x1 is zero in every row the fit uses. Remove
       it.`` or ``garchFit: regressor x2 is a linear combination of the
       constant and the mean terms before it. Remove it.`` An AR term is named
       as, for example, ``ar1 (y lagged 1)``.
   * - 20
     - The mean terms fit *y* exactly
     - ``garchFit: the mean terms fit y exactly; there is no volatility to
       model.``
   * - 5, 12, -1
     - Internal errors
     - ``garchFit: internal error in the numerical library.`` and similar.
       Please report them to Aptech support with the data and the call.

References
----------

- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. *Journal of Econometrics* 31, 307-327.
- Bollerslev, T. (1987). A conditionally heteroskedastic time series model for speculative prices and rates of return. *Review of Economics and Statistics* 69, 542-547.
- Bollerslev, T. and J.M. Wooldridge (1992). Quasi-maximum likelihood estimation and inference in dynamic models with time-varying covariances. *Econometric Reviews* 11, 143-172.
- Engle, R.F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. *Econometrica* 50, 987-1007.
- Glosten, L.R., R. Jagannathan and D.E. Runkle (1993). On the relation between the expected value and the volatility of the nominal excess return on stocks. *Journal of Finance* 48, 1779-1801.

Library
-------
timeseries

Source
------
garch.src

.. seealso:: Functions :func:`garchForecast`, :func:`garchControlCreate`, :func:`garchResults`, :func:`garchDiagnostics`, :doc:`garch-from-tsmt`
