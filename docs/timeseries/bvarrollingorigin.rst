bvarRollingOrigin
=================

Purpose
-------
Evaluate Bayesian VAR forecasts out of sample: refit at a series of forecast origins and score the forecasts of the following periods, for several prior tightness values at once.

Format
------

.. function:: ev = bvarRollingOrigin(y, tightness, model_names, reestimation_policy, truth_vintage)
              ev = bvarRollingOrigin(y, tightness, model_names, "expanding", truth_vintage, p=2, initial_window=160, h=8)
              ev = bvarRollingOrigin(y, tightness, model_names, "expanding", truth_vintage, choose_tightness="map")

   :param y: the data, oldest row first. A single date column in a dataframe is used as the time index and left out of the model.
   :type y: TxM matrix or dataframe

   :param tightness: overall tightness of each fixed-tightness model. May be empty when *choose_tightness* is set.
   :type tightness: vector

   :param model_names: one label per value in *tightness*, plus one for the chosen model when *choose_tightness* is set.
   :type model_names: string array

   :param reestimation_policy: "expanding" (each origin's training window starts at the first row) or "rolling" (a window of *initial_window* rows that moves with the origin).
   :type reestimation_policy: string

   :param truth_vintage: a label for the data the forecasts are scored against (for example the database vintage), kept in the result.
   :type truth_vintage: string

   :param choose_tightness: Optional keyword. "" (default): fixed values only. "map" adds a model whose overall tightness is chosen again on each origin's training window, as :func:`bvarHyperopt` chooses it by default (log marginal likelihood plus a Gamma prior on the tightness, mode 0.2, standard deviation 0.4). "ml" chooses by the log marginal likelihood alone. The chosen model comes after the fixed ones.
   :type choose_tightness: string

   :param p: Optional keyword, lag order. Default = 1.
   :type p: scalar

   :param const: Optional keyword, 1 to include a constant. Default = 1.
   :type const: scalar

   :param initial_window: Optional keyword, number of rows in the first training window; the first forecast starts at row *initial_window* + 1. Required in practice: the default 0 is refused.
   :type initial_window: scalar

   :param h: Optional keyword, forecast horizon. Default = 1. The last origin leaves *h* rows to score.
   :type h: scalar

   :param step: Optional keyword, rows between forecast origins. Default = 1.
   :type step: scalar

   :param n_draws: Optional keyword, simulated paths per model and origin. Default = 5000.
   :type n_draws: scalar

   :param lag1_prior_mean: Optional keyword, prior mean of each variable's coefficient on its own first lag: ``"zero"``, ``"random_walk"`` (1), one number in [0,1] for every variable, or a vector with one number per variable. Default = ``"zero"`` (suits data in changes or growth rates; use ``"random_walk"`` for levels). It applies to every model, the fixed tightness values and a chosen tightness alike.
   :type lag1_prior_mean: string, scalar or Mx1 vector

   :param lag_decay: Optional keyword, Minnesota lag decay. Default = 1.
   :type lag_decay: scalar

   :param alpha0: Optional keyword, prior degrees of freedom of the residual covariance; 0 (default) uses *m* + 2.
   :type alpha0: scalar

   :param intercept_vc: Optional keyword, prior variance of the constants. Default = 1e7.
   :type intercept_vc: scalar

   :param residual_variance_policy: Optional keyword, how the prior's residual scales are estimated on each training window. Default = "arp_full_training".
   :type residual_variance_policy: string

   :param posterior_seed_base: Optional keyword, seed of the first origin's posterior draws; origin *k* uses *posterior_seed_base* + (*k* - 1) x *origin_seed_stride*. Every model at an origin uses the same seeds. Default = 120260723.
   :type posterior_seed_base: scalar

   :param pit_bins: Optional keyword, number of bins of the probability integral transform histograms. Default = 10.
   :type pit_bins: scalar

   :return ev: An instance of a :class:`bvarRollingResult` structure. The main members:

       .. list-table::
          :widths: auto

          * - ev.n_origins
            - Scalar, number of forecast origins.

          * - ev.origin_rows
            - n_origins x 1, the row at which each forecast starts.

          * - ev.origin_dates
            - n_origins x 1, the date at which each forecast starts; empty if *y* had no date column.

          * - ev.model_names
            - The model labels, fixed models first.

          * - ev.model_tightness
            - n_models x 1, each model's tightness; missing for the chosen model.

          * - ev.chosen_tightness
            - n_origins x 1, the tightness chosen at each origin; empty without *choose_tightness*.

          * - ev.status
            - n_origins x (1 + n_models), 0 where the cell succeeded; the first column is the least-squares VAR. A tightness search that does not converge or stops at the edge of its range (where :func:`bvarHyperopt` reports *status* "at_bound") is a fit failure (1), and its *chosen_tightness* entry is missing.

          * - ev.mean_crps
            - h x (n_models x m), the continuous ranked probability score averaged over origins; lower is better. Columns: model, then variable.

          * - ev.rmse
            - h x (n_models x m), root mean squared error of the forecast mean.

          * - ev.mean_log_score_loss
            - h x (n_models x m), average negative log predictive density.

          * - ev.ols_rmse
            - h x m, root mean squared error of the least-squares VAR forecast.

          * - ev.crps, ev.forecast_mean, ev.forecast_median, ev.actual
            - (n_origins x h) x ..., the same quantities origin by origin (rows: origin, then horizon).

          * - ev.interval68_lower, ev.interval68_upper, ev.interval90_lower, ev.interval90_upper
            - 68% and 90% central intervals, origin by origin.

          * - ev.summary_available
            - Scalar, 1 if every cell succeeded; the averages are missing otherwise, and *ev.summary_reason* says why.

   :rtype ev: struct

Examples
--------

Fixed Tightness Against the Marginal-Likelihood Choice
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Quarterly US data, 1960Q1-2019Q4: the date and six growth rates
    // (the default prior centre, lag1_prior_mean = "zero", suits growth rates)
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium_dated.csv"));
    y = data[., "date" "gdp" "cons" "inv" "defl" "wage" "hours"];

    // A forecast every fourth quarter from 2000Q1, eight quarters ahead
    string names = { "fixed 0.2", "tight 0.05", "chosen" };
    ev = bvarRollingOrigin(y, 0.2 | 0.05, names, "expanding", "FRED-QD 2026-02",
        p=2, initial_window=160, h=8, step=4, n_draws=1000, choose_tightness="map");

    print "Forecast origins:" ev.n_origins;
    print "Chosen tightness, first and last origin:" ev.chosen_tightness[1 ev.n_origins]';

    // CRPS of inflation (variable 4 of 6), one and eight quarters ahead,
    // by model (columns: model, then variable)
    print ev.mean_crps[1 8, 4 10 16];

The full comparison, with a guide, is the workflow
``examples/workflows/bvar_shrinkage_choice.e``.

Remarks
-------

At each origin every model is fitted on the training rows only: the prior's
residual scales, the posterior and, for the chosen model, the tightness are
all recomputed from those rows. Forecasts that start at consecutive origins
overlap, so the scores of different origins are not independent.

The chosen model at an origin is exactly the model with its tightness fixed
at the chosen value: the same prior, the same seeds, the same scores.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarHyperopt`, :func:`bvarFit`, :func:`bvarForecast`
