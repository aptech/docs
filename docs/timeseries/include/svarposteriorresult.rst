.. list-table::
   :widths: auto

   * - sir.irf_median
     - Array of (n_ahead+1) mxm matrices, posterior median impulse responses. ``sir.irf_median[h+1][i, j]`` is the median response of variable i to shock j at horizon h.

   * - sir.irf_bands
     - Array of :class:`credibleBand` structures. Default length 2 (68% and 90%). Access via ``sir.irf_bands[1].level``, ``sir.irf_bands[1].lower``, ``sir.irf_bands[1].upper``. Each ``.lower`` and ``.upper`` is an array of (n_ahead+1) mxm matrices.

   * - sir.cirf_median
     - Array of (n_ahead+1) mxm matrices, posterior median cumulative IRF.

   * - sir.cirf_bands
     - Array of :class:`credibleBand` structures. Default length 2 (68% and 90%). Access via ``sir.cirf_bands[1].level``, ``sir.cirf_bands[1].lower``, ``sir.cirf_bands[1].upper``. Each ``.lower`` and ``.upper`` is an array of (n_ahead+1) mxm matrices.

   * - sir.fevd_median
     - Array of (n_ahead+1) mxm matrices, posterior median FEVD. Each row sums to 1.0.

   * - sir.fevd_bands
     - Array of :class:`credibleBand` structures. Default length 2 (68% and 90%). Access via ``sir.fevd_bands[1].level``, ``sir.fevd_bands[1].lower``, ``sir.fevd_bands[1].upper``. Each ``.lower`` and ``.upper`` is an array of (n_ahead+1) mxm matrices.

   * - sir.n_attempted
     - Scalar, total posterior draws attempted.

   * - sir.n_accepted
     - Scalar, draws that yielded a valid rotation.

   * - sir.accept_rate
     - Scalar, acceptance rate (n_accepted / n_attempted).

   * - sir.n_ahead
     - Scalar, number of horizons.

   * - sir.m
     - Scalar, number of variables.

   * - sir.var_names
     - Mx1 string array, variable names.
