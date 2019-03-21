
cdfFnc
==============================================

Purpose
----------------
Computes the cumulative distribution function of the noncentral F distribution.

Format
----------------
.. function:: cdfFnc(x, n1, n2, d)

    :param x: values of upper limits of integrals, :math:`x > 0`.
    :type x: Nx1 vector

    :param v1: degrees of freedom of numerator, :math:`n1 > 0`.
    :type v1: scalar

    :param v2: degrees of freedom of denominator, :math:`n2 > 0`.
    :type v2: scalar

    :param d: noncentrality parameter, :math:`d > 0`.
        
        This is the square root of the noncentrality parameter
        that sometimes goes under the symbol lambda. (See Scheffe,
        The Analysis of Variance, App. IV, 1959.)
    :type d: scalar

    :returns: y (*Nx1 vector*)

Remarks
-------

For invalid inputs, :func:`cdfFnc` will return a scalar error code which, when
its value is assessed by function :func:`scalerr`, corresponds to the invalid
input. If the first input is out of range, :func:`scalerr` will return a 1; if
the second is out of range, :func:`scalerr` will return a 2; etc.

.. seealso:: :func:`cdfTnc`, :func:`cdfChinc`

