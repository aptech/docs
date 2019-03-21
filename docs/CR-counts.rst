
counts
==============================================

Purpose
----------------

Counts the numbers of elements of a vector that fall into specified ranges.

Format
----------------
.. function:: counts(x, v)

    :param x: the numbers to be counted
    :type x: Nx1 vector

    :param v: breakpoints specifying the ranges within which counts are to be made. The vector *v* MUST be sorted in ascending order.
    :type v: Px1 vector

    :returns: c (*Px1 vector*), the counts of the elements of *x* that fall into the regions:
       
        .. math::

            x <= v[1],
            v[1] < x <= v[2],
            .
            .
            .
            v[p-1] < x <= v[p]

Remarks
-------

If the maximum value of *x* is greater than the last element (the maximum
value) of *v*, the sum of the elements of the result, *c*, will be less than
:math:`N`, the total number of elements in *x*.

If

::

       1
       2
       3
       4      4
   x = 5  v = 5
       6      8
       7
       8
       9

then

::

       4
   c = 1
       3

The first category can be a missing value if you need to count missings
directly. Also :math:`+∞` or :math:`-∞` are allowed as breakpoints. The missing value
must be the first breakpoint if it is included as a breakpoint and
infinities must be in the proper location depending on their sign. :math:`-∞`
must be in the :math:`[2,1]` element of the breakpoint vector if there is a
missing value as a category as well, otherwise it has to be in the :math:`[1,1]`
element. If :math:`+∞` is included, it must be the last element of the
breakpoint vector.

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

