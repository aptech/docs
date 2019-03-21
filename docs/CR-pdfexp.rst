
pdfexp
==============================================

Purpose
----------------

Computes the probability density function for the exponential distribution.

Format
----------------
.. function:: pdfexp(x,a,b)

    :param x: Nx1 vector or scalar. x must be greater than  a.
    :type x: NxK matrix

    :param a: , Nx1 vector or scalar, ExE conformable with x.
    :type a: Location parameter; NxK matrix

    :param b: the scale parameter sometimes called beta.  b must be greater than 0.
    :type b: Scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)

