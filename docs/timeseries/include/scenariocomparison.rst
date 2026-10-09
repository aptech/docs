.. list-table::
   :widths: auto

   * - sc.baseline
     - :class:`condForecastResult` of the first scenario (without stored draws); the VAR branch uses the fit's selected *sigma* and automatically extends its trend.

   * - sc.alternative
     - :class:`condForecastResult` of the second scenario (without stored draws).

   * - sc.unconditional
     - hxm matrix, the model's own forecast with no assumed path: the :func:`bvarForecast` median for a :func:`bvarFit` result, the :func:`varForecast` point forecast for a :func:`varFit` result.

   * - sc.difference
     - hxm matrix, pointwise median across draws of the alternative's expected path minus the baseline's.

   * - sc.difference_bands
     - Array of :class:`credibleBand` structures, bands of the difference, one per level.

   * - sc.difference_draws
     - (n_draws*h)xm matrix, every draw's difference when *store_draws* = 1 (rows (d-1)*h+1 to d*h belong to draw d); empty otherwise.

   * - sc.levels
     - Vector, the central masses of the bands.

   * - sc.fixed_coefficients
     - Scalar, 1 for a :func:`varFit` result (the difference has no coefficient uncertainty), 0 otherwise.

   * - sc.n_draws
     - Scalar, number of draws.

   * - sc.seed
     - Scalar, the seed used.

   * - sc.names
     - 2x1 string array, the scenario names.

   * - sc.var_names
     - Mx1 string array, variable names.

   * - sc.shown
     - Vector, the variable numbers printed.

   * - sc.label
     - String, title of the printed tables.

   * - sc.units
     - String, units shown in the titles.

   * - sc.forecast_dates
     - hx1 vector, dates of the forecast steps when the fit is dated; empty otherwise.

   * - sc.freq
     - String, frequency of the dates.

   * - sc.period_labels
     - hx1 string array, the period labels printed (for example 2020Q1).
