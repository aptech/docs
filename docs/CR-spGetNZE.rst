
spGetNZE
==============================================

Purpose
----------------
Returns the non-zero values in a sparse matrix, as well as their corresponding row and column indices.

Format
----------------
.. function:: spGetNZE(x)

    :param x: 
    :type x: MxN sparse matrix

    :returns: vals (*Nx1 vector*), non-zero values in x.

    :returns: rinds (*Nx1 vector*), row indices of corresponding non-zero values.

    :returns: cinds (*Nx1 vector*), column indices of corresponding non-zero values.

Examples
----------------

::

    sparse matrix y;
    x = { 0 0 0 10,
          0 2 0  0,
          0 0 0  0,
          5 0 0  0,
          0 0 0  3 };
    
    //Create sparse matrix from 'x'       
    y = denseToSp(x,0);
    
    //Get non-zero values, row indices and column indices
    { v,r,c } = spGetNZE(y);

v, the non-zero values, is equal to:

::

    10 
     2 
     5 
     3

r, the row indices, is equal to:

::

    1 
     2 
     4 
     5

c, the column indices, is equal to:

::

    4 
     2 
     1 
     4

.. seealso:: Functions :func:`spNumNZE`
