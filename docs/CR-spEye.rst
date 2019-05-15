
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

    :returns: y (*n x n sparse identity matrix*) 

Remarks
-------

Since sparse matrices are strongly typed in GAUSS, *y* must be defined as
a sparse matrix before the call to :func:`spEye`.

Examples
----------------

::

    // Declare 'y' a sparse matrix
    sparse matrix y;
    
    // Create 3x3 sparse identity matrix
    y = spEye(3);

*y* is now equal to:

::

    1  0  1
    0  1  0
    0  0  1

.. seealso:: Functions :func:`spCreate`, :func:`spOnes`, :func:`denseToSp`

