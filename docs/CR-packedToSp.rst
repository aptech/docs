
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

    :returns: y (*r x c sparse matrix*) .

Remarks
-------

If p is Nx3, y will be a real sparse matrix. Otherwise, if p is Nx4, y
will be complex.

The format for p is as follows:

If p is Nx3:

+-----------------+-------------+----------------+
| Column 1        | Column 2    | Column 3       |
+-----------------+-------------+----------------+
| non-zero values | row indices | column indices |
+-----------------+-------------+----------------+

If p is Nx4:

+----------------------+---------------------------+-------------+----------------+
| Column 1             | Column 2                  | Column 3    | Column 4       |
+----------------------+---------------------------+-------------+----------------+
| real non-zero values | imaginary non-zero values | row indices | column indices |
+----------------------+---------------------------+-------------+----------------+

Note that spCreate may be faster.

Since sparse matrices are strongly typed in GAUSS, y must be defined as
a sparse matrix before the call to packedToSp.


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
