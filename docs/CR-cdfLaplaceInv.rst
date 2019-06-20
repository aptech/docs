
cdfLaplaceInv
==============================================

Purpose
----------------
Computes the Laplace inverse cumulative distribution function.

Format
----------------
.. function:: cdfLaplaceInv(p, loc, scale)

    :param p: Probabilities at which to compute the inverse of the Laplace cumulative distribution function. :math:`0 \lt p \lt 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param loc: Location parameter, ExE conformable with *x*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter; ExE conformable with *x*. :math:`0 < scale `.
    :type scale: NxK matrix, Nx1 vector or scalar

    :returns: **x** (*NxK matrix, Nx1 vector or scalar*) - each value of *x* is the smallest integer such that the Laplace cumulative distribution function with *loc* and *scale* evaluated at *x* is equal to or exceeds the corresponding value of *p*.

Examples
---------

::
    // Probabilities
    p = {0.1, 0.25, 0.5, 0.75, 0.95};

    // Location parameter
    loc = 0;

    // Scale parameter
    scale = 3;

    x = cdfLaplaceInv(x, loc, scale);
    print "x =" x;

After the above code:

::

  x =
    -4.8283
    -2.0794
    0.0000
    2.0794
    6.9078

.. seealso:: :func:`cdfLaplace`
