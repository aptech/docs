
boxcox
==============================================

Purpose
----------------
Computes the Box-Cox function.

Format
----------------
.. function:: boxcox(x, lambda)

    :param x: 
    :type x: MxN matrix or P-dimensional array where the last two dimensions are MxN

    :param lambda: 
    :type lambda: KxL matrix or P-dimensional array where the last two dimensions are KxL, ExE conformable to x.

    :returns: y, max(M,L)xmax(N,K) or P-dimensional array where the last two dimensions are max(M,L)xmax(N,K).

Remarks
-------

Allowable range for *x* is: :math:`x > 0`

The :func:`boxcox` function computes:

.. math:: boxcox(x) = (xλ - 1)/λ

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

