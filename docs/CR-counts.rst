
counts
==============================================

Purpose
----------------

Counts the numbers of elements of a vector that fall into specified ranges.

Format
----------------
.. function:: c = counts(x, v)

    :param x: the numbers to be counted
    :type x: Nx1 vector

    :param v: breakpoints specifying the ranges within which counts are to be made. The vector *v* MUST be sorted in ascending order.
    :type v: Px1 vector

    :return c: the counts of the elements of *x* that fall into the regions:

        .. math::

            x \leq v[1],\\
            v[1] < x \leq v[2],\\
            \vdots\\
            v[p-1] < x \leq v[p]

    :rtype c: Px1 vector

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
directly. Also :math:`+\infty` or :math:`-\infty` are allowed as breakpoints. The missing value
must be the first breakpoint if it is included as a breakpoint and
infinities must be in the proper location depending on their sign. :math:`-\infty`
must be in the :math:`[2, 1]` element of the breakpoint vector if there is a
missing value as a category as well, otherwise it has to be in the :math:`[1, 1]`
element. If :math:`+\infty` is included, it must be the last element of the
breakpoint vector.

Examples
----------------

Basic example
+++++++++++++

Count the number of elements which are in a specific range.

::

    // Original data
    x = { 1.5, 3, 5, 4, 1, 3 };

    // Break points
    v = { 0, 2, 4 };

    // Get counts
    c = counts(x, v);

::

        1.5
        3       0       0
    x = 5   v = 2   c = 2
        4       4       3
        1
        3

Count integers
++++++++++++++

Count how many times each integer from 1 to 10 is present in a vector.

::

    x = { 9, 8, 9, 9, 6, 8, 6, 7 };

    ints = seqa(1, 1, 10);

    c = counts(x, ints);

::

          1      0 
          2      0 
          3      0 
          4      0 
   ints = 5  c = 0 
          6      2 
          7      1 
          8      2 
          9      3 
         10      0 
