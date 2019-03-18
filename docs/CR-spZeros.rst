
spZeros
==============================================

Purpose
----------------
Creates a sparse matrix containing no non-zero values.

Format
----------------
.. function:: spZeros(r, c)

    :param r: rows of output matrix.
    :type r: scalar

    :param c: columns of output matrix.
    :type c: scalar

    :returns: y (*TODO*), r x c sparse matrix.

Examples
----------------

::

    sparse matrix y;
    
    //Create a 4x3 sparse matrix with all elements set to 0
    y = spZeros(4,3);
    
    //Create a dense matrix with the same values as 'y'
    d = spToDense(y);

The contents of d are equal to:

::

    0 0 0
    0 0 0
    0 0 0
    0 0 0

.. seealso:: Functions :func:`spOnes`, :func:`spEye`
