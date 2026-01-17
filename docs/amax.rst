
amax
==============================================

Purpose
----------------

Moves across one dimension of an N-dimensional array and finds the largest element.

Format
----------------
.. function:: y = amax(x, dim)

    :param x: The N-dimensional array from which to find the maximum values.
    :type x: N-dimensional array.

    :param dim: The dimension across which to find the maximum value.
    :type dim: Scalar

    :return y: The maximum values found along the specified dimension.
    :rtype y: N-dimensional array

Examples
----------------

::

    rndseed 9823432;

    /*
    ** Create random normal numbers with a standard deviation
    ** of 10 and round them to the nearest integer
    */
    x = round(10*rndn(24, 1));

    // Reshape them from a 24x1 vector into 2x3x4 array
    x = areshape(x, 2|3|4);

    // Calculate the max across the second dimension
    dim = 2;
    y = amax(x, dim);

After this calculation:
x[1,1,1] through x[1,3,4] =

::

    -14.000000      4.0000000       6.0000000      -4.0000000
     1.0000000      8.0000000       10.000000       9.0000000
    -3.0000000      12.000000       5.0000000      -26.000000

x[2,1,1] through x[2,3,4] =

::

     4.0000000      6.0000000       4.0000000       2.0000000
     1.0000000      16.000000       9.0000000      -4.0000000
    -4.0000000     -8.0000000      -10.000000       8.0000000

y[1,1,1] through y[1,1,4] =

::

    1.0000000       12.000000       10.000000       9.0000000

y[2,1,1] through y[2,1,4] =

::

    4.0000000       16.000000       9.0000000       8.0000000

Use the same *x* array and calculate the max across dimension 1:

::

    y2 = amax(x, 1);

After this calculation, *x* remains the same, but *y2* is:
y2[1,1,1] through y2[1,3,1] =

::

    6.0000000
    10.000000
    12.000000

y2[2,1,1] through y2[2,3,1] =

::

    6.0000000
    16.000000
    8.0000000

Remarks
-------

The output *y*, will have the same sizes of dimensions as *x*, except that
the dimension indicated by *dim* will be collapsed to 1.

.. seealso:: Functions :func:`amin`, :func:`maxc`
