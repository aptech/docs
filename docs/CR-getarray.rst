
getarray
==============================================

Purpose
----------------

Gets a contiguous subarray from an N-dimensional array.

Format
----------------
.. function:: getarray(a, loc)

    :param a: array
    :type a: N-dimensional array

    :param loc: vector of indices into the array to locate the subarray of interest where :math:`1 <= M <= N`.
    :type loc: Mx1 vector

    :returns: y (*[N-M]-dimensional subarray or scalar*)

Remarks
-------

If :math:`N - M > 0`, getarray will return an array of [N-M] dimensions, otherwise,
if :math:`N - M = 0`, it will return a scalar.


Examples
----------------

::

    a = seqa(1,1,720);
    a = areshape(a,2|3|4|5|6);
    loc = { 2,1 };
    y = getarray(a,loc);

*y* will be a 4x5x6 array of sequential values, beginning at :math:`[1,1,1]` with 361, and ending at :math:`[4,5,6]` with 480.

.. seealso:: Functions :func:`getmatrix`

