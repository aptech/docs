
cholsol
==============================================

Purpose
----------------

Solves a system of linear equations given the Cholesky factorization of the system.

Format
----------------
.. function:: cholsol(b, C)

    :param b: 
    :type b: NxK matrix

    :param C: 
    :type C: NxN matrix

    :returns: x (*NxK matrix*)

Remarks
-------

*C* is the Cholesky factorization of a linear system of equations :math:`A`. *x* is
the solution for :math:`Ax = b`. *b* can have more than one column. If so, the
system is solved for each column, i.e., :math:`A\*x[., i] = b[., i]`.

Since :math:`A\ -1 = I/A` and :code:`eye(N)` creates an identity matrix of size :math:`N`:

::

   cholsol(eye(N), C);

is equivalent to:

::

   invpd(A);

Thus, if you have the Cholesky factorization of :math:`A`, cholsol is the most
efficient way to obtain the inverse of :math:`A`.

Examples
----------------

::

    // Assign the right-hand side 'b' and the Cholesky 
    // factorization 'C'
    b = { 0.03177513, 0.41823100, 1.70129375 };
    C = { 1.73351215 1.53201723 1.78102499,
                   0 1.09926365 0.63230050,
                   0          0 0.67015361 };
    
    // Solve the system of equations
    x = cholsol(b,C);
    
    // Note: C'C is equivalent to C'*C
    A = C'C;
    
    // Solve the system of equations
    x2 = b/A;
    
        -1.9440       -1.9440
    x = -1.5269  x2 = -1.5269
         3.2158        3.2158

.. seealso:: Functions :func:`chol`

