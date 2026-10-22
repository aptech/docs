
cdfBeta
==============================================

Purpose
----------------

Computes the incomplete Beta function (i.e., the cumulative distribution function of the Beta distribution).

Format
----------------
.. function:: p = cdfBeta(x, a, b)

    :param x: Values at which to evaluate the Beta cdf. An *x* below 0 returns 0 and an *x* above 1 returns 1.
    :type x: NxK matrix

    :param a: ExE conformable with *x*. :math:`a > 0`
    :type a: LxM matrix

    :param b: ExE conformable with *x* and *a*. :math:`b > 0`
    :type b: PxQ matrix

    :return p: *p* is the integral from 0 to *x* of the beta distribution with parameters *a* and *b*.

    :rtype p: matrix, max(N,L,P) by max(K,M,Q)

Examples
----------------

::

    // Values
    x = { 0.0506, 0.1886, 0.3781, 0.5763 };

    // Beta parameters
    a = 0.5;
    b = 0.3;

    // Total probabilities
    p = cdfBeta(x, a, b);
    print "p = "	 p;

After running above code,

::

  p =
    0.1000
    0.2000
    0.3000
    0.4000

Remarks
-------

If *a* or *b* is not greater than 0, :func:`cdfBeta` returns a scalar error code
and :func:`scalerr` returns the position of that argument: 2 for *a*, 3 for *b*.
A missing value in any argument returns a missing value.


.. seealso:: Functions :func:`cdfChic`, :func:`cdfFc`, :func:`cdfN`, :func:`cdfNc`, :func:`cdfTc`, :func:`gamma`
