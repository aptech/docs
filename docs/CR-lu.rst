
lu
==============================================

Purpose
----------------

Computes the LU decomposition of a square matrix with partial
(row) pivoting, such that: X = LU.

Format
----------------
.. function:: lu(x)

    :param x: NxN square nonsingular matrix.
    :type x: TODO

    :returns: l (*TODO*), NxN ''scrambled'' lower triangular matrix. This is
        a lower triangular matrix that has been reordered
        based on the row pivoting.

    :returns: u (*TODO*), NxN upper triangular matrix.

Examples
----------------

::

    //Set seed for repeatable random numbers
    
    rndseed 13;
    
    //Print format, display 4 digits after decimal point
    format /rd 10,4;
    
    A = rndn(3,3);
    { L, U } = lu(A);
    A2 = L*U;

::

    -0.0195     0.4054    -0.0874 
    A =   -1.2948     0.1734     1.9712 
           0.5408    -0.1294     0.7646 
    
           0.0150     1.0000     0.0000 
    L =    1.0000     0.0000     0.0000 
          -0.4177    -0.1414     1.0000 
    
          -1.2948     0.1734     1.9712 
    U =    0.0000     0.4028    -0.1170 
           0.0000     0.0000     1.5714 
    
          -0.0195     0.4054    -0.0874 
    L*U = -1.2948     0.1734     1.9712 
           0.5408    -0.1294     0.7646

.. seealso:: Functions :func:`crout`, :func:`croutp`, :func:`chol`

LU decomposition row pivoting real and complex matrix
