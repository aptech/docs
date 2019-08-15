
countwts
==============================================

Purpose
----------------

Returns a weighted count of the numbers of elements of a vector that fall into specified ranges.

Format
----------------
.. function:: c = countwts(x, v, w)

    :param x: the numbers to be counted.
    :type x: Nx1 vector

    :param v: the breakpoints specifying the ranges within which counts are to be made. This MUST be sorted
        in ascending order (lowest to highest).
    :type v: Px1 vector

    :param w: weights.
    :type w: Nx1 vector

    :return c: the weighted counts of the
        elements of x that fall into the regions:

        .. math::

            x < v[1],\\
            v[1] ≤ x < v[2],\\
            \vdots\\
            v[p-1] ≤ x < v[p]

        That is, when :math:`x[i]` falls into region *j*, the weight
        :math:`w[i]` is added to the jth counter.

    :rtype c: Px1 vector

Remarks
-------

If any elements of *x* are greater than the last element of *v*, they will
not be counted.

Missing values are not counted unless there is a missing in *v*. A missing
value in *v* MUST be the first element in *v*.

Examples
----------------

::

    // Original data
    x = { 1, 3, 2, 4, 1, 3 };

    // Weights
    w = { .25, 1, .333, .1, .25, 1 };

    // Break points
    v = { 0, 1, 2, 3, 4 };

    // Get counts
    c = countwts(x,v,w);

::

        0.0000000
        0.5000000
    c = 0.3330000
        2.0000000
        0.1000000
