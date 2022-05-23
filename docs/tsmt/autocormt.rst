=========
autocormt
=========

10.0.7autocor
=============

Purpose
-------
Computes specified autocorrelations for each column of a matrix.

Library
-------
tsmt

Format
------
a = autocor(x, k_f, k_l);

Input
-----
+-----+---------------------------------------------------------------+
   | x   | NxK matrix. Autocorrelations will be computed for each column |
   |     | separately. *x* is assumed to have 0 mean.                    |
   +-----+---------------------------------------------------------------+
   | k_f | scalar, in range [0, rows\ |image3|], denoting the first      |
   |     | autocorrelation lag to compute.                               |
   +-----+---------------------------------------------------------------+
   | k_l | scalar, in range [0, rows(x)-1], denoting the last            |
   |     | autocorrelation lag to compute. It must be that f ≦ 1; if l=0 |
   |     | and f=0 , then *k_l* is set to rows(x)-1 and all              |
   |     | autocorrelations from *k_f* to *k_l* are computed. If if l=0  |
   |     | and f<0 , then only the *0\ th* order autocorrelation is      |
   |     | computed.                                                     |
   +-----+---------------------------------------------------------------+

Output
------
+---+-----------------------------------------------------------------+
   | a | GxK matrix, where G = l - f + 1, containing the                 |
   |   | autocorrelations of order |image6| for each of the columns of   |
   |   | *x*. If the variance of any variable is 0, missings will be     |
   |   | returned for that variable.                                     |
   +---+-----------------------------------------------------------------+

Examples
--------
Example 1: Calculate ACF for a vector

   ::

new;
cls;
library tsmt;

// Step 1: Use 'acf' function as a comparison

// Import time series data
// Get file name with full path
file = getGAUSSHome() $+ "pkgs/tsmt/examples/beef_prices.csv";

// Import beef price data 
beef = loadd(fname);

// Define the max number of lags
k = 5;

// Define the order of differencing
// If acf is from original time series data, then d = 0
d = 0; 

// Call acf function
beef_acf = acf(beef, k, d);

// Print results with the number of lags
print "From acf function: ";
print "Lag"$~"ACF";
print seqa(1,1,k)~beef_acf;
print ;

// Step 2: Use 'autocor' function in tsmt package

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

ACF from acf function: 
              
Lag              ACF 
1.0000000       0.98474980 
2.0000000       0.96196414 
3.0000000       0.94023737 
4.0000000       0.92037936 
5.0000000       0.90134772 

ACF from autocor function: 
Lag              ACF 

1.0000000       0.98474980 
2.0000000       0.96196414 
3.0000000       0.94023737 
4.0000000       0.92037936 
5.0000000       0.90134772 

   **Example 2: Calculate ACF for a matrix**

   ::

//Set up a random seed
rndseed 22;

// Simulate a data set
x = rndn(10,5);

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
-  The *0\ th* autocorrelation will always be 1.

The data are assumed to have 0 mean. Thus, use:

::

   x = x - meanc(x)';   

prior to the use of this function if the mean is not 0.

   -  autocor VS acf

autocor can calculate autocorrelation function (ACF) for multiple
columns at one time.

acf can calculate autocorrelation function (ACF) for one column
with the order of differencing, and acf will demean the data
automatically.

Source
------
autoregmt.src

.. |image1| image:: _static/images/Equation687.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image2| image:: _static/images/Equation687.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image3| image:: _static/images/Equation687.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image4| image:: _static/images/Equation688.svg
   :class: mcReset
.. |image5| image:: _static/images/Equation688.svg
   :class: mcReset
.. |image6| image:: _static/images/Equation688.svg
   :class: mcReset
