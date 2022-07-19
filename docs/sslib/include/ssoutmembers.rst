.. list-table::
    :widths: auto

    * - sctl.final_params
      - String array, parameter names.
    * - sctl.resid
      - Vector, specifies the index of the variables which should be constrained stationary.
    * - sctl.fitted
      - Vector, specifies the index of the variables which should be constrained positive.
    * - sctl.df_model
      - Vector, specifies the index of the variables which should be constrained positive.
    * - sctl.df_resid
      - Vector, specifies the index of the variables which should be constrained positive.
    * - sctl.numObs
      - Vector, specifies the index of the variables which should be constrained positive.
    * - sctl.mleResults
      - Instance of a `cmlmtResults` structure, used for fine-tuning maximum likelihood   estimation. Further information provided in the `cmlmt` documentation.
    * - sctl.kfResults
      - Instance of a `kalmanOut` structure, contains the results from the :func:`kalmanFilter`.

        .. list-table::
            :widths: auto

            * - kout.filtered_state
              - Matrix, k_endog x numObs, filtered states.
            * - kout.filtered_state_cov
              - Array, numObs x k_endog x k_endog, filtered state covariances.
            * - kout.predicted_state
              - Matrix, k_endog x (numObs+1), predicted states.
            * - kout.predicted_state_cov
              - Array, numObs x k_endog x k_endog, predicted state covariances.
            * - kout.forecast
              - Matrix, k_endog x numObs, forecasts.
            * - kout.forecast_error
              - Matrix, k_endog x numObs, forecast error.
            * - kout.forecast_error_cov
              - Array, numObs x k_endog x k_endog, forecast error covariances.
            * - kout.loglikelihood
              - Matrix, k_endog x (numObs+1), computed loglikelihood.
    * - sctl.ssmFinal
      - Instance of a `ssModel` structure, contains the state space system matrices used in the :func:`kalmanFilter`. Contains the following members:

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
