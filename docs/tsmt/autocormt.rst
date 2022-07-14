autocormt
=========

Purpose
-------
Computes specified autocorrelations for each column of a matrix.

Format
------
.. function:: a = autocor(x, k_f, k_l);

  :param x: Autocorrelations will be computed for each column separately. *x* is assumed to have 0 mean.
  :type x: NxK matrix

  :param k_f: Denotes first autocorrelation to compute. Range :math:`[0, rows(x) -1]`.
  :type k_f: scalar

  :param k_l: Denotes the last autocorrelation lags. Must be less than the number of rows of *x*. Range :math:`[0, rows(x) -1]`. If :math:`k_f = 0` and :math:`k_l = 0`, then all possible correlations are computed. If :math:`k_f \lt 0` and :math:`k_l = 0` then the zero order correlation is computed.
  :type k_l: scalar

  :return a: The autocorrelations for each column of *x*. Missing values will be returned if the variance of any variable is `0`.
  :rtype a: matrix


Examples
--------

Example 1: Calculate ACF for a vector
++++++++++++++++++++++++++++++++++++++

::

  new;
  cls;
  library tsmt;

  // Step 1: Use 'acf' function as a comparison

  // Import time series data
  // Get file name with full path
  fname = getGAUSSHome() $+ "examples/beef_prices.csv";

  // Import beef price data
  beef = loadd(fname, "beef_price");

  // Demean beef price data first
  bfdm = beef - meanc(beef);

  // Define first lag for acf , 0 ≤ k_f ≤ N-1
  k_f = 1;

  // Define last lag for acf, 0 ≤ k_l ≤ N-1
  k_l = 5;

  // Compute ACF for demeaned beef price
  a = autocor(bfdm, k_f, k_l);

  // Print results
  print "ACF from autocor function: ";
  print "Lag"$~"ACF";
  print seqa(k_f,1, k_l - k_f + 1)~a;

The results:

::

  ACF from autocor function:
  Lag              ACF

  1.0000000       0.98474980
  2.0000000       0.96196414
  3.0000000       0.94023737
  4.0000000       0.92037936
  5.0000000       0.90134772

Example 2: Calculate ACF for a matrix
++++++++++++++++++++++++++++++++++++++

::

 // Set up a random seed
 rndseed 22;

 // Simulate a data set
 x = rndn(10, 5);

 // Demean data first
 x = x - meanc(x)';

 // Define first lag, k_f
 k_f = 1;

 // Define last lag, k_l
 k_l = 6;

 // Call autocor function
 a = autocor(x, k_f, k_l);

 // Print results
 print "ACF for each column in the matrix";
 print "Lag"$~"ACF of C_1"$~"ACF of C_2"$~"ACF of C_3"$~"ACF of C_4"$~"ACF of C_5";
 print seqa(k_f,1, k_l - k_f + 1)~a;

The results are:

::

  ACF for each column in the matrix
        Lag       ACF of C_1       ACF of C_2       ACF of C_3       ACF of C_4       ACF of C_5

  1.0000000      -0.23535560      -0.23233084      -0.43327598      -0.12392805       0.46121428
  2.0000000      -0.13586178       0.32137672      0.014887577      -0.49854290     0.0097333377
  3.0000000     -0.097818783     -0.095531616      0.021427194      0.054173501      -0.14611108
  4.0000000       0.24352134      -0.33590273      -0.12080847       0.29314286      0.019374906
  5.0000000      -0.24234876       0.15793212     -0.049016036      -0.13335620      0.013169333
  6.0000000     -0.090657186      -0.36787111     -0.040987953      -0.37958321      -0.13512905

Remarks
-------
The data are assumed to have 0 mean. Thus, use:

::

   x = x - meanc(x)';

prior to the use of this function if the mean is not 0.

:func:`autocor` VS :func:`acf`
+++++++++++++++++++++++++++++++++
The :func:`autocor` function can calculate autocorrelation function (ACF) for multiple
columns at one time.

The :func:`acf` can calculate autocorrelation function (ACF) for one column
with the order of differencing, and acf will demean the data
automatically.

Library
-------
tsmt

Source
------
autoregmt.src

.. seealso:: Functions :func:`acf`
