
arrayinit
==============================================

Purpose
----------------
Creates an N-dimensional array with a specified fill value.

Format
----------------
.. function:: arrayinit(orders,  value)

    :param orders: the sizes of the dimensions of the array.
    :type orders: Nx1 vector of orders

    :param value: value to initialize. If value is complex the result will be complex.
    :type value: scalar

    :returns: y (*TODO*), N-dimensional array with each element equal to the value of  value.

Examples
----------------

::

    val = 3.14;
    orders = { 2, 100, 9 };
    y = arrayinit(orders, val);

y will be a 2x100x9 array with each element equal to 3.14.

.. seealso:: Functions :func:`arrayalloc`
