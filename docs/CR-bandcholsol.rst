
bandcholsol
==============================================

Purpose
----------------

Solves the system of equations :math:`Ax = b` for *x*, given the lower
triangle of the Cholesky decomposition of a positive definite
banded matrix :math:`A`.

Format
----------------
.. function:: bandcholsol(b, l)

    :param b: 
    :type b: KxM matrix

    :param l: 
    :type l: KxN compact form matrix

    :returns: x (KxM matrix)

Remarks
________________

Given a positive definite banded matrix *A*, there exists a matrix *L*, the
lower triangle of the Cholesky decomposition of *A*, such that :math:`A = LL'`. *l*
is the compact form of *L*; see :func:`band` for a description of the format of *l*.

*b* can have more than one column. If so, :math:`Ax = b` is solved for each
column. That is,

.. math:: A*x[.,i] = b[.,i]

Examples
----------------

::

    // Create matrix 'A' and right-hand side 'b'
    A = { 1 2 0 0,
          2 8 1 0,
          0 1 5 2,
          0 0 2 3 };
    b = { 1.3, 2.1, 0.7, 1.8 }; 
    
    // Create banded matrix form of 'A'
    Aband = band(A,1);
    
    // Cholesky factorization of the banded 'A'
    Lband = bandchol(Aband);
    
    // Solve the system of equations
    x = bandcholsol(b, Lband);

After the code above is run:

::

    0.000  1.000       1.495      1.300        1.300 
    Lband = 2.000  2.000  x = -0.098  b = 2.100  A*x = 2.100 
            0.500  2.179      -0.110      0.700        0.700 
            0.918  1.469       0.673      1.800        1.800


.. seealso:: Functions :func:`band`, :func:`bandchol`, :func:`bandltsol`, :func:`bandrv`, :func:`bandsolpd`

