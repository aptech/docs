
cdfChincInv
==============================================

Purpose
----------------
Computes the quantile or inverse of noncentral chi-square cumulative distribution function.

Format
----------------
.. function:: cdfChincInv(y, df, nonc)

    :param y: Nx1 vector or scalar. The integral from 0 to *x*.
    :type y: NxK matrix

    :param df:  The degrees of freedom. *df* > 0.
    :type df: ExE conformable with *y*

    :param nonc:  The noncentrality parameter. Note: This is the square root of the noncentrality parameter that sometimes goes under the symbol lambda. *nonc* > 0.
    :type nonc: ExE conformable with *y*

    :returns: x (*NxK matrix or Nx1 vector or scalar*). The upper limit of the integrals of the noncentral chi-square distribution with *df* degrees of freedom and noncentrality *nonc*.

Remarks
-------

.. NOTE:: Input *nonc* is the square root of the noncentrality parameter that sometimes goes under the symbol lambda.

For invalid inputs, :func:`cdfChincinv` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, scalerr will return a 2; etc.

.. seealso:: :func:`cdfChinc`, :func:`cdfChic`, :func:`cdfFnc`, :func:`cdfTnc`

