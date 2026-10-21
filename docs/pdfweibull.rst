
pdfWeibull
==============================================

Purpose
----------------
Computes the probability density function of a Weibull random variable.

Format
----------------
.. function:: p = pdfWeibull(x, shape, scale)

    :param x: *x* must be greater than 0.
    :type x: NxK matrix, Nx1 vector or scalar

    :param shape: Shape parameter (:math:`k` below), ExE conformable with *x*. *shape* must be greater than 0.
    :type shape: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter (:math:`\lambda` below), may be matrix, ExE conformable with *x*. *scale* must be greater than 0.
    :type scale: NxK matrix, Nx1 vector or scalar

    :return p: the probability density function of a Weibull random variable evaluated at *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function of a Weibull random variable is defined as

.. math::

    f(x, \lambda, k) = \begin{cases}
    \frac{k}{\lambda} \big(\frac{x}{\lambda}\big)^{k-1} e^{-(x/\lambda)k}, & x \geq 0\\
    0, &  x < 0
    \end{cases}


Examples
----------------

::

    // Data points
    x = { 0.5, 1, 2, 3 };

    // Weibull PDF with shape = 2, scale = 1
    p = pdfWeibull(x, 2, 1);
    print p;

After the code above, *p* is equal to:

::

       0.77880078
       0.73575888
      0.073262556
    0.00074045882

.. seealso:: Functions :func:`cdfWeibull`, :func:`cdfWeibullInv`
