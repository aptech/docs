
pdfLaplace
==============================================

Purpose
----------------

Computes the probability density function for the Laplace distribution.

Format
----------------
.. function:: y = pdfLaplace(x,a,b)

    :param x: data
    :type x: NxK matrix, Nx1 vector or scalar.

    :param a: location parameter.
    :type a: scalar

    :param b: scale parameter. *b* must be greater than 0.
    :type b: scalar

    :return y: 

    :rtype y: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function for the Laplace distribution is defined as

.. DANGER:: Fix equations

::

   f(x)=12bexp-|x-a|b

.. seealso:: Functions :func:`cdfCauchy`, :func:`pdfCauchy`

