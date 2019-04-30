
pdfTruncNorm
==============================================

Purpose
----------------
Computes the cumulative distribution function of the
		normal distibution over the interval from a to b.

Format
----------------
.. function:: pdfTruncNorm(x, a, b, mu_bar, sigma_bar)

    :param x: NxK matrix, or N-dimensional array.
    :type x: scalar

    :param a: lower limit of the integration window.
    :type a: scalar

    :param b: lower limit of the integration window.
    :type b: scalar

    :param mu_bar: mean parameter.
    :type mu_bar: scalar

    :param sigma_bar: standard deviation parameter.
    :type sigma_bar: scalar

    :returns: p (*scalar or NxK matrix or N-dimensional array*), the probability density
        of the cumulative distribution over the interval from *a* to *b*.

Examples
----------------

::

    x = 0.5;
    a = -1;
    b = 1;
    mu = 0;
    s = 1;
              
    // Compute the PDF at x = 0.5
    // over the closed region [-1,1]
    p = pdfTruncNorm(x, a, b, mu, s);

After the above code, *p* equals:

::

    0.51570345

.. seealso:: Functions :func:`pdfn`, :func:`cdfTruncNorm`, :func:`cdfLogNorm`

