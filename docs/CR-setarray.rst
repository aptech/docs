
setarray
==============================================

Purpose
----------------
Sets a contiguous subarray of an N-dimensional array.

.. _setarray:
.. index:: setarray

Format
----------------

::

    setarray a, loc, src;

**Parameters**

:param a: (*N-dimensional array*) destination

:loc: (*vector*)  Mx1 vector of indices into the array to locate the subarray of interest where :math:`M` is a value from 1 to :math:`N`.

:src: (*[N-M]-dimensional array, matrix, or scalar*) data

Remarks
-------

`setarray` resets the specified subarray of *a* in place, without making a
copy of the entire array. Therefore, it is faster than `putarray`.

If *loc* is an Nx1 vector, then *src* must be a scalar. If *loc* is an [N-1]x1
vector, then *src* must be a 1-dimensional array or a 1xL vector, where :math:`L`
is the size of the fastest moving dimension of the array. If *loc* is an
[N-2]x1 vector, then *src* must be a KxL matrix, or a KxL 2-dimensional
array, where :math:`K` is the size of the second fastest moving dimension.

Otherwise, if *loc* is an Mx1 vector, then *src* must be an [N-M]-dimensional
array, whose dimensions are the same size as the corresponding dimensions of array *a*.

Examples
----------------

::

    a = arrayalloc(2|3|4|5|6,0);
    src = arrayinit(4|5|6,5);
    loc = { 2,1 };
    setarray a,loc,src;

This example sets the contiguous 4x5x6 subarray of *a* beginning at [2,1,1,1,1] to the array *src*, in which each element is set to the specified value 5.

.. seealso:: Functions `putarray`

