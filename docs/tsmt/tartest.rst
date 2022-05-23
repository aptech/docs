tarTest
=======

Purpose
-------
Estimates the p\ :sup:`th` order threshold autoregression model.

Format
------
.. function:: TARout = tarTest(yt, tar0)

   :param yt: data. 
   :type yt: Nx1 vector

   :param tar0: :class:`TARControl` structure containing the following elements:

      .. list-table::
         :widths: auto

         * - p
           - scalar, Autoregressive order of the STAR model. 
         * - omit
           - scalar, Nx1 vector number of lags (below p) to omit from the matrix. 
         * - lowerQuantile
           - scalar, the lower quantile. 
         * - upperQuantile
           - scalar, the upper quantile. 
         * - rep
           - scalar, the number of simulation replications. 
         * - printOutput
           - scalar, 0 or 1, 1 prints output to the screen. 
         * - graph
           - scalar, 0 or 1, 1 turns on plotting. 
         * - dstart
           - scalar, start date of the time series in DT scalar format as used by plotTS. 
         * - freq
           - scalar, Data frequency, 12 for monthly, 4 for quarterly or 1 for annual. 

   :type tar0: struct

   :return TAROut: :class:`TAROut` structure containing the following return elements:

      .. list-table::
         :widths: auto

         * - tests
           - vector of test statistics (in order): SupLM, ExpLM, AveLM, SupLMs, ExpLMs, AveLMs. 
         * - pvalues
           - vector, estimated asymptotic p-values or test statistics. 
         * - coefficients
           - matrix, first column contains estimated coefficients and second column contains standard errors. 
         * - regimeErrorVariance
           - vector, 2x1, error variance for Regime 1 and Regime 2, respectively. 
         * - thresholdLag
           - scalar, threshold variable lag. 
         * - thresholdValue
           - scalar, threshold estimate. 
         * - errorVariance
           - scalar, threshold model error variance. 

   :rtype TAROut: struct


Example
-------

::

   new;
   cls;
   library tsmt;

   //Real GNP data 
   //Seasonally adjusted and transformed in annualized quarterly growth rates
   //1947-1990
   gnp = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/gnp_4790.fmt");
   yg = ln(gnp[., 1]);
   y = (yg[2:rows(yg)]-yg[1:rows(yg)-1])*400;

   //Declare the structure 
   struct TARControl tar0;


   //Initialize the structure 
   tar0 = TARControlCreate();

   //Maximum number of lags considered
   tar0.p = 5;

   //Lags to omit from the test
   omit = { 3, 4 };
   tar0.omit = omit;

   //Number of replications for Monte Carlo 
   tar0.rep = 5000;

   //Data start date and frequency
   tar0.dstart = 1947;
   tar0.freq = 4;

   //Run function
   struct TAROut tarfnl;
   tarfnl = tarTest( y, tar0 );


References
----------
#. Hansen, B.E. (1996). Inference when a nuisance parameter is nost identified under the null hypothesis, Econometrica, 64(2), 413-430.
#. Franses, P.H. and Dijk, D. (2000) Non-linear Time Series Models in Empirical Finance. Cambridge University Press, New York.

Library
-------
tsmt

Source
------
tartest.src
