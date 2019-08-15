
areshape
==============================================

Purpose
----------------
Reshapes a scalar, matrix, or array into an array of user-specified size.

Format
----------------
.. function:: y = areshape(x, orders)

    :param x:
    :type x: scalar or matrix or N-dimensional array.

    :param orders: orders. the sizes of the dimensions of the new array.
    :type orders: Mx1 vector

    :return y: created from data in *x*.

    :rtype y: M-dimensional array

Remarks
-------

If there are more elements in *x* than in *y*, the remaining elements are
discarded. If there are not enough elements in *x* to fill *y*, then when
:func:`areshape` runs out of elements, it goes back to the first element of *x*
and starts getting additional elements from there.

Examples
----------------

::

    x = 3;
    orders = { 2, 3, 4 };
    y = areshape(x, orders);

*y* will be a 2x3x4 array of threes.

::

    // Create a 30x3 matrix with consecutive integer values
    x = reshape(seqa(1, 1, 90), 30, 3);

    orders = { 2, 3, 4, 5 };
    y = areshape(x, orders);

*y* will be a 2x3x4x5 array. Since *y* contains 120 elements and *x* contains only 90, the first 90 elements of *y* will be set to the sequence of integers from 1 to 90 that are contained in *x*, and the last 30 elements of *y* will
be set to the sequence of integers from 1 to 30 contained in the first 30 elements of *x*.

::

    // Create a 20x3 matrix with consecutive integer values
    x = reshape(seqa(1, 1, 60), 20, 3);

    orders = { 3, 2, 4 };
    y = areshape(x, orders);

*y* will be a 3x2x4 array. Since *y* contains 24 elements, and *x* contains 60, the elements of *y* will be set to the sequence of integers from 1 to 24 contained in the first 24 elements of *x*.

.. seealso:: Functions :func:`aconcat`, :func:`squeeze`
