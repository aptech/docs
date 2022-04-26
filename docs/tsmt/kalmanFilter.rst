============
kalmanFilter
============

10.0.29kalmanFilter
===================

Purpose
-------

.. container::
   :name: Purpose

   Data filtering algorithm.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   out = kalmanFilter(y, Z, d, H, T, c, R, Q, a_0, p_0);

Input
-----

.. container::
   :name: Input

   === ===================================================
   yt  matrix, px1, numerical vector of times series data.
   Z   matrix, pxM, design matrix.
   d   matrix, px1, observation intercept.
   H   matrix, pxp, observation disturbance covariance.
   T   matrix, mxm, transition matrix.
   c   matrix, px1, state intercept.
   R   matrix, mxr, selection matrix.
   Q   matrix, rxr, state disturbance covariance matrix.
   a_0 matrix, mx1, initial prior state mean.
   p_0 matrix, mxm, initial prior covariance matrix.
   === ===================================================

Output
------

.. container::
   :name: Output

   +------+---------------------------+---------------------------+---+
   | kout | An instance of            |                           |   |
   |      | ankalmanOutstructure. The |                           |   |
   |      | following members ofkout  |                           |   |
   |      | are referenced within     |                           |   |
   |      | this routine:             |                           |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.filtered_state       | Matrix, pxT, filtered     |   |
   |      |                           | states.                   |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.filtered_state_cov   | Array, Txpxp, filtered    |   |
   |      |                           | state covariances.        |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.predicted_state      | Matrix, px(T+1),          |   |
   |      |                           | predicted states.         |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.predicted_state_cov  | Array, Txpxp, predicted   |   |
   |      |                           | state covariances.        |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.forecast             | Matrix, pxT, forecasts.   |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.forecast_error       | Matrix, pxT, forecast     |   |
   |      |                           | error.                    |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.forecast_error_cov   | Array, Txpxp, forecast    |   |
   |      |                           | error covariances.        |   |
   +------+---------------------------+---------------------------+---+
   |      | kout.loglikelihood        | Matrix, px(T+1), computed |   |
   |      |                           | loglikelihood.            |   |
   +------+---------------------------+---------------------------+---+

Remarks
-------

.. container::
   :name: Remarks

   The kalman filter inputs are based on the state space representation:

   .. image:: GeneratedImages/Equations/Equation698.svg
      :class: mcReset

   .. image:: GeneratedImages/Equations/Equation699.svg
      :class: mcReset

   .. image:: GeneratedImages/Equations/Equation700.svg
      :class: mcReset

   .. image:: GeneratedImages/Equations/Equation701.svg
      :class: mcReset

   where the |image1| equation is known as the observation or
   measurement equation, and the |image2| equation is the transition
   equation.

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Load data
      y = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/nile.dat");

      //Set up state space matrices
      sigma_e = 15099;
      sigma_n = 1469.1;

      //Linear level model
      Z = 1;
      H = sigma_e;
      T = 1;
      Q = sigma_n;
      R = 1;
      d = 0;
      c = 0;

      //Initial state variables
      a_0 = 0;
      p_0 = 10e7;

      struct kalmanResult rslt; 
      rslt = kalmanFilter(y', Z, d, H, T, c, R, Q, a_0, p_0);

Source
------

.. container:: gfunc
   :name: Source

   kalman_filter.src

.. |image1| image:: GeneratedImages/Equations/Equation702.svg
   :class: mcReset
.. |image2| image:: GeneratedImages/Equations/Equation703.svg
   :class: mcReset
