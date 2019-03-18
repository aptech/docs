
spBiconjGradSol
==============================================

Purpose
----------------

Attempts to solve the system of linear equations Ax = b using the biconjugate gradient method where A is a sparse matrix.

Format
----------------
.. function:: spBiconjGradSol(a,  b,  epsilon,  maxit)

    :param a: sparse matrix.
    :type a: NxN

    :param b: dense vector.
    :type b: Nx1

    :param epsilon: Method tolerance: If epsilon is set to 0, the default tolerance is set to 1e-6.
    :type epsilon: TODO

    :param maxit: Maximum number of iterations. If maxit is set to 0, the default setting is 300 iterations.
    :type maxit: TODO

    :returns: x (*TODO*), Nx1 dense vector.

Examples
----------------

::

    nz = { 33.446  82.641 -12.710 -25.062   0.000, 
             0.000 -26.386  17.016  21.576 -45.273, 
             0.000 -42.331 -47.902   0.000   0.000, 
             0.000 -26.517 -22.135 -76.827  31.920, 
            10.364 -29.843 -20.277   0.000  65.816 };
     b = { 10.349, 
           -3.117, 
            4.240, 
            0.013, 
            2.115 };
     
     sparse matrix a;
     a = densetosp(nz,0);
     
     //Setting the third and fourth arguments to 0 employs the 
     //default tolerance and maxit settings
     x = spBiconjGradSol(a,b,0,0);
     
     //Solve the system of equations using the '/' operator for 
     //comparison
     x2 = b/a;

The output from the above code:

::

    0.135 
          0.055 
    x =  -0.137 
          0.018 
         -0.006 
        
          0.135 
          0.055 
    x2 = -0.137 
          0.018 
         -0.006

Remarks
+++++++

If convergence is not reached within the maximum number of iterations
allowed, the function will either terminate the program with an error
message or return an error code which can be tested for with the scalerr
function. This depends on the trap state as follows:

+-----------------------------------+-----------------------------------+
| **trap 1**                        | return error code: 60             |
+-----------------------------------+-----------------------------------+
| **trap 0**                        | terminate with error message:     |
|                                   | Unable to converge in allowed     |
|                                   | number of iterations.             |
+-----------------------------------+-----------------------------------+

If matrix A is not well conditioned use the / operator to perform the
solve. If the matrix is symmetric, spConjGradSol will be approximately
twice as fast as spBiconjGradSol.

.. seealso:: Functions :func:`spConjGradSol`
