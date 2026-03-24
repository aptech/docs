
matalloc
==============================================

Purpose
----------------

Allocates a matrix with unspecified contents.

Format
----------------
.. function:: y = matalloc(r, c)

    :param r: rows.
    :type r: scalar

    :param c: columns.
    :type c: scalar

    :return y: 

    :rtype y: RxC matrix

Remarks
-------

The contents are unspecified. This function is used to allocate a matrix
that will be written to in sections using indexing or used with the
`Foreign Language Interface` as an output matrix for a function called
with `dllcall`.

Examples
--------

::

    // Allocate a 3x2 matrix, then fill it
    y = matalloc(3, 2);
    y[1, .] = 1~2;
    y[2, .] = 3~4;
    y[3, .] = 5~6;
    print y;

.. seealso:: Functions :func:`matinit`, :func:`ones`, :func:`zeros`, :func:`eye`

