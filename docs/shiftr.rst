
shiftr
==============================================

Purpose
----------------
Shifts the rows of a matrix.

Format
----------------
.. function:: y = shiftr(x, s, f)

    :param x: data to be shifted
    :type x: NxK matrix

    :param s: specifies the amount of shift
    :type s: scalar or Nx1 vector

    :param f: specifies the value to fill in
    :type f: scalar or Nx1 vector

    :return y: shifted matrix
    :rtype y: NxK matrix

Examples
----------------

::

    // Data matrix
    x = { 1 2,
          3 4 };

    // Amount of shift
    s = { 1,
         -1 };

    // Value to fill in
    f = { 99,
         999 };

    // Shift the matrix
    y = shiftr(x, s, f);

Now *y* is equal to:

::

    99   1
    4  999

::

    // Data 
    x = { 1 2 3,
          4 5 6,
          7 8 9 };

    // Amount to shift
    s = { 0,
          1,
          2 };

    // Value to fill in
    f = 0;

    // Shift the matrix
    y2 = shiftr(x, s, f);

Now *y2* is equal to:

::

    1  2  3
    0  4  5
    0  0  7

Remarks
-------

The shift is performed within each row of the matrix, horizontally. If
the shift value is positive, the elements in the row will be moved to
the right. A negative shift value causes the elements to be moved to the
left. The elements that are pushed off the end of the row are lost, and
the fill value will be used for the new elements on the other end.

.. seealso:: Functions :func:`rotater`
