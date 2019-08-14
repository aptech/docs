
walkindex
==============================================

Purpose
----------------

Walks the index of an array forward or backward through a specified dimension.

Format
----------------
.. function:: ni = walkindex(i, o, dim)

    :param i: where :math:`M <= N`.
    :type i: Mx1 vector of indices into an array

    :param o: orders of an N-dimensional array
    :type o: Nx1 vector

    :param dim: :math:`[1-to-M]`, index into the vector of indices *i*, corresponding to the dimension to walk through,
        positive to walk the index forward, or negative to walk backward.
    :type dim: scalar

    :returns: ni (*Mx1 vector of indices*), the new index.

Remarks
-------

:func:`walkindex` will return a scalar error code if the index cannot walk
further in the specified dimension and direction.

Examples
----------------

::

    orders =(3,4,5,6,7);
    
    // Create a 3x4x5x6x7 dimensional array with each element 
    // equal to 1
    a = arrayinit(orders,1);
    
    ind = { 2,3,3 };
    ind = walkindex(ind,orders,-2);

::

          2
    ind = 2
          3

This example decrements the second value of the index vector *ind*.

::

    ind = walkindex(ind,orders,3);

::

          2
    ind = 2
          4

Using the orders from the example above and the *ind* that was returned, 
this example increments the third value of the index vector *ind*.

.. seealso:: Functions :func:`nextindex`, :func:`previousindex`, :func:`loopnextindex`

