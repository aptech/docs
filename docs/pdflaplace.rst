
pdfLaplace
==============================================

Purpose
----------------

Computes the probability density function for the Laplace distribution.

Format
----------------
.. function:: p = pdfLaplace(x, a, b)

    :param x: data
    :type x: NxK matrix, Nx1 vector or scalar.

    :param a: location parameter.
    :type a: scalar

    :param b: scale parameter. *b* must be greater than 0.
    :type b: scalar

    :return p: the probability density function for the Laplace distribution at the elements in *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function for the Laplace distribution is defined as

.. math::

   f(x) = \frac{1}{2b} exp \bigg(- \frac{|x-a|}{b} \bigg)

Examples
----------------

::

    // Data points
    x = { -2, -1, 0, 1, 2 };

    // Laplace PDF with location = 0, scale = 1
    p = pdfLaplace(x, 0, 1);
    print p;

After the code above, *p* is equal to:

::

       0.067667642
        0.18393972
        0.50000000
        0.18393972
       0.067667642

.. seealso:: Functions :func:`cdfCauchy`, :func:`pdfCauchy`
