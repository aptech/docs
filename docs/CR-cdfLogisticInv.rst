
cdfLogisticInv
==============================================

Purpose
----------------
Computes the logistic inverse cumulative distribution function.

Format
----------------
.. function:: cdfLogisticInv(p, a, b)

    :param p: must be greater than 0 and less than 1.
    :type p: NxK matrix or Nx1 vector or scalar

    :param a: Location parameter, ExE conformable with  *p*.
    :type a: NxK matrix or Nx1 vector or scalar

    :param b: Scale parameter, ExE conformable with *p*. *b* must be greater than 0.
    :type b: NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)


.. seealso:: :func:`pdfLogistic`, :func:`cdfLogistic`

