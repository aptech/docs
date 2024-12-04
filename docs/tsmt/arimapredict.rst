arimaPredict
============

Purpose
-------
Estimates forecasts using estimation results obtained from :func:`arimaFit`.

Format
------
.. function:: f = arimaPredict(b, y, e, h)

   :param b: estimated coefficients
   :type b: Kx1 vector

   :param y: data.
   :type y: Nx1 vector

   :param e: residuals reported by arimamt program.
   :type e: Nx1 vector

   :param h: the number of step-ahead forecasts to computer.
   :type h: scalar

   :return f:

      .. list-table::
         :widths: auto

         * - :math:`[.,1]`
           - Lower forecast confidence bounds.
         * - :math:`[.,2]`
           - Forecasts.
         * - :math:`[.,3]`
           - Upper forecast confidence bounds.

   :rtype f: hx3 matrix


Example
-------

::

   new;
   cls;
   library tsmt;

   // Simulate data
   seed = 423458;
   y = simarmamt(.3, 1, 0, 2, 0, 250, 1, .5, seed);

   // Integrated series
   z = cumsumc(y);

   // Declare arima out structures
   struct arimamtOut amo;

   // Set AR order
   p = 1;

   // Set order of differencing
   d = 1;

   // Estimate model
   amo = arimaFit(z, p, d);

   // Forecast model
   f = arimaPredict(amo, z, 25);

The first five forecasts printed to the screen are:

::

  Forecasts for ARIMA(1,1,0) Model.   95% Confidence Interval Computed.

  Period      LCL        Forecasts        UCL     Forecast Std. Err.
   251    480.694133    481.751067    482.808002      0.539262
   252    481.268540    483.021519    484.774499      0.894394
   253    482.000099    484.313042    486.625985      1.180095
   254    482.830115    485.611374    488.392633      1.419036
   255    483.724926    486.911907    490.098888      1.626041

Remarks
-------
*  Data must be transformed before being sent to :func:`arimaPredict`.
*  The :func:`arimaPredict` procedure does not compute forecasts for models with fixed regressors.

Library
-------
tsmt

Source
------
forecastmt.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaSS`, :func:`simarmamt`
