
cdfFncInv
==============================================

Purpose
----------------
Computes the quantile or inverse of noncentral F cumulative distribution function.

Format
----------------
.. function:: cdfFncInv(y, dfn, dfd, nonc)

    :param y: Nx1 vector or scalar.
    :type y: NxK matrix

    :param dfn: The degrees of freedom numerator. :math:`dfn > 0`.
    :type dfn: ExE conformable with *y*

    :param dfd: The degrees of freedom denominator. :math:`dfd > 0`.
    :type dfd: ExE conformable with *y*

    :param nonc: The noncentrality parameter. Note: This is the square root of the noncentrality parameter that sometimes goes under the symbol lambda. :math:`nonc > 0`.
    :type nonc: ExE conformable with *y*

    :returns: x (*NxK matrix or Nx1 vector or scalar*). The upper limit of the integrals of the noncentral F distribution.

Remarks
-------

.. NOTE:: Input *nonc* is the square root of the noncentrality parameter that sometimes goes under the symbol lambda.

For invalid inputs, :func:`cdfFncInv` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

.. seealso:: :func:`cdfFnc`, :func:`cdfChinc`, :func:`cdfChic`, :func:`cdfTnc`

