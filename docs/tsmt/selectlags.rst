selectLags
==========

Purpose
-------
Select lags based on method of statistical inference.

Format
------
.. function:: { stat,p_mat } = selectLags(y, x [, maxlag, method, print_out])

   :param y: Nx1 data to be tested.
   :type y: matrix

   :param x: NxK, exogenous regressor. Set equal to 0 if there are no exogenous variables.
   :type x: matrix

   :param maxlag: Optional, maximum lags. Default = 12.
   :type maxlag: scalar

   :param method: Optional, lag selection method:

      .. list-table::
         :widths: auto

         * - AIC
           - Akaike information criterion. (Default)
         * - BIC
           - Bayesian information criterion.
         * - HQC
           - Hannan-Quinn criterion.
         * - FPE
           - Final prediction error.
         * - ALL
           - All methods computed. 

   :type method: string

   :param printOut: Optional, indicator to print out. 1 = print out, 0 = no print out. Default = 1.
   :type printOut: scalar

   :return stat: lag selection criterion values.
   :rtype stat: matrix

   :return p_mat: optimal VAR lags.
   :rtype p_mat: matrix

Example
-------
::

   new;
   cls;
   library tsmt;

   // Use the simarmamt procedure to generate ar data
   // This generates 1000 observations of and
   // AR(4) series with a constant
   // and standard deviation equal to 1.
   b = { 0.1, .3, -.4, 0.2 };
   q = 0;
   p = 4;
   const = 1;
   tr = 0;
   n = 1000;
   k = 1;
   std = 1;
   seed = 19786;

   y = simarmamt( b, p, q, const, tr, n, k, std, seed );

   // Set parameters for the simarmamt procedure
   // Exogenous variables -- Add intercept
   x = ones( rows(y), 1 );

   // Max number of lags to test for
   p = 8;

   // Method to test
   method = "AIC";
   printOut =1 ;

   { stat , p_mat } = selectLags( y, x, p, method, printOut );

   // Method to test
   method = "ALL";

   { stat_all , p_mat_all } = selectLags( y, x, p, method, printOut );

Library
-------
tsmt

Source
------
selectlags.src
