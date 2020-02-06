
walkindex
==============================================

Purpose
----------------

Walks the index of an array forward or backward through a specified dimension.

Format
----------------
.. function:: new_idx = walkindex(idx, orders, dim)

    :param idx: where :math:`M <= N`.
    :type idx: Mx1 vector of indices into an array

    :param orders: orders of an N-dimensional array
    :type orders: Nx1 vector

    :param dim: :math:`[1-to-M]`, index into the vector of indices *idx*, specifying which dimension to walk through.
        A positive value will walk the index forward, while a negative value will walk backward.
    :type dim: scalar

    :return new_idx: the new index.

    :rtype new_idx: Mx1 vector of indices

Examples
----------------

Walk down the columns of a matrix
+++++++++++++++++++++++++++++++++++

::

    orders = { 4, 3 };

    // Starting index
    idx = { 1, 1 };

    // Get the next index 
    idx = walkindex(idx, orders, 1); 

::

After the above code, *idx* will equal:

::

    2
    1

If we call it again, like this:

::

    // Starting idx = { 2, 1 }
    idx = walkindex(idx, orders, 1); 

*idx* will be changed to:

::

    3
    1

We can see that :func:`walkindex` is incrementing the first index by one each time we call it. 

Walk down the rows of a matrix
+++++++++++++++++++++++++++++++

We will continue with our example from above, but this time we will change the final input, *dim*, equal to two to increment the second index. 

::

    // Starting idx = { 3, 1 }
    idx = walkindex(idx, orders, 2); 

*idx* will be changed to:

::

    3
    2

Walk backwards through a 3-D array
+++++++++++++++++++++++++++++++++++

This example decrements the second value of the index vector *idx*.

::

    orders = { 2, 4, 3 };
    
    idx = { 2, 3, 3 };
    idx = walkindex(idx, orders, -2);

::

          2
    idx = 2
          3

Since the absolute value of the final input, *dim* was equal to two, the second index was modified. Since the value was negative
the index was decremented.


Walk forwards through a 3-D array
+++++++++++++++++++++++++++++++++++

This example will continue with the final value of *idx* from the previous example.

::

    // Starting idx = { 2, 2, 3 }
    idx = walkindex(idx, orders, 3);

Since the final input, *dim*, is equal to positive three, the third element of *idx* is increased by one.

::

          2
    idx = 2
          4


Remarks
-------

* :func:`nextindex` is often more useful.
* :func:`walkindex` will return a scalar error code if the index cannot walk
  further in the specified dimension and direction.

.. seealso:: Functions :func:`nextindex`, :func:`previousindex`, `loopnextindex`

