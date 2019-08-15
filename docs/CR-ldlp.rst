
ldlp
==============================================

Purpose
----------------

Returns the Bunch-Kaufmann factorization of a real symmetric matrix along with a permutation vector.

Format
----------------
.. function:: ldl_factor = ldlp(A)

    :param A: data
    :type A: NxN real symmetric matrix

    :return ldl_factor: containing the factors *L* and *D* as well as the permutation vector *P*, which can be passed directly to :func:`ldlsol` to solve a system of linear equations.

    :rtype ldl_factor: (N+1)xN matrix

Remarks
-------

Matrix factorization is the most computationally intense part of solving
a system of linear equations. The factorization can be saved and reused
multiple times to prevent the need to repeat the matrix factorization
step. :func:`ldlp` uses the LAPACK function *dsytrf* to compute the factorization.


Examples
----------------

::

    A = { 5   9   3   4, 
          9  -6   8   1, 
          3   8   2   3, 
          4   1   3   9 };
    b = { 1.4, 4, 0.5, 3 };
    
    // Factorize matrix 'A'
    ldl_f = ldlp(A);
    
    // Solve system of equations
    x = ldlsol(b, ldl_f);

The above code will solve the system of linear equations :math:`Ax = b`, assigning *x* to be equal to:

::

         0.5729 
    x = -0.1529 
        -0.2829 
         0.1900

.. seealso:: Functions :func:`ldlsol`, :func:`chol`, :func:`solpd`

