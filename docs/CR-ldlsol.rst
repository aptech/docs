
ldlsol
==============================================

Purpose
----------------

Computes the solution to a system of linear equations given a factorized matrix returned by the function :func:`ldlp` and one or more right hand sides.

Format
----------------
.. function:: x = ldlsol(b, ldl_factor)

    :param b: the right hand sides of the system of linear equations.
    :type b: Nx1 vector or NxK matrix

    :param ldl_factor: contains the a factorization returned from the function :func:`ldlp`.
    :type ldl_factor: Nx(N+1) matrix

    :return x: contains the solution to LDLTx = b.

    :rtype x: Nx1 vector or NxK matrix

Remarks
-------

Matrix factorization is the most computationally intense part of solving
a system of linear equations. The factorization can be saved and reused
multiple times to prevent the need to repeat the matrix factorization
step. :func:`ldlsol` uses the LAPACK function *dsytrs* to solve the system of
linear equations.


Examples
----------------

::

    // Assign A matrix
    A = { 5   9   3   4,
          9  -6   8   1,
          3   8   2   3,
          4   1   3   9 };

    // Assign b matrix
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

.. seealso:: Functions :func:`ldlp`, :func:`lusol`, :func:`solpd`
