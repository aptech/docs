
pdfLaplace
==============================================

Purpose
----------------

Computes the probability density function for the Laplace distribution.

Format
----------------
.. function:: p = pdfLaplace(x, loc, scale)

    :param x: data
    :type x: NxK matrix, Nx1 vector or scalar.

    :param loc: location parameter.
    :type loc: scalar

    :param scale: scale parameter. *scale* must be greater than 0.
    :type scale: scalar

    :return p: the probability density function for the Laplace distribution at the elements in *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function for the Laplace distribution is defined as

.. math::

   f(x) = \frac{1}{2 \cdot scale} exp \bigg(- \frac{|x-loc|}{scale} \bigg)

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
