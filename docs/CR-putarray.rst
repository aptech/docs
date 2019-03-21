
putarray
==============================================

Purpose
----------------

Puts a contiguous subarray into an N-dimensional array and returns the resulting array.

Format
----------------
.. function:: putarray(a, loc, src)

    :param a: 
    :type a: N-dimensional array

    :param loc: where M is a value from 1 to N.
    :type loc: Mx1 vector of indices into the array to locate the subarray of interest

    :param src: , matrix, or scalar.
    :type src: [N-M]-dimensional array

    :returns: y (N-dimensional array), 
Examples
----------------

::

    //Create a 2x3x4x5x6 dimensional array with unspecified 
    //contents
    a = arrayalloc(2|3|4|5|6,0);
    
    //Create a 4x5x6 dimensional array with all elements equal 
    //to 5
    src = arrayinit(4|5|6,5);
    
    loc = { 2,1 };
    a = putarray(a,loc,src);

a
src

.. seealso:: Functions :func:`setarray`
