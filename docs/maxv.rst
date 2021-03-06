
maxv
==============================================

Purpose
----------------

Performs an element by element comparison of two matrices and returns the maximum value for each element.

Format
----------------
.. function:: z = maxv(x, y)

    :param x: data
    :type x: NxK matrix

    :param y: data
    :type y: NxK matrix

    :return z: values are the maximum of each element from the arguments *x* and *y*.

    :rtype z: NxK matrix

Examples
----------------

::

    // Create the sequence 1, 2, 3,...10
    x = seqa(1, 1, 10);

    // Set 'y' equal to the reverse order of 'x'
    y = rev(x);

    z = maxv(x, y);

::

        1       10       10
        2        9        9
        3        8        8
        4        7        7
    x = 5    y = 6    z = 6
        6        5        6
        7        4        7
        8        3        8
        9        2        9
       10        1       10

Remarks
-------

:func:`maxv` works for sparse matrices as well as arrays.

.. seealso:: Functions :func:`minv`
