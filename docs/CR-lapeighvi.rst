
lapeighvi
==============================================

Purpose
----------------

Computes selected eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix.

Format
----------------
.. function:: lapeighvi(x, il, iu, abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param il: index of the smallest desired eigenvalue ranking them from smallest to largest.
    :type il: scalar

    :param iu: index of the largest desired eigenvalue, iu must be greater than  il.
    :type iu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged when it is determined to lie in an interval
        [a, b] of width less than or equal to abstol + EPS*max(|a|, |b|), where
        EPS is machine precision. If abstol is less than or equal to zero, then EPS*||T|| will be used in its place,
        where  T is the tridiagonal matrix obtained by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :returns: ve (*(iu- il+1)x1 vector*) , eigenvalues.

    :returns: va (*Nx(iu- il+1) matrix*) , eigenvectors.

Remarks
-------

lapeighvi computes iu-il+1 eigenvalues and eigenvectors given a range of
indices, i.e., theith to jth eigenvalues, ranking them from smallest to
largest. To find eigenvalues and eigenvectors within a specified range
see lapeighvb. lapeighvi is based on the LAPACK drivers DSYEVX and
ZHEEVX. Further documentation of these functions may be found in the
LAPACK User's Guide.


Examples
----------------

::

    x = { 5 2 1,
          2 6 2,
          1 2 9 };
     
    il = 2;
    iu = 3;
    { ve,va } = lapeighvi(x,il,iu,0);
    print "ve = " ve;
    print "va = " va;

::

    ve =
    6.0000
    10.6056
    
    va =
    -0.5774   0.3197
    -0.5774   0.4908
     0.5774   0.8105

.. seealso:: Functions :func:`lapeighvb`, :func:`lapeighb`

eigenvalue eigenvectors real symmetric complex Hermitian matrix
