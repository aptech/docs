
countwts
==============================================

Purpose
----------------

Returns a weighted count of the numbers of elements of a vector that fall into specified ranges.

Format
----------------
.. function:: countwts(x,  v,  w)

    :param x: the numbers to be counted.
    :type x: Nx1 vector

    :param v: the breakpoints specifying the ranges
        within which counts are to be made. This MUST be sorted
        in ascending order (lowest to highest).
    :type v: Px1 vector

    :param w: containing weights.
    :type w: Nx1 vector

    :returns: c (*TODO*), Px1 vector containing the weighted counts of the
        elements of x that fall into the regions:
        
        x < v[1],
        v[1] ≤ x < v[2],
        .
        .
        .
        v[p-1] ≤ x < v[p]
        
        That is, when x[i] falls into region j, the weight
        w[i] is added to the jth counter.

Examples
----------------

::

    x = { 1, 3, 2, 4, 1, 3 };
    w = { .25, 1, .333, .1, .25, 1 };
    v = { 0, 1, 2, 3, 4 };
    c = countwts(x,v,w);

::

    0.0000000
        0.5000000
    c = 0.3330000
        2.0000000
        0.1000000

