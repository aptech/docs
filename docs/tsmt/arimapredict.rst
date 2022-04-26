============
arimaPredict
============

10.0.5arimaPredict
==================

Purpose
-------

.. container::
   :name: Purpose

   Estimates forecasts using estimation results obtained from arimaFit.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   f = arimaPredict(b, y, e, h);

Input
-----

.. container::
   :name: Input

   = =======================================================
   b K×1 vector, estimated coefficients                       
   y N×1 vector, data.                                        
   e N×1 vector, residuals reported by arimamt program.       
   h scalar, the number of step-ahead forecasts to computer.  
   = =======================================================

Output
------

.. container::
   :name: Output

   = =========== =================================
   f h×3 matrix, 
     [ ., 1]     Lower forecast confidence bounds.
     [ ., 2]     Forecasts.
     [ ., 3]     Upper forecast confidence bounds.
   = =========== =================================

Remarks
-------

.. container::
   :name: Remarks

   Data must be transformed before being sent to arimaPredict.

   arimaPredict does not compute forecasts for models with fixed
   regressors.

Example
-------

.. container::
   :name: Example

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

Source
------

.. container:: gfunc
   :name: Source

   forecastmt.src
