
setarray
==============================================

Purpose
----------------
Sets a contiguous subarray of an N-dimensional array.

Format
----------------
.. function:: setarray a, loc, src

    :param a: 
    :type a: N-dimensional array

    :param loc: where M is a value from 1 to N.
    :type loc: Mx1 vector of indices into the array to locate the subarray of interest

    :param src: , matrix, or scalar.
    :type src: [N-M]-dimensional array

Remarks
-------

setarray resets the specified subarray of a in place, without making a
copy of the entire array. Therefore, it is faster than putarray.

Ifloc is an Nx1 vector, then src must be a scalar. Ifloc is an [N-1]x1
vector, thensrc must be a 1-dimensional array or a 1xL vector, where L
is the size of the fastest moving dimension of the array. If loc is an
[N-2]x1 vector, thensrc must be a KxL matrix, or a KxL 2-dimensional
array, where K is the size of the second fastest moving dimension.

Otherwise, ifloc is an Mx1 vector, thensrc must be an [N-M]-dimensional
array, whose dimensions are the same size as the corresponding
dimensions of array a.


Examples
----------------

::

    a = arrayalloc(2|3|4|5|6,0);
    src = arrayinit(4|5|6,5);
    loc = { 2,1 };
    setarray a,loc,src;

This example sets the contiguous 4x5x6 subarray of a beginning at [2,1,1,1,1] to the array src, in which each element is set to the specified value 5.

.. seealso:: Functions :func:`putarray`
