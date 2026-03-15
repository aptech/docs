
cdfTruncNorm
==============================================

Purpose
----------------
Computes the cumulative distribution function of the normal distribution over the interval from *a* to *b*.

Format
----------------
.. function:: p = cdfTruncNorm(x, a, b, mu_bar, sigma_bar)

    :param x: Values at which to evaluate the cumulative distribution function of the normal distribution.
    :type x: NxK matrix

    :param a: lower limit of the integration window.
    :type a: Scalar

    :param b: upper limit of the integration window.
    :type b: Scalar

    :param mu_bar: mean parameter.
    :type mu_bar: Scalar

    :param sigma_bar: standard deviation parameter.
    :type sigma_bar: Scalar

    :return p: the probability density
        of the cumulative distribution over the interval from *a* to *b*.

    :rtype p: scalar or NxK matrix or N-dimensional array

Examples
----------------

::

    // Value
    x = 0.6;

    //Lower limit
    a = -1;

    // Upper limit
    b = 1;

    // Mean parameter
    mu_bar = 2.3;

    // Standard deviation parameter
    sigma_bar = 1;

    /*
    ** Compute the CDF at x = 0.6
    ** over the closed region [-1,1]
    ** of the distribution N ~ (2.3, 1)
    */
    p = cdfTruncNorm(x, a, b, mu_bar, sigma_bar);

After the above code, *p* equals:

    0.45767633

.. seealso:: Functions :func:`cdfn_cdfNc`, :func:`pdfTruncNorm`, :func:`cdfLogNorm`
