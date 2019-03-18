
cdfTc
==============================================

Purpose
----------------
Computes the complement of the cdf of the Student's t distribution.

Format
----------------
.. function:: cdfTc(x,  n)

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
    y = cdfTc(x,n);

After running above code,

::

    y = 
    0.46332617
    0.42713516
    0.39188165
    0.35796758

.. seealso:: Functions :func:`cdfTci`

Technical Notes
+++++++++++++++

For results greater than 0.5e-30, the absolute error is approx. ±1e-14
and the relative error is approx. ±1e-12. If you multiply the relative
error by the result, then take the minimum of that and the absolute
error, you have the maximum actual error for any result. Thus, the
actual error is approx. ±1e-14 for results greater than 0.01. For
results less than 0.01, the actual error will be less. For example, for
a result of 0.5e-30, the actual error is only ±0.5e-42.

References
++++++++++

#. Abramowitz, M. and I.A. Stegun, eds. Handbook of Mathematical
   Functions. 7th ed. Dover, New York, 1970. ISBN 0-486-61272-4.

#. Hill, G.W. ''Algorithm 395 Student's t-Distribution.'' Comm. ACM.
   Vol. 13, No. 10, Oct. 1970.

#. Hill, G.W. ''Reference Table: Student's t-Distribution Quantiles to
   20D.'' Division of Mathematical Statistics Technical Paper No. 35.
   Commonwealth Scientific and Industrial Research Organization,
   Australia, 1972.

complement student t cdf cumulative distribution function
