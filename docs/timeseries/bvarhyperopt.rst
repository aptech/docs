bvarHyperopt
============

Purpose
-------
Choose the overall tightness of a Minnesota prior (and, optionally, the tightness of the sum-of-coefficients and single-unit-root priors) by marginal likelihood.

Format
------

.. function:: ho = bvarHyperopt(y)
              ho = bvarHyperopt(y, p=4)
              ho = bvarHyperopt(y, p=4, lag1_prior_mean=prior_means)
              ho = bvarHyperopt(y, ctl=ctl)

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

          * - ctl.hyperopt_map
            - Scalar, the objective. 1 (default): log marginal likelihood plus the log of a Gamma prior on each tightness chosen (overall tightness: mode 0.2, standard deviation 0.4; sum-of-coefficients and single-unit-root tightness: mode 1, standard deviation 1), as in Giannone, Lenza and Primiceri (2015). 0: log marginal likelihood alone.

          * - ctl.soc_tightness
            - Scalar. 0 (default): no sum-of-coefficients prior. A positive value adds that prior and chooses its tightness too, starting from this value, together with the lag decay (*ctl.lag_decay*, between 0.5 and 3).

          * - ctl.sur_tightness
            - Scalar. 0 (default): no single-unit-root prior. A positive value adds that prior and chooses its tightness too; it requires *ctl.soc_tightness* > 0.

          * - ctl.lag1_prior_mean
            - Scalar or vector, the prior mean of each variable's own first lag: one value for all variables, or a row or column vector with one value per variable, each in [0,1]. Default = 1 (random walk). Use 0 for series in changes or growth rates.

          * - ctl.intercept_prior
            - String. "fixed_vc" (default) holds the prior variance of the constants at *ctl.constant_vc* (default 1e7) while the tightness changes; "litterman_coupled" scales it with the overall tightness. The two give different choices.

          * - ctl.residual_variance_policy
            - String, how the prior's residual scales are estimated. Default: "arp_full_training". :func:`bvarGlp2015ControlCreate` sets the scales Giannone, Lenza and Primiceri use.

   :type ctl: struct

   :return ho: An instance of a :class:`hyperoptResult` structure containing:

       .. list-table::
          :widths: auto

          * - ho.overall_tightness
            - Scalar, the chosen overall tightness.

          * - ho.soc_tightness
            - Scalar, the chosen sum-of-coefficients tightness; 0 if that prior is not used.

          * - ho.sur_tightness
            - Scalar, the chosen single-unit-root tightness; 0 if that prior is not used.

          * - ho.lag_decay
            - Scalar, the lag decay: chosen when the sum-of-coefficients prior is used, otherwise *ctl.lag_decay*.

          * - ho.log_ml
            - Scalar, the log marginal likelihood at the chosen values.

          * - ho.log_hyperprior
            - Scalar, the log prior of the chosen tightness values; 0 when *ctl.hyperopt_map* = 0. The maximized objective is *ho.log_ml* + *ho.log_hyperprior*.

          * - ho.converged
            - Scalar, 1 if the search converged: for the overall tightness alone, to a peak inside its range; with the sum-of-coefficients prior, to a point that meets the optimality conditions, which may lie on a bound of one of the values.

          * - ho.at_bound
            - Scalar, 1 if the overall tightness stopped at the edge of its range (0.001 or 5) in the search for the overall tightness alone: the objective was still rising there, so no peak was found. *ho.converged* is then 0. With the sum-of-coefficients prior the values are chosen jointly, and the search checks its own optimality conditions at the bounds, so *ho.at_bound* is 0 and *ho.converged* gives the result.

          * - ho.status
            - String, "converged", "not_converged" or "at_bound".

          * - ho.n_evals
            - Scalar, number of marginal-likelihood evaluations.

          * - ho.residual_variances
            - Mx1 vector, the residual scales used by the prior.

          * - ho.residual_variance_policy
            - String, how those scales were estimated.

          * - ho.ctl
            - :class:`bvarControl` structure: the input settings, including the prior means, with the chosen tightness values filled in, ready to pass to :func:`bvarFit` as *ctl*.

   :rtype ho: struct

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

    ho = bvarHyperopt(data, ctl=ctl);
    fit = bvarFit(data, ctl=ho.ctl);

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

    ho = bvarHyperopt(y, p=4, lag1_prior_mean={ 0, 1, 1, 1 });
    fit = bvarFit(y, ctl=ho.ctl);

    // The same search with every series centred at 1 (the default).
    ho_rw = bvarHyperopt(y, p=4);

With GDP growth centred at 0 the search chooses an overall tightness of
about 0.25, with a log marginal likelihood of -1367.5; with every series
centred at 1 it chooses about 0.33, with -1376.2. *ho.ctl* carries the prior
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

    ho = bvarHyperopt(data, ctl=ctl);

The overall, sum-of-coefficients and single-unit-root tightness and the
lag decay are chosen together.

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

*ho.status* = "at_bound" means the objective keeps rising toward the edge
of the search range, so the returned overall tightness is that edge, not a
peak. At the lower edge the data favour shrinking the coefficients all the
way to the prior mean; at the upper edge the prior hardly matters. The
printout says so, and *ho.converged* is 0. *ho.ctl* still holds the edge
value: check *ho.status* before fitting with it.

To evaluate the choice on forecasts, use :func:`bvarRollingOrigin` with
*choose_tightness="map"*, which repeats the choice on each forecast
origin's data. Pass it the same *lag1_prior_mean*: its default is
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

.. seealso:: Functions :func:`bvarFit`, :func:`bvarControlCreate`, :func:`bvarGlp2015ControlCreate`, :func:`bvarRollingOrigin`
