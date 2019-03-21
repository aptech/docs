
arrayindex
==============================================

Purpose
----------------
Converts a scalar vector index to a vector of indices for an N-dimensional array.

Format
----------------
.. function:: arrayindex(scalar_idx, orders)

    :param scalar_idx: index into vector or 1-dimensional array.
    :type scalar_idx: scalar

    :param orders: orders of an N-dimensional array
    :type orders: Nx1 vector

    :returns: i (*Nx1 vector of indices*), index of corresponding element in N-dimensional array.

Remarks
-------

This function and its opposite, :func:`singleindex`, allow you to easily convert
between an N-dimensional index and its corresponding location in a
1-dimensional object of the same size.

Examples
----------------

::

    // Set the rng seed for repeatable random numbers
    rndseed 982348;
    
    orders = { 2, 3, 4, 5 };
    
    /*
    ** Create 120x1 vector of uniform random numbers
    ** (2*3*4*5 = 120)
    */
    v = rndu(prodc(orders), 1);
    
    /*
    ** Reshape the 120x1 random vector into a
    ** 2x3x4x5 dimensional array
    */
    a = areshape(v, orders);
    
    vi = 50;
    ai = arrayindex(vi, orders);
    
    print "vi = " vi;
    print "ai = " ai;
    print "v[vi] = " v[vi];
    print "getarray(a, ai) = "; getarray(a, ai);

The code above, produces the following output:

::

    vi =   50.000
    ai =
       1.000
       3.000
       2.000
       5.000
    v[vi] =    0.047
    getarray(a, ai) =    0.047

This example allocates a vector of random numbers and creates a 4-dimensional array using the same data.
The 50th element of the vector *v* corresponds to the element of array *a*
that is indexed with *ai*.

.. seealso:: Functions :func:`singleindex`

