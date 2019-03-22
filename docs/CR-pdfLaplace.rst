
pdfLaplace
==============================================

Purpose
----------------

Computes the probability density function for the Laplace distribution.

Format
----------------
.. function:: pdfLaplace(x,a,b)

    :param x: Nx1 vector or scalar.
    :type x: NxK matrix

    :param a: location parameter.
    :type a: Scalar

    :param b: scale parameter.  b must be greater than 0.
    :type b: Scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)



Remarks
-------

The probability density function for the Laplace distribution is defined
as

::

   f(x)=12bexp-|x-a|b

.. seealso:: Functions :func:`cdfCauchy`, :func:`pdfCauchy`
