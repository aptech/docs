
cdfBetaInv
==============================================

Purpose
----------------
Computes the quantile or inverse of the Beta cumulative distribution function.

Format
----------------
.. function:: cdfBetaInv(p, a, b)

    :param p: 0 < *p* < 1.
    :type p: NxK matrix, Nx1 vector or scalar

    :param a: *p* < 0 < *a*.
    :type a: ExE conformable

    :param b: *p* < 0 < *b*.
    :type b: ExE conformable

    :returns: x (*NxK matrix, Nx1 vector or scalar*)

Remarks
----------------
For invalid inputs, :func:`cdfBetaInv` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

Examples
----------------

::

    y = { 0.14228251, 0.20662575, 0.26057158, 0.31087052 };
    a = 0.5;
    b = 0.3;
    p = cdfBeta(y,a,b);
    print "p = "	p;

After running above code,

::

    p =
    	0.1
    	0.2
    	0.3
    	0.4

.. seealso:: Functions :func:`cdfBeta`, :func:`cdfBinomial`, :func:`cdfNegBinomial`

