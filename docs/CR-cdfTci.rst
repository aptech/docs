
cdfTci
==============================================

Purpose
----------------
Computes the inverse of the complement of the Student's t cdf.

Format
----------------
.. function:: cdfTci(p, df)

    :param p: complementary Student's t probability levels, :math:`0 <= p <= 1`.
    :type p: NxK real matrix

    :param df: degrees of freedom, :math:`df > 1`, *df* need not be integral. ExE conformable with *p*.
    :type df: LxM real matrix

    :returns: **x** (*matrix, max(N,L) by max(K,M) real*)- each value of *x* is the smallest integer such that the complement of the Student's t distribution is equal to or exceeds the corresponding value of *p*. :math:`cdfTc(x, df) =  p`.

Remarks
-------

:math:`cdfTc(cdfTci(p, df)) = p` to within the errors given below:

.. csv-table::
    :widths: auto

    ":math:`0.5e-30  < p < 0.01`", "accurate to :math:`\pm 1` in 12th digit"
    ":math:`0.01  < p`", "accurate to :math:`\pm 1e-14`"

Extreme values of arguments can give rise to underflows, but no
overflows are generated.


Examples
----------------

::
    // Probabilities
    p = {0.1,0.25, 0.5,0.75,0.95};

    // Degrees of freedom
    df = 3;

    x = cdfTci(p, df);

After running above code,

::
    x =
    1.6377
    0.7649
    0.0000
    -0.7649
    -2.3534

.. seealso:: cdfTc
