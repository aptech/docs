
cdfChic
==============================================

Purpose
----------------

Computes the complement of the cdf of the chi-squared distribution.

Format
----------------
.. function:: cdfChic(x, n)

    :param x: Values at which to evaluate the complement of the chi-squared cdf.
    :type x: NxK matrix. :math:`x > 0`

    :param df: ExE conformable with *x*, degrees of freedom. :math:`df > 0`
    :type df: LxM matrix

    :returns: **p** (*matrix, max(N,L) by max(K,M)*) - Each element in *p* is the complement of the chi-squared cdf value evaluated at the corresponding element in *x*.


Remarks
-------

A -1 is returned for those elements with invalid inputs.

This equals :math:`1 - Χ_n^2(x)`, Thus, to get the chi-squared cdf, subtract
:code:`cdfChic(x, n)` from 1. The complement of the cdf is computed because this
is what is most commonly needed in statistical applications and
it can be computed with fewer problems of roundoff error.

Examples
----------------

::
    // Vector of values
    x = { .1, .2, .3, .4 };

    // Degrees of freedom
    df = 3;

    // Call cdfChic
    p = cdfChic(x, n);
    print "p = " p;

After running the above code,

::

  p =
    0.9918
    0.9776
    0.9600
    0.9402

Technical Notes
--------------------------

For :math:`n \leq 1000`, the incomplete gamma function is used and the absolute
error is approx. :math:`\pm6e-13`.

For :math:`n \gt 1000`, a Normal approximation is used and the absolute error is
:math:`\pm2e-8`.

For higher accuracy when :math:`n \gt 1000`, use:

::

   1 - cdfGam(0.5*x, 0.5*n);

References
--------------

#. Bhattacharjee, G.P. "Algorithm AS 32, the Incomplete Gamma Integral."
   Applied Statistics. Vol. 19, 1970, 285-87.

#. Mardia K.V. and P.J. Zemroch. Tables of the F- and related
   distributions with algorithms. Academic Press, New York, 1978. ISBN
   0-12-471140-5.

#. Peizer, D.B. and J.W. Pratt. "A Normal Approximation for Binomial, F,
   Beta, and other Common, Related Tail Probabilities, I." Journal of
   the American Statistical Association. Vol. 63, Dec. 1968, 1416-56.

.. seealso:: Functions :func:`cdfBeta`, :func:`cdfFc`, :func:`cdfNc`, :func:`cdfTc`, :func:`gamma`
