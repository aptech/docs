
cdfFc
==============================================

Purpose
----------------
Computes the complement of the cumulative distribution function of the F distribution.

Format
----------------
.. function:: p = cdfFc(x, df_n, df_d)

    :param x: Values at which to evaluate the complement of the F distribution cdf. An *x* below 0 returns 1.
    :type x: NxK matrix

    :param df_n: ExE conformable with *x*. Degrees of freedom of numerator, :math:`df_n > 0`.
    :type df_n: LxM matrix

    :param df_d: ExE conformable with *x* and *df_n*. Degrees of freedom of denominator, :math:`df_d > 0`.
    :type df_d: PxQ matrix

    :return p: Each element in *p* is the complement of the F distribution cdf value evaluated at the corresponding element in *x*.

    :rtype p: matrix, max(N,L,P) by max(K,M,Q)

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

    df_n = n_vars;
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

.. math:: 1 - G(x, df_n, df_d)

where *G* is the *F* cdf with *df_n* and *df_d* degrees of freedom. Thus, to get the *F* cdf, use:

::

    1 - cdfFc(x, df_n, df_d);

The complement of the cdf is computed because this is what is most
commonly needed in statistical applications, and because it can be
computed with fewer problems of roundoff error.

If *df_n* or *df_d* is not greater than 0, :func:`cdfFc` returns a scalar error
code and :func:`scalerr` returns the position of that argument: 2 for *df_n*,
3 for *df_d*. An *x* below 0 is not an error: it returns 1. A missing value in
any argument returns a missing value.

.. seealso:: Functions :func:`cdfBeta`, :func:`cdfChic`, :func:`cdfN`, :func:`cdfNc`, :func:`cdfTc`, :func:`gamma`
