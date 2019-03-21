
spDenseSubmat
==============================================

Purpose
----------------
Returns a dense submatrix of a sparse matrix.

Format
----------------
.. function:: spDenseSubmat(x, rinds, cinds)

    :param x: 
    :type x: MxN sparse matrix

    :param rinds: row indices.
    :type rinds: Kx1 vector

    :param cinds: column indices.
    :type cinds: Lx1 vector

    :returns: y (*KxL dense matrix*), the intersection of  rinds and  cinds.

Remarks
-------

Ifrinds  orcinds are scalar zeros, all rows or columns will be returned.


Examples
----------------

::

    sparse matrix y;
    x = { 0  0  0 10,
          0  2  0  0,
          0  0  0  0,
          5  0  0  0,
          0  0  0  3 };
    
    //Set 'y' to be a sparse matrix with the same values as 'x'
    y = denseToSp(x,0);
    
    //Extract a submatrix from 'y' with all rows of 'y' and 
    //columns 1, 3 and 4 
    d = spDenseSubmat(y,0,1|3|4);

Now d  is equal to:

::

    0  0 10
    0  0  0
    0  0  0
    5  0  0
    0  0  3

.. seealso:: Functions :func:`spSubmat`
