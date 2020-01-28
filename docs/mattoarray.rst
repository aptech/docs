
mattoarray
==============================================

Purpose
----------------

Converts a matrix to a type array.

Format
----------------
.. function:: y = mattoarray(x)

    :param x: data
    :type x: matrix

    :return y: data converted to an array type. 

    :rtype y: 1-or-2-dimensional array

Examples
----------------

::

    // Set x to be a 2x3 matrix of fives
    x = 5*ones(2, 3);

    // Convert x to an array
    // and save as  y
    y = mattoarray(x);

*y* will be a 2x3 array of fives.

Remarks
-------

If the argument *x* is a scalar, :func:`mattoarray` will simply return the scalar,
without changing it to a type array.

.. seealso:: Functions :func:`arraytomat`
