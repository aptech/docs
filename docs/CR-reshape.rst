
reshape
==============================================

Purpose
----------------
Reshapes a matrix.

Format
----------------
.. function:: reshape(x,  r,  c)

    :param x: NxK matrix.
    :type x: TODO

    :param r: new row dimension.
    :type r: scalar

    :param c: new column dimension.
    :type c: scalar

    :returns: y (*TODO*), r x c matrix created from the elements of  x.

Examples
----------------

::

    y = reshape(x,2,6);

::

    1  2  3  4
    if x =  5  6  7  8  then y = 1  2  3  4  5  6
            9 10 11 12           7  8  9 10 11 12

::

    1  2  3
    if x =  4  5  6  then y = 1  2  3  4  5  6
            7  8  9           7  8  9  1  2  3

::

    1  2  3  4  5
    if x =  6  7  8  9 10  then y = 1  2  3  4  5  6
           11 12 13 14 15           7  8  9 10 11 12

::

    if x = 1  2  then y = 1 2 3 4 1 2
           3  4           3 4 1 2 3 4

::

    if x = 1  then y = 1 1 1 1 1 1
                       1 1 1 1 1 1

.. seealso:: Functions :func:`submat`, :func:`vec`
