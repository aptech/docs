
ssKalmanSmooth
==============================================

Purpose
----------------

Fixed-interval (Rauch-Tung-Striebel) smoother for a time-invariant state space model -- given the filtered state estimates from a forward Kalman filter pass, computes smoothed state estimates that also use information from every later observation, not just observations up to and including the current period. Runs a standard backward recursion from the last period down to the first, using the filtered state/covariance at each period together with the one-step-ahead prediction into the following period.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** ``rsltOrY`` is now an ordinary
   required parameter rather than a "dynamic argument"; it was never
   optional, and it still accepts either a :class:`kalmanResult` or a
   data matrix, positionally, exactly as in 1.0.0. See
   :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: { a_TS, p_TS } = ssKalmanSmooth(ssm, rsltOrY)

    :param ssm: a filled instance of an :class:`ssModel` structure (e.g. ``sOut.ssmFinal`` after :func:`ssFit`).
    :type ssm: Struct

    :param rsltOrY: EITHER an instance of a :class:`kalmanResult` structure (typically ``sOut.kfResults`` from a prior :func:`ssFit` call, or the return of :func:`ssKalmanFilter`) -- its filtered state/covariance are reused directly, with no refiltering. OR an nobs x k_endog data matrix, in which case the ordinary (non-diffuse) Kalman filter is run first internally, using ``a_0 = 0`` and ``p_0 = 10e6*I`` (a "big-K" approximate diffuse prior, NOT the exact diffuse filter) -- see Remarks.
    :type rsltOrY: struct or Matrix

    :return a_TS: Matrix, k_states x nobs, smoothed state means.
    :rtype a_TS: Matrix

    :return p_TS: Array, nobs x k_states x k_states, smoothed state covariances.
    :rtype p_TS: Array

Examples
----------------

::

    new;
    library cmlmt, tsmt, sslib;

    // Load data
    fname = getGAUSShome $+ "pkgs/tsmt/examples/enders_sim2.dat";
    y = loadd(fname);
    y = y[., "ar2"];

    // Set up parameter vector and start values
    param_vec_st = asDF(zeros(3, 1), "param");

    param_vec_st[1] = -0.322;
    param_vec_st[2] = 0.433;
    param_vec_st[3] = 0.0025;

    // Declare shape
    k_endog = 1;
    k_states = 2;
    k_posdef = 1;

    // Declare control structure
    struct ssControl ssctl;
    ssCtl = ssControlCreate(k_states, k_endog);

    // Set fixed parameters of model
    ssctl.ssm.Z = { 1 0 };
    ssctl.ssm.R[1, 1] = 1;

    // Parameter names
    ssCtl.param_names = "phi1"$|"phi2"$|"sigma2";

    // Constraint variables
    ssCtl.stationary_vars = 1|2;
    ssCtl.positive_vars = 3;

    // Call ssFit function
    struct ssOut sOut;
    sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

    // Reuse the Kalman filter results already computed by ssFit --
    // no refiltering
    { a_TS, p_TS } = ssKalmanSmooth(sOut.ssmFinal, sOut.kfResults);

    // Set up procedure for updating SS model
    // structure
    proc (0) = updateSSModel(struct ssModel *ssmod, param);

      // Set up kalman filter matrices
      ssmod->T =  param[1 2]'|(1~0);
      ssmod->Q[1, 1] = param[3];

    endp;

Remarks
-------

This function should be called after the :class:`ssOut` structure has been filled by :func:`ssFit`, passing ``sOut.kfResults`` so the already-computed filtered states are reused directly. Passing the raw data matrix instead re-runs the ordinary Kalman filter with an approximate ("big-K") diffuse prior rather than the exact diffuse filter :func:`ssFit` itself would have used under ``ssCtl.init == "diffuse"`` -- for a model fit that way, prefer passing ``sOut.kfResults`` over passing ``y``.

:func:`ssKalmanSmoothTVP` (``sstvp.src``) generalizes the same backward recursion to a time-varying-parameter model.

Source
------

sskalman.src

.. seealso:: Functions :func:`ssFit`, :func:`ssKalmanSmoothTVP`, :func:`ssKalmanFilter`
