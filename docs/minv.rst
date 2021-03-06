
minv
==============================================

Purpose
----------------

Performs an element by element comparison of two matrices and returns the minimum value for each element.

Format
----------------
.. function:: z = minv(x, y)

    :param x: data
    :type x: NxK matrix

    :param y: data
    :type y: NxK matrix

    :return z: values are the minimum of each element from the arguments *x* and *y*.

    :rtype z: NxK matrix

Examples
----------------

::

    // Create the multiplicative sequence 1, 2, 4, 8
    x = seqm(1, 2, 4);

    // Reverse the order of the elements in 'x' and assign them
    // to 'y'
    y = rev(x);

    z = minv(x, y);

After the code above:

::

        1          8          1
    x = 2      y = 4      z = 2
        4          2          2
        8          1          1

Remarks
-------

:func:`minv` works for sparse matrices as well as arrays.

.. seealso:: Functions :func:`maxv`
