
cdfTci
==============================================

Purpose
----------------
Computes the inverse of the complement of the Student's t cdf.

Format
----------------
.. function:: x = cdfTci(p, df)

    :param p: complementary Student's t probability levels, :math:`0 <= p <= 1`.
    :type p: NxK real matrix

    :param df: degrees of freedom, :math:`df > 1`, *df* need not be an integer. ExE conformable with *p*.
    :type df: LxM real matrix

    :return x: each value of *x* is the value such that the complement of the Student's t distribution is equal to the corresponding value of *p*. :code:`cdfTc(x, df) =  p`.

    :type x: matrix, max(N,L) by max(K,M) real

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
