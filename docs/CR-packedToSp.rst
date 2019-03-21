
packedToSp
==============================================

Purpose
----------------

Creates a sparse matrix from a packed matrix of non-zero values and row and column indices.

Format
----------------
.. function:: packedToSp(r, c, p)

    :param r: rows of output matrix.
    :type r: scalar

    :param c: columns of output matrix.
    :type c: scalar

    :param p: containing non-zero values and row and column indices.
    :type p: Nx3 or Nx4 matrix

    :returns: y (*TODO*), r x c sparse matrix.

Examples
----------------

::

    //Declare 'y' to be a sparse matrx
    sparse matrix y;
    
    //Create a 15x10 matrix 'y' in which:
    //y[2,4] = 1.1; y[5,1] = 2.3; y[8,9] = 3.4; 
    //y[13,5] = 4.2
    //all other values in 'y' will be zeros
    p = { 1.1 2 4, 2.3 5 1, 3.4 8 9, 4.2 13 5 };
    y = packedToSp(15,10,p);

After the code above, y is a sparse matrix, containing
the following non-zero values:

::

    Non-zero value     Index
    
        1.1            (2,4)
        2.3            (5,1)
        3.4            (8,9)
        4.2           (13,5)

.. seealso:: Functions :func:`spCreate`, :func:`denseToSp`
