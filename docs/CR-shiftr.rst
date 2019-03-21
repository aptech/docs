
shiftr
==============================================

Purpose
----------------
Shifts the rows of a matrix.

Format
----------------
.. function:: shiftr(x, s, f)

    :param x: 
    :type x: NxK matrix to be shifted

    :param s: 
    :type s: scalar or Nx1 vector specifying the amount of
        shift

    :param f: 
    :type f: scalar or Nx1 vector specifying the value to fill in

    :returns: y (*TODO*), NxK shifted matrix.

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

Now y is equal to:

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

Now y2 is equal to:

::

    1  2  3
    0  4  5
    0  0  7

.. seealso:: Functions :func:`rotater`
