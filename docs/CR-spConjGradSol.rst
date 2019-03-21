
spConjGradSol
==============================================

Purpose
----------------
Attempts to solve the system of linear equations Ax = b using the conjugate gradient method where A is a symmetric sparse matrix.

Format
----------------
.. function:: spConjGradSol(a, b, epsilon, maxit)

    :param a: symmetric sparse matrix.
    :type a: NxN

    :param b: dense vector.
    :type b: Nx1

    :param epsilon: , the default tolerance is set to 1e-6.
    :type epsilon: Method tolerance: If epsilon is set to 0

    :param maxit:  If maxit is set to 0, the default setting is 300 iterations.
    :type maxit: Maximum number of iterations

    :returns: x (*TODO*), Nx1 dense vector

Examples
----------------

::

    nz = {   0.000   2845.607     0.000     0.000     0.000,
          2845.607  10911.430     0.000     0.000     0.000,
             0.000      0.000  3646.798  2736.338 -2674.440,
             0.000      0.000  2736.338  7041.526 -3758.528,
             0.000      0.000 -2674.440 -3758.528  7457.899 };
     sparse matrix a;
     
    //Set 'a' to be a sparse matrix with the same contents as 
    //the dense matrix 'nz' 
    a = densetosp(nz,0);
    
    //Create our right-hand-side
    b = { 10.349,
           -3.117,
            4.240,
            0.013,
            2.115 };
     
    //Setting the third and fourth arguments to 0 employs the 
    //default tolerance maxit settings
    x = spConjGradSol(a,b,0,0);
     
    newb = a*x;

The results from the above code are:

::

    -0.01504075 
           0.00363683 
    x  =   0.00203504 
          -0.00033936 
           0.00084234
    
          10.34900000 
          -3.11700000 
    newb = 4.24000000 
           0.01300000 
           2.11500000

Remarks
-------

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

If matrix A is not symmetric or well conditioned use the / operator to
perform the solve. For a nonsymmetric, but well conditioned matrix A,
use spBiconjGradSol.

.. seealso:: Functions :func:`spBiconjGradSol`

| 
