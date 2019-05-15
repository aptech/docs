
solpd
==============================================

Purpose
----------------
Solves a set of positive definite linear equations.

Format
----------------
.. function:: solpd(b, A)

    :param b: NxK matrix or M-dimensional array where the last two dimensions are NxK
    :type b: matrix or array

    :param A: NxN symmetric positive definite matrix or M-dimensional array where the 
        NxN 2-dimensional arrays described by the last two dimensions are symmetric and positive definite
    :type A: matrix or array

    :returns: x (*NxK matrix or M-dimensional array*) where the last two dimensions are NxK, the solutions for
        the system of equations, :math:`Ax = b`.

Remarks
-------

.. DANGER:: check equations

*b* can have more than one column. If so, the system of equations is
solved for each column, i.e., :math:`A*x[., i] = b[., i]`.

This function uses the Cholesky decomposition to solve the system
directly. Therefore it is more efficient than using :math:`inv(A)*b`.

If *b* and *A* are M-dimensional arrays, the sizes of their corresponding
M-2 leading dimensions must be the same. The resulting array will
contain the solutions for the system of equations given by each of the
corresponding 2-dimensional arrays described by the two trailing
dimensions of *b* and *A*. In other words, for a 10x4x2 array *b* and a 10x4x4
array *A*, the resulting array *x* will contain the solutions for each of
the 10 corresponding 4x2 arrays contained in *b* and 4x4 arrays contained
in *A*. Therefore, :math:`A[n,.,.]*x[n,.,.] = b[n,.,.]`, for :math:`1 ≤ n ≤ 10`.

:func:`solpd` does not check to see that the matrix *A* is symmetric. :func:`solpd` will
look only at the upper half of the matrix including the principal diagonal.

If the *A* matrix is not positive definite:

=========== ==================================
``trap 1``  return scalar error code 30.
``trap 0``  terminate with an error message.
=========== ==================================

One obvious use for this function is to solve for least squares
coefficients. The effect of this function is thus similar to that of the
``/`` operator.

If *X* is a matrix of independent variables, and *Y* is a vector containing
the dependent variable, then the following code will compute the least
squares coefficients of the regression of *Y* on *X*:

::

   b = solpd(X'Y,X'X);

Examples
----------------

::

    n = 5;
    format /lo 16,8;
    
    A = rndn(n,n);
    A = A'A;
    x = rndn(n,1);
    b = A*x;
    
    x2 = solpd(b,A);
    
    print " X solpd(b,A) Difference";
    print x~x2~x-x2;

::

    X solpd(b,A) Difference
     
     0.32547881   0.32547881  -4.9960036e-16
     1.5190182    1.5190182   -1.7763568e-15
     0.88099266   0.88099266   1.5543122e-15
     1.8192784    1.8192784   -2.2204460e-16
    -0.060848175 -0.060848175 -1.4710455e-15

.. seealso:: Functions :func:`chol`, :func:`invpd`, `trap`

