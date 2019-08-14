
putarray
==============================================

Purpose
----------------

Puts a contiguous subarray into an N-dimensional array and returns the resulting array.

Format
----------------
.. function:: y = putarray(a, loc, src)

    :param a: destination data
    :type a: N-dimensional array

    :param loc: indices into the array to locate the subarray of interest, where *M* is a value from 1 to *N*.
    :type loc: Mx1 vector

    :param src: source data
    :type src: [N-M]-dimensional array or matrix or scalar.

    :returns: y (*N-dimensional array*)

Remarks
-------

If *loc* is an Nx1 vector, then *src* must be a scalar. If *loc* is an [N-1]x1
vector, then *src* must be a 1-dimensional array or a 1xL vector, where *L*
is the size of the fastest moving dimension of the array. If *loc* is an
[N-2]x1 vector, then *src* must be a KxL matrix, or a KxL 2-dimensional
array, where *K* is the size of the second fastest moving dimension.

Otherwise, if *loc* is an Mx1 vector, then *src* must be an [N-M]-dimensional
array, whose dimensions are the same size as the corresponding
dimensions of array *a*.


Examples
----------------

::

    // Create a 2x3x4x5x6 dimensional array with unspecified 
    // contents
    a = arrayalloc(2|3|4|5|6,0);
    
    // Create a 4x5x6 dimensional array with all elements equal 
    // to 5
    src = arrayinit(4|5|6,5);
    
    loc = { 2,1 };
    a = putarray(a,loc,src);

This example sets the contiguous 4x5x6 subarray of *a* beginning at [2,1,1,1,1] to 
the array *src*, in which each element is set to the specified value 5.

.. seealso:: Functions `setarray`

