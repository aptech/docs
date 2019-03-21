
cdfExp
==============================================

Purpose
----------------
Computes the cumulative distribution function for the exponential distribution.

Format
----------------
.. function:: cdfExp(x, a, m)

    :param x: 
    :type x: NxK matrix or Nx1 vector or scalar.

    :param a: Location parameter, ExE conformable with *x*. *a* must be less than *x*.
    :type a: ; NxK matrixor Nx1 vector or scalar

    :param m: Mean parameter, ExE conformable with *x*. *m* must be greater than 0.
    :type m: ; NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)

Remarks
-------

The cumulative distribution function for the exponential distribution is defined as

.. math:: 1−exp⁡(−x−ab)

.. seealso:: Function :func:`pdfExp`

