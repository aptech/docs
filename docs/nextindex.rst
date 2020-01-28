
nextindex
==============================================

Purpose
----------------

Returns the index of the next element or subarray in an array.

Format
----------------
.. function:: nind = nextindex(ind, orders)

    :param ind: indices into an array where :math:`M <= N`.
    :type ind: Mx1 vector

    :param orders: orders of an N-dimensional array
    :type orders: Nx1 vector

    :return nind: the index of the next element or subarray in the array corresponding to *orders*.

    :rtype nind: Mx1 vector

Examples
----------------

::

    // Dimensions of an array
    orders = { 3, 4, 5, 6, 7 };

    // Starting index
    ind = { 2, 3, 5 };

    // Return the index for the next element
    nind1 = nextindex(ind, orders);

After the code above, *nind1* will be equal to:

::

    2
    4
    1

In this example, :func:`nextindex` incremented *ind* to index the next 6x7 subarray in array *a*.

Using the same data from above, a subsequent call to :func:`nextindex`:

::

    nind2 = nextindex(nind1, orders);

will assign *nind2* to be equal to:

::

    2
    4
    2

Remarks
-------

:func:`nextindex` will return a scalar error code if the index cannot be incremented.

.. seealso:: Functions :func:`previousindex`, :func:`loopnextindex`, :func:`walkindex`
