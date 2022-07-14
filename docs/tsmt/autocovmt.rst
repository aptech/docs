autocovmt
=========

Purpose
-------
Computes specified autocovariances for each column of a matrix.

Format
------
.. function:: a = autocov(x, f, l);

  :param x: autocovariances will be computed for each column separately. *x* is assumed to have 0 mean.
  :type x: NxK matrix

  :param k_f: Denotes first autocovariance to compute. Range :math:`[0, rows(x) -1]`.
  :type k_f: scalar

  :param k_l: Denotes the last autocovariance lags. Must be less than the number of rows of *x*. Range :math:`[0, rows(x) -1]`. If :math:`k_f = 0` and :math:`k_l = 0`, then all possible correlations are computed. If :math:`k_f \lt 0` and :math:`k_l = 0` then the zero order correlation is computed.
  :type k_l: scalar

  :return a: The autocovariances for each column of *x*. Missing values will be returned if the variance of any variable is `0`.
  :rtype a: matrix

Examples
--------
Example 1: Calculate autocovariance for a vector
+++++++++++++++++++++++++++++++++++++++++++++++++

::

  new;
  cls;
  library tsmt;

  // Get file name with full path
  file = getGAUSSHome() $+ "examples/beef_prices.csv";

  // Import beef price data
  beef = loadd(fname, "beef_price");

  // Demean beef price data first
  bfdm = beef - meanc(beef);

  // Define first lag, 0 ≤ k_f ≤ N-1
  k_f = 0;

  // Define last lag, 0 ≤ k_l ≤ N-1
  k_l = 5;

  // Compute autocovariance for demeaned beef price
  a = autocov(bfdm, k_f, k_l);

  // Print results
  print "Lag"$~"autocovariance";
  print seqa(k_f, 1, k_l - k_f + 1)~a;

The results:

::

        Lag   autocovariance

  0.00000000        1800.8245
   1.0000000        1773.3616
   2.0000000        1732.3286
   3.0000000        1693.2025
   4.0000000        1657.4417
   5.0000000        1623.1691

Example 2: Calculate autocovariance for a matrix
+++++++++++++++++++++++++++++++++++++++++++++++++++

::

  new;

  // Set up a random seed
 rndseed 22;

 // Simulate a data set
 x = rndn(10, 5);

 // Demean data first
 x = x - meanc(x)';

 // Define first lag, k_f
 k_f = 0;

 // Define last lag, k_l
 k_l = 6;

 // Call autocov function
 a = autocov(x, k_f, k_l);

 // Print results
 print "Lag"$~"autocov of C_1"$~"autocovof C_2"$~"autocovof C_3"$~"autocovof C_4"$~"autocov of C_5";
 print seqa(k_f, 1, k_l - k_f + 1)~a;

The results are:

::

 Lag           autocov of C_1    autocovof C_2    autocovof C_3   autocovof C_4   autocov of C_5

 0.00000000       0.65765163        1.1915671       0.75573287       0.50407153       0.39901953
 1.0000000       -0.15478200      -0.27683779      -0.32744090     -0.062468602       0.18403351
 2.0000000      -0.089349723       0.38294194      0.011251031      -0.25130128     0.0038837918
 3.0000000      -0.064330682      -0.11383233      0.016193235      0.027307319     -0.058301173
 4.0000000        0.16015220      -0.40025065     -0.091298936       0.14776497     0.0077309661
 5.0000000       -0.15938106       0.18818673     -0.037043030     -0.067221065     0.0052548212
 6.0000000      -0.059620846      -0.43834313     -0.030975944      -0.19133709     -0.053919130


Remarks
-------
The zeroth autocovariance is just the variance of the variable. The divisor for each autocovariance is the number of elements involved in its computation. Thus, the *p\ th*\  order cross product is divided by
:math:`N-P`, where :math:`N = rows(x)`, to obtain the *p\ th* order autocovariance.

The data are assumed to have 0 mean. Thus, use:

::

 x = x - meanc(x)';

prior to the use of this function if the mean is not 0.

Library
-------
tsmt

Source
------
autoregmt.src
