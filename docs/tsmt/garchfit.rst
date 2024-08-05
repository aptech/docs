garchFit
========

Purpose
-------
Estimates univariate GARCH model.

Format
------

.. function:: gOut = garchFit(y, p [, q, gctl])
              gOut = garchFit(y, x, p [, q, gctl])
              gOut = garchFit(dataset, formula, p [, q, gctl])

   :param y: dependent variables.
   :type y: Matrix

   :param x: independent variables.
   :type x: Matrix

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. ``"y ~ X1 + X2"`` 'y' is the name of dependent variable, '``X1``' and '``X2``' are names of independent variables; E.g. ``"y ~ ."`` , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param p: order of the GARCH parameters.
   :type p: scalar

   :param q: Optional input. order of the ARCH parameters.
   :type q: scalar

   :param gctl: Optional input. :class:`garchControl` structure.

      .. include:: include/garchcontrol.rst

   :type gctl: struct

   :return gOut: :class:`garchEstimation` structure containing the following members:

      .. include:: include/garchestimation.rst

   :rtype gOut: struct


Example
-------

::

   new;
   cls,;
   library tsmt;

   y = loadd(getGAUSSHome("pkgs/tsmt/examples/garch.dat"));

   struct garchEstimation gOut;
   gOut = garchFit(y, 1, 1);


This prints the following output:

:: 

  ================================================================================
  Model:                   GARCH(1,1)          Dependent variable:               Y
  Time Span:                  Unknown          Valid cases:                    300
  ================================================================================
                               Coefficient            Upper CI            Lower CI

            beta0[1,1]             0.01208            -0.00351             0.02768 
            garch[1,1]             0.15215            -0.46226             0.76655 
            arch[1,1]              0.18499             0.01761             0.35236 
            omega[1,1]             0.01429             0.00182             0.02675 
  ================================================================================

                  AIC:                                                   315.54085 
                  LRS:                                                   307.54085

Library
-------
tsmt

Source
------
tsgarch.src

.. seealso:: Functions :func:`garchMFit`, :func:`garchGJRFit`
