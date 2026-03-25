.. list-table::
   :widths: auto

   * - fc.forecasts
     - hxm matrix, point forecasts. hx1 for univariate (ARIMA), hxm for multivariate (VAR/BVAR).

   * - fc.se
     - hxm matrix, forecast standard errors.

   * - fc.lower
     - hxm matrix, lower confidence or credible bound.

   * - fc.upper
     - hxm matrix, upper confidence or credible bound.

   * - fc.level
     - Scalar, confidence or credible level used (e.g., 0.95).

   * - fc.h
     - Scalar, forecast horizon.

   * - fc.m
     - Scalar, number of variables (1 for ARIMA).

   * - fc.var_names
     - Mx1 string array, variable names. Empty for univariate models.
