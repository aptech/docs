
cdfGenPareto
==============================================

Purpose
----------------
Computes the cumulative distribution function for the Generalized Pareto distribution.

Format
----------------
.. function:: p = cdfGenPareto(x, loc, scale, shape)

    :param x: Values at which to evaluate the Generalized Pareto cdf. :math:`x > 0`.
    :type x: NxK matrix, Nx1 vector or scalar

    :param loc: Location parameter, ExE conformable with *x*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter, ExE conformable with *x*. :math:`scale > 0`.
    :type scale: NxK matrix, Nx1 vector or scalar

    :param shape: Shape parameter, ExE conformable with *x*.
    :type shape: NxK matrix, Nx1 vector or scalar

    :return p: Each element in *p* isthe Generalized Pareto cdf evaluated at the corresponding element in *x*.

    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The cumulative distribution function for the Generalized Pareto
distribution is defined as:

.. math::

    f(x,\mu,\sigma,k) =
    \begin{cases} 1 - (1 + k\frac{x-\mu}{\sigma})^{\frac{-1}{k}},& k \ne 0\\
    1 - exp(-\frac{x-\mu}{\sigma}), & k = 0
    \end{cases}


Examples
---------

::

    // Set location parameter
    loc = 0;

    // Set scale parameter
    scale = 2;

    // Set shape parameter
    shape = 5;

    p = cdfGenPareto(3, loc, scale, shape);

After the above code, `p` is equal to

::

     0.3482


.. seealso:: :func:`pdfGenPareto`
