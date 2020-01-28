
singleindex
==============================================

Purpose
----------------
Converts a vector of indices for an N-dimensional array to a scalar vector index.

Format
----------------
.. function:: si = singleindex(i, o)

    :param i: indices into an N-dimensional array
    :type i: Nx1 vector

    :param o: orders of an N-dimensional array
    :type o: Nx1 vector

    :return si: index of corresponding element in 1-dimensional array or vector.

    :rtype si: scalar

Examples
----------------

::

    // Set orders
    orders = { 2, 3, 4 };

    // Allocate array
    a = arrayalloc(orders,0);
    ai = { 2, 1, 3 };

    // Set array
    setarray a, ai, 49;
    v = vecr(a);
    vi = singleindex(ai, orders);

    print "ai = " ai;
    print "vi = " vi;
    print "getarray(a, ai) = " getarray(a, ai);
    print "v[vi] = " v[vi];

::

    ai =
       2.0000000
       1.0000000
       3.0000000

    vi = 15.000000

    getarray(a, ai) = 49.000000
    
    v[vi] = 49.000000

This example allocates a 3-dimensional array *a* and sets
the element corresponding to the index vector *ai* to 49. It then
creates a vector, *v*, with the same data. The element in
the array *a* that is indexed by *ai* corresponds
to the element of the vector *v* that is indexed by *vi*.

Remarks
-------

This function and its opposite, :func:`arrayindex`, allow you to convert between
an N-dimensional index and its corresponding location in a 1-dimensional object of the same size.

.. seealso:: Functions :func:`arrayindex`
