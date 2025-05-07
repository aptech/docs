garchGJRFit
===========

Purpose
-------
Estimates asymmetric GJR-GARCH model.

Library
-------
tsmt

Format
------
.. function:: gOut = garchGJRFit(y, p [, q, gctl]);
              gOut = garchGJRFit(y, p [, q, gctl]);
              gOut = garchGJRFit(dataset, formula, p [, q, gctl]);


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

          .. include:: tsmt/include/garchcontrol.rst

      :type c0: struct

      :return gOut: :class:`garchEstimation` structure containing the following members:

          .. include:: tsmt/include/garchestimation.rst

      :rtype gOut: struct


Example
-------

::

  new;
  cls,;
  library tsmt;

  y = loadd( getGAUSSHome("pkgs/tsmt/examples/gjrgarch_data.gdat"));

  // GARCH control structure
  struct garchControl gctl;
  gctl = garchControlCreate;

  // Set pointer to function to 
  // control optimization settings
  gctl.sqpsolvemtControlproc = &prc;

  // Set covariance type to be 
  // Quasi-Maximum Likelihood
  gctl.covtype = 2;

  // Control sqpSolveMT optimization
  proc prc(struct sqpSolveMTControl c0);
      c0.printiters = 10;
      retp(c0);
  endp;

  // GARCH order
  p = 1;

  // ARCH order
  q = 1;

  // Estimate model
  struct garchEstimation gOut;
  gOut = garchgjrFit(y, p, q, gCtl);

This prints the following output:

:: 

  ================================================================================
  Model:               GJR-GARCH(1,1)          Dependent variable:               Y
  Time Span:              1980-01-20:          Valid cases:                   1000
                          1982-10-15                                              
  ================================================================================
                               Coefficient            Upper CI            Lower CI

          beta0[1,1]               0.01089             0.00323             0.01855 
          garch[1,1]               0.11990            -0.15034             0.39015 
           arch[1,1]               0.10397             0.01426             0.19367 
            tau[1,1]               0.21660             0.07062             0.36259 
          omega[1,1]               0.01100             0.00694             0.01506 
  ================================================================================

                AIC:                                                  1316.65106 
                LRS:                                                  1306.65106

Source
------
tsgarch.src

.. seealso:: Functions :func:`garchFit`, :func:`garchMFit`, :func:`igarchFit`
