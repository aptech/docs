
beta
==============================================

Purpose
----------------

Computes the standard Beta function, also called the Euler integral. The beta function is defined as:
B(x,y)  =  ∫01      tx−1(1−t)y−1dt

Format
----------------
.. function:: beta(x,y)

    :param x: scalar or NxK matrix; x may be real or complex.
    :type x: TODO

    :param y: ExE conformable with x.
    :type y: LxM matrix

    :returns: f (*TODO*), NxK matrix.

