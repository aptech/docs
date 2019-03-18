
lapeighb
==============================================

Purpose
----------------

Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by bounds.

Format
----------------
.. function:: lapeighb(x, vl, vu, abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param vl: lower bound of the interval to be searched for eigenvalues.
    :type vl: scalar

    :param vu: upper bound of the interval to be searched for eigenvalues;  vu must be greater than  vl.
    :type vu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged
        when it is determined to lie in an interval [a, b] of
        width less than or equal to:
        
        abstol + EPS*max(|a|, |b|)
        where EPS is machine precision. If abstol is less than or equal to
        zero, then EPS*||T|| will be used in its place,
        where T is the tridiagonal matrix obtained by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :returns: ve (*Mx1 vector*), eigenvalues, where M is the number of eigenvalues on
        the half open interval [vl, vu]. If no eigenvalues are found
        then  ve is a scalar missing value.

Examples
----------------

::

    x = { 5 2 1,
          2 6 2,
          1 2 9 };
     
    vl = 5;
    vu = 10;
    ve = lapeighb(x,vl,vu,1e-15);
    print ve;

The code above returns:

::

    6.0000

.. seealso:: Functions :func:`lapeighvi`, :func:`lapeighvb`

eigenvalues real symmetric complex Hermitian matrix selected by bounds
