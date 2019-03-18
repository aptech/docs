
cholsol
==============================================

Purpose
----------------

Solves a system of linear equations given the Cholesky factorization of the system.

Format
----------------
.. function:: cholsol(b, C)

    :param b: NxK matrix.
    :type b: TODO

    :param C: NxN matrix.
    :type C: TODO

    :returns: x (*TODO*), NxK matrix.

Examples
----------------

::

    //Assign the right-hand side 'b' and the Cholesky 
    //factorization 'C'
    b = { 0.03177513, 0.41823100, 1.70129375 };
    C = { 1.73351215 1.53201723 1.78102499,
                   0 1.09926365 0.63230050,
                   0          0 0.67015361 };
    
    //Solve the system of equations
    x = cholsol(b,C);
    
    //Note: C'C is equivalent to C'*C
    A = C'C;
    
    //Solve the system of equations
    x2 = b/A;
    
        -1.9440       -1.9440
    x = -1.5269  x2 = -1.5269
         3.2158        3.2158

.. seealso:: Functions :func:`chol`

solve system equation cholesky factorization matrix
