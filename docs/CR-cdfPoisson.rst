
cdfPoisson
==============================================

Purpose
----------------
Computes the Poisson cumulative distribution function.

Format
----------------
.. function:: p = cdfPoisson(x, lambda)

    :param x: Values at which to evaluate the cumulative distribution function for the Poisson distribution. :math:`x > 0`.
    :type x: NxK matrix, Nx1 vector or scalar

    :param lambda: The mean parameter.
    :type lambda: ExE conformable with *x*

    :return p: Each element in *p* is the cumulative distribution function of the Poisson distribution evaluated at the corresponding element in *x*.

    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

For invalid inputs, :func:`cdfPoisson` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

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

.. seealso:: Functions :func:`cdfPoissonInv`, :func:`pdfPoisson`, :func:`cdfBinomial`, :func:`cdfNegBinomial`
