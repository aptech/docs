igarchFit
=========

Purpose
-------
Estimates integrated GARCH model, i.e., a model containing a unit root.

Format
------
.. function:: gOut = igarchFit(y, p [, q, gCtl])
              gOut = igarchFit(y, x, p [, q, gCtl])
              gOut = igarchFit(dataset, formula, p [, q, gCtl])

   :param y: dependent variables.
   :type y: Matrix

   :param x: independent variables.
   :type x: Matrix

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. "y ~ X1 + X2" 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. "y ~ ." , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param p: order of the GARCH parameters.
   :type p: scalar

   :param q: Optional input, order of the ARCH parameters.
   :type q: scalar

   :param gctl: Optional input, :class:`garchControl` structure.

      .. include:: tsmt/include/garchcontrol.rst

   :type gCtl: struct

   :return gOut: :class:`garchEstimation` structure.

      .. include:: tsmt/include/garchestimation.rst

   :rtype out1: struct


Example
-------
::

   new;
   cls;
   library tsmt;

   y = loadd(getGAUSSHome("pkgs/tsmt/examples/igarch.dat"));

   struct garchEstimation gOut;
   gOUt = igarchFit(y, 1, 1); 

This prints the following output:

::

  ================================================================================
  Model:                 I-GARCH(1,1)          Dependent variable:               Y
  Time Span:                  Unknown          Valid cases:                    300
  ================================================================================
                               Coefficient            Upper CI            Lower CI

            beta0[1,1]             0.02710            -0.04224             0.09644 
            garch[1,1]             0.81404             0.71688             0.91120 
             arch[1,1]             0.18596             0.06604             0.30587 
            omega[1,1]             0.01468            -0.00739             0.03675 
  ================================================================================

                  AIC:                                                  -635.63652 
                  LRS:                                                  -643.63652

Library
-------
tsmt

Source
------
tsgarch.src
