
pdfCauchy
==============================================

Purpose
----------------

Computes the probability density function for the Cauchy distribution.

Format
----------------
.. function:: y = pdfCauchy(x, mu, sigma)

    :param x: data
    :type x: NxK matrix, Nx1 vector or scalar

    :param mu: Location parameter. ExE conformable with *x*.
    :type mu: NxK matrix, Nx1 vector or scalar

    :param sigma: Scale parameter. ExE conformable with *x*. *sigma* must be greater than 0.
    :type sigma: NxK matrix, Nx1 vector or scalar

    :return y: 

    :rtype y: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function for the Cauchy distribution is defined as:

.. DANGER:: fix equations

.. math::

   f(x)=(πσ(1+(x−μσ)2))−1

.. seealso:: Functions :func:`cdfCauchy`

