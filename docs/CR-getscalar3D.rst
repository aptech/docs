
getscalar3D
==============================================

Purpose
----------------

Gets a scalar from a 3-dimensional array.

Format
----------------
.. function:: y = getscalar3D(a, i1, i2, i3)

    :param a: Data
    :type a: 3-dimensional array

    :param i1: index into the slowest moving dimension of the array.
    :type i1: scalar

    :param i2: index into the second slowest moving dimension of the array.
    :type i2: scalar

    :param i3: index into the fastest moving dimension of the array.
    :type i3: scalar

    :return y: the element of the array indicated by the indices.

    :rtype y: scalar

Examples
----------------

::

    // Create a column vector 1, 2, 3,...24
    a = seqa(1, 1, 24);

    // Reshape the column vector into a 2x3x4 dimensional array
    a = areshape(a, 2|3|4);

    y = getscalar3D(a, 1, 3, 2);

A 2x3x4 dimensional array can be thought of as two 3x4 dimensional matrices. The call to :func:`getScalar3D` above, returns the
:math:`[3,2]` element of the first of these matrices. The value of which is:

::

    y = 10

Remarks
-------

:func:`getscalar3D` returns the scalar that is located in the :math:`[i1, i2, i3]`
position of array *a*.

A call to :func:`getscalar3D` is faster than using the more general :func:`getmatrix`
function to get a scalar from a 3-dimensional array.


.. seealso:: Functions :func:`getmatrix`, :func:`getscalar4D`, :func:`getarray`
