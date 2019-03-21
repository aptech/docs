
pdflogistic
==============================================

Purpose
----------------

Computes the probability density function for the logistic distribution.

Format
----------------
.. function:: pdflogistic(x,a,b)

    :param x: an Nx1 vector or scalar.
    :type x: NxK matrix

    :param a: , Nx1 vector or scalar, ExE conformable with x.
    :type a: Location parameter; NxK matrix

    :param b: , Nx1 vector or scalar, ExE conformable with x.  b must be greater than 0.
    :type b: Scale parameter; NxK matrix

    :returns: y (*NxK matrix or Nx1 vector or scalar*)

