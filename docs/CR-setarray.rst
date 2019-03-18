
setarray
==============================================

Purpose
----------------
Sets a contiguous subarray of an N-dimensional array.

Format
----------------
.. function:: setarray a,  loc,  src

    :param a: N-dimensional array.
    :type a: TODO

    :param loc: where M is a value from 1 to N.
    :type loc: Mx1 vector of indices into the array to locate the subarray of interest

    :param src: [N-M]-dimensional array, matrix, or scalar.
    :type src: TODO

Examples
----------------

::

    a = arrayalloc(2|3|4|5|6,0);
    src = arrayinit(4|5|6,5);
    loc = { 2,1 };
    setarray a,loc,src;

This example sets the contiguous 4x5x6 subarray of a beginning at [2,1,1,1,1] to the array src, in which each element is set to the specified value 5.

.. seealso:: Functions :func:`putarray`
