
cdfTruncNorm
==============================================

Purpose
----------------
Computes the cumulative distribution function of the normal distibution over the interval from *a* to *b*.

Format
----------------
.. function:: cdfTruncNorm(x, a, b, mu_bar, sigma_bar)

    :param x: NxK matrix, or N-dimensional array.
    :type x: Scalar

    :param a: lower limit of the integration window.
    :type a: Scalar

    :param b: lower limit of the integration window.
    :type b: Scalar

    :param mu_bar: mean parameter.
    :type mu_bar: Scalar

    :param sigma_bar: standard deviation parameter.
    :type sigma_bar: Scalar

    :returns: p (*scalar or NxK matrix or N-dimensional array*), the probability density
        of the cumulative distribution over the interval from *a* to *b*.

Examples
----------------

::

    x = 0.6;
    a = -1;
    b = 1;
    mu = 2.3;
    s = 1;
              
    // Compute the CDF at x = 0.6
    // over the closed region [-1,1]
    // of the distribution N ~ (2.3, 1)
    p = cdfTruncNorm(x, a, b, mu, s);
    
    After the above code, 'p' equals:
    
    0.45767633

.. seealso:: Functions :func:`cdfn_cdfNc`, :func:`pdfTruncNorm`, :func:`cdfLogNorm`

