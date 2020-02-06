
previousindex
==============================================

Purpose
----------------

Returns the index of the previous element or subarray in an array.

Format
----------------
.. function:: pi = previousindex(i, orders)

    :param i: indices into an array where :math:`M <= N`.
    :type i: Mx1 vector

    :param orders: orders of an N-dimensional array
    :type orders: Nx1 vector

    :return pi: the index of the previous element or subarray in the array corresponding to *orders*.

    :rtype pi: Mx1 vector of indices

Examples
----------------

::

    // Set orders
    orders = { 3, 4, 5, 6, 7 };

    // Initialize array
    a = areshape(1, orders);

    // Get orders of the array
    orders = getorders(a);

    // Set starting index
    ind = { 2, 3, 1 };

    // Get previous index
    pi = previousindex(ind, orders);

After the code above, ``pi`` is equal to:

::

          2
    pi =  2
          5

In this example, :func:`previousindex` decremented ``pi`` to index the previous 6x7 subarray in array *a*.

Remarks
-------

:func:`previousindex` will return a scalar error code if the index cannot be decremented.


.. seealso:: Functions :func:`nextindex`, `loopnextindex`, :func:`walkindex`
