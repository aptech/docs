.. list-table::
   :widths: auto

   * - irf.median
     - Array of (n_ahead+1) mxm matrices, posterior median impulse responses.

   * - irf.bands
     - Array of :class:`credibleBand` structures. Default length 2 (68% and 90%). Access via ``irf.bands[1].level``, ``irf.bands[1].lower``, ``irf.bands[1].upper``. Each ``.lower`` and ``.upper`` is an array of (n_ahead+1) mxm matrices.

   * - irf.n_ahead
     - Scalar, number of horizons computed.

   * - irf.m
     - Scalar, number of variables.

   * - irf.n_draws
     - Scalar, number of posterior draws used.

   * - irf.var_names
     - Mx1 string array, variable names.
