
previousindex
==============================================

Purpose
----------------

Returns the index of the previous element or subarray in an array.

Format
----------------
.. function:: previousindex(i, o)

    :param i: indices into an array where :math:`M <= N`.
    :type i: Mx1 vector

    :param o: orders of an N-dimensional array
    :type o: Nx1 vector

    :returns: pi (*Mx1 vector of indices*), the index of the previous element or subarray in the array corresponding to *o*.

Remarks
-------

:func:`previousindex` will return a scalar error code if the index cannot be decremented.


Examples
----------------

::

    orders = {3,4,5,6,7};
    a = areshape(1,orders);
    orders = getorders(a);
    ind = { 2,3,1 };
    ind = previousindex(ind,orders);

After the code above, ind is equal to:

::

          2
    ind = 2
          5

In this example, :func:`previousindex` decremented *ind* to index the previous 6x7 subarray in array *a*.

.. seealso:: Functions :func:`nextindex`, :func:`loopnextindex`, :func:`walkindex`

