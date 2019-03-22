
spToDense
==============================================

Purpose
----------------
Converts a sparse matrix to a dense matrix.

Format
----------------
.. function:: spToDense(x)

    :param x: 
    :type x: MxN sparse matrix

    :returns: y (*MxN dense matrix*) .

Remarks
-------

A dense matrix is just a normal format matrix.


Examples
----------------

::

    sparse matrix y;
    
    //Create a 4x4 sparse identity matrix
    y = spEye(4);
    
    //Create a dense matrix with the same values as 'y'
    d = spToDense(y);

The dense matrix d is equal to:

::

    1  0  0  0
    0  1  0  0
    0  0  1  0
    0  0  0  1

.. seealso:: Functions :func:`spDenseSubmat`, :func:`denseToSp`
