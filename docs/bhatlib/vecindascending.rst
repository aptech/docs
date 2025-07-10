vecindascending
==============================================

Purpose
----------------
Creates an index of elements in ascending order.

Format
----------------
.. function:: w = vecindascending(r)

    :param r: Vector r containing the elements to be indexed.
    :type r: vector

    :return w: A vector of the same dimension as r, containing the indices of the elements in r sorted in ascending order. The index of the minimum element in r is the first element, the index of the second lowest element is the second element, and so on.
    :rtype w: vector

Example
----------------

Given a vector `r`:

::

    r = { 3, 1, 2 };

Applying `vecindascending` to create `w`:

::

    w = vecindascending(r);

After the above code is run, `w` equals:

::

    2
    3
    1

This result indicates that the smallest element (1) is in the second position of the original vector `r`, the second smallest (2) is in the third position, and the largest (3) is in the first position.

.. seealso:: :func:`vecdup`, :func:`vecndup`

