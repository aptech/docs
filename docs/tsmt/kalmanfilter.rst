kalmanFilter
============

Purpose
-------
Data filtering algorithm.

Format
------
.. function:: kout = kalmanFilter(y, Z, d, H, T, c, R, Q, a_0, p_0)

   :param yt: numerical vector of times series data.
   :type yt: px1 matrix

   :param Z: design matrix.
   :type Z: pxM matrix

   :param d: observation intercept.
   :type d: px1 matrix

   :param H: observation disturbance covariance.
   :type H: pxp matrix

   :param T: transition matrix.
   :type T: mxm matrix

   :param c: state intercept.
   :type c: px1 matrix

   :param R: selection matrix.
   :type R: mxr matrix

   :param Q: state disturbance covariance matrix.
   :type Q: rxr matrix

   :param a_0: initial prior state mean.
   :type a_0: mx1 matrix

   :param p_0: initial prior covariance matrix.
   :type p_0: mxm matrix

   :return kout: Instance of a :class:`kalmanOut` structure. The following members of *kout* are referencing within this routine:

      .. list-table::
         :widths: auto

         * - kout.filtered_state
           - Matrix, pxT, filtered states.
         * - kout.filtered_state_cov
           - Array, Txpxp, filtered state covariances.
         * - kout.predicted_state
           - Matrix, px(T+1), predicted states.
         * - kout.predicted_state_cov
           - Array, Txpxp, predicted state covariances.
         * - kout.forecast
           - Matrix, pxT, forecasts.
         * - kout.forecast_error
           - Matrix, pxT, forecast error.
         * - kout.forecast_error_cov
           - Array, Txpxp, forecast error covariances.
         * - kout.loglikelihood
           - Matrix, px(T+1), computed loglikelihood.

   :rtype kout: struct


Example
-------

::

   new;
   cls;
   library tsmt;

   // Load data
   y = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/nile.dat");

   // Set up state space matrices
   sigma_e = 15099;
   sigma_n = 1469.1;

   // Linear level model
   Z = 1;
   H = sigma_e;
   T = 1;
   Q = sigma_n;
   R = 1;
   d = 0;
   c = 0;

   // Initial state variables
   a_0 = 0;
   p_0 = 10e7;

   struct kalmanResult rslt;
   rslt = kalmanFilter(y', Z, d, H, T, c, R, Q, a_0, p_0);

Remarks
-------

The kalman filter inputs are based on the state space representation:

- :math:`y_t = d_t + Z_t\alpha_t + \epsilon_t`
- :math:`\epsilon_t \sim N(0, H_t)`
- :math:`\alpha_{t+1} = c_t + T_t\alpha_t + R\eta_t`
- :math:`\eta_t \sim N(0, Q_t)`

where the :math:`y_t` equation is known as the observation or
measurement equation, and the :math:`\alpha_t+1` equation is the transition
equation.

Library
-------
tsmt

Source
------
kalman_filter.src
