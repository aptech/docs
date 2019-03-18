
spEye
==============================================

Purpose
----------------
Creates a sparse identity matrix.

Format
----------------
.. function:: spEye(n)

    :param n: order of identity matrix.
    :type n: scalar

    :returns: y (*TODO*), n x n sparse identity matrix.

Examples
----------------

::

    //Declare 'y' a sparse matrix
    sparse matrix y;
    
    //Create 3x3 sparse identity matrix
    y = spEye(3);

y is now equal to:

::

    1  0  1
    0  1  0
    0  0  1

.. seealso:: Functions :func:`spCreate`, :func:`spOnes`, :func:`denseToSp`
