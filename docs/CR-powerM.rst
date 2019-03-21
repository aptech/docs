
powerM
==============================================

Purpose
----------------

Returns the power n of a matrix A, as the matrix product of n copies of A.

Format
----------------
.. function:: powerM(A, n)

    :param A: 
    :type A: NxN square matrix

    :param n: the power or exponent.
    :type n: Scalar

    :returns: B (*NxN square matrix*), the power of a matrix A

Examples
----------------

::

    A = { 1 2, 
          3 4 };
    					
    //Compute power matrix
    B = powerM(A, 3);
    
    print "A = " A; 
    print ;				
    print "B = " B;

After the code above:

::

    A=
    1.0000000        2.0000000 
    3.0000000        4.0000000 
    
    B=
    37.000000        54.000000 
    81.000000        118.00000

.. seealso:: Functions :func:`crossprd`

matrix power n product operation
