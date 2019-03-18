
aeye
==============================================

Purpose
----------------

Creates an N-dimensional array in which the planes described by the
two trailing dimensions of the array are equal to the identity.

Format
----------------
.. function:: aeye(ord)

    :param ord: the sizes of the dimensions
        of  a.
    :type ord: Nx1 vector of orders

    :returns: a (*TODO*), N-dimensional array, containing 2-dimensional identity arrays.

Examples
----------------

::

    v = { 2, 3, 3 };
    a = aeye(v);

a will be a 2x3x3 array, such that:
[1,1,1] through [1,3,3] =

::

    1 0 0
    0 1 0
    0 0 1

[2,1,1] through [2,3,3] =

::

    1 0 0
    0 1 0
    0 0 1

.. seealso:: Functions :func:`eye`
