
spToDense
==============================================

Purpose
----------------
Converts a sparse matrix to a dense matrix.

Format
----------------
.. function:: spToDense(x)

    :param x: MxN sparse matrix.
    :type x: TODO

    :returns: y (*TODO*), MxN dense matrix.

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
