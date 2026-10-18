
ssFitTVP
==============================================

Purpose
----------------

Estimates parameters of a time-varying-parameter state-space model using Kalman filtering and maximum likelihood estimation -- the time-varying-parameter (TVP) analogue of :func:`ssFit`.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration, and the
   optional argument below is a keyword argument that may be supplied by
   name. The positional order is unchanged from 1.0.0. See
   :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: out = ssFitTVP(&updateTVPModel, param_vec, y [, ssctl])

    :param &updateTVPModel: pointer to a procedure that specifies how to update the time-varying state space system matrices. Takes the same two arguments as :func:`ssFit`'s update procedure -- a pointer to the model structure, and the parameter vector -- except the first argument is a :class:`tvpModel`, not an :class:`ssModel`. See Remarks.
    :type &updateTVPModel: function pointer

    :param param_vec: Contains starting values for parameters to be estimated. This parameter vector is used in the ``updateTVPModel`` procedure to update the state space system matrices.
    :type param_vec: Vector

    :param y: Matrix, nobs x k_endog, observed data.
    :type y: Matrix

    :param ssctl: Optional keyword argument, default ``{}``, an instance of an :class:`ssControl` structure. Normally an instance is initialized by calling ``ssControlCreate(k_states, k_endog, k_posdef, nobs)`` (``nobs > 1`` allocates ``ssctl.tvp`` instead of ``ssctl.ssm``). For an instance named *sctl*, the relevant members are:

        .. list-table::
            :widths: auto

            * - sctl.param_names
              - String array, parameter names.
            * - sctl.stationary_vars
              - Vector, specifies the index of the variables which should be constrained stationary.
            * - sctl.positive_vars
              - Vector, specifies the index of the variables which should be constrained positive.
            * - sctl.init
              - String, Kalman filter initialization mode: ``"diffuse"`` (default), ``"stationary"``, or ``"mixed"`` -- see :func:`ssFit` for what each means. The TVP filters support all three identically.
            * - sctl.stationary_states
              - Only used when sctl.init is ``"mixed"`` -- see :func:`ssFit`.
            * - sctl.gradproc
              - Optional, pointer to a procedure supplying an analytic gradient (see Remarks). Leaving this unset (the default) changes nothing -- CMLMT numerically differentiates the likelihood as usual.
            * - sctl.ctl
              - Instance of a :class:`cmlmtControl` structure, used for fine-tuning maximum likelihood estimation. Further information is provided in the CMLMT documentation. One field is reinterpreted rather than passed straight through: ``sctl.ctl.trustRadius`` is treated as a step cap measured in the units of the parameters listed in *sctl.positive_vars*, by multiplying it by the largest absolute value among their starting values, floored at 1. CMLMT applies ``trustRadius`` as an **absolute** per-element bound on the search direction, but a variance parameter's raw value is ``sqrt(sigma2)`` and so scales linearly with the data -- so an absolute cap makes the iteration count grow in proportion to the scale of ``y`` and eventually fail outright, even though rescaling ``y`` is a mathematically identical fit. The rescaling is exactly a no-op whenever those starting values are ``O(1)`` or smaller, is skipped entirely when *positive_vars* is unset, and leaves a missing scalar (CMLMT's documented "no trust region") alone.
            * - sctl.tvp
              - Instance of a :class:`tvpModel` structure. Same members as :class:`ssModel`, except ``Z``/``d``/``H``/``T``/``c``/``R``/``Q`` are each an *array* with one page per period. A scalar assigned to one of these members is applied to every period automatically. A non-scalar matrix that is constant over time must still be supplied as a genuine nobs-page array, with the same matrix on every page. Contains the following members:

                .. list-table::
                    :widths: auto

                    * - tvp.Z
                      - Array, nobs x k_endog x k_states, design matrix.
                    * - tvp.d
                      - Array, nobs x k_endog x 1, observation intercept.
                    * - tvp.H
                      - Array, nobs x k_endog x k_endog, observation disturbance covariance.
                    * - tvp.T
                      - Array, nobs x k_states x k_states, transition matrix.
                    * - tvp.c
                      - Array, nobs x k_states x 1, state intercept.
                    * - tvp.R
                      - Array, nobs x k_states x k_posdef, selection matrix.
                    * - tvp.Q
                      - Array, nobs x k_posdef x k_posdef, state disturbance covariance.
                    * - tvp.a_0
                      - Matrix, k_states x 1, initial prior state mean.
                    * - tvp.p_0
                      - Matrix, k_states x k_states, initial prior state covariance.

    :type ssctl: struct

    :return out: an instance of an :class:`ssOut` structure. Same fields as :func:`ssFit`'s output, with two differences: the fitted model is returned in ``sOut.tvpFinal`` (a :class:`tvpModel`), not ``sOut.ssmFinal``, and post-estimation on the fitted model needs :func:`ssIRFTVP`/:func:`ssPredictTVP`/:func:`ssPredictSETVP` (which freeze the time-varying system at one period before delegating to the time-invariant post-estimation procedures), not :func:`ssIRF`/:func:`ssPredict`/:func:`ssPredictSE`.
    :rtype out: struct

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

    // Declare shape
    k_endog = 1;
    k_states = 1;
    k_posdef = 1;

    // Declare control structure
    struct ssControl ssctl;
    ssctl = ssControlCreate(k_states, k_endog, k_posdef, nobs);

    // Set fixed system matrices -- Z is genuinely time-varying, the
    // rest are constant (wrapped to every period automatically)
    ssctl.tvp.Z = buildZ(nobs);
    ssctl.tvp.T = 1;
    ssctl.tvp.c = 0;
    ssctl.tvp.R = 1;
    ssctl.tvp.d = 0;

    // Parameter names
    ssctl.param_names = "sigma2_h"$|"sigma2_q";
    ssctl.positive_vars = 1|2;

    // Set up procedure for updating tvpModel structure
    proc (0) = updateTVPModel(struct tvpModel *tvpmod, param);
        tvpmod->H = param[1];
        tvpmod->Q = param[2];
    endp;

    // Call ssFitTVP function
    struct ssOut sOut;
    sOut = ssFitTVP(&updateTVPModel, { 0.3, 0.3 }, y, ssctl);

Remarks
-------

The update procedure only needs to specify the system matrices that actually vary with the estimated parameters, same as :func:`ssFit`. A member left untouched keeps whatever ``ssctl.tvp`` already held (typically set by the caller before calling :func:`ssFitTVP`, for any matrix that is fixed rather than estimated). A scalar assigned to an array member is applied to every period, but a non-scalar constant must be supplied as a genuine nobs-page array (for example built with ``arrayinit`` and filled page by page, as ``buildZ`` does in the example above), since GAUSS does not perform that promotion itself.

**Analytic gradients.** ``sctl.gradproc`` is supported exactly as in :func:`ssFit` -- a second procedure of the same shape as ``updateTVPModel``, but filling in a :class:`tvpModelGrad` (the derivatives of each system matrix, at each period, with respect to each parameter) instead of a :class:`tvpModel`. Supported for every ``sctl.init`` mode (``"diffuse"``, ``"stationary"``, ``"mixed"``) and alongside a ``stationary_vars``/``positive_vars`` transform, the same way :func:`ssFit`'s analytic gradients are.

**Standard errors with transformed parameters.** When ``stationary_vars`` or ``positive_vars`` is set, CMLMT estimates the raw, unconstrained parameters, and ``sOut.covpar`` (also ``sOut.mleResults.covPar``) and ``sOut.mleResults.waldlimits`` are converted to the units of ``sOut.final_params`` by the delta method, ``J*covPar*J'``, with ``J`` the Jacobian of the transform at the estimates; no further likelihood evaluation is made. The Wald limits use CMLMT's own formula, ``final_params -/+ cdftci(alpha/2, numObs - k) * se``, with ``alpha = sctl.ctl.alpha`` (0.05 by default). A row and column of ``covpar`` (and that parameter's Wald limits) are missing when CMLMT could not estimate the raw parameter's variance, or when a ``positive_vars`` variance is numerically on its zero boundary: its t-ratio ``final_params[p]/se`` is at most 5e-4. Standard asymptotics do not hold on a boundary, and the delta-method standard error there only reflects where the optimizer stopped. The rule is scale-free, but how close to zero CMLMT gets before it stops depends on the scale of the data, so on badly scaled data a zero variance can still come back unmasked with a tiny standard error. Up to version 2.1.0 these quantities came from a second CMLMT run without the transform, which could fail (a missing ``covpar``, or a ``G0518`` abort) when a variance was estimated at zero.

Source
------

sstvp.src

.. seealso:: Functions :func:`ssFit`, :func:`ssControlCreate`, :func:`ssIRFTVP`, :func:`ssPredictTVP`, :func:`ssPredictSETVP`, :func:`ssKalmanSmoothTVP`
