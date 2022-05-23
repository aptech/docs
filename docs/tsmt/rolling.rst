rolling
=======

Purpose
-------
Performs rolling OLS regressions for a provided vector of dependent data and matrix of independent regressors.

Format
------
.. function:: {coef, res, w} = rolling(yt, xt, window, add, graph)

   :param yt: panel series data. 
   :type yt: Tx1 numerical vector

   :param xt: estimation regressors. 
   :type xt: TxK numerical matrix

   :param window: Optional input, a positive integer specifying a fixed window size of K< window <T. A window size of less than zero results in an expanding window. Default = 0.
   :type window: scalar

   :param add: Optional input, specifying the initial observation for the forward expanding window. Negative values indicate a backward window expansion, beginning with the last add number of observations. The add input is valid only if a negative window size is provided. Default = 0.
   :type add: scalar

   :param graph: Optional input, any number greater than zero will graph the rolling values of all coefficient estimates, including the constant. Default = 1.
   :type graph: scalar

   :return coef: rolling coefficient estimates.
   :rtype coef: matrix

   :return res: one-step ahead rolling residuals.
   :rtype res: matrix

   :return w: standardized one-step ahead rolling residuals.
   :rtype w: matrix


Example
-------

::

   new;
   cls;
   library tsmt;
   rndseed 23563425;

   /********************************************/
   //This generates 400 observations of an
   //linear time series with a break in the constant 
   //at observations 120 

   b1 = { 1.2, -2, 0.75 };
   b2 = { 5, -2, 0.75 };

   n1 = 120;
   n_tot = 400;
   xt = ones( n_tot, 1 )~rndn( n_tot, 2 );
   et = rndn( n_tot, 1 );

   //Create series with break
   y1 = xt[1:n1, .]*b1 + et[1:n1, .];
   y2 = xt[n1+1:n_tot, .]*b2 + et[n1+1:n_tot, .];
   yt_break = y1|y2;

   /********************************************/
   //Set parameters to run a rolling window regression
   //Positive window sets fixed window
   wind = 15;

   //Fixed window regression
   { beta, res, w } = rolling( yt_break, xt, wind );

   /********************************************/
   //Next set parameters to run an forward expanding window regression
   //Set-up expanding window size
   //Negative window results in expanding window size
   wind = -15;

   //Add specifies increment to increase window size by
   //and is irrelevant for rolling window regression
   add = 15;

   //Draw plot from second call to 'rolling' in new window
   plotOpenWindow( );

   //Expanding window estimation
   { beta_fwd, res_fwd, w_fwd } = rolling( yt_break, xt, wind, add );

Remarks
-------
The GAUSS rolling procedure performs rolling OLS regressions for a
provided vector of dependent data and matrix of independent
regressors.

Reference
---------
Zivot, E., and Wang, J. (2002). Modeling Financial Time Series with S-PLUS. Springer-Verlag, New York.

Library
-------
tsmt

Source
------
rolling.src
