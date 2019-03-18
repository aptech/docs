
xpnd
==============================================

Purpose
----------------
Expands a column vector into a symmetric matrix.

Format
----------------
.. function:: xpnd(v)

    :param v: to be expanded into a symmetric matrix.
    :type v: Kx1 vector

    :returns: x (*MxM matrix*), the results of taking  v and
        filling in a symmetric matrix with its elements.
        M =( (-1 + sqrt(1 + 8 * K) )/2)

Examples
----------------

::

    x = { 1,
          2, 3,
          4, 5, 6,
          7, 8, 9, 10 };
    y = xpnd(x);

After the code above, the variables x and y are equal to:

::

    1
        2
        3
        4       1   2   4   7
    x = 5   y = 2   3   5   8
        6       4   5   6   9
        7       7   8   9  10
        8
        9
       10

.. seealso:: Functions :func:`vech`
