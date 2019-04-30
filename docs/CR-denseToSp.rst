
denseToSp
==============================================

Purpose
----------------

Converts a dense matrix to a sparse matrix.

Format
----------------
.. function:: denseToSp(x, eps)

    :param x: 
    :type x: MxN dense matrix

    :param eps: elements of *x* whose absolute values are less than
        or equal to *eps* will be treated as zero.
    :type eps: scalar

    :returns: y (*MxN sparse matrix*) .

Remarks
-------

A dense matrix is just a normal format matrix.

Since sparse matrices are strongly typed in GAUSS, *y* must be defined as
a sparse matrix before the call to :func:`denseToSp`.


Examples
----------------

::

    // Declare 'y' as a sparse matrix
    sparse matrix y;
    
    x = { 0.01 0.00 0.01 1.00,
          0.00 4.00 0.02 0.00,
          0.00 0.01 0.00 0.00,
          0.02 0.00 -2 0.00 };
          
    // Create a sparse matrix 'y' from 'x' and set all elements
    // less than 0.04 equal to 0      
    y = denseToSp(x,0.04);

After the code above, *y* is equal to:

::

    0.00   0.00   0.00   1.00 
    0.00   4.00   0.00   0.00 
    0.00   0.00   0.00   0.00 
    0.00   0.00  -2.00   0.00

.. seealso:: Functions :func:`spCreate`, :func:`spDenseSubmat`, :func:`spToDense`

