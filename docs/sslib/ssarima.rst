ssARIMA
=======

Purpose
-------
Estimates ARIMA models using a state space representation, the Kalman filter, and maximum likelihood.

Format
------

.. function:: sOut = ssARIMA(y, p [, d, q, const, trend])

   :param y: data.
   :type y: Nx1 vector

   :param p: the autoregressive order.
   :type p: Scalar

   :param d: Optional argument, the order of differencing. Default = 0.
   :type d: Scalar

   :param q: Optional argument, the moving average order. Default = 0.
   :type q: Scalar

   :param const: Optional argument, an indicator variable to include a constant in the model. Set to 1 to include trend, 0 otherwise. Default = 0.
   :type const: Scalar

   :param trend: Optional argument, an indicator variable to include a trend in the model. Set to 1 to include trend, 0 otherwise. Default = 0.
   :type trend: Scalar

   :return sOut: an instance of an :class:`ssOut` structure. For an instance named *sOut*, the members are:

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

   :rtype sOut: Struct

Example
-------

::

 new;
 library tsmt, cmlmt, sslib;

 // Create file name with full path
 fname = __FILE_DIR $+ "wpi1.dat";

 // Load variable 'wpi' from 'wpi1.dat'
 y = loadd(fname, "wpi");

 // Model settings
 p = 1;
 d = 1;
 q = 1;
 trend = 0;
 const = 1;

 // Declare 'sOut' to be an ssOut structure
 // to hold the estimation results and then
 // estimate the model
 struct ssOut sOut;
 sOut = ssARIMA(y, p, d, q, const, trend);

The example above prints the following results

::

  Return Code:                                                             0
  Log-likelihood:                                                     -158.8
  Number of Cases:                                                       122
  AIC:                                                                 325.7
  AICC:                                                                  326
  BIC:                                                                 336.9
  HQIC:                                                                  324
  Covariance Method:                                    ML covariance matrix
 ==========================================================================

        Parameters         Estimates         Std. Err.            T-stat             Prob.          Gradient
 -------------------------------------------------------------------------------------------------------------
      phi : y[t-1]            0.8681            0.0550           15.7842            0.0000                 .
    theta : e[t-1]           -0.4059            0.1004           -4.0435            0.0001                 .
            Sigma2            0.5238            0.0530            9.8892            0.0000                 .
          Constant            0.8000            0.3204            2.4973            0.0125                 .

  Correlation matrix of the parameters
 --------------------------------------------------------------------------

      1.0000     -0.6201      0.0538     -0.3066
     -0.6201      1.0000      0.0077      0.0218
      0.0538      0.0077      1.0000     -0.1796
     -0.3066      0.0218     -0.1796      1.0000

  Model and residual diagnostics:
 ==========================================================================

  Ljung-Box (Q):                                                      0.0713
  Prob(Q):                                                             0.789
  Heteroskedasticity (H):                                               27.7
  Prob(H):                                                          1.77e-19
  Jarque-Bera (JB):                                                     10.2
  Prob(JB):                                                          0.00611
  Skew:                                                                0.288
  Kurtosis:                                                             4.29
 ==========================================================================

Source
------
ssarima.src

.. seealso:: Functions :func:`ssFit`, :func:`ssSARIMA`
