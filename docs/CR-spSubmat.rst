
spSubmat
==============================================

Purpose
----------------
Returns a sparse submatrix of a sparse matrix.

Format
----------------
.. function:: spSubmat(x, rinds, cinds)

    :param x: 
    :type x: MxN sparse matrix

    :param rinds: row indices.
    :type rinds: Kx1 vector

    :param cinds: column indices.
    :type cinds: Lx1 vector

    :returns: s (*KxL sparse matrix*), the intersection of  rinds and  cinds.

Examples
----------------

::

    sparse matrix y;
    sparse matrix z;
    
    x = { 0 0 0 10,
          0 2 0 0,
          0 0 0 0,
          5 0 0 0,
          0 0 0 3 };
    
    y = denseToSp(x,0);
    
    //Extract all columns; rows 1, 3 and 4
    z = spSubmat(y,1|3|4,0);
    
    //Extract all values from 'z' into a dense matrix 'd'
    d = spDenseSubmat(z,0,0);

Now d is equal to:

::

    0.00   0.00   0.00  10.00 
      0.00   0.00   0.00   0.00 
      5.00   0.00   0.00   0.00

.. seealso:: Functions :func:`spDenseSubmat`
