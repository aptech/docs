
bandcholsol
==============================================

Purpose
----------------

Solves the system of equations 	Ax = b for x, given the lower
triangle of the Cholesky decomposition of a positive definite
banded matrix  A.

Format
----------------
.. function:: bandcholsol(b,  l)

    :param b: KxM matrix.
    :type b: TODO

    :param l: KxN compact form matrix.
    :type l: TODO

    :returns: x (*TODO*), KxM matrix.

Examples
----------------

::

    //Create matrix 'A' and right-hand side 'b'
    A = { 1 2 0 0,
          2 8 1 0,
          0 1 5 2,
          0 0 2 3 };
    b = { 1.3, 2.1, 0.7, 1.8 }; 
    
    //Create banded matrix form of 'A'
    Aband = band(A,1);
    
    //Cholesky factorization of the banded 'A'
    Lband = bandchol(Aband);
    
    //Solve the system of equations
    x = bandcholsol(b, Lband);

After the code above is run:

::

    0.000  1.000       1.495      1.300        1.300 
    Lband = 2.000  2.000  x = -0.098  b = 2.100  A*x = 2.100 
            0.500  2.179      -0.110      0.700        0.700 
            0.918  1.469       0.673      1.800        1.800

.. seealso:: Functions :func:`band`, :func:`bandchol`, :func:`bandltsol`, :func:`bandrv`, :func:`bandsolpd`

Cholesky decomposition positive definite banded matrix solve equation
