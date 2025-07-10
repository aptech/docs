rearrange
==============================================

Purpose
----------------
Rearranges a vector based on positioning on the upper diagonal matrix of dimension m.

Format
----------------
.. function:: { w } = rearrange(r)

    :param r: Column vector based on the upper diagonal of a matrix with dimension m. The dimension of r should be (m*(m+1)/2) x 1.
    :type r: vector

    :return w: Output vector rearranged from the input vector. It has the same dimension as r.
    :rtype w: vector

Example
----------------

::

    // Given a column vector r
    r = { 1, 2, 3, 4, 5, 6 };

    // After applying the rearrange function to create w
    w = rearrange(r);

After the above code, *w* equals:

::

    1
    2
    4
    3
    5
    6

.. seealso:: :func:`vecdup`, :func:`vecndup`

