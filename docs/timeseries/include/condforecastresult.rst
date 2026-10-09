.. list-table::
   :widths: auto

   * - cfc.median
     - hxm matrix, pointwise median of the simulated paths. For a VAR fit the shocks use its selected *sigma* and the trend is continued automatically.

   * - cfc.lower
     - hxm matrix, lower edge of the first band in *cfc.bands*.

   * - cfc.upper
     - hxm matrix, upper edge of the first band in *cfc.bands*.

   * - cfc.level
     - Scalar, central mass of the first band.

   * - cfc.bands
     - Array of :class:`credibleBand` structures, one per requested level: *level*, *lower*, *upper*, *q_lower*, *q_upper*.

   * - cfc.levels
     - Vector, the requested central masses.

   * - cfc.effect
     - hxm matrix, scenario effect: for each parameter draw, the expected path with the conditions minus the expected path without them; pointwise median across draws.

   * - cfc.effect_bands
     - Array of :class:`credibleBand` structures, bands of the scenario effect.

   * - cfc.draws
     - (n_draws*h)xm matrix, every simulated path when *store_draws* = 1 (rows (d-1)*h+1 to d*h belong to path d); empty otherwise.

   * - cfc.effect_draws
     - (n_draws*h)xm matrix, every draw's scenario effect when *store_draws* = 1, same layout; empty otherwise.

   * - cfc.forecast_dates
     - hx1 vector, dates of the forecast steps when the fit is dated; empty otherwise.

   * - cfc.freq
     - String, frequency of the dates.

   * - cfc.h
     - Scalar, forecast horizon.

   * - cfc.m
     - Scalar, number of variables.

   * - cfc.n_draws
     - Scalar, number of simulated paths.

   * - cfc.constraint_path
     - hxm matrix, the path as given: missing values are free cells.

   * - cfc.averages
     - Nx3 matrix, the conditions on averages as given; empty if none.

   * - cfc.average_vars
     - Nx1 vector, the variable number of each averages row.

   * - cfc.method
     - String, "posterior draws" (:func:`bvarFit`) or "fixed coefficients" (:func:`varFit`).

   * - cfc.max_condition_residual
     - Scalar, the largest relative miss of any condition over all paths.

   * - cfc.seed
     - Scalar, the seed used.

   * - cfc.xreg_future
     - hxK matrix, future user exogenous values as supplied, without the generated VAR trend; empty if none.

   * - cfc.var_names
     - Mx1 string array, variable names.
