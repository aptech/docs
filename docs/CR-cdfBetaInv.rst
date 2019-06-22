
cdfBetaInv
==============================================

Purpose
----------------
Computes the quantile or inverse of the Beta cumulative distribution function.

Format
----------------
.. function:: cdfBetaInv(p, a, b)

    :param p: Probabilities at which to compute the inverse of the Beta cumulative distribution function. :math:`0 \lt p \lt 1`
    :type p: NxK matrix, Nx1 vector or scalar

    :param a: ExE conformable with *p*. :math:`a > 0`
    :type a: LxM matrix

    :param b: ExE conformable with *p* and *a*. :math:`b > 0`
    :type b: PxQ matrix

    :returns: **x** (*NxK matrix, Nx1 vector or scalar*) - Each value of `x` is the value which if passed to :func:`cdfBeta` will return the corresponding value of `p`.

Remarks
----------------
For invalid inputs, :func:`cdfBetaInv` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

Examples
----------------

::

    // List of probabilities
    p = { 0.10, 0.20, 0.30, 0.40 };

    // Beta parameters
    a = 0.5;
    b = 0.3;

    // Call cdfBetaInv
    x = cdfBetaInv(p, a, b);
    print "x = "	x;

After running the above code,

::

  x =
    0.0506
    0.1886
    0.3781
    0.5763

.. seealso:: Functions :func:`cdfBeta`, :func:`cdfBinomial`, :func:`cdfNegBinomial`
