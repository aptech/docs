
cdfChic
==============================================

Purpose
----------------

Computes the complement of the cdf of
the chi-square distribution.

Format
----------------
.. function:: cdfChic(x,  n)

    :param x: NxK matrix.
    :type x: TODO

    :param n: ExE conformable with x.
    :type n: LxM matrix

    :returns: y (*TODO*), max(N,L) by max(K,M) matrix.

Examples
----------------

::

    x = { .1, .2, .3, .4 };
    n = 3;
    y = cdfChic(x,n);
    print "y = " y;

::

    0.991837 
    y = 0.977589 
        0.960028 
        0.940242

.. seealso:: Functions :func:`cdfBeta`, :func:`cdfFc`, :func:`cdfNc`, :func:`cdfTc`, :func:`gamma`

Technical Notes
+++++++++++++++

For n <= 1000, the incomplete gamma function is used and the absolute
error is approx. ±6e-13.

For n > 1000, a Normal approximation is used and the absolute error is
±2e-8.

For higher accuracy when n > 1000, use:

::

   1 - cdfGam(0.5*x, 0.5*n);

References
++++++++++

#. Bhattacharjee, G.P. "Algorithm AS 32, the Incomplete Gamma Integral."
   Applied Statistics. Vol. 19, 1970, 285-87.

#. Mardia K.V. and P.J. Zemroch. Tables of the F- and related
   distributions with algorithms. Academic Press, New York, 1978. ISBN
   0-12-471140-5.

#. Peizer, D.B. and J.W. Pratt. "A Normal Approximation for Binomial, F,
   Beta, and other Common, Related Tail Probabilities, I." Journal of
   the American Statistical Association. Vol. 63, Dec. 1968, 1416-56.

chi square complement cdf cumulative distribution function
