autoregFit
==========

Purpose
-------
Estimates coefficients of a regression model with autoregressive errors of any specified order.

Format
------
.. function:: aro = autoregFit(y, x, lagvars, order[, arc])
              aro = autoregFit(dataset, formula, lagvars, order[, arc])

   :param y: data.
   :type y: Nx1 vector

   :param x: independent data.
   :type x: Nxk vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. ``"y ~ X1 + X2"`` 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. ``"y ~ ."`` , ``.`` means including all variables except dependent variable 'y';
   :type formula: string

   :param lagvars: the number of periods to lag the variables inindvars. If there are no lagged variables, set to scalar 0. The variables in indvars will be lagged the number of periods indicated in the corresponding entries inlagvars. The dependent variable in depvar can be included in indvars can be repeated if each corresponding entry in lagvars is a different value.
   :type lagvars: Kx1 vector

   :param order: order of the autoregressive process; must be greater than 0 and less than the number of observations.
   :type order: scalar

   :param arc: Optional input. Instance of an :class:`automtControl` structure. The following members of arc are referenced within this routine:

      .. list-table::
         :widths: auto

         * - arc.const
           - scalar. If 1, constant will be used in model; else not. Default = 1.
         * - arc.init
           - scalar. If 1, only initial estimates will be computed. Default = 0.
         * - arc.iter
           - scalar. If 0, iteration information will not be printed. If 1, iteration information will be printed (arc.outputmust be nonzero). Default = 0.
         * - arc.maxvec
           - scalar, the maximum number of elements allowed in any one matrix. Default = 20000.
         * - arc.output
           - scalar, if nonzero, results are printed to screen. Default = 1.
         * - arc.tol
           - scalar, convergence tolerance. Default = 1e-5.

   :type arc: struct

   :return aro: An instance of an :class:`automtOut` structure containing the following members:

      .. list-table::
         :widths: auto

         * - aro.acor
           - (L+1)x1 vector, autocorrelations.
         * - aro.acov
           - (L+1)x1 vector, autocovariances.
         * - aro.chisq
           - scalar, -2\* log-likelihood.
         * - aro.coefs
           - Kx1 vector, estimated regression coefficients.
         * - aro.phi
           - Lx1 vector, lag coefficients.
         * - aro.rsq
           - scalar, explained variance.
         * - aro.sigsq
           - scalar, variance of white noise error.
         * - aro.tobs
           - scalar, number of observations.
         * - aro.vcb
           - KxK matrix, covariance matrix of estimated regression coefficients.
         * - aro.vcphi
           - LxL matrix, covariance matrix of *phi*.
         * - aro.vsig
           - scalar, variance of aro.sigsq (variance of the variance of white noise error).
         * - aro.tsmtDesc 
           - An instance of the :class:`tsmtModelDesc` structure containing the following members:
  
             .. include:: tsmt/include/tsmtmodeldesc.rst

         * - aro.sumStats 
           - An instance of the :class:`tsmtSummaryStats` structure containing the following members:
  
             .. include:: tsmt/include/tsmtsummarystats.rst

         * - aro.ll
           - Scalar, the model log-likelihood. 
         * - aro.aic 
           - Scalar, the model AIC.
         * - aro.sbc 
           - Scalar, the model SBC.
            
   :rtype aro: struct


Examples
--------

Data matrices
++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   //Load data
   data = loadd(getGAUSSHome("pkgs/tsmt/examples/autoregmt.dat"));
   y = data[., 1];
   x = data[., 2 3];

   //Lag of independent variables
   lag_vars = 0;

   //Autoregressive order
   order = 3;

   //Initialized automtOut structure
   struct automtOut aro;

   //Call autoregFit function
   aro = autoregFit(y, x, lag_vars, order);

The final results are:

::

  ML ESTIMATES        
  ================================================================================
  Model:                   AUTOREG(3)          Dependent variable:               Y
  Time Span:                  Unknown          Valid cases:                    200
  SSE:                        484.481          Degrees of freedom:             197
  Log Likelihood:             554.456          RMSE:                         1.556
  AIC:                      -1102.912          SEE:                          1.568
  SBC:                      -1093.017          Durbin-Watson:                0.664
  R-squared:                    0.231          Rbar-squared:                 0.219
  ================================================================================

  COEFFICIENTS OF INDEPENDENT VARIABLES (beta)                
  Coefficient                Estimate      Std. Err.        T-Ratio     Prob |>| t
  ================================================================================

  CONSTANT                     -0.267          0.516         -0.516          0.606 
  X1                            0.503          0.060          8.341          0.000 
  X2                            0.592          0.059          9.975          0.000 
  ================================================================================

  AUTOREGRESSIVE PARAMETERS (phi)                             
  Lag                        Estimate      Std. Err.        T-Ratio     Prob |>| t
  ================================================================================

  Y L(1)                        0.246          0.066          3.744          0.000 
  Y L(2)                        0.264          0.065          4.033          0.000 
  Y L(3)                        0.368          0.066          5.603          0.000 
  ================================================================================

  AUTOCORRELATIONS AND AUTOCOVARIANCES    
  Lag                 Autocovariances         Autocorrelations
  ============================================================

  L(0)                         2.323                    1.000 
  L(1)                         1.564                    0.673 
  L(2)                         1.573                    0.677 
  L(3)                         1.655                    0.713 


Dataset and formula string
++++++++++++++++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   // Lag of independent variables
   lag_vars = 0;

   // Autoregressive order
   order = 3;

   // Initialized automtOut structure
   struct automtOut aro;

   // Call autoregFit function
   aro = autoregFit(getGAUSSHome("pkgs/tsmt/examples/autoregmt.dat"), "Y ~ X1 + X2", lag_vars, order);

The results printed to screen are:

::

  ML ESTIMATES        
  ================================================================================
  Model:                   AUTOREG(3)          Dependent variable:               Y
  Time Span:                  Unknown          Valid cases:                    200
  SSE:                        484.481          Degrees of freedom:             197
  Log Likelihood:             554.456          RMSE:                         1.556
  AIC:                      -1102.912          SEE:                          1.568
  SBC:                      -1093.017          Durbin-Watson:                0.664
  R-squared:                    0.231          Rbar-squared:                 0.219
  ================================================================================

  COEFFICIENTS OF INDEPENDENT VARIABLES (beta)                
  Coefficient                Estimate      Std. Err.        T-Ratio     Prob |>| t
  ================================================================================

  CONSTANT                     -0.267          0.516         -0.516          0.606 
  X1                            0.503          0.060          8.341          0.000 
  X2                            0.592          0.059          9.975          0.000 
  ================================================================================

  AUTOREGRESSIVE PARAMETERS (phi)                             
  Lag                        Estimate      Std. Err.        T-Ratio     Prob |>| t
  ================================================================================

  Y L(1)                        0.246          0.066          3.744          0.000 
  Y L(2)                        0.264          0.065          4.033          0.000 
  Y L(3)                        0.368          0.066          5.603          0.000 
  ================================================================================

  AUTOCORRELATIONS AND AUTOCOVARIANCES    
  Lag                 Autocovariances         Autocorrelations
  ============================================================

   L(0)                         2.323                    1.000 
   L(1)                         1.564                    0.673 
   L(2)                         1.573                    0.677 
   L(3)                         1.655                    0.713 

Remarks
-------
This program will handle only datasets that fit in memory.

All autoregressive parameters are estimated up to the specified lag.
You cannot estimate only the first and fourth lags, for instance.

The algorithm will fail if the model is not stationary at the
estimated parameters. Thus, in that sense it automatically tests for
stationarity.


Library
-------
tsmt

Source
------
autoregmt.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaSS`, :func:`arimaControlCreate`
