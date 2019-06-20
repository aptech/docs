
cdfBeta
==============================================

Purpose
----------------

Computes the incomplete Beta function (i.e., the cumulative distribution function of the Beta distribution).

Format
----------------
.. function:: cdfBeta(x, a, b)

    :param x: Values at which to evaluate the Beta cdf. :math:`0 \leq x \leq 1`
    :type x: NxK matrix

    :param a: ExE conformable with *x*. :math:`a > 0`
    :type a: LxM matrix

    :param b: ExE conformable with *x* and *a*. :math:`b > 0`
    :type b: PxQ matrix

    :returns: **p** (*matrix, max(N,L,P) by max(K,M,Q)*) - *p* is the integral from 0 to *x* of the beta distribution with parameters *a*
    and *b*. A -1 is returned for those elements with invalid inputs.

Examples
----------------

::

    // Values
    x = { 0.0506, 0.1886, 0.3781, 0.5763 };

    // Beta parameters
    a = 0.5;
    b = 0.3;

    // Total probabilities
    p = cdfBeta(x, a, b);
    print "p = "	 p;

After running above code,

::

  p =
    0.1000
    0.2000
    0.3000
    0.4000


Technical Notes
-------------------

:func:`cdfBeta` has the following approximate accuracy:

+--------+---+-----------+----+---------+----------------------------------+
|        |   | max(a, b) | <= | 500     | absolute error is approx. ±5e-13 |
+--------+---+-----------+----+---------+----------------------------------+
| 500    | < | max(a, b) | <= | 10,000  | absolute error is approx. ±5e-11 |
+--------+---+-----------+----+---------+----------------------------------+
| 10,000 | < | max(a, b) | <= | 200,000 | absolute error is approx. ±1e-9  |
+--------+---+-----------+----+---------+----------------------------------+

References
------------

#. Bol'shev, L.N."Asymptotically Perason's Transformations." Teor.
   Veroyat. Primen. Theory of Probability and its Applications. Vol. 8,
   No. 2, 1963, 129-55.
#. Boston N.E. and E.L. Battiste. "Remark on Algorithm 179 Incomplete
   Beta Ratio." Comm. ACM. Vol. 17, No. 3, March 1974, 156-57.
#. Ludwig, O.G. "Algorithm 179 Incomplete Beta Ratio." Comm. ACM. Vol.
   6, No. 6, June 1963, 314.
#. Mardia, K.V. and P.J. Zemroch. Tables of the F- and related
   distributions with algorithms. Academic Press, New York, 1978. ISBN
   0-12-471140-5.
#. Peizer, D.B. and J.W. Pratt. "A Normal Approximation for Binomial, F,
   Beta, and Other Common, Related Tail Probabilities, I." Journal of
   the American Statistical Association. Vol. 63, Dec. 1968, 1416-56.
#. Pike, M.C. and J.W. Pratt. "Remark on Algorithm 179 Incomplete Beta
   Ratio." Comm. ACM. Vol. 10, No. 6, June 1967, 375-76.

.. seealso:: Functions :func:`cdfChic`, :func:`cdfFc`, :func:`cdfN`, :func:`cdfNc`, :func:`cdfTc`, :func:`gamma`
