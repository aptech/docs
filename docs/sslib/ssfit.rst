
ssFit
==============================================

Purpose
----------------

Estimates parameters of a state-space model using Kalman filtering and maximum likelihood estimation.

Format
----------------
.. function:: out = ssFit(&updateSSModel, par, y [, ctl])

    :param &updateSSModel: pointer to a procedure that specifies how to update the state space system matrices. See remarks for further information.
    :type &updateSSModel: function pointer

    :param par: Contains starting values for parameters to be estimated. This parameter vector is used in the `updateSSModel` procedure to update the state space system matrices.
    :type par: Vector

    :param y: Observed data.
    :type y: Vector

    :param ctl: Optional input, instance of an :class:`ssControl` structure. Normally an instance is initialized by calling :func:`ssControlCreate` and members of this instance can be set to other values by the user. For an instance named *sctl*, the members are:

     .. list-table::
        :widths: auto

        * - sctl.param_names
          - String array, parameter names.
        * - sctl.stationary_vars
          - Vector, specifies the index of the variables which should be constrained stationary.
        * - sctl.positive_vars
          - Vector, specifies the index of the variables which should be constrained positive.
        * - sctl.ctl
          - Instance of a :class:`cmlmtControl` structure, used for fine-tuning maximum likelihood estimation. Further information provided in the `cmlmt` documentation.
        * - sctl.ssm
          - Instance of a :class:`ssModel` structure, contains the state space system matrices used in the :func:`kalmanFilter`. Contains the following members:

            .. list-table::
                :widths: auto

                * - ssm.Z
                  - k_endog x k_states, transition matrix.
                * - ssm.d
                  - k_endog x 1, observation intercept.
                * - ssm.H
                  - k_endog x k_endog, observation disturbance covariance.
                * - ssm.T
                  - k_states x k_states, design matrix.
                * - ssm.c
                  - k_states x k_states, state intercept.
                * - ssm.R
                  - k_states x k_posdef, selection matrix.
                * - ssm.Q
                  - k_states x k_posdef, state disturbance covariance.
                * - ssm.a_0
                  - k_states x 1, initial prior state mean.
                * - ssm.p_0
                  - k_states x k_states, initial prior state covariance.

    :type ctl: struct

    :return out: an instance of an :class:`ssOut` structure. For an instance named *sOut*, the members are:

      .. list-table::
        :widths: auto

        * - sOut.final_params
          - String array, final parameter estimates.
        * - sOut.resid
          - Vector, residuals.
        * - sOut.fitted
          - Vector, the fitted y values based on final parameter estimates.
        * - sOut.df_model
          - Vector, degrees of freedom of the model.
        * - sOut.df_resid
          - Vector, degrees of freedom of the residuals.
        * - sOut.numObs
          - Vector, number of observations.
        * - sOut.mleResults
          - Instance of a :class:`cmlmtResults` structure. Further information provided  in the `cmlmt` documentation.
        * - sOut.kfResults
          - Instance of a :class:`kalmanOut` structure, contains the results from the :func:`kalmanFilter`.

            .. list-table::
                :widths: auto

                * - kfResults.filtered_state
                  - Matrix, k_endog x numObs, filtered states.
                * - kfResults.filtered_state_cov
                  - Array, numObs x k_endog x k_endog, filtered state covariances.
                * - kfResults.predicted_state
                  - Matrix, k_endog x (numObs+1), predicted states.
                * - kfResults.predicted_state_cov
                  - Array, numObs x k_endog x k_endog, predicted state covariances.
                * - kfResults.forecast
                  - Matrix, k_endog x numObs, forecasts.
                * - kfResults.forecast_error
                  - Matrix, k_endog x numObs, forecast error.
                * - kfResults.forecast_error_cov
                  - Array, numObs x k_endog x k_endog, forecast error covariances.
                * - kfResults.loglikelihood
                  - Matrix, k_endog x (numObs+1), computed loglikelihood.

        * - sOut.ssmFinal
          - Instance of a :class:`ssModel` structure, contains the final state space system matrices used in the :func:`kalmanFilter`. Contains the following members:

            .. list-table::
                :widths: auto

                * - ssmFinal.Z
                  - k_endog x k_states, transition matrix.
                * - ssmFinal.d
                  - k_endog x 1, observation intercept.
                * - ssmFinal.H
                  - k_endog x k_endog, observation disturbance covariance.
                * - ssmFinal.T
                  - k_states x k_states, design matrix.
                * - ssmFinal.c
                  - k_states x k_states, state intercept.
                * - ssmFinal.R
                  - k_states x k_posdef, selection matrix.
                * - ssmFinal.Q
                  - k_states x k_posdef, state disturbance covariance.
                * - ssmFinal.a_0
                  - k_states x 1, initial prior state mean.
                * - ssmFinal.p_0
                  - k_states x k_states, initial prior state covariance.
        * - sOut.aic
          - Scalar, model Akaike's information criterion.
        * - sOut.aicc
          - Scalar, model corrected Akaike's information criterion.
        * - sOut.bic
          - Scalar, model Schwarz’ Bayesian information criterion.
        * - sOut.hqic
          - Scalar, model Hannan–Quinn information criterion.
        * - sOut.ssy
          - Scalar, sum of squares total (Deviations of y from mean of y).
        * - sOut.sse
          - Scalar, sum of squared errors.
        * - sOut.mse
          - Scalar, means squared errors.
        * - sOut.rsquared
          - Scalar, model r-squared.
        * - sOut.ljung_box
          - Scalar, Ljung-Box Q-test for autocorrelation.
        * - sOut.ljung_box_pval
          - Scalar, p-value of the Ljung-Box Q-test for autocorrelation.
        * - sOut.hetero_test
          - Scalar, tests for the null hypothesis of no heteroskedasticity.
        * - sOut.hetero_test_pval
          - Scalar, p-value of the test for the null hypothesis of no heteroskedasticity.
        * - sOut.jb_stat
          - Scalar, the Jarque-Bera goodness-of-fit test on model residuals.
        * - sOut.jb_stat_pval
          - Scalar, p-value ofthe Jarque-Bera goodness-of-fit test.
        * - sOut.standardized_forecast_errors
          - Scalar, standardized forecast errors used in all residual diagnostics.
        * - sOut.skew
          - Scalar, sample skewness of the standardized forecast errors.
        * - sOut.kurtosis
          - Scalar, sample kurtosis of the standardized forecast errors.
        * - sOut.irf
          - Scalar, model impulse response functions.
        * - sOut.forecasts
          - Scalar, forecasts.

    :rtype out: struct

Examples
----------------

::

    new;
    library cmlmt, tsmt, ssdev;

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
    struct ssControl ssCtl;
    ssCtl = ssControlCreate(k_states, k_endog);

    // Set fixed parameters of model
    ssCtl.ssm.Z = { 1 0 };
    ssCtl.ssm.R[1, 1] = 1;

    // Parameter names
    ssCtl.param_names = "phi1"$|"phi2"$|"sigma2";

    // Constraint variables
    ssCtl.stationary_vars = 1|2;
    ssCtl.positive_vars = 3;

    // Call ssFit function
    struct ssOut sOut;
    sOut = ssFit(&updateSSModel, param_vec_st, y, ssCtl);

    // Set up procedure for updating SS model
    // structure
    proc (0) = updateSSModel(struct ssModel *ssmod, param);

      // Set up kalman filter matrices
      ssmod->T =  param[1 2]'|(1~0);
      ssmod->Q[1, 1] = param[3];

    endp;

The results printed to screen are

::

  Return Code:                                                             0
  Log-likelihood:                                                      -38.3
  Number of Cases:                                                       100
  AIC:                                                                 82.59
  AICC:                                                                82.84
  BIC:                                                                 90.41
  HQIC:                                                                81.17
  Covariance Method:                                    ML covariance matrix
  ==========================================================================

  Parameters   Estimates   Std. Err.      T-stat       Prob.    Gradient
  --------------------------------------------------------------------------
        phi1      0.6845      0.0890      7.6913      0.0000      0.0000
        phi2     -0.4639      0.0904     -5.1333      0.0000      0.0000
      sigma2      0.0884      0.0126      6.9972      0.0000      0.0000

 Correlation matrix of the parameters
 --------------------------------------------------------------------------

      1.0000     -0.4756     -0.0132
     -0.4756      1.0000      0.0278
     -0.0132      0.0278      1.0000

 Wald 95% Confidence Limits
 --------------------------------------------------------------------------
  Parameters   Estimates Lower Limit Upper Limit    Gradient
 --------------------------------------------------------------------------
        phi1      0.6845     -0.6826     -0.3753      0.0000
        phi2     -0.4639      0.2657      0.7817      0.0000
      sigma2      0.0884      0.2552      0.3395      0.0000

 Model and residual diagnostics:
 ==========================================================================

 Ljung-Box (Q):                                                       0.024
 Prob(Q):                                                             0.877
 Heteroskedasticity (H):                                               1.04
 Prob(H):                                                             0.908
 Jarque-Bera (JB):                                                     6.34
 Prob(JB):                                                           0.0421
 Skew:                                                                0.021
 Kurtosis:                                                             1.76
 ==========================================================================

Remarks
-------

The update function is a required user-provided procedure which specifies how the state space system matrices should be updated with the underlying model parameters.

The update function must always take the same inputs:

* A pointer to a `ssModel` structure which contains the state space system matrices.
* A vector of parameters.

The update function should only specify system matrices which contain parameters, it should not specify fixed system matrices.

For example, we might have the following update function specifying how the parameters of a model should be placed in the state space matrices:

::

   proc (0) = updateSSModel(struct ssModel *ssmod, param);

    // Set up kalman filter matrices
    ssmod->T =  param[1 2]'|(1~0);
    ssmod->Q[1, 1] = param[3];

   endp;



Source
------

ssmain.src

.. seealso:: Functions :func:`ssControlCreate`, :func:`ssIRF`, :func:`ssPredicta`
