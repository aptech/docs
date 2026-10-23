bvarFit
=======

Purpose
-------
Fit a Bayesian VAR with the conjugate Minnesota prior.

Format
------

.. function:: fit = bvarFit(y)
              fit = bvarFit(y, p=4, lag1_prior_mean=0|1|1|1, overall_tightness=0.2)
              fit = bvarFit(y, ctl=ctl)
              fit = bvarFit(y, p=4, overall_tightness=bvarChoose(0.2))

   :param y: the data, one column per variable. A dataframe's column names label the output; a single date-typed column is used as the time index and left out of the model. A matrix's variables are labeled "Y1", "Y2", ...
   :type y: TxM matrix or dataframe

   :param p: Optional keyword, lag order. Default = 1.
   :type p: scalar

   :param lag1_prior_mean: Optional keyword, prior mean of each variable's coefficient on its own first lag: ``"random_walk"`` (1, for persistent series such as levels, rates and inflation), ``"zero"`` (for growth rates), one value for every variable, or a vector with one value per variable, each in [0,1]. Every other coefficient has prior mean 0. Default = ``"random_walk"``.
   :type lag1_prior_mean: string, scalar or Mx1 vector

   :param overall_tightness: Optional keyword, how hard the prior pulls: roughly the prior standard deviation of each variable's coefficient on its own first lag. Smaller values pull harder. A number holds it at that value; ``bvarChoose(start)`` chooses it by marginal likelihood before the fit (see the Remarks). Default = 0.2.
   :type overall_tightness: scalar or struct

   :param lag_decay: Optional keyword, how much harder longer lags are pulled: the prior standard deviation for lag *l* is the one for lag 1 divided by :math:`l^{\text{lag\_decay}}`. A number, or ``bvarChoose(start)`` to choose it. Default = 1.
   :type lag_decay: scalar or struct

   :param soc_tightness: Optional keyword, tightness of the sum-of-coefficients prior (Doan, Litterman & Sims 1984), which pulls the sum of each variable's own-lag coefficients toward 1. 0 turns it off; a positive value turns it on, and smaller values pull harder. A number, or ``bvarChoose(start)`` to choose it (``bvarChoose()`` on a value of 0 adds the prior and starts at 1). Default = 0.
   :type soc_tightness: scalar or struct

   :param sur_tightness: Optional keyword, tightness of the single-unit-root prior (Sims 1993), which pulls the system toward a common stochastic trend. 0 turns it off. A number, or ``bvarChoose(start)`` to choose it, as *soc_tightness*. Default = 0.
   :type sur_tightness: scalar or struct

   :param residual_variance_policy: Optional keyword, how the residual scales that set the prior's units are found: ``"arp_full_training"`` (default: the residual variance of each variable's own AR(p) with a constant, on the estimation sample), ``"glp2015_post_var_trim_ar1"`` (AR(1) residual variance after dropping the first *p* observations, as Giannone, Lenza & Primiceri 2015) or ``"supplied"`` (the values in *residual_variances*).
   :type residual_variance_policy: string

   :param residual_variances: Optional keyword, Mx1 residual scales for ``"supplied"``, or ``bvarChoose()`` / ``bvarChoose(v)`` to choose them before the fit (``bvarChoose()`` starts at the values *residual_variance_policy* gives; ``bvarChoose(v)`` starts at *v* and needs ``"supplied"``). Default = empty.
   :type residual_variances: Mx1 vector or struct

   :param choose_by: Optional keyword, the objective of a prior search, as in :func:`bvarPriorSelect`: ``"map"`` (default) or ``"ml"``. Used only when a setting is marked with :func:`bvarChoose`.
   :type choose_by: string

   :param n_draws: Optional keyword, number of posterior draws. Default = 5000.
   :type n_draws: scalar

   :param seed: Optional keyword, random number seed. Default = 42.
   :type seed: scalar

   :param xreg: Optional keyword, exogenous regressors, one row per observation of *y*. Default = none.
   :type xreg: TxK matrix

   :param exogenous_scale: Optional keyword, prior standard deviation of the coefficients on *xreg*, relative to the equation's error standard deviation. Default = 1.
   :type exogenous_scale: scalar

   :param dates: Optional keyword, POSIX dates for matrix input. Not needed when *y* is a dataframe with a date column. Default = none.
   :type dates: Tx1 vector

   :param freq: Optional keyword, frequency of the dates: ``"annual"``, ``"quarterly"``, ``"monthly"``, ``"weekly"`` or ``"daily"``. Default = inferred from the dates.
   :type freq: string

   :param quiet: Optional keyword, 1 to suppress printing. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of a :class:`bvarControl` structure, which holds every setting, including those that have no keyword (such as the intercept prior). When *ctl* is given, its values are used except where a keyword is also given: a keyword given together with *ctl* replaces that field for this call, and *ctl* itself is not changed. *dates* and *freq* are not fields of *ctl* and always apply. A control holds values only: a setting to be chosen is marked in the call with :func:`bvarChoose`. An instance is created by :func:`bvarControlCreate` and has these members:

       .. include:: include/bvarcontrol.rst

   :type ctl: struct

   :return fit: An instance of a :class:`bvarResult` structure containing:

       .. include:: include/bvarresult.rst

       .. list-table::
          :widths: auto

          * - result.prior_search
            - :class:`priorSelectResult` structure, the search run before the fit when a setting was marked with :func:`bvarChoose`; its members are described on the :func:`bvarPriorSelect` page. With nothing marked there is no search: *result.prior_search.ran* is 0 and *result.prior_search.status* is ``"not_run"``.

   :rtype fit: struct

Examples
--------

Four US series
++++++++++++++

::

    new;
    library timeseries;

    // Four quarterly US series, 1960Q1-2019Q4: GDP growth and inflation
    // (annualized percent changes), unemployment and the funds rate (percent)
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    // Prior centre 0 for GDP growth, 1 (random walk) for the three
    // persistent series; overall tightness 0.2
    fit = bvarFit(y, p=2, lag1_prior_mean=0|1|1|1, overall_tightness=0.2);

The output starts:

::

    BVAR(2), conjugate Minnesota prior
    ================================================================================
    Variables:                         4    Observations:                        240
    Lags:                              2    Effective obs.:                      238
    Constant:                        Yes    Posterior draws:                   5,000
    Tightness:                       0.2    Log marg. lik.:                 -1394.77
    Own-lag mean:            by equation

    Equation 1: gdp_growth (own first-lag prior mean 0)
    Regressor          Center      SD  Lower 68%  Upper 68%
    -------------------------------------------------------
    gdp_growth(-1)     0.1696  0.0676     0.1011     0.2358
    inflation(-1)     -0.1486  0.0962    -0.2450    -0.0538
    unemployment(-1)  -1.0931  0.6748    -1.7798    -0.4458
    fed_funds(-1)      0.0244  0.2025    -0.1715     0.2305
    gdp_growth(-2)     0.1191  0.0556     0.0642     0.1752
    inflation(-2)     -0.0691  0.0864    -0.1550     0.0180
    unemployment(-2)   1.3124  0.6629     0.6700     1.9808
    fed_funds(-2)     -0.0059  0.1961    -0.2065     0.1873
    Constant           1.5249  0.8405     0.6868     2.3681

and continues with the other three equations in the same layout, ending:

::

    Center: analytic matrix-t posterior mean (= median = mode).
    SD and 68% interval: equal-tailed quantiles of 5,000 posterior draws.

Choosing the lag order by marginal likelihood
++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    // Log marginal likelihood of one to six lags. Marginal likelihoods compare
    // only on the same observations, so each fit starts late enough that all
    // of them explain the same 234 quarters (1961Q3-2019Q4).
    max_lags = 6;
    print "Lags   Log ML";
    for lag (1, max_lags, 1);
        fit = bvarFit(y[max_lags-lag+1:rows(y), .], p=lag, lag1_prior_mean=0|1|1|1, quiet=1);
        print sprintf("%4d%10.2f", lag, fit.log_ml);
    endfor;

The output is:

::

    Lags   Log ML
       1  -1403.38
       2  -1370.87
       3  -1357.99
       4  -1357.53
       5  -1355.53
       6  -1355.30

A difference in log marginal likelihood is a log Bayes factor: three lags
improve on two by 12.9, after which the gains are small.

Levels data and the sum-of-coefficients prior
++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Seven quarterly US series in levels (logs of GDP, prices, consumption,
    // investment, hours and compensation, and the funds rate), 1959Q1-2008Q4,
    // the data of Giannone, Lenza and Primiceri (2015)
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    // The control struct sets the fields that have no keyword: here the
    // sum-of-coefficients prior, which pulls the lag sums toward a unit root
    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 5;
    ctl.overall_tightness = 0.2;
    ctl.lag1_prior_mean = 1;
    ctl.soc_tightness = 1;
    ctl.quiet = 1;
    with_soc = bvarFit(data, ctl=ctl);

    ctl.soc_tightness = 0;
    without_soc = bvarFit(data, ctl=ctl);

    print "Log ML with the sum-of-coefficients prior:    " sprintf("%.2f", with_soc.log_ml);
    print "Log ML without it:                            " sprintf("%.2f", without_soc.log_ml);

The output is:

::

    Log ML with the sum-of-coefficients prior:    3108.22
    Log ML without it:                            3094.62

On these data the prior raises the log marginal likelihood by 13.6. To
choose the tightness values by marginal likelihood instead, mark them with
:func:`bvarChoose`:
``bvarFit(data, p=5, overall_tightness=bvarChoose(), lag_decay=bvarChoose(), soc_tightness=bvarChoose())``
chooses the overall and sum-of-coefficients tightness and the lag decay,
then fits at the values found.

Remarks
-------

**Model.** With :math:`y_t` the M variables at time *t*,

.. math::

   y_t = c + B_1 y_{t-1} + \cdots + B_p y_{t-p} + \varepsilon_t, \qquad \varepsilon_t \sim N(0, \Sigma).

Stacking the coefficients in the Kxm matrix :math:`B = [B_1 \cdots B_p \; c]'` (K = Mp + 1, plus
the columns of *xreg*), the conjugate Minnesota prior is

.. math::

   \text{vec}(B) \mid \Sigma \sim N\bigl(\text{vec}(B_0),\; \Sigma \otimes \Omega\bigr), \qquad
   \Sigma \sim IW\bigl((\alpha_0 - M - 1)\,\text{diag}(\sigma_1^2, \ldots, \sigma_M^2),\; \alpha_0\bigr).

:math:`B_0` is zero except each variable's coefficient on its own first lag
(*lag1_prior_mean*). :math:`\Omega` is diagonal: the row for lag *l* of variable *j* is
:math:`\lambda^2 / (l^{2d} \sigma_j^2)`, with :math:`\lambda` the overall tightness and *d* the lag decay, and the
constant's row is *ctl.constant_vc* (1e7, effectively flat). The residual scales
:math:`\sigma_j^2` come from each variable's own AR(p) regression on the estimation
sample. :math:`\alpha_0` defaults to M + 2.

Because the prior covariance has this Kronecker form, a variable's own lags
and the other variables' lags are shrunk alike, apart from each variable's
scale; this is what keeps the posterior in closed form.

**Posterior.** The posterior is again Normal-inverse-Wishart, so *b_post* is
the exact posterior mean of the coefficients, and the draws are independent
draws from the posterior: there is no burn-in and no convergence to check.
The draws give the standard deviations and credible intervals, which move a
little with the seed. *log_ml* is the log marginal likelihood, in closed form.

**Choosing the prior centre.** Use 1 (a random walk) for series that drift,
such as levels, interest rates and inflation, and 0 for growth rates
(Banbura, Giannone & Reichlin 2010). A random-walk centre on a growth rate
pulls toward a persistent series the data do not show; a zero centre on a
level pulls toward a series that returns quickly to its mean.

**Choosing the prior in the same call.** A prior setting given as a plain
number is held at that value. Given as ``bvarChoose(x)``, it is chosen by
marginal likelihood before the fit, starting at *x* (``bvarChoose()`` starts
at the setting's value in *ctl*, or its default), and the model is then
fitted at the values found. The settings :func:`bvarPriorSelect` can choose,
and the combinations it offers, apply here too. The result is the fit that
:func:`bvarPriorSelect` with the same keywords followed by
``bvarFit(y, ctl=ps.ctl)`` gives, and *result.prior_search* holds that
search; its printout comes before the fit's unless *quiet* = 1. With nothing
marked there is no search, so ``bvarFit(y, ctl=ps.ctl)`` fits the chosen
prior without searching again.

**Settings in the control struct.** The intercept prior and the other
settings that have no keyword are set in a :class:`bvarControl` structure.
The fit's settings, with resolved values, are kept in *fit.fit_settings*.

References
----------

- Banbura, M., D. Giannone, and L. Reichlin (2010). "Large Bayesian vector auto regressions." *Journal of Applied Econometrics*, 25(1), 71-92.
- Doan, T., R. Litterman, and C. Sims (1984). "Forecasting and conditional projection using realistic prior distributions." *Econometric Reviews*, 3(1), 1-100.
- Giannone, D., M. Lenza, and G. E. Primiceri (2015). "Prior selection for vector autoregressions." *Review of Economics and Statistics*, 97(2), 436-451.
- Kadiyala, K. R. and S. Karlsson (1997). "Numerical methods for estimation and inference in Bayesian VAR-models." *Journal of Applied Econometrics*, 12(2), 99-132.
- Litterman, R. B. (1986). "Forecasting with Bayesian vector autoregressions: five years of experience." *Journal of Business & Economic Statistics*, 4(1), 25-38.
- Sims, C. A. (1993). "A nine-variable probabilistic macroeconomic forecasting model." In J. H. Stock and M. W. Watson (eds.), *Business Cycles, Indicators and Forecasting*, University of Chicago Press, 179-212.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarControlCreate`, :func:`bvarChoose`, :func:`bvarForecast`, :func:`bvarPriorSelect`, :func:`varFit`, :func:`varLagSelect`, :func:`forecastEval`
