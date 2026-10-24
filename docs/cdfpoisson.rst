
cdfPoisson
==============================================

Purpose
----------------
Computes the Poisson cumulative distribution function.

Format
----------------
.. function:: p = cdfPoisson(x, lambda)

    :param x: Values at which to evaluate the cumulative distribution function for the Poisson distribution. An *x* within 1e-9 (relative) of a whole number is treated as that whole number. Any other fractional *x* is rounded down. An *x* below 0 returns 0.
    :type x: NxK matrix, Nx1 vector or scalar

    :param lambda: The mean parameter. :math:`lambda \geq 0`.
    :type lambda: ExE conformable with *x*

    :return p: Each element in *p* is the cumulative distribution function of the Poisson distribution evaluated at the corresponding element in *x*.

    :rtype p: NxK matrix, Nx1 vector or scalar

Examples
----------------
Suppose that a hospital emergency department sees and average of 200 patients during the Friday
evening shift. What is the probability that they will see fewer than 250 patients during any one Friday evening shift.

::

    // The mean parameter
    lambda = 200;

    // Value to compute cdf
    x = 250;

    p = cdfPoisson(x, lambda);

After running above code,

::

    p = 0.99971538 or 99.715%

Remarks
-------

If *lambda* is below 0, :func:`cdfPoisson` returns a scalar error code and
:func:`scalerr` returns 2, the position of *lambda*. An *x* below 0 is not an
error: it returns 0. A missing value in either argument returns a missing
value.

.. seealso:: Functions :func:`cdfPoissonInv`, :func:`pdfPoisson`, :func:`cdfBinomial`, :func:`cdfNegBinomial`
