
cdfTc
==============================================

Purpose
----------------
Computes the complement of the cdf of the Student's t distribution.

Format
----------------
.. function:: cdfTc(x, df)

    :param x: values at which to evaluate the cumulative distribution function for the Student's t distribution. :math:`−\infty \leq x \leq \infty`.
    :type x: NxK matrix

    :param df: ExE conformable with *x*. Degrees of freedom. :math:`df > 1`.
    :type df: LxM matrix

    :returns: **p** (*matrix, max(N,L) by max(K,M)*) - Each element in *p* is the complement of the cumulative distribution function of the Student's t distribution evaluated at the corresponding element in *x*.

Remarks
-------

A -1 is returned for those elements with invalid inputs.

This equals:

.. math:: 1 − F(x,df)

where *F* is the t cdf with *df* degrees of freedom. Thus, to get the t cdf,
subtract :code:`cdfTc(x, df)` from 1. The complement of the cdf is computed
because this is what is most commonly needed in statistical
applications, and because it can be computed with fewer problems of
roundoff error.

Examples
----------------

::

    // Values
    x = { .1, .2, .3, .4 };

    // Degrees of freedom
    df = 3;

    p = cdfTc(x, df);

After running above code,

::

    p =
    0.46332617
    0.42713516
    0.39188165
    0.35796758

Technical Notes
------------

For results greater than 0.5e-30, the absolute error is approx. ±1e-14
and the relative error is approx. ±1e-12. If you multiply the relative
error by the result, then take the minimum of that and the absolute
error, you have the maximum actual error for any result. Thus, the
actual error is approx. ±1e-14 for results greater than 0.01. For
results less than 0.01, the actual error will be less. For example, for
a result of 0.5e-30, the actual error is only ±0.5e-42.

References
------------

#. Abramowitz, M. and I.A. Stegun, eds. Handbook of Mathematical
   Functions. 7th ed. Dover, New York, 1970. ISBN 0-486-61272-4.

#. Hill, G.W. ''Algorithm 395 Student's t-Distribution.'' Comm. ACM.
   Vol. 13, No. 10, Oct. 1970.

#. Hill, G.W. ''Reference Table: Student's t-Distribution Quantiles to
   20D.'' Division of Mathematical Statistics Technical Paper No. 35.
   Commonwealth Scientific and Industrial Research Organization,
   Australia, 1972.

.. seealso:: Functions :func:`cdfTci`
