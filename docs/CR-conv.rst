
conv
==============================================

Purpose
----------------

Computes the convolution of two vectors.

Format
----------------
.. function:: conv(b, x,  f,  l)

    :param b: Nx1 vector.
    :type b: TODO

    :param x: Lx1 vector.
    :type x: TODO

    :param f: the first convolution to compute.
    :type f: scalar

    :param l: the last convolution to compute.
    :type l: scalar

    :returns: c (*Qx1 result*), where: Q = (l - f + 1)
        
        If f is 0, the first
        to the l'th convolutions are computed. If  l is 0, the
        f'th to the last convolutions are computed. If  f and  l
        are both zero, all the convolutions are computed.

