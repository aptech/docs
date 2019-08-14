
aeye
==============================================

Purpose
----------------

Creates an N-dimensional array in which the planes described by the
two trailing dimensions of the array are equal to the identity.

Format
----------------
.. function:: a = aeye(ord)

    :param ord: the sizes of the dimensions of *a*.
    :type ord: Nx1 vector of orders

    :returns: a (*N-dimensional array*), containing 2-dimensional identity arrays.

Remarks
-------

If *ord* contains numbers that are not integers, they will be truncated to
integers.

The planes described by the two trailing dimensions of *a* will contain
1's down the diagonal and 0's everywhere else.

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
