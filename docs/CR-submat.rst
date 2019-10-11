
submat
==============================================

Purpose
----------------
Extracts a submatrix of a matrix, with the appropriate rows and columns given by the elements of vectors.

Format
----------------
.. function:: y = submat(x, r, c)

    :param x: data
    :type x: NxK matrix

    :param r: row indices
    :type r: LxM matrix

    :param c: column indices
    :type c: PxQ matrix

    :return y: of *x*, *y* may be larger than *x*.

    :rtype y: (L*M)x(P*Q) submatrix

Examples
----------------

::

    // Create 12x1 vector with consecutive numbers
    x = seqa(1, 1, 12);
    
    // Reshape the 12x1 vector into a 3x4 matrix
    x = reshape(x, 3, 4);
    
    v1 = 1 3;
    v2 = 2 4;
    
    // Extract sub-matrices
    y = submat(x,v1,v2);
    z = submat(x,0,v2);

After the code above, the matrix values are:

::

        1  2  3  4
    x = 5  6  7  8
        9 10 11 12
    
    y =  2  4
        10 12
    
         2  4
    z =  6  8
        10 12

Remarks
-------

If :math:`r = 0`, then all rows of *x* will be used. If :math:`c = 0`, then all columns of *x* will be used.

.. seealso:: Functions :func:`diag`, :func:`vec`, :func:`reshape`

