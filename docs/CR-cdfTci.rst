
cdfTci
==============================================

Purpose
----------------
Computes the inverse of the complement of the Student's  t cdf.

Format
----------------
.. function:: cdfTci(p,  n)

    :param p: complementary Student's  t probability levels,
        0 <= p <= 1.
    :type p: NxK real matrix

    :param n: degrees of freedom,  n > 1,  n need not be
        integral. ExE conformable with  p.
    :type n: LxM real matrix

    :returns: x (*TODO*), max(N,L) by max(K,M) real matrix, Student's t deviates, such that
        cdfTc(x,  n) =  p.

