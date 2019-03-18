
arrayalloc
==============================================

Purpose
----------------
Creates an N-dimensional array with unspecified contents.

Format
----------------
.. function:: arrayalloc(o, cf)

    :param o: the sizes of the dimensions of the array.
    :type o: Nx1 vector of orders

    :param cf: 0 to allocate real array, or 1 to allocate complex array.
    :type cf: scalar

    :returns: y (*TODO*), N-dimensional array.

Examples
----------------

::

    orders = { 2, 3, 4 };
    y = arrayalloc(orders, 1);

y will be a complex 2x3x4 array with unspecified contents.

::

    // Set orders to create a 7x5x3 dimensional array
    orders = { 7, 5, 3 };
    
    // Create a real 7x5x3 dimensional array 
    y = arrayalloc(orders, 0);

.. seealso:: Functions :func:`arrayinit`, :func:`setarray`
