.. list-table::
   :widths: auto

   * - sir.irf_median
     - Array of (n_ahead+1) mxm matrices, posterior median impulse responses. ``sir.irf_median[h+1][i, j]`` is the median response of variable i to shock j at horizon h.

   * - sir.irf_lower_68
     - Array of (n_ahead+1) mxm matrices, lower 68% credible band (16th percentile).

   * - sir.irf_upper_68
     - Array of (n_ahead+1) mxm matrices, upper 68% credible band (84th percentile).

   * - sir.irf_lower_90
     - Array of (n_ahead+1) mxm matrices, lower 90% credible band (5th percentile).

   * - sir.irf_upper_90
     - Array of (n_ahead+1) mxm matrices, upper 90% credible band (95th percentile).

   * - sir.cirf_median
     - Array of (n_ahead+1) mxm matrices, posterior median cumulative IRF.

   * - sir.cirf_lower_68
     - Array of (n_ahead+1) mxm matrices, lower 68% cumulative IRF band.

   * - sir.cirf_upper_68
     - Array of (n_ahead+1) mxm matrices, upper 68% cumulative IRF band.

   * - sir.cirf_lower_90
     - Array of (n_ahead+1) mxm matrices, lower 90% cumulative IRF band.

   * - sir.cirf_upper_90
     - Array of (n_ahead+1) mxm matrices, upper 90% cumulative IRF band.

   * - sir.fevd_median
     - Array of (n_ahead+1) mxm matrices, posterior median FEVD. Each row sums to 1.0.

   * - sir.fevd_lower_68
     - Array of (n_ahead+1) mxm matrices, lower 68% FEVD band.

   * - sir.fevd_upper_68
     - Array of (n_ahead+1) mxm matrices, upper 68% FEVD band.

   * - sir.fevd_lower_90
     - Array of (n_ahead+1) mxm matrices, lower 90% FEVD band.

   * - sir.fevd_upper_90
     - Array of (n_ahead+1) mxm matrices, upper 90% FEVD band.

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

   * - sir.shock_names
     - Mx1 string array, shock labels.
