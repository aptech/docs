bvarPriorSelect
===============

Purpose
-------
Choose prior settings of a Minnesota BVAR by marginal likelihood: the overall tightness and, when marked with :func:`bvarChoose`, the residual variances the prior is built on, the lag decay, and the tightness of the sum-of-coefficients and single-unit-root priors.

Format
------

.. function:: ps = bvarPriorSelect(y)
              ps = bvarPriorSelect(y, p=4)
              ps = bvarPriorSelect(y, p=4, residual_variances=bvarChoose())
              ps = bvarPriorSelect(y, p=4, lag1_prior_mean=prior_means)
              ps = bvarPriorSelect(y, ctl=ctl)

   :param y: endogenous variables. A single date column in a dataframe is used as the time index and left out of the model.
   :type y: TxM matrix or dataframe

   :param p: Optional keyword, lag order. Default = 1.
   :type p: scalar

   :param overall_tightness: Optional keyword, a number (held at that value) or ``bvarChoose(start)`` (chosen, starting at *start*). Default: chosen, starting at 0.2, or at *ctl.overall_tightness* when *ctl* is given. A plain number with nothing else marked is refused: nothing would be chosen.
   :type overall_tightness: scalar or struct

   :param residual_variances: Optional keyword, a vector of residual variances, one per series (held; needs *residual_variance_policy* = ``"supplied"``), ``bvarChoose()`` (chosen, starting at the values *residual_variance_policy* gives) or ``bvarChoose(v)`` (chosen, starting at *v*; needs *residual_variance_policy* = ``"supplied"``). Each chosen variance is searched between 1/100 and 100 times its start. Default: held at the values *residual_variance_policy* gives.
   :type residual_variances: Mx1 vector or struct

   :param lag_decay: Optional keyword, how much harder longer lags are pulled: a number (held) or ``bvarChoose(start)`` (chosen, between 0.5 and 3). Default = 1, held. It cannot be chosen with one lag, where the prior does not depend on it.
   :type lag_decay: scalar or struct

   :param soc_tightness: Optional keyword, tightness of the sum-of-coefficients prior: a number (held; 0 means the prior is off) or ``bvarChoose(start)`` (chosen, between 0.0001 and 50). ``bvarChoose()`` on a value of 0 adds the prior and starts the search at 1. Default = 0.
   :type soc_tightness: scalar or struct

   :param sur_tightness: Optional keyword, tightness of the single-unit-root prior, as *soc_tightness*. Default = 0.
   :type sur_tightness: scalar or struct

   :param residual_variance_policy: Optional keyword, how the prior's residual variances are found, as in :func:`bvarFit`: ``"arp_full_training"`` (default: the residual variance of an autoregression with *p* lags for each series), ``"glp2015_post_var_trim_ar1"`` (the variances Giannone, Lenza and Primiceri use; :func:`bvarGlp2015ControlCreate` sets it) or ``"supplied"`` (the values in *residual_variances*). When the residual variances are chosen, these values are where the search starts and the centre of each variance's range.
   :type residual_variance_policy: string

   :param choose_by: Optional keyword, the objective. ``"map"`` (default): log marginal likelihood plus the log of the priors Giannone, Lenza and Primiceri (2015) put on what is chosen: a Gamma prior on each tightness (overall tightness: mode 0.2, standard deviation 0.4; sum-of-coefficients and single-unit-root tightness: mode 1, standard deviation 1) and, when the residual variances are chosen, an inverse-gamma prior on each of them (shape and scale 0.02 squared). An included sum-of-coefficients or single-unit-root prior that is held keeps its Gamma term, as a constant. ``"ml"``: log marginal likelihood alone, with none of these priors.
   :type choose_by: string

   :param lag1_prior_mean: Optional keyword, prior mean of each variable's coefficient on its own first lag, as in :func:`bvarFit`: ``"random_walk"`` (1, for persistent series such as levels), ``"zero"`` (for changes or growth rates), one number in [0,1] for every variable, or a vector with one number per variable. Default = ``"random_walk"``. The prior means are a fixed part of the prior: the search chooses the tightness, not the means.
   :type lag1_prior_mean: string, scalar or Mx1 vector

   :param xreg: Optional keyword, exogenous regressors. The prior scale of their coefficients (*exogenous_scale*) is held.
   :type xreg: TxK matrix

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of a :class:`bvarControl` structure (see :func:`bvarControlCreate`). Its values are used except where a keyword is also given: a keyword given together with *ctl* replaces that field for this call, and *ctl* itself is not changed. A control holds values only; what is chosen is marked in the call with :func:`bvarChoose`, and ``bvarChoose()`` starts at the control's value. A setting that matters here and has no keyword:

       .. list-table::
          :widths: auto

          * - ctl.const_prior
            - String. "fixed" (default) holds the prior variance of the constants at *ctl.const_prior_variance* (default 1e7) while the tightness changes; "litterman_coupled" scales it with the overall tightness. The two give different choices.

   :type ctl: struct

   :return ps: An instance of a :class:`priorSelectResult` structure containing:

       .. list-table::
          :widths: auto

          * - ps.overall_tightness
            - Scalar, the overall tightness, chosen or held.

          * - ps.soc_tightness
            - Scalar, the sum-of-coefficients tightness, chosen or held; 0 if that prior is not used.

          * - ps.sur_tightness
            - Scalar, the single-unit-root tightness, chosen or held; 0 if that prior is not used.

          * - ps.lag_decay
            - Scalar, the lag decay, chosen or held.

          * - ps.choose
            - String array, what the search chose, in the order ``"overall_tightness"``, ``"residual_variances"``, ``"lag_decay"``, ``"soc_tightness"``, ``"sur_tightness"``.

          * - ps.log_ml
            - Scalar, the log marginal likelihood at the chosen values.

          * - ps.log_hyperprior
            - Scalar, the log prior of the chosen values; 0 when *choose_by* = ``"ml"``. The maximized objective is *ps.log_ml* + *ps.log_hyperprior*.

          * - ps.converged
            - Scalar, 1 if the search met its convergence test; 0 whenever *ps.at_bound* names a setting. It can be 1 after a line-search abort; *ps.stop_reason* shows it.

          * - ps.at_bound
            - String array naming the chosen settings that stopped at an edge of their range, where the objective was still rising, so that no peak was found: ``""`` (none), or one or more of ``"overall_tightness"``, ``"residual_variances"``, ``"lag_decay"``, ``"soc_tightness"`` and ``"sur_tightness"``. Any name makes *ps.status* ``"at_bound"`` and *ps.converged* 0.

          * - ps.status
            - String, "converged", "not_converged" or "at_bound". Test ``ps.status $== "at_bound"`` to ask whether anything stopped at an edge.

          * - ps.stop_reason
            - String, how the search ended: ``"converged"``, ``"line_search_abort"``, ``"warning"``, ``"iteration_limit"``, ``"other"``, or ``"golden_section"`` for the search of the overall tightness alone.

          * - ps.projected_gradient_norm
            - Scalar, the largest projected-gradient component at the end of the search; missing for ``"golden_section"``.

          * - ps.n_evals
            - Scalar, number of marginal-likelihood evaluations.

          * - ps.residual_variances
            - Mx1 vector, the residual variances of the chosen prior: the values *residual_variance_policy* gives, or the chosen values when the search chooses them.

          * - ps.residual_variance_policy
            - String, the rule that gave the residual variances; when the search chooses them, the rule that gave their starting values.

          * - ps.fit_settings
            - :class:`bvarControl` structure: every setting at the value to fit at, the chosen ones and the held ones, including the prior means, ready to pass to :func:`bvarFit` as *ctl*. ``bvarFit(y, ctl=ps.fit_settings)`` fits the chosen prior without searching again, on these data or on new data. When the residual variances are chosen it carries them (*residual_variance_policy* = ``"supplied"``), so the fit uses them. To search again from the previous answer, repeat the call with ``ctl=ps.fit_settings`` and the same marks: with nothing marked, only the overall tightness is searched and everything else is held.

   :rtype ps: struct

Examples
--------

Choose the Tightness, Then Fit
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Seven quarterly US series (six in log levels, and the federal funds rate),
    // 1959Q1-2008Q4 (the data of Giannone, Lenza and Primiceri 2015). The
    // default prior centre, a random walk (ctl.lag1_prior_mean = 1), suits levels.
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 5;

    ps = bvarPriorSelect(data, ctl=ctl);
    fit = bvarFit(data, ctl=ps.fit_settings);

With nothing marked, the overall tightness is chosen, starting at
*ctl.overall_tightness*, and every other setting is held. The printout shows
the lag order and the own-lag prior mean the search used, the overall
tightness (about 0.14 here) marked "chosen", the residual variances marked
"from the rule" (the values *residual_variance_policy* gives), the log
marginal likelihood, the log prior of the tightness and their sum, then the
fit at the chosen tightness.

Different Prior Means for Different Series
++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Quarterly US GDP growth, inflation, unemployment and the federal funds
    // rate, 1960Q1-2019Q4. GDP growth is not persistent, so its own first lag
    // is centred at 0; the other three series are persistent and centred at 1.
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    ps = bvarPriorSelect(y, p=4, lag1_prior_mean={ 0, 1, 1, 1 });
    fit = bvarFit(y, ctl=ps.fit_settings);

    // The same search with every series centred at 1 (the default).
    ps_rw = bvarPriorSelect(y, p=4);

With GDP growth centred at 0 the search chooses an overall tightness of
about 0.25, with a log marginal likelihood of -1367.5; with every series
centred at 1 it chooses about 0.33, with -1376.2. *ps.fit_settings* carries the prior
means, so the fit uses them too.

Add the Sum-of-Coefficients and Single-Unit-Root Priors
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    // Add both priors and choose their tightness, starting at 1, together
    // with the overall tightness and the lag decay
    ps = bvarPriorSelect(data, p=5, overall_tightness=bvarChoose(),
        lag_decay=bvarChoose(), soc_tightness=bvarChoose(1),
        sur_tightness=bvarChoose(1));

The overall, sum-of-coefficients and single-unit-root tightness and the
lag decay are chosen together. Given as plain numbers instead
(``soc_tightness=1, sur_tightness=1``), the two priors are included but
held at 1 while the overall tightness alone is chosen.

Choose the Residual Variances Too, and Compare the Forecasts
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // The data of Giannone, Lenza and Primiceri (2015): logs multiplied by
    // four, the federal funds rate in decimals.
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 5;

    // Residual variances fixed at their autoregression values (the default).
    ps_fixed = bvarPriorSelect(data, ctl=ctl);

    // Residual variances chosen together with the tightness.
    ps = bvarPriorSelect(data, ctl=ctl, residual_variances=bvarChoose());
    fit = bvarFit(data, ctl=ps.fit_settings);

    // Which setting forecasts better on these data? Choose the prior again
    // at each of 20 forecast dates (1989Q1 to 2008Q1) and score the forecasts.
    ev_fixed = bvarRollingOrigin(data, {}, "variances fixed", "expanding", "2015 data",
        p=5, initial_window=120, h=4, step=4, n_draws=1000,
        lag1_prior_mean="random_walk", overall_tightness=bvarChoose());
    ev_chosen = bvarRollingOrigin(data, {}, "variances chosen", "expanding", "2015 data",
        p=5, initial_window=120, h=4, step=4, n_draws=1000,
        lag1_prior_mean="random_walk", overall_tightness=bvarChoose(),
        residual_variances=bvarChoose());

    // Root mean squared error with chosen variances relative to fixed ones:
    // horizons 1 to 4 in rows, the seven series in columns. Below 1 is better.
    print ev_chosen.rmse ./ ev_fixed.rmse;

With fixed residual variances the search chooses a tightness of about 0.14;
with the residual variances chosen too, about 0.22, and the log marginal
likelihood rises from 3098.8 to 3117.0. The first printout reports the
residual variances as "from the rule", the second as "chosen". The two
tightness values are not
comparable: the chosen residual variances are up to seven times the
autoregression values, and a prior with larger residual variances is tighter
at the same tightness (see the Remarks). On these data the two settings
forecast about equally well: every ratio in the last table is between 0.96
and 1.02.

Remarks
-------

The marginal likelihood of a tightness value is the probability the model
assigned, before seeing the data, to the sample it then observed. Under
the conjugate Minnesota prior it has a closed form, so each evaluation is
fast and the search needs no simulation. A very tight prior predicts the
sample badly because it rules out dynamics the data have; a very loose
prior spreads its predictions over coefficient values the data never
support. Giannone, Lenza and Primiceri (2015) show that choosing the
tightness this way forecasts well.

The prior means of the own first lags (*lag1_prior_mean*) are part of the
prior whose tightness is being chosen; they stay fixed during the search.
Giannone, Lenza and Primiceri centre every own first lag at 1, for data in
levels; a mean of 0 for a series that is not persistent keeps the same
closed form. The sum-of-coefficients prior, when added, centres the sum of
each variable's own-lag coefficients at 1 whatever its *lag1_prior_mean*.

**What is chosen and what is held.** A setting given as a plain number is
held at that value. A setting given as ``bvarChoose(x)`` is chosen, and the
search starts at *x*; ``bvarChoose()`` starts at the setting's own value
(its value in *ctl*, else its default; a sum-of-coefficients or
single-unit-root tightness of 0 starts at 1). With nothing marked, the
overall tightness is chosen, starting at 0.2 or at *ctl.overall_tightness*
when *ctl* is given, and every other setting is held. A call that holds the
overall tightness and marks nothing else is refused: nothing would be
chosen. *ps.choose* lists what was chosen.

The settings that can be chosen, and the combinations available:

- overall_tightness (the default)
- overall_tightness, residual_variances
- overall_tightness, soc_tightness
- overall_tightness, soc_tightness, sur_tightness
- overall_tightness, lag_decay, soc_tightness
- overall_tightness, lag_decay, soc_tightness, sur_tightness
- overall_tightness, residual_variances, lag_decay, soc_tightness
- overall_tightness, residual_variances, lag_decay, soc_tightness, sur_tightness
- overall_tightness, residual_variances, soc_tightness, sur_tightness

With the overall tightness alone, or with the residual variances, an
included sum-of-coefficients or single-unit-root prior is held at its value.
With the overall tightness alone, holding such a prior can make the search
slower: its faster method works only without the dummy-observation priors.
The other combinations choose every included dummy-observation prior. Any
other combination is refused as not yet available. A setting not in the
chosen combination is held: for example,
``soc_tightness=bvarChoose(1), sur_tightness=bvarChoose(1)`` chooses the
overall, sum-of-coefficients and single-unit-root tightness with the lag
decay held at its value.

Search ranges: overall tightness 0.0001 to 5; lag decay 0.5 to 3;
sum-of-coefficients and single-unit-root tightness 0.0001 to 50. A start
outside its range is refused. Each residual variance is searched between
1/100 and 100 times its start, so a supplied start moves both the start and
the range; the usual call, ``residual_variances=bvarChoose()``, starts at
the values of *residual_variance_policy*.

With the overall tightness alone, the search is one-dimensional: a grid of
32 points followed by golden-section refinement on the log scale. The start
is one extra point tried after the grid, and the result depends on it only
when it is the best point tried. When other settings are chosen too, they
are chosen jointly by a bounded quasi-Newton search. That search moves from
its start to a nearby peak of its objective, which need not be the highest;
compare ``log_ml + log_hyperprior`` from more than one start.

**The residual variances.** The Minnesota prior needs one residual variance
per series: it sets the scale of the prior on the error covariance, and it
converts the tightness into a prior standard deviation for each
coefficient (the prior variance of a coefficient on a lag of series *j* is
proportional to the tightness squared divided by the residual variance of
series *j*). By default each residual variance is the residual variance of
an autoregression of that series, computed once and held fixed while the
tightness is chosen. With ``residual_variances=bvarChoose()`` the search
chooses them together with the tightness, as Giannone, Lenza and Primiceri
(2015) do: each is searched between 1/100 and 100 times its autoregression
value, starting there, by a
bounded quasi-Newton search with exact derivatives, from one starting
point. *ps.residual_variances* holds the chosen values and *ps.fit_settings* carries
them, so ``bvarFit(y, ctl=ps.fit_settings)`` fits the chosen prior.

A tightness chosen together with the residual variances cannot be compared
with one chosen with fixed residual variances. Larger residual variances
make the prior on the coefficients tighter at the same tightness, so the
search answers them with a different tightness; what matters is the pair.

Whether the setting improves forecasts cannot be read from the fit on the
sample, and it differs from one system to the next. In a separate
calculation of the same method (not a run of these procedures) on monthly
US data, with 120-month windows, 13 lags and the prior chosen again at every
forecast date, forecasts of employment, consumer prices and the federal
funds rate 1, 3, 6 and 12 months ahead were scored from 1983 to 2007.
Choosing the residual variances changed the root mean squared errors as
follows:

- 3 series: nearly every forecast slightly worse.
- 7 series: employment slightly worse at every horizon, the funds rate
  better at every horizon, consumer prices better beyond one month.
- 20 series: employment and the funds rate better at every horizon,
  consumer prices equal at one month and better beyond.
- 40 series: employment and consumer prices worse at every horizon, the
  funds rate better at every horizon.
- 60 series: employment worse at every horizon, consumer prices and the
  funds rate better at every horizon.
- 125 series: employment and the funds rate better at every horizon,
  consumer prices worse at one month and better beyond.

Compare the two settings on your own data with :func:`bvarRollingOrigin`,
which repeats the choice at each forecast date, as in the last example
above. That example prints root mean squared errors; the setting also
changes the width of the forecast bands, which *ev.mean_crps* scores.

*ps.fit_settings* holds the residual variances chosen on the sample given to
:func:`bvarPriorSelect`. A procedure that refits with *ps.fit_settings* on other
samples keeps those variances; it does not choose them again.

**Units of the data.** Under the default criterion (``"map"``) each chosen
residual variance has the paper's inverse-gamma prior, whose peak is near
0.02 squared. It suits data scaled as the authors' quarterly data were:
series in logs multiplied by four (so that quarterly changes read as annual
rates), and rates in decimals (0.05 for five percent). In those units a one-step
forecast error of 0.02 is ordinary. For data in other units the prior says
something else. For three monthly series in plain logs (decimals), whose
one-step errors are far smaller than 0.02, it raised every chosen residual
variance, doubled the chosen tightness (0.45 against 0.22 for the same
series multiplied by 100) and widened the one-step forecast bands by 7 to 16
percent on average over 1983 to 2007. Put the data in the authors' units, or pass
``choose_by="ml"``, which removes this prior
together with the prior on the tightness; the choice then does not depend
on the units of the data.

*ps.status* = "at_bound" means the objective keeps rising toward the edge
of a search range, so the returned value is that edge, not a peak;
*ps.at_bound* names the chosen settings that stopped. For the overall
tightness: at the lower edge the data favour shrinking the coefficients all
the way to the prior mean; at the upper edge the prior hardly matters. For a
residual variance: the data favour a value more than 100 times away from its
starting value. The printout gives the range of each setting that stopped
and, for the residual variances, which series and which edge, and
*ps.converged* is 0. A held setting is never named. *ps.fit_settings* still holds
the edge values: check *ps.status* before fitting with it.

To evaluate the choice on forecasts, use :func:`bvarRollingOrigin` with
``overall_tightness=bvarChoose()``, and ``residual_variances=bvarChoose()``
as well to choose the residual variances, which repeats the choice on each
forecast origin's data. Pass it the same *lag1_prior_mean*: its default is
``"zero"``, not ``"random_walk"``.

References
----------

- Giannone, D., M. Lenza, and G. E. Primiceri (2015). "Prior selection for vector autoregressions." *Review of Economics and Statistics*, 97(2), 436-451.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarChoose`, :func:`bvarFit`, :func:`bvarControlCreate`, :func:`bvarGlp2015ControlCreate`, :func:`bvarRollingOrigin`
