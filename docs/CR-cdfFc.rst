
cdfFc
==============================================

Purpose
----------------
Computes the complement of the cumulative distribution function of the F distribution.

Format
----------------
.. function:: cdfFc(x, df_n, df_d)

    :param x: Values at which to evaluate the complement of the F distribution cdf. :math:`x > 0`.
    :type x: NxK matrix

    :param df_n: ExE conformable with *x*. Degrees of freedom of numerator, :math:`df_n > 0`.
    :type df_n: LxM matrix

    :param df_d: ExE conformable with *x* and *n1*. Degrees of freedom of denominator, :math:`df_d > 0`.
    :type df_d: PxQ matrix

    :returns: **p** (*matrix, max(N,L,P) by max(K,M,Q)*) - Each element in *p* is the complement of the F distribution cdf value evaluated at the corresponding element in *x*.

Examples
----------------
:func:`cdffc` can be used to calculate a p-value from an F-statistic.

::

    /*
    ** Computing the parameters
    */
    // Number of observations
    n_obs = 100;

    // Number of variables
    n_vars = 5;

    // Setting n1
    df_n = n_vars;

    // Setting n2
    df_d = n_obs - n_vars - 1;

    // Value to calculate p_value at
    f_stat = 2.4;

    // Call cdfFc
    p_value = cdfFc(f_stat, df_n, df_d);
    print p_value;

will return:

::

    0.042803132

Remarks
------------

This procedure finds the complement of the F distribution cdf which equals

.. math:: 1 - G(x, n1, n2)

where *G* is the *F* cdf with *n1* and *n2* degrees of freedom. Thus, to get the *F* cdf, use:

::

    1 - cdfFc(x, n1, n2);

The complement of the cdf is computed because this is what is most
commonly needed in statistical applications, and because it can be
computed with fewer problems of roundoff error.

A -1 is returned for those elements with invalid inputs.

For :math:`max(n1,n2) \leq 1000`, the absolute error is approx. :math:`\pm5e-13`. For
:math:`max(n1,n2) > 1000`, Normal approximations are used and the absolute error
is approx. :math:`\pm2e-6`.

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
