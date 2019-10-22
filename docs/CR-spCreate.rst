
spCreate
==============================================

Purpose
----------------
Creates a sparse matrix from vectors of non-zero values, row indices, and column indices.

Format
----------------
.. function:: y = spCreate(r, c, vals, rinds, cinds)

    :param r: rows of output matrix.
    :type r: scalar

    :param c: columns of output matrix.
    :type c: scalar

    :param vals: non-zero values.
    :type vals: Nx1 vector

    :param rinds: row indices of corresponding non-zero values.
    :type rinds: Nx1 vector

    :param cinds: column indices of corresponding non-zero values.
    :type cinds: Nx1 vector

    :return y: 

    :rtype y: RxC sparse matrix

Examples
----------------

::

    // Declare 'y' to be a sparse matrix
    
    sparse matrix y;
    
    // Create the non-zero values to place in the sparse matrix
    vals = { 1.7, 2.4, 3.2, 4.5 };
    
    // Set the row and column indices for the location in which
    // to place each successive element of 'vals' into the new 
    // matrix
    rinds = { 2,5,8,13 };
    cinds = { 4,1,9,5 };
    
    y = spCreate(15,10,vals,rinds,cinds);

This example creates a 15x10 sparse matrix *y*, containing the following non-zero values:

================ =======
Non-zero value   Index
================ =======
1.7              (2,4)
2.4              (5,1)
3.2              (8,9)
4.5              (13,5)
================ =======

Remarks
-------

Since sparse matrices are strongly typed in GAUSS, *y* must be defined as
a sparse matrix before the call to :func:`spCreate`.

.. seealso:: Functions :func:`packedToSp`, :func:`denseToSp`, :func:`spEye`

