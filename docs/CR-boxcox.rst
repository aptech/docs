
boxcox
==============================================

Purpose
----------------
Computes the Box-Cox function.

Format
----------------
.. function:: y = boxcox(x, lambda)

    :param x: where the last two dimensions are MxN
    :type x: MxN matrix or P-dimensional array 

    :param lambda: where the last two dimensions are KxL, ExE conformable to x.
    :type lambda: KxL matrix or P-dimensional array

    :return y: where the last two dimensions are max(M,L)xmax(N,K)

    :rtype y: max(M,L)xmax(N,K) or P-dimensional array

Examples
----------------

::

    x = { .2, .4, .8, 1, 1.2, 1.4 };
    lambda = .4;
    y = boxcox(x, lambda);

After the code above:

::

        -1.187
        -0.767
    y = -0.213
         0.000
         0.189
         0.360

Remarks
-------

Allowable range for *x* is: :math:`x > 0`

The :func:`boxcox` function computes:

.. math:: boxcox(x) = (xλ - 1)/λ

