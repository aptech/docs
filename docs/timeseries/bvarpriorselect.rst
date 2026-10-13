bvarPriorSelect
===============

Purpose
-------
Choose the overall tightness of a Minnesota prior by marginal likelihood and, optionally, the residual variances the prior is built on and the tightness of the sum-of-coefficients and single-unit-root priors.

Format
------

.. function:: ps = bvarPriorSelect(y)
              ps = bvarPriorSelect(y, p=4)
              ps = bvarPriorSelect(y, p=4, lag1_prior_mean=prior_means)
              ps = bvarPriorSelect(y, ctl=ctl)

   :param y: endogenous variables. A single date column in a dataframe is used as the time index and left out of the model.
   :type y: TxM matrix or dataframe

   :param p: Optional keyword, lag order. Default = 1. Ignored when *ctl* is given (set *ctl.p*).
   :type p: scalar

   :param lag1_prior_mean: Optional keyword, prior mean of each variable's coefficient on its own first lag, as in :func:`bvarFit`: ``"random_walk"`` (1, for persistent series such as levels), ``"zero"`` (for changes or growth rates), one number in [0,1] for every variable, or a vector with one number per variable. Default = ``"random_walk"``. The prior means are a fixed part of the prior: the search chooses the tightness, not the means. Ignored when *ctl* is given (set *ctl.lag1_prior_mean*).
   :type lag1_prior_mean: string, scalar or Mx1 vector

   :param xreg: Optional keyword, exogenous regressors. Ignored when *ctl* is given (set *ctl.xreg*).
   :type xreg: TxK matrix

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of a :class:`bvarControl` structure (see :func:`bvarControlCreate`). Its prior settings are held fixed while the tightness is chosen; *ctl.overall_tightness* is the starting value. When *ctl* is given, *p*, *lag1_prior_mean* and *xreg* are ignored. Settings that matter here:

       .. list-table::
          :widths: auto

          * - ctl.prior_selection
            - String, what the search chooses. ``"tightness"`` (default): the tightness; the residual variances stay at the values *ctl.residual_variance_policy* gives. ``"tightness_and_residual_variances"``: the residual variance of each series as well, searched between 1/100 and 100 times that value. See the Remarks.

          * - ctl.prior_selection_criterion
            - String, the objective. ``"map"`` (default): log marginal likelihood plus the log of the priors Giannone, Lenza and Primiceri (2015) put on what is chosen: a Gamma prior on each tightness (overall tightness: mode 0.2, standard deviation 0.4; sum-of-coefficients and single-unit-root tightness: mode 1, standard deviation 1) and, when the residual variances are chosen, an inverse-gamma prior on each of them (shape and scale 0.02 squared). ``"ml"``: log marginal likelihood alone, with none of these priors.

          * - ctl.soc_tightness
            - Scalar. 0 (default): no sum-of-coefficients prior. A positive value adds that prior and chooses its tightness too, starting from this value, together with the lag decay (*ctl.lag_decay*, between 0.5 and 3).

          * - ctl.sur_tightness
            - Scalar. 0 (default): no single-unit-root prior. A positive value adds that prior and chooses its tightness too; it requires *ctl.soc_tightness* > 0.

          * - ctl.lag1_prior_mean
            - Scalar or vector, the prior mean of each variable's own first lag: one value for all variables, or a row or column vector with one value per variable, each in [0,1]. Default = 1 (random walk). Use 0 for series in changes or growth rates.

          * - ctl.intercept_prior
            - String. "fixed_vc" (default) holds the prior variance of the constants at *ctl.constant_vc* (default 1e7) while the tightness changes; "litterman_coupled" scales it with the overall tightness. The two give different choices.

          * - ctl.residual_variance_policy
            - String, how the prior's residual variances are estimated. Default: "arp_full_training" (the residual variance of an autoregression with *ctl.p* lags for each series). :func:`bvarGlp2015ControlCreate` sets the variances Giannone, Lenza and Primiceri use. When the residual variances are chosen, these values are where the search starts and the centre of each variance's range.

   :type ctl: struct

   :return ps: An instance of a :class:`priorSelectResult` structure containing:

       .. list-table::
          :widths: auto

          * - ps.overall_tightness
            - Scalar, the chosen overall tightness.

          * - ps.soc_tightness
            - Scalar, the chosen sum-of-coefficients tightness; 0 if that prior is not used.

          * - ps.sur_tightness
            - Scalar, the chosen single-unit-root tightness; 0 if that prior is not used.

          * - ps.lag_decay
            - Scalar, the lag decay: chosen when the sum-of-coefficients prior is used, otherwise *ctl.lag_decay*.

          * - ps.log_ml
            - Scalar, the log marginal likelihood at the chosen values.

          * - ps.log_hyperprior
            - Scalar, the log prior of the chosen values; 0 when *ctl.prior_selection_criterion* = ``"ml"``. The maximized objective is *ps.log_ml* + *ps.log_hyperprior*.

          * - ps.converged
            - Scalar, 1 if the search converged: for the overall tightness alone, to a peak inside its range; with the sum-of-coefficients prior and fixed residual variances, to a point that meets the optimality conditions, which may lie on a bound of one of the values. 0 whenever *ps.at_bound* names something.

          * - ps.at_bound
            - String array naming what stopped at an edge of its range, where the objective was still rising, so that no peak was found: ``""`` (nothing), ``"tightness"``, ``"residual_variances"``, or both (a 2x1 array). With *ctl.prior_selection* = ``"tightness"`` only the search for the overall tightness alone reports it (range 0.001 to 5); with the sum-of-coefficients prior the values are chosen jointly, the search checks its own optimality conditions at the bounds, *ps.at_bound* is ``""`` and *ps.converged* gives the result. With the residual variances chosen, the tightness (range 0.0001 to 5) and the residual variances (each 1/100 to 100 times its starting value) are both reported.

          * - ps.status
            - String, "converged", "not_converged" or "at_bound". Test ``ps.status $== "at_bound"`` to ask whether anything stopped at an edge.

          * - ps.n_evals
            - Scalar, number of marginal-likelihood evaluations.

          * - ps.residual_variances
            - Mx1 vector, the residual variances of the chosen prior: the values *ctl.residual_variance_policy* gives, or the chosen values when the search chooses them.

          * - ps.residual_variance_policy
            - String, how the residual variances were estimated; when the search chooses them, the rule that gave their starting values.

          * - ps.ctl
            - :class:`bvarControl` structure: the input settings, including the prior means, with the chosen tightness values filled in, ready to pass to :func:`bvarFit` as *ctl*. When the residual variances are chosen it carries them (*residual_variance_policy* = ``"supplied"``), so the fit uses them.

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
    fit = bvarFit(data, ctl=ps.ctl);

The printout shows the lag order and the own-lag prior mean the search
used, the chosen overall tightness (about 0.14 here), the log marginal
likelihood, the log prior of the tightness and their sum, then the fit at
the chosen tightness.

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
    fit = bvarFit(y, ctl=ps.ctl);

    // The same search with every series centred at 1 (the default).
    ps_rw = bvarPriorSelect(y, p=4);

With GDP growth centred at 0 the search chooses an overall tightness of
about 0.25, with a log marginal likelihood of -1367.5; with every series
centred at 1 it chooses about 0.33, with -1376.2. *ps.ctl* carries the prior
means, so the fit uses them too.

Add the Sum-of-Coefficients and Single-Unit-Root Priors
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 5;
    ctl.soc_tightness = 1;     // add the prior; start the search at 1
    ctl.sur_tightness = 1;

    ps = bvarPriorSelect(data, ctl=ctl);

The overall, sum-of-coefficients and single-unit-root tightness and the
lag decay are chosen together.

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
    ctl.prior_selection = "tightness_and_residual_variances";
    ps = bvarPriorSelect(data, ctl=ctl);
    fit = bvarFit(data, ctl=ps.ctl);

    // Which setting forecasts better on these data? Choose the prior again
    // at each of 20 forecast dates (1989Q1 to 2008Q1) and score the forecasts.
    ev_fixed = bvarRollingOrigin(data, {}, "variances fixed", "expanding", "2015 data",
        p=5, initial_window=120, h=4, step=4, n_draws=1000,
        lag1_prior_mean="random_walk", prior_selection="tightness");
    ev_chosen = bvarRollingOrigin(data, {}, "variances chosen", "expanding", "2015 data",
        p=5, initial_window=120, h=4, step=4, n_draws=1000,
        lag1_prior_mean="random_walk",
        prior_selection="tightness_and_residual_variances");

    // Root mean squared error with chosen variances relative to fixed ones:
    // horizons 1 to 4 in rows, the seven series in columns. Below 1 is better.
    print ev_chosen.rmse ./ ev_fixed.rmse;

With fixed residual variances the search chooses a tightness of about 0.14;
with the residual variances chosen too, about 0.22, and the log marginal
likelihood rises from 3098.8 to 3117.0. The second printout reports the
residual variances as estimated. The two tightness values are not
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

With the overall tightness alone, the search is one-dimensional: a grid
followed by golden-section refinement on the log scale, between 0.001 and
5. With the sum-of-coefficients (and single-unit-root) prior added, the
values (and the lag decay) are chosen jointly by a bounded quasi-Newton
search.

**The residual variances.** The Minnesota prior needs one residual variance
per series: it sets the scale of the prior on the error covariance, and it
converts the tightness into a prior standard deviation for each
coefficient (the prior variance of a coefficient on a lag of series *j* is
proportional to the tightness squared divided by the residual variance of
series *j*). By default each residual variance is the residual variance of
an autoregression of that series, computed once and held fixed while the
tightness is chosen. With *ctl.prior_selection* =
``"tightness_and_residual_variances"`` the search chooses them together with
the tightness, as Giannone, Lenza and Primiceri (2015) do: each is searched
between 1/100 and 100 times its autoregression value, starting there, by a
bounded quasi-Newton search with exact derivatives, from one starting
point. *ps.residual_variances* holds the chosen values and *ps.ctl* carries
them, so ``bvarFit(y, ctl=ps.ctl)`` fits the chosen prior.

A tightness chosen with estimated residual variances cannot be compared
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

*ps.ctl* holds the residual variances chosen on the sample given to
:func:`bvarPriorSelect`. A procedure that refits with *ps.ctl* on other
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
percent on average over 1983 to 2007. Put the data in the authors' units, or set
*ctl.prior_selection_criterion* = ``"ml"``, which removes this prior
together with the prior on the tightness; the choice then does not depend
on the units of the data.

*ps.status* = "at_bound" means the objective keeps rising toward the edge
of a search range, so the returned value is that edge, not a peak;
*ps.at_bound* names what stopped. For the overall tightness: at the lower
edge the data favour shrinking the coefficients all the way to the prior
mean; at the upper edge the prior hardly matters. For a residual variance:
the data favour a value more than 100 times away from its starting value.
The printout says which series and which edge, and *ps.converged* is 0.
With the residual variances chosen together with the sum-of-coefficients
prior, the lag decay and the tightness of the dummy-observation priors are
not named in *ps.at_bound*. *ps.ctl* still holds the edge values:
check *ps.status* before fitting with it.

To evaluate the choice on forecasts, use :func:`bvarRollingOrigin` with
*prior_selection="tightness"* or
*prior_selection="tightness_and_residual_variances"*, which repeats the
choice on each forecast origin's data. Pass it the same *lag1_prior_mean*:
its default is ``"zero"``, not ``"random_walk"``.

References
----------

- Giannone, D., M. Lenza, and G. E. Primiceri (2015). "Prior selection for vector autoregressions." *Review of Economics and Statistics*, 97(2), 436-451.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarControlCreate`, :func:`bvarGlp2015ControlCreate`, :func:`bvarRollingOrigin`
