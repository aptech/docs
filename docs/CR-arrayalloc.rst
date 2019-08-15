
arrayalloc
==============================================

Purpose
----------------
Creates an N-dimensional array with unspecified contents.

Format
----------------
.. function:: y = arrayalloc(orders, cf)

    :param orders: the sizes of the dimensions of the array.
    :type orders: Nx1 vector of orders

    :param cf: 0 to allocate real array, or 1 to allocate complex array.
    :type cf: scalar

    :return y: 

    :rtype y: N-dimensional array

Remarks
-------

The contents are unspecified. To create a new array with all elements
initialized to a particular scalar value, use :func:`arrayinit`.

:func:`arrayalloc` is used to allocate an array that will be written to in
sections using `setarray`, or indexed assignments. It is much faster to
preallocate an array and fill in sections during a loop rather than
adding new sections with concatentaion.

Examples
----------------

::

    orders = { 2, 3, 4 };
    y = arrayalloc(orders, 1);

*y* will be a complex 2x3x4 array with unspecified contents.

::

    // Set orders to create a 7x5x3 dimensional array
    orders = { 7, 5, 3 };

    // Create a real 7x5x3 dimensional array
    y = arrayalloc(orders, 0);

.. seealso:: Functions :func:`arrayinit`, `setarray`
