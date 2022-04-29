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

   //Simulate data
   seed = 423458;
   y = simarmamt(.3, 1, 0, 2, 0, 250, 1, .5, seed);

   //Integrated series    
   z = cumsumc(y);                       

   //Declare arima out structures
   struct arimamtOut amo;

   //Set AR order
   p = 1;

   //Set order of differencing
   d = 1;

   //Estimate model
   amo = arimaFit(z, p, d);

   //Forecast model
   f =  arimaPredict(amo.b, z, amo.e, 25);

Remarks
-------
Data must be transformed before being sent to arimaPredict.

arimaPredict does not compute forecasts for models with fixed regressors.

Library
-------
tsmt

Source
------
forecastmt.src
