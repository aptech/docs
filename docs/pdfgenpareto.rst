
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

Examples
----------------

::

    // Data points
    x = { 0.5, 1, 2, 3 };

    // Generalized Pareto PDF with location = 0, scale = 1, shape = 0.5
    p = pdfGenPareto(x, 0, 1, 0.5);
    print p;

After the code above, *p* is equal to:

::

       0.51200000
       0.29629630
       0.12500000
      0.064000000

.. seealso:: Functions :func:`cdfGenPareto`
