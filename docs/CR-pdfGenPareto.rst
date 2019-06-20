
pdfGenPareto
==============================================

Purpose
----------------

Computes the probability density function for the Generalized Pareto distribution.

Format
----------------
.. function:: pdfGenPareto(x, a, sigma, k)

    :param x: data 
    :type x: NxK matrix, Nx1 vector or scalar.

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix, Nx1 vector or scalar

    :param sigma: Scale parameter, ExE conformable with *x*. *sigma* must be greater than 0.
    :type sigma: NxK matrix, Nx1 vector or scalar

    :param k: Shape parameter, ExE conformable with *x*.
    :type k: NxK matrix, Nx1 vector or scalar

    :returns: y (*NxK matrix, Nx1 vector or scalar*)

Remarks
-------

The probability density function for the Generalized Pareto distribution
is defined as

.. DANGER:: fix equations

.. math::

   f(x)={1σ(1+k(x−μ)σ)−1−1/k1σexp⁡(−(x−μ)σ)k≠0k=0

.. seealso:: Functions :func:`cdfGenPareto`

