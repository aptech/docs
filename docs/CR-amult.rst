
amult
==============================================

Purpose
----------------
Performs matrix multiplication on the planes described by the two trailing dimensions of N-dimensional arrays.

Format
----------------
.. function:: y = amult(a, b)

    :param a:
    :type a: N-dimensional array

    :param b:
    :type b: N-dimensional array

    :returns: y (*N-dimensional array*), containing the product of the matrix multiplication of the planes described by the two trailing dimensions of *a* and *b*.

Remarks
-------

The multiplication operator, ``*``, performs the same operation for arrays as :func:`amult`.

All leading dimensions must be strictly conformable, and the two
trailing dimensions of each array must be matrix-product conformable.

Examples
----------------

::

    /*
    ** Create an additive sequence from 1-12 and reshape it into
    ** a 2x3x2 dimensional
    */
    a = areshape(seqa(1, 1, 12), 2|3|2);

    b = areshape(seqa(1, 1, 16), 2|2|4);

    /*
    ** Multiply the two 3x2 matrices in 'a' by the corresponding
    ** 2x4 matrices in 'b'
    */
    y = amult(a, b);

*a* is a 2x3x2 array, such that:
[1,1,1] through [1,3,2] =

::

    1.0000000        2.0000000
    3.0000000        4.0000000
    5.0000000        6.0000000

[2,1,1] through [2,3,2] =

::

    7.0000000        8.0000000
    9.0000000        10.000000
    11.000000        12.000000

*b* is a 2x2x4 array, such that:
[1,1,1] through [1,2,4] =

::

    1.0000000       2.0000000       3.0000000       4.0000000
    5.0000000       6.0000000       7.0000000       8.0000000

[2,1,1] through [2,2,4] =

::

    9.0000000       10.000000       11.000000       12.000000
    13.000000       14.000000       15.000000       16.000000

*y* will be a 2x3x4 array, such that:
[1,1,1] through [1,3,4] =

::

    11.000000       14.000000       17.000000       20.000000
    23.000000       30.000000       37.000000       44.000000
    35.000000       46.000000       57.000000       68.000000

[2,1,1] through [2,3,4] =

::

    167.00000       182.00000       197.00000       212.00000
    211.00000       230.00000       249.00000       268.00000
    255.00000       278.00000       301.00000       324.00000
