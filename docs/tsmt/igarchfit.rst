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

   :param gCtl: Optional input, :class:`garchControl` structure.

      .. list-table::
         :widths: auto

         * - c0.density
           - scalar, density of error term:
           
             0 - Normal
             
             1 - Student's t
             
             3 - skew generalized t. 

         * - c0.asymmetry
           - scalar, if nonzero assymetry terms are added. 
         * - c0.inmean
           - scalar, GARCH-in-mean, square root of conditional variance is included in the mean equation. 
         * - c0.stConstraintsType
           - scalar, type of enforcement of stationarity requirements:
           
             1 - roots of characteristic polynomial constrained outside unit circle
             
             2 - arch, GARCH parameters constrained to sum to less than one and greater than zero
             
             3 - none.

         * - c0.cvConstraintsType
           - scalar, type of enforcement of nonnegative conditional variances:
           
             0 - direct constraints
             
             1 - Nelson & Cao constraints.

         * - c0.covType
           - scalar, type of covariance matrix of parameters:
           
             1 - ML
             
             2 - QML
             
             3 - none. 

   :type c0: struct

   :return out1: :class:`garchEstimation` structure.

      .. list-table::
         :widths: auto

         * - out1.aic
           - scalar, Akiake criterion.
         * - out1.bic
           - scalar, Bayesian information criterion. 
         * - out1.lrs
           - scalar, likelihood ratio statistic. 
         * - out1.numObs
           - scalar, number of observations. 
         * - out1.df
           - scalar, degrees of freedom. 
         * - out1.par
           - instance of PV structure containing parameter estimates. 
         * - out1.retcode
           - scalar, return code. out1.moment KxK matrix, moment m?atrix of parameter estimates.

             :1: normal convergence. 
             :2: forced exit. 
             :3: function calculation failed. 
             :4: gradient calculation failed. 
             :5: Hessian calculation failed. 
             :6: line search failed. 
             :7: error with constraints. 
             :8: function complex.

         * - out1.moment
           - KxK matrix, moment matrix of parameter estimates.
         * - out1.climits
           - Kx2 matrix, confidence limits. 
     
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
