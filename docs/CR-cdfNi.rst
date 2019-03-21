
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

    :returns: x (*NxK real matrix*), Normal deviates, such that: :math:`cdfN(p) = x`

Remarks
-------

:math:`cdfN(cdfNi(p)) = p` to within the errors given below:

+----------+---+---+----+-----------------+------------------------------+
|          |   | p | <= | 4.6e-308        | -37.5 is returned            |
+----------+---+---+----+-----------------+------------------------------+
| 4.6e-308 | < | p | <  | 5e-24           | accurate to ±5 in 12th digit |
+----------+---+---+----+-----------------+------------------------------+
| 5e-24    | < | p | <  | 0.5             | accurate to ±1 in 13th digit |
+----------+---+---+----+-----------------+------------------------------+
| 0.5      | < | p | <  | 1 - 2.22045e-16 | accurate to ±5 in 15th digit |
+----------+---+---+----+-----------------+------------------------------+
|          |   | p | ≥  | 1 - 2.22045e-16 | 8.12589 is returned          |
+----------+---+---+----+-----------------+------------------------------+


.. seealso:: :func:`cdfN`

