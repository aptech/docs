
cdfLogistic
==============================================

Purpose
----------------
Computes the cumulative distribution function for the logistic distribution.

Format
----------------
.. function:: cdfLogistic(x, loc, scale)

    :param x: Values at which to evaluate the cumulative distribution function for the logistic distribution.
    :type x: NxK matrix, Nx1 vector or scalar.

    :param loc: Location parameter, ExE conformable with *x*.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param scale: Scale parameter; ExE conformable with *x*. :math:`0 < scale `.
    :type scale: NxK matrix, Nx1 vector or scalar

    :returns: **p** (*NxK matrix, Nx1 vector or scalar*) - Each element in *p* is the cumulative distribution function for the logistic distribution evaluated at the corresponding element in *x*.

Remarks
-------

The cumulative distribution function for the logistic distribution is
defined as:

.. math::

    f(x, \mu, \sigma) = \frac{1}{1 + exp(-z)}

where

.. math::

    z = \frac{x - \mu}{\sigma}

Examples
--------

::
    // Values of interest
    x = { 1, 2, 3 };

    // Location parameter
    loc = 0;

    // Scale parameter
    s = 2;

    p = cdfLogistic(x, loc, s);

After the above code, `p` will equal:

::

    0.6225
    0.7311
    0.8176

.. seealso:: :func:`pdfLogistic`
