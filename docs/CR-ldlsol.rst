
ldlsol
==============================================

Purpose
----------------

Computes the solution to a system of linear equations given a factorized matrix returned by the function ldlp and one or more right hand sides.

Format
----------------
.. function:: ldlsol(b, ldl_factor)

    :param b: the right hand sides of the system of linear equations.
    :type b: Nx1 vector or NxK matrix

    :param ldl_factor: , containing the a factorization returned from the GAUSS function ldlp.
    :type ldl_factor: Nx(N+1) matrix

    :returns: x (*Nx1 vector or NxK matrix*), containing the solution to LDLTx = b.

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

.. seealso:: Functions :func:`ldlp`, :func:`lusol`, :func:`solpd`

solution system linear equation given factorized matrix ldlp ldl
factorization decomposition solve linear equation solution
