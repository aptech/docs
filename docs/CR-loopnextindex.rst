
loopnextindex
==============================================

Purpose
----------------

Increments an index vector to the next logical index and jumps to the specified label if the index did not wrap to the beginning.

.. _loopnextindex:
.. index:: loopnextindex

Format
----------------

::

    loopnextindex lab, i, o [, dim];

**Parameters:**

:lab: (*literal*) label to jump to if `loopnextindex` succeeds.
:i: (*Mx1 vector*) indices into an array where :math:`M <= N`.
:o: (*Nx1 vector*) orders of an N-dimensional array
:dim: (*scalar*) :math:`[1-M]`, index into the vector of indices *i*, corresponding to the dimension to walk through, positive to walk the index forward, or negative to walk backward.

Remarks
-------

If the argument *dim* is given, `loopnextindex` will walk through only the
dimension indicated by *dim* in the specified direction. Otherwise, if *dim*
is not given, each call to `loopnextindex` will increment *i* to index the
next element or subarray of the corresponding array.

`loopnextindex` will jump to the label indicated by *lab* if the index can
walk further in the specified dimension and direction, otherwise it will
fall out of the loop and continue through the program.

When the index matches the vector of orders, the index will be reset to
the beginning and program execution will resume at the statement
following the `loopnextindex` statement.


Examples
----------------
At its essence, `loopnextindex` provides a simple way to iterate over the orders of a multi-dimensional array.

::

    // The orders of the array
    orders = { 2, 3, 4 };

    // The starting index of the array
    ind = { 1, 1, 1 };

    // Label to return to
    lnilab:

    // Print current index
    print "ind = " ind;

    // Loop through indices and return
    // to label lnilab 
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

This next example uses the variable *ind* to iterate over and make assignments to the array, *a*.

::

    // Set orders of array
    orders = { 2, 3, 4, 5, 6, 7 };

    // Allocate array to zeroes
    a = arrayalloc(orders, 0);

    // Set starting index
    ind = { 1, 1, 1, 1 };

    // Label to return to
    loopni:

    // Set 6x7 subarray at current index
    // to a random matrix
    setarray a, ind, rndn(6,7);

    // Loop to next index and
    // return to label loopni
    loopnextindex loopni, ind, orders;

This example sets each 6x7 subarray of array *a*,
by incrementing the index at each call of `loopnextindex`
and then going to the label *loopni*. When *ind*
cannot be incremented, the program drops out of the loop and continues.

::

    // Starting index
    ind = { 1, 1, 4, 5 };

    // Label
    loopni2:

    // Set 6x7 subarray to random matrix
    setarray a, ind, rndn(6,7);

    // Increment second value of index vector
    // and return to label loopni2
    loopnextindex loopni2, ind, orders, 2;

Using the array and vector of orders from the example above, this
example increments the second value of the index vector *ind*
during each call to `loopnextindex`. This loop will set
the 6x7 subarrays of a that begin at :math:`[1,1,4,5,1,1]`,
:math:`[1,2,4,5,1,1]`, and :math:`[1,3,4,5,1,1]`, and then drop out of the loop.

.. seealso:: Functions :func:`nextindex`, :func:`previousindex`, :func:`walkindex`
