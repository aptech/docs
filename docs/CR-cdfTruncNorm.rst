
cdfTruncNorm
==============================================

Purpose
----------------
Computes the cumulative distribution function of the normal distribution over the interval from *a* to *b*.

Format
----------------
.. function:: cdfTruncNorm(x, a, b, mu_bar, sigma_bar)

    :param x: NxK matrix, or N-dimensional array. Values at which to evaluate the cumulative distribution function of the normal distribution.
    :type x: Scalar

    :param l_lim: lower limit of the integration window.
    :type l_lim: Scalar

    :param u_lim: lower limit of the integration window.
    :type u_lim: Scalar

    :param mu_bar: mean parameter.
    :type mu_bar: Scalar

    :param std_bar: standard deviation parameter.
    :type std_bar: Scalar

    :returns: **p** (*scalar or NxK matrix or N-dimensional array*) - the probability density
        of the cumulative distribution over the interval from *l_lim* to *u_lim*.

Examples
----------------

::
    // Value
    x = 0.6;

    //Lower limit
    l_lim = -1;

    // Upper limit
    u_lim = 1;

    // Mean parameter
    mu_bar = 2.3;

    // Standard deviation parameter
    std_bar = 1;

    /*
    ** Compute the CDF at x = 0.6
    ** over the closed region [-1,1]
    ** of the distribution N ~ (2.3, 1)
    */
    p = cdfTruncNorm(x, l_lim, u_lim, mu_bar, std_bar);

After the above code, 'p' equals:

    0.45767633

.. seealso:: Functions :func:`cdfn_cdfNc`, :func:`pdfTruncNorm`, :func:`cdfLogNorm`
