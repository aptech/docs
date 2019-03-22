
pdfCauchy
==============================================

Purpose
----------------

Computes the probability density function for the Cauchy distribution.

Format
----------------
.. function:: pdfCauchy(x,mu,sigma)

    :param x: an Nx1 vector or scalar.
    :type x: NxK matrix

    :param mu: , Nx1 vector or scalar, ExE conformable with x.
    :type mu: Location parameter; NxK matrix

    :param sigma: , Nx1 vector or scalar, ExE conformable with x.  sigma must be greater than 0.
    :type sigma: Scale parameter; NxK matrix

    :returns: y (*NxK matrix or Nx1 vector or scalar*)



Remarks
-------

The probability density function for the Cauchy distribution is defined
as

::

   f(x)=(πσ(1+(x−μσ)2))−1

.. seealso:: Functions :func:`cdfCauchy`
