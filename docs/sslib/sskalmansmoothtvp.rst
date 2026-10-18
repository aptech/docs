
ssKalmanSmoothTVP
==============================================

Purpose
----------------

:func:`ssKalmanSmooth` (the fixed-interval / Rauch-Tung-Striebel smoother) generalized to a time-varying-parameter model, exactly as the time-varying Kalman filter used by :func:`ssFitTVP` generalizes the time-invariant one: the same backward recursion, but ``T``/``c``/``R``/``Q`` are looked up fresh at each period instead of held fixed. :func:`ssFitTVP`'s own filtering step already gives correctly time-varying FILTERED estimates; this function turns those into SMOOTHED (full-sample, not just real-time-causal) estimates -- the time-varying-parameter counterpart to :func:`ssKalmanSmooth`.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** ``rsltOrY`` is now an ordinary
   required parameter rather than a "dynamic argument"; it was never
   optional, and it still accepts either a :class:`kalmanResult` or a
   data matrix, positionally, exactly as in 1.0.0. See
   :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: { a_TS, p_TS } = ssKalmanSmoothTVP(tvpm, rsltOrY)

    :param tvpm: a filled instance of a :class:`tvpModel` structure (e.g. ``sOut.tvpFinal`` after :func:`ssFitTVP`) -- ``Z``, ``d``, ``H``, ``T``, ``c``, ``R``, ``Q`` (each either a constant or a genuine nobs-page array), and ``a_0``/``p_0``.
    :type tvpm: Struct

    :param rsltOrY: EITHER an instance of a :class:`kalmanResult` structure (typically ``sOut.kfResults`` from a prior :func:`ssFitTVP` call) -- its filtered state/covariance are reused directly, with no refiltering. OR an nobs x k_endog data matrix, in which case the ordinary (non-diffuse) time-varying Kalman filter is run first internally using ``tvpm``'s own ``a_0``/``p_0``. For a model that needs exact diffuse initialization, pass ``sOut.kfResults`` from :func:`ssFitTVP` instead, which was computed with the filter selected by ``ssCtl.init``.
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

    // Local level model with a known break in Z after period 30
    y = loadd(getGAUSSHome("pkgs/sslib/examples/tvp_local_level.csv"), "y");
    nobs = rows(y);

    proc (1) = buildZ(nobs);
        local a, i;
        a = arrayinit(nobs|1|1, 0);
        for i(1, 30, 1);
            a[i,.,.] = 1.0;
        endfor;
        for i(31, nobs, 1);
            a[i,.,.] = 1.5;
        endfor;
        retp(a);
    endp;

    struct ssControl ssctl;
    ssctl = ssControlCreate(1, 1, 1, nobs);
    ssctl.tvp.Z = buildZ(nobs);
    ssctl.tvp.T = 1;
    ssctl.tvp.c = 0;
    ssctl.tvp.R = 1;
    ssctl.tvp.d = 0;
    ssctl.tvp.H = 0.25;
    ssctl.param_names = "Q";
    ssctl.positive_vars = 1;

    proc (0) = updateTVPModel(struct tvpModel *tvpmod, param);
        tvpmod->Q = param[1];
    endp;

    struct ssOut sOut;
    sOut = ssFitTVP(&updateTVPModel, { 0.3 }, y, ssctl);

    // Reuse the Kalman filter results already computed by ssFitTVP --
    // no refiltering
    { a_TS, p_TS } = ssKalmanSmoothTVP(sOut.tvpFinal, sOut.kfResults);

Remarks
-------

The RTS backward recursion itself is unchanged from :func:`ssKalmanSmooth` -- at each period ``i`` (working backward from ``nobs-1`` to 1), the one-step-ahead prediction into period ``i+1`` uses period ``i``'s OWN ``T``/``c``/``R``/``Q`` (matching the filter's own convention: the transition FROM period ``i``), so a genuinely time-varying ``T`` means each backward step uses different smoother gain matrices, not a single fixed one.

Validated two ways: (1) against :func:`ssKalmanSmooth` itself on a model whose "time-varying" matrices are actually constant across every period (must match exactly); (2) against an independent numpy RTS-smoother implementation on a model with a genuine break in ``T``, confirming smoothed estimates properly differ from filtered ones and that the smoothed path is uniformly tighter (lower variance) than the filtered path, as RTS smoothing theory requires -- see ``test/sstvpsmooth.inc``.

Source
------

sstvp.src

.. seealso:: Functions :func:`ssFitTVP`, :func:`ssKalmanSmooth`, :func:`ssIRFTVP`, :func:`ssPredictTVP`
