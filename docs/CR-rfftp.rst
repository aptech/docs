
rfftp
==============================================

Purpose
----------------

Computes a real 1- or 2-D FFT. Returns the results in a packed format.

Format
----------------
.. function:: rfftp(x)

    :param x: 
    :type x: NxK real matrix or K-length real vector

    :returns: y (*TODO*), Lx(M/2+1) matrix or (M/2+1)-length vector, where
        L and M are the smallest powers of 2 greater than or equal
        to N and K, respectively.

