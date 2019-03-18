
ldlp
==============================================

Purpose
----------------

Returns the Bunch-Kaufmann factorization of a real symmetric matrix along with a permutation vector.

Format
----------------
.. function:: ldlp(A)

    :param A: NxN real symmetric matrix.
    :type A: TODO

    :returns: ldl_factor (*TODO*), (N+1)xN matrix, containing the factors L and D as well as the permutation vector P, which can be passed directly to ldlsol to solve a system of linear equations.

Examples
----------------

::

    A = { 5   9   3   4, 
          9  -6   8   1, 
          3   8   2   3, 
          4   1   3   9 };
    b = { 1.4, 4, 0.5, 3 };
    
    //Factorize matrix 'A'
    ldl_f = ldlp(A);
    
    //Solve system of equations
    x = ldlsol(b, ldl_f);

Ax = b
x

::

    0.5729 
    x = -0.1529 
        -0.2829 
         0.1900

.. seealso:: Functions :func:`ldlsol`, :func:`chol`, :func:`solpd`

Bunch-Kaufmann factorization real symmetric matrix permutation vector
