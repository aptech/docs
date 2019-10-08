
pdfGenPareto
==============================================

Purpose
----------------

Computes the probability density function for the Generalized Pareto distribution.

Format
----------------
.. function:: y = pdfGenPareto(x, a, sigma, k)

    :param x: data
    :type x: NxK matrix, Nx1 vector or scalar.

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix, Nx1 vector or scalar

    :param sigma: Scale parameter, ExE conformable with *x*. *sigma* must be greater than 0.
    :type sigma: NxK matrix, Nx1 vector or scalar

    :param k: Shape parameter, ExE conformable with *x*.
    :type k: NxK matrix, Nx1 vector or scalar

    :return p: the probability density function for the Generalized Pareto distribution for the elements in *x*.

    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function for the Generalized Pareto distribution
is defined as

.. math::

    f(x)= \begin{cases}
    \frac{1}{\sigma}\big(1 + k
      \frac{x-\mu}{\sigma} \big)^{-1 - 1/k},& k\neq 0\\
    \frac{1}{\sigma}exp(\frac{x-\mu}{\sigma}), &  k = 0
    \end{cases}

.. seealso:: Functions :func:`cdfGenPareto`
