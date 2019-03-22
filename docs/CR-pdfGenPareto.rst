
pdfGenPareto
==============================================

Purpose
----------------

Computes the probability density function for the Generalized Pareto distribution.

Format
----------------
.. function:: pdfGenPareto(x,a,sigma,k)

    :param x: an Nx1 vector or scalar.
    :type x: NxK matrix

    :param a: , Nx1 vector or scalar, ExE conformable with x.
    :type a: Location parameter; NxK matrix

    :param sigma: , Nx1 vector or scalar, ExE conformable with x.  sigma must be greater than 0.
    :type sigma: Scale parameter; NxK matrix

    :param k: , Nx1 vector or scalar, ExE conformable with x.
    :type k: Shape parameter; NxK matrix

    :returns: y (*NxK matrix or Nx1 vector or scalar*)



Remarks
-------

The probability density function for the Generalized Pareto distribution
is defined as

::

   f(x)={1σ(1+k(x−μ)σ)−1−1/k1σexp⁡(−(x−μ)σ)k≠0k=0

.. seealso:: Functions :func:`cdfGenPareto`
