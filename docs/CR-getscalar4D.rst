
getscalar4D
==============================================

Purpose
----------------

Gets a scalar from a 4-dimensional array.

Format
----------------
.. function:: y = getscalar4D(a, i1, i2, i3, i4)

    :param a: Data
    :type a: 4-dimensional array

    :param i1: index into the slowest moving dimension of the array.
    :type i1: scalar

    :param i2: index into the second slowest moving dimension of the array.
    :type i2: scalar

    :param i3: index into the second fastest moving dimension of the array.
    :type i3: scalar

    :param i4: index into the fastest moving dimension of the array.
    :type i4: scalar

    :return y: the element of the array indicated by the indices.

    :type y: scalar

Remarks
-------

:func:`getscalar4D` returns the scalar that is located in the :math:`[i1, i2, i3, i4]`
position of array *a*.

A call to :func:`getscalar4D` is faster than using the more general :func:`getmatrix`
function to get a scalar from a 4-dimensional array.


Examples
----------------

::

    // Create a column vector 1, 2, 3, ... ,120
    a = seqa(1, 1, 120);

    /*
    ** Reshape the column vector
    ** into a 2x3x4x5 dimensional array
    */
    a = areshape(a, 2|3|4|5);

    // Get the scalar in the 1,3,2,5 element
    y = getscalar4D(a, 1, 3, 2, 5);

The code above assigns *y* equal to 50.

.. seealso:: Functions :func:`getmatrix`, :func:`getscalar3D`, :func:`getarray`
