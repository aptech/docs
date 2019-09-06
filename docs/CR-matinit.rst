
matinit
==============================================

Purpose
----------------

Allocates a matrix with a specified fill value.

Format
----------------
.. function:: y = matinit(r, c, v)

    :param r: rows.
    :type r: scalar

    :param c: columns.
    :type c: scalar

    :param v: value to initialize.
    :type v: scalar

    :return y: with each element equal to the value of *v*.

    :rtype y: RxC matrix

Examples
----------------

::

    // Set print format
    format /rd 6,2;

    // Allocate a 3x4 matrix 
    // and set elements to be
    // pi
    print matinit(3, 4, pi);

      3.14   3.14   3.14   3.14
      3.14   3.14   3.14   3.14
      3.14   3.14   3.14   3.14

.. seealso:: Functions :func:`matalloc`, :func:`ones`, :func:`zeros`, :func:`eye`
