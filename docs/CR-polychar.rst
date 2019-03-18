
polychar
==============================================

Purpose
----------------

Computes the characteristic polynomial of a square matrix.

Format
----------------
.. function:: polychar(x)

    :param x: NxN matrix.
    :type x: TODO

    :returns: c (*TODO*), (N+1)x1 vector of coefficients of the Nth order
        characteristic polynomial of x:
        
        p(x) = c[1]*xn + c[2]*x(n-1) + ... + c[n]*x + c[n+1];

