
cdfTci
==============================================

Purpose
----------------
Computes the inverse of the complement of the Student's :math:`t` cdf.

Format
----------------
.. function:: cdfTci(p, n)

    :param p: complementary Student's t probability levels, :math:`0 <= p <= 1`.
    :type p: NxK real matrix

    :param n: degrees of freedom, :math:`n > 1`, *n* need not be integral. ExE conformable with *p*.
    :type n: LxM real matrix

    :returns: x (*matrix*), max(N,L) by max(K,M) real matrix, Student's t deviates, such that :math:`cdfTc(x, n) =  p`.

Remarks
-------

:math:`cdfTc(cdfTci(p, n)) = p` to within the errors given below:

+---------+---+---+---+------+------------------------------+
| 0.5e-30 | < | p | < | 0.01 | accurate to ±1 in 12th digit |
+---------+---+---+---+------+------------------------------+
| 0.01    | < | p |   |      | accurate to ±1e-14           |
+---------+---+---+---+------+------------------------------+

Extreme values of arguments can give rise to underflows, but no
overflows are generated.

.. seealso:: cdfTc

