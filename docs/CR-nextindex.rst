
nextindex
==============================================

Purpose
----------------

Returns the index of the next element or subarray in an array.

Format
----------------
.. function:: nextindex(i, o)

    :param i: where M<=N.
    :type i: Mx1 vector of indices into an array

    :param o: 
    :type o: Nx1 vector of orders of an N-dimensional array

    :returns: ni (*Mx1 vector of indices*), the index of the next element or subarray in the array corresponding to  o.

Examples
----------------

::

    //Dimensions of an array
    orders = { 3, 4, 5, 6, 7);
    
    //Starting index
    ind = { 2, 3, 5 };
    
    //Return the index for the next element
    ind = nextindex(ind,orders);

After the code above, ind will be equal to:

::

    2
    4
    1

In this example, nextindex incremented ind
to index the next 6x7 subarray in array a.
Using the same data from above, a subsequent call to nextindex:

::

    ind = nextindex(ind,orders);

will assign ind to be equal to:

::

    2
    4
    2

.. seealso:: Functions :func:`previousindex`, :func:`loopnextindex`, :func:`walkindex`
