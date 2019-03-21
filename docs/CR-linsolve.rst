
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

Remarks
-------

linsolve solves for x by computing inv(A)\*b. If A is square and b
contains more than 1 column, it is much faster to use linsolve than the
/ operator. However, while faster, there is some sacrifice in accuracy.

A test shows linsolve to be acccurate to within approximately 1.2e-11,
while the slash operator '/' is accurate to within approximately 4e-13.
However, the accuracy sacrifice can be much greater for poorly
conditioned matrices.


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
