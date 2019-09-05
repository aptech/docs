
lapeighvi
==============================================

Purpose
----------------

Computes selected eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix.

Format
----------------
.. function:: { ve, va } = lapeighvi(x, il, iu, abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param il: index of the smallest desired eigenvalue ranking them from smallest to largest.
    :type il: scalar

    :param iu: index of the largest desired eigenvalue, *iu* must be greater than *il*.
    :type iu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged when it is determined to lie in an interval
        :math:`[a, b]` of width less than or equal to :math:`abstol + EPS*max(|a|, |b|)`, where
        *EPS* is machine precision. If *abstol* is less than or equal to zero, then :math:`EPS*||T||` will be used in its place,
        where *T* is the tridiagonal matrix obtained by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :return ve: eigenvalues.

    :rtype ve: (iu-il+1)x1 vector

    :return va: eigenvectors.

    :rtype va: Nx(iu-il+1) matrix

Remarks
-------

:func:`lapeighvi` computes :math:`iu-il+1` eigenvalues and eigenvectors given a range of
indices, i.e., the ith to jth eigenvalues, ranking them from smallest to
largest. To find eigenvalues and eigenvectors within a specified range
see :func:`lapeighvb`. :func:`lapeighvi` is based on the LAPACK drivers *DSYEVX* and
*ZHEEVX*. Further documentation of these functions may be found in the
LAPACK User's Guide.


Examples
----------------

::

    // Assign x
    x = { 5 2 1,
          2 6 2,
          1 2 9 };

    // Index of smallest desired eigenvalue
    il = 2;

    // Index of largest desired eigenvalue
    iu = 3;

    // Compute eigenvalues with indices between
    // il and iu and the corresponding eigenvectors
    { ve, va } = lapeighvi(x, il, iu, 0);
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
