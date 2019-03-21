
getarray
==============================================

Purpose
----------------

Gets a contiguous subarray from an N-dimensional array.

Format
----------------
.. function:: getarray(a, loc)

    :param a: 
    :type a: N-dimensional array

    :param loc: where 1 <= M <= N.
    :type loc: Mx1 vector of indices into the array to locate the subarray of interest

    :returns: y (*TODO*), [N-M]-dimensional subarray or scalar.

Remarks
-------

If N-M>0, getarray will return an array of [N-M] dimensions, otherwise,
if N-M=0, it will return a scalar.


Examples
----------------

::

    a = seqa(1,1,720);
    a = areshape(a,2|3|4|5|6);
    loc = { 2,1 };
    y = getarray(a,loc);

y will be a 4x5x6 array of sequential
values, beginning at [1,1,1] with 361, and ending at [4,5,6] with
480.

.. seealso:: Functions :func:`getmatrix`
