
shiftr
==============================================

Purpose
----------------
Shifts the rows of a matrix.

Format
----------------
.. function:: shiftr(x, s, f)

    :param x: data to be shifted
    :type x: NxK matrix 

    :param s: specifying the amount of shift
    :type s: scalar or Nx1 vector 

    :param f: specifying the value to fill in
    :type f: scalar or Nx1 vector

    :returns: y (*NxK shifted matrix*)

Remarks
-------

The shift is performed within each row of the matrix, horizontally. If
the shift value is positive, the elements in the row will be moved to
the right. A negative shift value causes the elements to be moved to the
left. The elements that are pushed off the end of the row are lost, and
the fill value will be used for the new elements on the other end.

Examples
----------------

::

    x = { 1 2,
          3 4 };
    s = { 1,
         -1 };
    f = { 99,
         999 };
    y = shiftr(x,s,f);

Now *y* is equal to:

::

    99   1
    4  999

::

    x = { 1 2 3,
          4 5 6,
          7 8 9 };
    s = { 0,
          1,
          2 };
    f = 0;
    y2 = shiftr(x,s,f);

Now *y2* is equal to:

::

    1  2  3
    0  4  5
    0  0  7

.. seealso:: Functions :func:`rotater`

