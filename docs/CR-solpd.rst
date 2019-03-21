
solpd
==============================================

Purpose
----------------
Solves a set of positive definite linear equations.

Format
----------------
.. function:: solpd(b, A)

    :param b: 
    :type b: NxK matrix or M-dimensional array where the last two dimensions are NxK

    :param A: 
    :type A: NxN symmetric positive definite matrix or M-dimensional array where the NxN 2-dimensional
        arrays described by the last two dimensions are symmetric and positive definite

    :returns: x (*TODO*), NxK matrix or M-dimensional array where the last two dimensions are NxK, the solutions for
        the system of equations, Ax = b.

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

.. seealso:: Functions :func:`chol`, :func:`invpd`, :func:`trap`

solve system positive definite linear equation
