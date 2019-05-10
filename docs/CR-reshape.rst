
reshape
==============================================

Purpose
----------------
Reshapes a matrix.

Format
----------------
.. function:: reshape(x, r, c)

    :param x: data
    :type x: NxK matrix

    :param r: new row dimension.
    :type r: scalar

    :param c: new column dimension.
    :type c: scalar

    :returns: y (*RxC matrix*) created from the elements of *x*.

Remarks
-------

Matrices are stored in row major order.

The first *c* elements are put into the first row of *y*, the second in the
second row, and so on. If there are more elements in *x* than in *y*, the
remaining elements are discarded. If there are not enough elements in *x*
to fill *y*, then when reshape runs out of elements, it goes back to the
first element of *x* and starts getting additional elements from there.


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

