
pdfCauchy
==============================================

Purpose
----------------

Computes the probability density function for the Cauchy distribution.

Format
----------------
.. function:: p = pdfCauchy(x, mu, sigma)

    :param x: data
    :type x: NxK matrix, Nx1 vector or scalar

    :param mu: Location parameter. ExE conformable with *x*.
    :type mu: NxK matrix, Nx1 vector or scalar

    :param sigma: Scale parameter. ExE conformable with *x*. *sigma* must be greater than 0.
    :type sigma: NxK matrix, Nx1 vector or scalar

    :return p: the probability density function for the Cauchy distribution for the elements in *x*.

    :rtypep: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function for the Cauchy distribution is defined as:

.. math::

   f(x) = \bigg(\pi \sigma \Big(1+\Big(\frac{x−\mu}{\sigma}\Big)^2\Big)\bigg) ^{−1}

.. seealso:: Functions :func:`cdfCauchy`
