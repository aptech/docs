
arrayinit
==============================================

Purpose
----------------
Creates an N-dimensional array with a specified fill value.

Format
----------------
.. function:: y = arrayinit(orders, val)

    :param orders: the sizes of the dimensions of the array.
    :type orders: Nx1 vector

    :param val: each element of the new array will be set equal to *val*. If *val* is complex the result will be complex.
    :type val: scalar

    :return y: with each element equal to the value of *val*.

    :type y: N-dimensional array

Examples
----------------

::

    val = 3.14;
    orders = { 2, 100, 9 };
    y = arrayinit(orders, val);

*y* will be a 2x100x9 array with each element equal to 3.14.

.. seealso:: Functions :func:`arrayalloc`
