
getmatrix4D
==============================================

Purpose
----------------

Gets a contiguous matrix from a 4-dimensional array.

Format
----------------
.. function:: y = getmatrix4D(a, i1, i2)

    :param a: Data.
    :type a: 4-dimensional array

    :param i1: index into the slowest moving dimension of the array.
    :type i1: scalar

    :param i2: index into the second slowest moving dimension of the array.
    :type i2: scalar

    :return y: where *L* is the size of the fastest moving
        dimension of the array and *K* is the size of the second fastest moving dimension.

    :rtype y: KxL matrix

Remarks
-------

:func:`getmatrix4D` returns the contiguous matrix that begins at the :math:`[i1, i2, 1, 1]`
position in array *a* and ends at the :math:`[i1, i2, K, L]` position.

A call to :func:`getmatrix4D` is faster than using the more general :func:`getmatrix`
function to get a matrix from a 4-dimensional array, especially when *i1*
and *i2* are the counters from nested `for` loops.


Examples
----------------

::

    // Create a column vector 1, 2, 3...120
    a = seqa(1, 1, 120);

    /*
    ** Reshape the column vector into a 2x3x4x5 dimensional
    ** array
    */
    a = areshape(a, 2|3|4|5);

    // Extract a submatrix
    y = getmatrix4D(a, 2, 3);

After the code above:

::

        101   102   103   104   105
    y = 106   107   108   109   110
        111   112   113   114   115
        116   117   118   119   120

.. seealso:: Functions :func:`getmatrix`, :func:`getscalar4D`, :func:`getarray`
