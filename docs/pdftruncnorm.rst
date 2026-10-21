
pdfTruncNorm
==============================================

Purpose
----------------
Computes the probability distribution function of the normal distribution over the interval from *a* to *b*.

Format
----------------
.. function:: p = pdfTruncNorm(x, a, b, mu, sigma)

    :param x: NxK matrix, or N-dimensional array.
    :type x: scalar

    :param a: lower limit of the integration window.
    :type a: scalar

    :param b: upper limit of the integration window.
    :type b: scalar

    :param mu: mean parameter.
    :type mu: scalar

    :param sigma: standard deviation parameter.
    :type sigma: scalar

    :return p: the probability density over the interval from *a* to *b*.

    :rtype p: NxK matrix, N-dimensional array or scalar

Examples
----------------

::

    x = 0.5;
    a = -1;
    b = 1;
    mu = 0;
    sigma = 1;

    // Compute the PDF at x = 0.5
    // over the closed region [-1, 1]
    p = pdfTruncNorm(x, a, b, mu, sigma);

After the above code, *p* equals:

::

    0.51570345

.. seealso:: Functions :func:`pdfn`, :func:`cdfTruncNorm`, :func:`cdfLogNorm`
