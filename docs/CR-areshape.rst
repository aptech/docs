
areshape
==============================================

Purpose
----------------
Reshapes a scalar, matrix, or array into an array of user-specified size.

Format
----------------
.. function:: areshape(x,  o)

    :param x: matrix, or N-dimensional array.
    :type x: scalar

    :param o: the sizes of the dimensions of the new array.
    :type o: Mx1 vector of orders

    :returns: y (*TODO*), M-dimensional array, created from data in x.

Examples
----------------

::

    x = 3;
    orders = { 2, 3, 4 };
    y = areshape(x, orders);

y will be a 2x3x4 array of threes.

::

    x = reshape(seqa(1, 1, 90), 30, 3);
    orders = { 2, 3, 4, 5 };
    y = areshape(x, orders);

y will be a 2x3x4x5 array. Since y contains 120 elements and x contains only 90, the first 90 elements of y will be set to the sequence of integers from 1 to 90 that are contained in x, and the last 30 elements of y will
be set to the sequence of integers from 1 to 30 contained in the first 30 elements of x.

::

    x = reshape(seqa(1, 1, 60), 20, 3);
    orders = { 3, 2, 4 };
    y = areshape(x, orders);

y will be a 3x2x4 array. Since y contains 24 elements, and x contains 60, the elements of y will be set to the sequence of integers from 1 to 24 contained in the first 24 elements of x.

.. seealso:: Functions :func:`aconcat`, :func:`squeeze`
