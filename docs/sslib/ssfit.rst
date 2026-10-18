
ssFit
==============================================

Purpose
----------------

Estimates parameters of a state-space model using Kalman filtering and maximum likelihood estimation.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration, and the
   optional argument below is a keyword argument that may be supplied by
   name. The positional order is unchanged from 1.0.0. See
   :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: sOut = ssFit(&updateSSModel, param_vec, y [, ssctl])

    :param &updateSSModel: pointer to a procedure that specifies how to update the state space system matrices. See Remarks.
    :type &updateSSModel: function pointer

    :param param_vec: Contains starting values for parameters to be estimated. This parameter vector is passed to the ``updateSSModel`` procedure to update the state space system matrices.
    :type param_vec: Vector

    :param y: Matrix, nobs x k_endog, observed data. Missing values are allowed.
    :type y: Matrix

    :param ssctl: Optional keyword argument, default ``{}``, an instance of an :class:`ssControl` structure. Normally an instance is initialized by calling :func:`ssControlCreate` and members of this instance can be set to other values by the user. For an instance named *sctl*, the members are:

     .. list-table::
        :widths: auto

        * - sctl.param_names
          - String array, parameter names.
        * - sctl.stationary_vars
          - Vector, specifies the index of the variables which should be constrained stationary.
        * - sctl.positive_vars
          - Vector, specifies the index of the variables which should be constrained positive.
        * - sctl.init
          - String, Kalman filter initialization mode: ``"diffuse"`` (default, every state treated as diffuse, using the exact diffuse Kalman filter), ``"stationary"`` (initializes at the unconditional/stationary state variance -- requires a stationary model), or ``"mixed"`` (some states diffuse, others at their own unconditional/stationary variance -- see sctl.stationary_states).
        * - sctl.stationary_states
          - Only used when sctl.init is ``"mixed"``. Vector, indices (1 .. k_states) of the states that should be initialized at their unconditional/stationary variance instead of diffusely; every other state is initialized diffusely. The listed states must evolve independently of the diffuse ones (the corresponding block of T must be zero).
        * - sctl.gradproc
          - Optional, pointer to a procedure supplying an analytic gradient (see Remarks). Leaving this unset (the default) changes nothing -- CMLMT numerically differentiates the likelihood as usual.
        * - sctl.likelihoodburn
          - Scalar, default 1. Number of leading periods :func:`ssResidDiagnostics` excludes from its residual-based tests.
        * - sctl.ctl
          - Instance of a :class:`cmlmtControl` structure, used for fine-tuning maximum likelihood estimation. Further information provided in the CMLMT documentation. One field is reinterpreted rather than passed straight through: ``sctl.ctl.trustRadius`` is treated as a step cap measured in the units of the parameters listed in *sctl.positive_vars*, by multiplying it by the largest absolute value among their starting values, floored at 1. CMLMT applies ``trustRadius`` as an **absolute** per-element bound on the search direction, but a variance parameter's raw value is ``sqrt(sigma2)`` and so scales linearly with the data -- so an absolute cap makes the iteration count grow in proportion to the scale of ``y`` and eventually fail outright, even though rescaling ``y`` is a mathematically identical fit. The rescaling is exactly a no-op whenever those starting values are ``O(1)`` or smaller, is skipped entirely when *positive_vars* is unset, and leaves a missing scalar (CMLMT's documented "no trust region") alone.
        * - sctl.ssm
          - Instance of an :class:`ssModel` structure, contains the state space system matrices. :func:`ssControlCreate` fills every matrix with zeros of the right size. Contains the following members:

            .. list-table::
                :widths: auto

                * - ssm.Z
                  - k_endog x k_states, design matrix.
                * - ssm.d
                  - k_endog x 1, observation intercept.
                * - ssm.H
                  - k_endog x k_endog, observation disturbance covariance.
                * - ssm.T
                  - k_states x k_states, transition matrix.
                * - ssm.c
                  - k_states x 1, state intercept.
                * - ssm.R
                  - k_states x k_posdef, selection matrix.
                * - ssm.Q
                  - k_posdef x k_posdef, state disturbance covariance.
                * - ssm.a_0
                  - k_states x 1, initial prior state mean.
                * - ssm.p_0
                  - k_states x k_states, initial prior state covariance.

    :type ssctl: struct

    :return sOut: an instance of an :class:`ssOut` structure. For an instance named *sOut*, the members are:

      .. list-table::
        :widths: auto

        * - sOut.final_params
          - Vector, k_params x 1, final parameter estimates, in the units the update procedure receives (after any ``stationary_vars``/``positive_vars`` transform).
        * - sOut.covpar
          - Matrix, k_params x k_params, covariance matrix of the parameter estimates (see Remarks).
        * - sOut.resid
          - Matrix, nobs x k_endog, one-step-ahead forecast errors.
        * - sOut.fitted
          - Matrix, nobs x k_endog, one-step-ahead predictions of y based on the final parameter estimates.
        * - sOut.likelihoodburn
          - Scalar, number of leading periods excluded from the residual diagnostics (copied from *sctl.likelihoodburn*).
        * - sOut.df_model
          - Scalar, degrees of freedom of the model (number of estimated parameters).
        * - sOut.df_resid
          - Scalar, degrees of freedom of the residuals.
        * - sOut.numObs
          - Scalar, number of observations.
        * - sOut.mleResults
          - Instance of a :class:`cmlmtResults` structure. Further information provided in the CMLMT documentation.
        * - sOut.kfResults
          - Instance of a :class:`kalmanResult` structure, contains the Kalman filter results at the final parameter estimates.

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

        * - sOut.ssmFinal
          - Instance of an :class:`ssModel` structure, contains the state space system matrices at the final parameter estimates. Its members have the same dimensions as *sctl.ssm* above.
        * - sOut.aic
          - Scalar, model Akaike's information criterion.
        * - sOut.aicc
          - Scalar, model corrected Akaike's information criterion.
        * - sOut.bic
          - Scalar, model Schwarz' Bayesian information criterion.
        * - sOut.hqic
          - Scalar, model Hannan-Quinn information criterion.
        * - sOut.lrs
          - Scalar, likelihood-ratio statistic.
        * - sOut.ssy
          - Scalar, sum of squares total (deviations of y from the mean of y).
        * - sOut.sse
          - Scalar, sum of squared errors.
        * - sOut.mse
          - Scalar, mean squared error.
        * - sOut.rsquared
          - Scalar, model R-squared.
        * - sOut.ljung_box
          - Vector, k_endog x 1, Ljung-Box Q-test for autocorrelation.
        * - sOut.ljung_box_pval
          - Vector, k_endog x 1, p-value of the Ljung-Box Q-test for autocorrelation.
        * - sOut.hetero_test
          - Vector, k_endog x 1, test statistic for the null hypothesis of no heteroskedasticity.
        * - sOut.hetero_test_pval
          - Vector, k_endog x 1, p-value of the test for the null hypothesis of no heteroskedasticity.
        * - sOut.jb_stat
          - Vector, k_endog x 1, the Jarque-Bera goodness-of-fit test on model residuals.
        * - sOut.jb_pval
          - Vector, k_endog x 1, p-value of the Jarque-Bera goodness-of-fit test.
        * - sOut.standardized_forecast_errors
          - Matrix, nobs x k_endog, standardized forecast errors used in all residual diagnostics.
        * - sOut.skew
          - Vector, k_endog x 1, sample skewness of the standardized forecast errors.
        * - sOut.kurtosis
          - Vector, k_endog x 1, sample kurtosis of the standardized forecast errors.
        * - sOut.structural
          - Instance of an :class:`ssStructuralInfo` structure. :func:`ssFit` sets ``sOut.structural.is_structural = 0``; the other members are only filled by :func:`ssStructuralTS`.

    :rtype sOut: struct

Examples
----------------

::

    new;
    library cmlmt, tsmt, sslib;

    // Load data
    fname = getGAUSSHome("pkgs/tsmt/examples/enders_sim2.dat");
    y = loadd(fname, "ar2");

    // Starting values for phi1, phi2 and sigma2
    param_vec_st = asDF(-0.322|0.433|0.0025, "param");

    // Model dimensions
    k_states = 2;
    k_endog = 1;
    k_posdef = 1;

    // Control structure filled with default values. No preceding
    // `struct ssControl ssctl;` declaration is needed.
    ssctl = ssControlCreate(k_states, k_endog, k_posdef);

    // Fixed system matrices
    ssctl.ssm.Z = { 1 0 };
    ssctl.ssm.R = { 1, 0 };

    // Parameter names
    ssctl.param_names = "phi1"$|"phi2"$|"sigma2";

    // Constrain phi1 and phi2 to stationarity, sigma2 to be positive
    ssctl.stationary_vars = 1|2;
    ssctl.positive_vars = 3;

    // Estimate the model
    sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

    // Procedure that places the parameters in the system matrices
    proc (0) = updateSSModel(struct ssModel *ssmod, param);
        ssmod->T = param[1 2]'|(1~0);
        ssmod->Q = param[3];
    endp;

The results printed to the screen begin with

::

    Return Code:                                                             0
    Log-likelihood:                                                     -21.26
    Number of Cases:                                                        99
    AIC:                                                                 48.52
    AICC:                                                                48.77
    BIC:                                                                 56.33
    HQIC:                                                                 47.1
    Covariance Method:                                    ML covariance matrix
    ==========================================================================

            Parameters         Estimates         Std. Err.            T-stat             Prob.          Gradient
    -------------------------------------------------------------------------------------------------------------
                  phi1            0.6845            0.0890            7.6913            0.0000            0.0000
                  phi2           -0.4639            0.0904           -5.1333            0.0000           -0.0000
                sigma2            0.0884            0.0126            6.9972            0.0000            0.0000

followed by the correlation matrix of the parameters, their Wald confidence limits, and the residual diagnostics.

Remarks
-------

The update function is a required user-provided procedure which specifies how the state space system matrices should be updated with the underlying model parameters.

The update function must always take the same inputs:

* A pointer to an :class:`ssModel` structure which contains the state space system matrices.
* A vector of parameters.

The update function should only specify system matrices which contain parameters, it should not specify fixed system matrices. Set the fixed matrices on *sctl.ssm* before calling :func:`ssFit`, as in the example above.

**Analytic gradients.** By default CMLMT numerically differentiates the whole likelihood to estimate a model's parameters. Setting ``sctl.gradproc`` to a pointer to a second update procedure lets :func:`ssFit` supply CMLMT an analytic gradient instead, which can be faster and more numerically robust for larger models. This second procedure takes the same two arguments as the model update procedure, but fills in an :class:`ssModelGrad` structure with the *derivatives* of each system matrix with respect to each parameter, instead of the matrices themselves. Each member (``dZ``, ``dd``, ``dH``, ``dT``, ``dc``, ``dR``, ``dQ``) is an array with one page per parameter, already sized and filled with zeros by :func:`ssFit`, so only the nonzero pages need to be set. For the model in the example above:

::

    proc (0) = updateSSModelGrad(struct ssModelGrad *dssmod, param);
        local dT, dQ, tmp;

        // A page of a structure member cannot be assigned in place
        // (dssmod->dT[1,.,.] = ... does not compile). Copy the array out,
        // assign its pages, then write it back.
        dT = dssmod->dT;
        tmp = { 1 0, 0 0 };     // d(T)/d(phi1)
        dT[1,.,.] = tmp;
        tmp = { 0 1, 0 0 };     // d(T)/d(phi2)
        dT[2,.,.] = tmp;
        dssmod->dT = dT;

        dQ = dssmod->dQ;
        dQ[3,.,.] = 1;          // d(Q)/d(sigma2)
        dssmod->dQ = dQ;

        // dZ, dd, dH, dc and dR keep their zero defaults: Z, d, H, c and R
        // do not depend on any parameter in this model.
    endp;

    ssctl.gradproc = &updateSSModelGrad;
    sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

Analytic gradients are supported for all three ``sctl.init`` modes (``"diffuse"``, the default, ``"stationary"``, and ``"mixed"``), and alongside ``stationary_vars``/``positive_vars`` transforms: ``updateSSModelGrad`` always differentiates with respect to the transformed parameters (the same ones ``updateSSModel`` receives), and :func:`ssFit` internally converts the result back to the raw, untransformed parameter space CMLMT is actually optimizing over via the chain rule, so no special handling is needed in ``updateSSModelGrad`` itself when a transform is active.

**Standard errors with transformed parameters.** When ``stationary_vars`` or ``positive_vars`` is set, CMLMT estimates the raw, unconstrained parameters, and ``sOut.covpar`` (also ``sOut.mleResults.covPar``) and ``sOut.mleResults.waldlimits`` are converted to the units of ``sOut.final_params`` by the delta method, ``J*covPar*J'``, with ``J`` the Jacobian of the transform at the estimates; no further likelihood evaluation is made. The Wald limits use CMLMT's own formula, ``final_params -/+ cdftci(alpha/2, numObs - k) * se``, with ``alpha = sctl.ctl.alpha`` (0.05 by default). A row and column of ``covpar`` (and that parameter's Wald limits) are missing when CMLMT could not estimate the raw parameter's variance, or when a ``positive_vars`` variance is numerically on its zero boundary: its t-ratio ``final_params[p]/se`` is at most 5e-4. Standard asymptotics do not hold on a boundary, and the delta-method standard error there only reflects where the optimizer stopped. The rule is scale-free, but how close to zero CMLMT gets before it stops depends on the scale of the data, so on badly scaled data a zero variance can still come back unmasked with a tiny standard error. Up to version 2.1.0 these quantities came from a second CMLMT run without the transform, which could fail (a missing ``covpar``, or a ``G0518`` abort) when a variance was estimated at zero.

Source
------

ssmain.src

.. seealso:: Functions :func:`ssControlCreate`, :func:`ssIRF`, :func:`ssPredict`, :func:`ssPredictSE`, :func:`ssKalmanSmooth`, :func:`ssFitTVP`
