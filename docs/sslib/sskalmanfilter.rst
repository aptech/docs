
ssKalmanFilter
==============================================

Purpose
----------------

Runs the ordinary (non-diffuse) Kalman filter directly against a filled :class:`ssModel` structure and a caller-supplied initial state -- a thin public wrapper around this library's own fixed replacement for TSMT's ``kalmanFilter``. Most callers reach the Kalman filter indirectly, through :func:`ssFit`/:func:`ssStructuralTS`/:func:`ssARIMA`; this function is for filtering a model directly, outside of an :func:`ssFit` estimation loop -- e.g. to inspect filtered states/forecasts for a model whose parameters are already fixed (known, not estimated), or as a building block for a custom diagnostic.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration. See
   :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: kfResults = ssKalmanFilter(y, ssm, a_0, p_0)

    :param y: Matrix, nobs x k_endog, observed data.
    :type y: Matrix

    :param ssm: instance of an :class:`ssModel` structure -- ``Z`` (k_endog x k_states design matrix), ``d`` (k_endog x 1), ``H`` (k_endog x k_endog), ``T`` (k_states x k_states transition matrix), ``c`` (k_states x 1), ``R`` (k_states x k_posdef) and ``Q`` (k_posdef x k_posdef). ``a_0``/``p_0`` on ``ssm`` itself are not used; supply them as separate arguments instead.
    :type ssm: Struct

    :param a_0: k_states x 1, initial state mean.
    :type a_0: Vector

    :param p_0: k_states x k_states, initial state covariance.
    :type p_0: Matrix

    :return kfResults: an instance of a :class:`kalmanResult` structure. Same shape as ``sOut.kfResults`` after :func:`ssFit`:

        .. list-table::
            :widths: auto

            * - kfResults.filtered_state
              - Matrix, k_states x nobs, filtered states.
            * - kfResults.filtered_state_cov
              - Array, nobs x k_states x k_states, filtered state covariances.
            * - kfResults.predicted_state
              - Matrix, k_states x (nobs+1), predicted states.
            * - kfResults.predicted_state_cov
              - Array, (nobs+1) x k_states x k_states, predicted state covariances.
            * - kfResults.forecast
              - Matrix, k_endog x nobs, forecasts.
            * - kfResults.forecast_error
              - Matrix, k_endog x nobs, forecast errors.
            * - kfResults.forecast_error_cov
              - Array, nobs x k_endog x k_endog, forecast error covariances.
            * - kfResults.loglikelihood
              - Vector, nobs x 1, log-likelihood contribution of each period.

    :rtype kfResults: struct

Examples
----------------

::

    new;
    library cmlmt, tsmt, sslib;

    // Load data
    fname = getGAUSSHome("pkgs/tsmt/examples/enders_sim2.dat");
    y = loadd(fname, "ar2");

    // A known (not estimated) AR(2) model
    struct ssModel ssm;
    ssm.Z = { 1 0 };
    ssm.d = 0;
    ssm.H = 0;
    ssm.T = (0.68~-0.46)|(1~0);
    ssm.c = 0|0;
    ssm.R = 1|0;
    ssm.Q = 0.09;

    a_0 = 0|0;
    p_0 = 10e6*eye(2);

    // No `struct kalmanResult kfResults;` declaration is needed
    kfResults = ssKalmanFilter(y, ssm, a_0, p_0);

    // Filtered states, one column per period
    print kfResults.filtered_state[., 1:5];

Remarks
-------

Always uses the ORDINARY filter, regardless of whether a state is diffuse. A large ``p_0``, as in the example, approximates a diffuse prior. There is no public exact-diffuse counterpart of this procedure: to use the exact diffuse filter, estimate the model with :func:`ssFit` (``sctl.init = "diffuse"``, the default) and use ``sOut.kfResults``, which holds the filter results at the final estimates.

Source
------

sskalman.src

.. seealso:: Functions :func:`ssFit`, :func:`ssKalmanSmooth`
