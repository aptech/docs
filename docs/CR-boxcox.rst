
boxcox
==============================================

Purpose
----------------
Computes the Box-Cox function.

Format
----------------
.. function:: boxcox (x,  lambda)

    :param x: MxN matrix or P-dimensional array where the last two dimensions are MxN.
    :type x: TODO

    :param lambda: KxL matrix or P-dimensional array where the last two dimensions are KxL, ExE conformable to x.
    :type lambda: TODO

    :returns: y (*TODO*), max(M,L)xmax(N,K) or P-dimensional array where the last two dimensions are max(M,L)xmax(N,K).

Examples
----------------

::

    x = { .2, .4, .8, 1, 1.2, 1.4 };
    lambda = .4;
    y = boxcox(x,lambda);

After the code above:

::

    -1.187
        -0.767
    y = -0.213
         0.000
         0.189
         0.360

box cox transformation
