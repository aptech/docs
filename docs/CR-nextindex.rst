
nextindex
==============================================

Purpose
----------------

Returns the index of the next element or subarray in an array.

Format
----------------
.. function:: ni = nextindex(i, o)

    :param i: indices into an array where :math:`M <= N`.
    :type i: Mx1 vector

    :param o: orders of an N-dimensional array
    :type o: Nx1 vector

    :returns: ni (*Mx1 vector of indices*), the index of the next element or subarray in the array corresponding to *o*.

Remarks
-------

:func:`nextindex` will return a scalar error code if the index cannot be incremented.

Examples
----------------

::

    // Dimensions of an array
    orders = { 3, 4, 5, 6, 7);
    
    // Starting index
    ind = { 2, 3, 5 };
    
    // Return the index for the next element
    ind = nextindex(ind,orders);

After the code above, ind will be equal to:

::

    2
    4
    1

In this example, :func:`nextindex` incremented *ind* to index the next 6x7 subarray in array *a*.

Using the same data from above, a subsequent call to :func:`nextindex`:

::

    ind = nextindex(ind,orders);

will assign *ind* to be equal to:

::

    2
    4
    2

.. seealso:: Functions :func:`previousindex`, :func:`loopnextindex`, :func:`walkindex`

