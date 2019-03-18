
loopnextindex
==============================================

Purpose
----------------

Increments an index vector to the next logical index and jumps to the specified label if the index did not wrap to the beginning.

Format
----------------
.. function:: loopnextindex lab, i, o [, dim]

    :param lab: label to jump to if loopnextindex succeeds.
    :type lab: literal

    :param i: where M<=N.
    :type i: Mx1 vector of indices into an array

    :param o: Nx1 vector of orders of an N-dimensional array.
    :type o: TODO

    :param dim: scalar [1-M], index into the vector of indices  i, corresponding to the dimension to walk through, positive to walk the index forward, or negative to walk backward.
    :type dim: TODO

Examples
----------------
At its essence, loopNextIndex provides a simple way to iterate over the orders of a multi-dimensional array.

::

    //The orders of the array
    orders = { 2, 3, 4 };
    
    //The starting index of the array
    ind = { 1, 1, 1 };
    
    lnilab:
    print "ind = " ind;
    loopNextIndex lnilab, ind, orders;

Running the code above, returns:

::

    ind = 
     1.000 
     1.000 
     1.000 
    ind = 
     1.000 
     1.000 
     2.000 
    ind = 
     1.000 
     1.000 
     3.000 
    ind = 
     1.000 
     1.000 
     4.000 
    ind = 
     1.000 
     2.000 
     1.000 
    ind = 
     1.000 
     2.000 
     2.000 
    ind = 
     1.000 
     2.000 
     3.000
     
     ...continuing on to end with...
     
     ind = 
     2.000 
     3.000 
     4.000

This next example uses the variable ind to iterate over and make assignments to the array, a.

::

    orders = { 2,3,4,5,6,7 };
    a = arrayalloc(orders,0);
    ind = { 1,1,1,1 };
     
    loopni:
     
    setarray a, ind, rndn(6,7);
    loopnextindex loopni, ind, orders;

This example sets each 6x7 subarray of array a, 
by incrementing the index at each call of loopnextindex 
and then going to the label loopni. When ind 
cannot be incremented, the program drops out of the loop and continues.

::

    ind = { 1,1,4,5 };
     
    loopni2:
     
    setarray a, ind, rndn(6,7);
    loopnextindex loopni2, ind, orders, 2;

Using the array and vector of orders from the example above, this 
example increments the second value of the index vector ind 
during each call to loopnextindex. This loop will set
the 6x7 subarrays of a that begin at [1,1,4,5,1,1], 
[1,2,4,5,1,1], and [1,3,4,5,1,1], and then drop out of the loop.

.. seealso:: Functions :func:`nextindex`, :func:`previousindex`, :func:`walkindex`
