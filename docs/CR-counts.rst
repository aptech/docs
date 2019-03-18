
counts
==============================================

Purpose
----------------

Counts the numbers of elements of a vector that fall into specified ranges.

Format
----------------
.. function:: counts(x,  v)

    :param x: Nx1 vector containing the numbers to be counted.
    :type x: TODO

    :param v: Px1 vector containing breakpoints specifying
        the ranges within which counts are to be made. The vector  v MUST be sorted in ascending order.
    :type v: TODO

    :returns: c (*Px1 vector*), the counts of the
        elements of x that fall into the regions:
        
        x <= v[1],
        v[1] < x <= v[2],
        .
        .
        .
        v[p-1] < x <= v[p]

Examples
----------------

::

    x = { 1.5, 3, 5, 4, 1, 3 };
    v = { 0, 2, 4 };
    c = counts(x,v);

::

    1.5
        3       0       0
    x = 2   v = 2   c = 2
        4       4       3
        1
        3

