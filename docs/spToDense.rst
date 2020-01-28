
spToDense
==============================================

Purpose
----------------
Converts a sparse matrix to a dense matrix.

Format
----------------
.. function:: y = spToDense(x)

    :param x: data
    :type x: MxN sparse matrix

    :return y: dense matrix converted from sparse matrix *x*.

    :rtype y: MxN dense matrix

Examples
----------------

::

    sparse matrix y;

    // Create a 4x4 sparse identity matrix
    y = spEye(4);

    // Create a dense matrix with the same values as 'y'
    d = spToDense(y);

The dense matrix *d* is equal to:

::

    1  0  0  0
    0  1  0  0
    0  0  1  0
    0  0  0  1

Remarks
-------

A dense matrix is just a normal format matrix.

.. seealso:: Functions :func:`spDenseSubmat`, :func:`denseToSp`
