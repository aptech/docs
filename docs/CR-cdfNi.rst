
cdfNi
==============================================

Purpose
----------------
Computes the inverse of the cdf of the Normal distribution.

Format
----------------
.. function:: cdfNi(p)

    :param p: Normal probability levels, :math:`0 <= p <= 1`.
    :type p: NxK real matrix

    :returns: **x** (*NxK real matrix*) - each value of *x* is the smallest integer such that the normal cumulative distribution function is equal to or exceeds the corresponding value of *p*. :math:`cdfN(p) = x`

Remarks
-------

:math:`cdfN(cdfNi(p)) = p` to within the errors given below:

:widths: auto

":math:`p \leq 4.6e-308 `", "-37.5 is returned"
":math:`4.6e-308 < p < 5e-24`", "accurate to :math:`\pm 5` in 12th digit"
":math:`5e-24 < p < 0.5`", "accurate to :math:`\pm 1` in 13th digit"
":math:`0.5 < p < 1 - 2.22045e-16`", "accurate to :math:`\pm 5` in 15th digit"
":math:`p \geq 1 - 2.22045e-16`", "8.12589 is returned"

.. seealso:: :func:`cdfN`
