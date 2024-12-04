garchMFit
=========

Purpose
-------
Estimates GARCH-in-mean model.

Format
------
.. function:: gOut = garchMFit(y, p [, q, gctl])
              gOut = garchMFit(y, x, p [, q, gctl])
              gOut = garchMFit(dataset, formula, p [, q, gctl])

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

      .. include:: include/garchcontrol.rst

   :type gCtl: struct

   :return gOut: :class:`garchEstimation` structure.

      .. include:: include/garchestimation.rst

   :rtype out1: struct

Example
-------
::
  
  new;
  library tsmt;


  // Declare 'c1' to be a garchControl struct
  // and fill with default values
  struct garchControl c1;
  c1 = garchControlCreate();

  // Assign pointer to procedure (defined below)
  // to apply settings for internal optimization
   c1.sqpsolvemtControlProc = &sqp;

  proc sqp(struct sqpsolvemtControl c0);
    c0.printiters = 0;
    c0.trustRadius = 0;
    c0.feasibletest = 0;
    c0.gradproc = 0;
    retp(c0);
  endp;

  struct garchEstimation gOut;
  gOut = garchMFIT(__FILE_DIR $+ "garchx.gdat" ,"Y ~ X1 + X2", 1, 1, c1);

This prints the following out:

::
  
  ================================================================================
  Model:                  GARCHM(1,1)          Dependent variable:               Y
  Time Span:                  Unknown          Valid cases:                   1000
  ================================================================================
                               Coefficient            Upper CI            Lower CI

            beta0[1,1]             0.02920            -0.01682             0.07522 
             beta[1,1]             0.40281             0.39450             0.41111 
             beta[2,1]             0.50075             0.49216             0.50934 
            garch[1,1]             0.11534            -0.21655             0.44723 
             arch[1,1]             0.25821             0.14992             0.36650 
            delta[1,1]            -0.07041            -0.39261             0.25179 
            omega[1,1]             0.01378             0.00702             0.02054 
  ================================================================================

                  AIC:                                                  1040.04992 
                  LRS:                                                  1026.04992
                
Library
-------
tsmt

Source
------
tsgarch.src

.. seealso:: Functions :func:`garchFit`, :func:`garchGJRFit`, :func:`igarchFit`
