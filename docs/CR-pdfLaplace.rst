
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

.. seealso:: Functions :func:`cdfCauchy`, :func:`pdfCauchy`
