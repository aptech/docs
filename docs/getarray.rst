
getarray
==============================================

Purpose
----------------

Gets a contiguous subarray from an N-dimensional array.

Format
----------------
.. function:: y = getarray(a, loc)

    :param a: array
    :type a: N-dimensional array

    :param loc: vector of indices into the array to locate the subarray of interest where :math:`1 <= M <= N`.
    :type loc: Mx1 vector

    :return y: The subarray of interest located in the *loc* of *a*.

    :rtype y: [N-M]-dimensional array or scalar

Examples
----------------

::

    // Generate vector
    vec_st = seqa(1, 1, 720);

    // Reshape `vec` into array
    a = areshape(vec_st, 2|3|4|5|6);

    // Location index
    loc = { 2, 1 };

    // Get scalar at location 2,1 of array a
    y = getarray(a, loc);

*y* will be a 4x5x6 array of sequential values, beginning at :math:`[1,1,1]` with 361, and ending at :math:`[4,5,6]` with 480.

Remarks
-------

If :math:`N - M > 0`, :func:`getarray` will return an array of [N-M] dimensions, otherwise,
if :math:`N - M = 0`, it will return a scalar.


.. seealso:: Functions :func:`getmatrix`
