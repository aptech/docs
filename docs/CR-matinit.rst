
matinit
==============================================

Purpose
----------------

Allocates a matrix with a specified fill value.

Format
----------------
.. function:: matinit(r, c, v)

    :param r: rows.
    :type r: scalar

    :param c: columns.
    :type c: scalar

    :param v: value to initialize.
    :type v: scalar

    :returns: y (*TODO*), r x c matrix with each element equal to the value of  v.

Examples
----------------

::

    format /rd 6,2;
    print matinit(3, 4, pi);

::

    3.14   3.14   3.14   3.14 
      3.14   3.14   3.14   3.14 
      3.14   3.14   3.14   3.14

.. seealso:: Functions :func:`matalloc`, :func:`ones`, :func:`zeros`, :func:`eye`
