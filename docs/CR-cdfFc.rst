
cdfFc
==============================================

Purpose
----------------
Computes the complement of the cumulative distribution function of the F distribution.

Format
----------------
.. function:: cdfFc(x, n1, n2)

    :param x: 
    :type x: NxK matrix

    :param n1: ExE conformable with *x*.
    :type n1: LxM matrix

    :param n2: ExE conformable with *x* and *n1*.
    :type n2: PxQ matrix

    :returns: y (*matrix*), max(N,L,P) by max(K,M,Q)

Examples
----------------
:func:`cdffc` can be used to calculate a p-value from an F-statistic.

::

    n_obs = 100;
    n_vars = 5;
    f_stat = 2.4;
    p_value = cdfFc(f_stat, n_vars, n_obs - n_vars - 1);
    print p_value;

will return:

::

    0.042803132

Remarks
------------

*y* is the integral from *x* to :math:`∞` of the *F* distribution with *n1* and *n2*
degrees of freedom.

This equals

.. math:: 1 - G(x, n1, n2)

where *G* is the *F* cdf with *n1* and *n2* degrees of freedom. Thus, to get the *F* cdf, use:

:: 

    1 - cdfFc(x, n1, n2);

The complement of the cdf is computed because this is what is most
commonly needed in statistical applications, and because it can be
computed with fewer problems of roundoff error.

Allowable ranges for the arguments are:

.. math::

    x > 0
   n1 > 0
   n2 > 0

A -1 is returned for those elements with invalid inputs.

For :math:`max(n1,n2) <= 1000`, the absolute error is approx. :math:`±5e-13`. For
:math:`max(n1,n2) > 1000`, Normal approximations are used and the absolute error
is approx. :math:`±2e-6`.

For higher accuracy when :math:`max(n1,n2) > 1000`, use

::

   cdfBeta(n2/(n2 + n1*x), n2/2, n1/2);

References
------------

#. Bol'shev, L.N. "Asymptotically Perason's Transformations." Teor.
   Veroyat. Primen. Theory of Probability and its Applications. Vol. 8,
   No. 2, 1963, 129-55.

#. Bosten, N.E. and E.L. Battiste. "Remark on Algorithm 179 Incomplete
   Beta Ratio." Comm. ACM. Vol. 17, No. 3, March 1974, 156-57.

#. Kennedy, W.J., Jr. and J.E. Gentle. Statistical Computing. Marcel
   Dekker, Inc., New York, 1980.

#. Ludwig, O.G. "Algorithm 179 Incomplete Beta Ratio." Comm. ACM. Vol.
   6, No. 6, June 1963, 314.

#. Mardia, K.V. and P.J. Zemroch. Tables of the F- and related
   distributions with algorithms. Academic Press, New York, 1978. ISBN
   0-12-471140-5.

#. Peizer, D.B. and J.W. Pratt. "A Normal Approximation for Binomial, F,
   Beta, and other Common, Related Tail Probabilities, I." Journal of
   the American Statistical Association. Vol. 63, Dec. 1968, 1416-56.

#. Pike, M.C. and I.D. Hill, "Remark on Algorithm 179 Incomplete Beta
   Ratio." Comm. ACM. Vol. 10, No. 6, June 1967, 375-76.

.. seealso:: Functions :func:`cdfBeta`, :func:`cdfChic`, :func:`cdfN`, :func:`cdfNc`, :func:`cdfTc`, :func:`gamma`

