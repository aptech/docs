
lapeighi
==============================================

Purpose
----------------

Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by index.

Format
----------------
.. function:: lapeighi(x, il, iu, abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param il: index of the smallest desired eigenvalue ranking them from smallest to largest.
    :type il: scalar

    :param iu: index of the largest desired eigenvalue, *iu* must be greater than *il*.
    :type iu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged
        when it is determined to lie in an interval :math:`[a, b]` of width less
        than or equal to :math:`abstol + EPS*max(|a|, |b|)`, where *EPS* is machine precision. 
        If *abstol* is less than or equal to zero, then :math:`EPS*||T||` will be used in its place, 
        where *T* is the tridiagonal matrix obtaineda by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :returns: ve (*(iu-il+1)x1 vector*) eigenvalues.

Remarks
-------

:func:`lapeighi` computes :math:`iu-il+1` eigenvalues only given a range of indices,
i.e., the ith to jth eigenvalues, ranking them from smallest to largest.
To find eigenvalues within a specified range see :func:`lapeighxb`. For
eigenvectors see :func:`lapeighvi`, or :func:`lapeighvb`. :func:`lapeighi` is based on the
LAPACK drivers *DSYEVX* and *ZHEEVX*. Further documentation of these
functions may be found in the LAPACK User's Guide.


Examples
----------------

::

    x = { 5 2 1,
          2 6 2,
          1 2 9 };
     
    il = 2;
    iu = 3;
    ve = lapeighi(x,il,iu,0);
    print ve;

The code above calculates the second and third eigenvalues and returns:

::

    6.0000
    10.6056

To calculate the first, second and third eigenvalues, reusing the same *x* from above:

::

    ve = lapeighi(x,1,3,0);
    print ve;

The output from this code is:

::

     3.3944
     6.0000
    10.6056

.. seealso:: Functions :func:`lapeighb`, :func:`lapeighvi`, :func:`lapeighvb`

