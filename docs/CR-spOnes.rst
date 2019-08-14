
spOnes
==============================================

Purpose
----------------
Generates a sparse matrix containing only ones and zeros

Format
----------------
.. function:: y = spOnes(r, c, rinds, cinds)

    :param r: rows of output matrix.
    :type r: scalar

    :param c: columns of output matrix.
    :type c: scalar

    :param rinds: row indices of ones.
    :type rinds: Nx1 vector

    :param cinds: column indices of ones.
    :type cinds: Nx1 vector

    :returns: y (*RxC sparse matrix*) of ones.

Remarks
-------

Since sparse matrices are strongly typed in GAUSS, *y* must be defined as
a sparse matrix before the call to :func:`spOnes`.

Examples
----------------

::

    // declare sparse matrix
    sparse matrix y;
    
    // Set row indices and column indices
    rinds = { 1, 3, 5 };
    cinds = { 2, 1, 3 };
    
    // Create a 5x4 sparse matrix with ones at the intersection 
    // of the 'rind' and 'cind'
    y = spOnes(5, 4, rinds, cinds);

The resulting *y* is equal to:

::

    0  1  0  0
    0  0  0  0
    1  0  0  0
    0  0  0  0
    0  0  1  0

.. seealso:: Functions :func:`spCreate`, :func:`spEye`, :func:`spZeros`, :func:`denseToSp`

