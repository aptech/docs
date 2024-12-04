hansen
======

Purpose
-------
Test for stability of all parameters using a cumulative sums of
weighted full sample residuals. The test employs the locally best
invariant tests in a Lagrange multiplier format.

Format
------

.. function:: { ny, prob } = hansen(yt, xt, print_out)

   :param yt: Tx1 numerical vector of panel series data.
   :type yt: Matrix

   :param xt: TxK numerical matrix of estimation regressors.
   :type xt: Matrix

   :param print_out: Optional input, 1 to print output to the screen; 0 to suppress output. Default = 1.
   :type print_out: Scalar

   :return ny: Hansen test statistic in order: Hansen test for parameter stability, Hansen test for variance constancy, Hansen test for joint stability.
   :rtype ny: Matrix

   :return crit: 1%, 2.5%, 5%, 7.5%, 10%, and 20% critical values.
   :rtype crit: Vector

Example
-------

::

   new;
   cls;
   library tsmt;
   
   // This generates 400 observations of a
   // linear time series with a break in the constant
   // at observations 120

   b1 = { 1.2, -2, 0.75 };
   b2 = { 5, -2, 0.75 };

   n1 = 120;
   n_tot = 400;
   xt = ones(n_tot, 1)~rndn(n_tot, 2);
   et = rndn(n_tot, 1);

   // Create series with break
   y1 = xt[1:n1, .]*b1 + et[1:n1, .];
   y2 = xt[n1+1:n_tot, .]*b2 + et[n1+1:n_tot, .];
   yt_break = y1|y2;

   /********************************************/
   // Run example including printOut of results
   { ny, crit } = hansen(yt_break, xt);

::
   
   Test:                                   Hansen-Nyblom (1989) 
   Test Variable:                                            Y1 
   Timespan:                                            Unknown 
   Ho:                                                Stability 
   Model:                                  No constant or trend 
   N. Obs:                                                  400 
   ============================================================

   Beta1                                                 21.998 
   Beta2                                                  0.263 
   Beta3                                                  0.091 
   Variance                                              11.161 
   Joint                                                 -9.182 

   Critical Values:
                               1%             5%            10%
                            2.120          1.680          1.490
   ============================================================

   Reject the null hypothesis of constancy of Beta1 at the 1% level.

   Cannot reject the null hypothesis of constancy of Beta2.

   Cannot reject the null hypothesis of constancy of Beta3.

   Reject the null hypothesis of constancy of variance at the 1% level.

   Reject the null hypothesis of joint constancy of all parameters at the 1% level.
   
Reference
---------
1. Nyblom, J. (1989). Testing for the constancy of parameters over time, Journal of American Statistical Association, 84(405), 223-230.
2. Hansen, B.E. (1992). Testing for parameter instability in linear models, Journal of Policy Modeling, 14(4): 517-533.

Library
-------
tsmt

Source
------
hansen.src

.. seealso:: Functions :func:`chowfcst`, :func:`sbreak`
