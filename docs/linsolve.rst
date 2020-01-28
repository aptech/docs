
linsolve
==============================================

Purpose
----------------

Solves :math:`Ax = b` using the inverse function.

Format
----------------
.. function:: x = linsolve(b, A)

    :param b: data
    :type b: NxK matrix

    :param A: data
    :type A: NxN matrix

    :return x: the linear solution of :math:`b/A` for each column in *b*.

    :rtype x: NxK matrix

Examples
----------------

::

    // Assign b
    b = { 2, 3, 4 };

    // Assign A
    A = { 10 2 3, 6 14 2, 1 1 9 };

    //  Solve Ax = b
    x = linsolve(b, A);
    print x

::

    0.04586330
    0.13399281
    0.42446043

Remarks
-------

:func:`linsolve` solves for *x* by computing :math:`inv(A) \times b`. If *A* is square and *b*
contains more than 1 column, it is much faster to use :func:`linsolve` than the
``/`` operator. However, while faster, there is some sacrifice in accuracy.

A test shows :func:`linsolve` to be acccurate to within approximately 1.2e-11,
while the slash operator ``/`` is accurate to within approximately 4e-13.
However, the accuracy sacrifice can be much greater for poorly
conditioned matrices.


.. seealso:: Functions :func:`qrsol`, :func:`qrtsol`, :func:`solpd`, :func:`cholsol`
