
chol
==============================================

Purpose
----------------

Computes the Cholesky decomposition of a symmetric, positive definite square matrix.

Format
----------------
.. function:: chol(x)

    :param x: NxN matrix.
    :type x: TODO

    :returns: y (*TODO*), NxN matrix containing the Cholesky decomposition of x.

Examples
----------------

::

    //'moment' calculates x'*x with options for handling missing data
    
    x = moment (rndn(100,4),0); 
    
    y = chol(x);             
     
    //y'y is equivalent to y'*y
    ypy = y'y;
    
        95.2801   8.6983   3.7248    1.5449      9.7612   0.8911   0.3816   0.1583
    x =  8.6983  83.4547  -6.1455  -12.5551  y = 0.0000   9.0918  -0.7133  -1.3964
         3.7248  -6.1455  87.6666   -3.0284      0.0000   0.0000   9.3280  -0.4379
         1.5449 -12.5551  -3.0284   90.8311      0.0000   0.0000   0.0000   9.4162
    
         95.2801   8.6983   3.7248   1.5449
    ypy = 8.6983  83.4547  -6.1455 -12.5551
          3.7248  -6.1455  87.6666  -3.0284
          1.5449 -12.5551  -3.0284  90.8311

.. seealso:: Functions :func:`crout`, :func:`solpd`

cholesky decomposition
