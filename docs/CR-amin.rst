
amin
==============================================

Purpose
----------------

Moves across one dimension of an N-dimensional array and finds the smallest element.

Format
----------------
.. function:: y = amin(x, dim)

    :param x: N-dimensional array
    :type x: array

    :param dim: the dimension across which to find the minimum value.
    :type dim: scalar

    :return y: 

    :type y: N-dimensional array

Remarks
-------

The output *y*, will have the same sizes of dimensions as *x*, except that
the dimension indicated by *dim* will be collapsed to 1.

Examples
----------------

::

    /*
    ** Setting the rng seed allows for repeatable
    ** random numbers
    */
    rndseed 8237348;

    /*
    ** Create a 24x1 vector of random normal numbers
    ** with a standard deviation of 10 and then round
    ** to the nearest integer value
    */
    x = round(10*rndn(24, 1));

    /*
    ** Reshape the 24x1 vector into a 2x3x4 dimensional array
    ** NOTE: The pipe operator '|' is for vertical concatenation
    */
    x = areshape(x, 2|3|4);

    dim = 2;
    y = amin(x, dim);

*x* is a 2x3x4 array, such that:
[1,1,1] through [1,3,4] =

::

     1.0000000      -11.000000       9.0000000      -8.0000000
    -2.0000000      -10.000000      -6.0000000      -5.0000000
    -5.0000000       17.000000       9.0000000      -2.0000000

[2,1,1] through [2,3,4] =

::

    -4.0000000      -2.0000000       7.0000000      -2.0000000
     4.0000000       13.000000      -16.000000       11.000000
     2.0000000      -1.0000000       12.000000      -16.000000

*y* will be a 2x1x4 array, such that:
[1,1,1] through [1,1,4] =

::

    -5.0000000      -11.000000      -6.0000000      -8.0000000

[2,1,1] through [2,1,4] =

::

    -4.0000000      -2.0000000      -16.000000      -16.000000

::

    y = amin(x, 1);

Using the same array *x* as the above example, this example finds the minimum value across the first dimension.
*y* will be a 2x3x1 array, such that:
[1,1,1] through [1,3,1] =

::

    -11.000000
    -10.000000
    -5.0000000

[2,1,1] through [2,3,1] =

::

    -4.0000000
    -16.000000
    -16.000000

.. seealso:: Functions :func:`amax`, :func:`minc`
