
cdfLaplace
==============================================

Purpose
----------------
Computes the cumulative distribution function for the Laplace distribution.

Format
----------------
.. function:: p = cdfLaplace(x, loc, scale)

    :param x: Values at which to evaluate the cumulative distribution function for the Laplace distribution.
    :type x: NxK matrix, Nx1 vector or scalar.

    :param loc: Location parameter, ExE conformable with *x*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter; ExE conformable with *x*. :math:`0 < scale`.
    :type scale: NxK matrix, Nx1 vector or scalar

    :return p: Each element in *p* is the cumulative distribution function for the Laplace distribution evaluated at the corresponding element in *x*.

    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The cumulative distribution function for the Laplace distribution is
defined as

.. math::

    f(x, \mu, b) = \begin{cases} \frac{1}{2} exp(\frac{(x-\mu)}{b}), & x \lt \mu\\
    1 - \frac{1}{2} exp(-\frac{(x - \mu)}{b}), & x \ge \mu
    \end{cases}


Examples
---------

::

    // Values of interest
    x = 2;

    // Location parameter
    loc = 0;

    // Scale parameter
    scale = 3;

    p = cdfLaplace(x, loc, scale);

After the above code, `p` will equal:

::

    0.7433

.. seealso:: :func:`cdfLaplaceInv`
