
linsolve
==============================================

Purpose
----------------

Solves Ax = b using the inverse function.

Format
----------------
.. function:: linsolve(b, A)

    :param b: 
    :type b: NxK matrix

    :param A: 
    :type A: NxN matrix

    :returns: x (*NxK matrix*), the linear solution of  b/A for each column in  b.

Examples
----------------

::

    b = { 2, 3, 4 };
    A = { 10 2 3, 6 14 2, 1 1 9 };
    x = linsolve(b,A);
    print x

::

    0.04586330
    0.13399281
    0.42446043

.. seealso:: Functions :func:`qrsol`, :func:`qrtsol`, :func:`solpd`, :func:`cholsol`

inverse function factorization solve linear equation solution
