
asum
==============================================

Purpose
----------------
Computes the sum across one dimension of an N-dimensional array.

Format
----------------
.. function:: y = asum(x, dim)

    :param x:
    :type x: N-dimensional array

    :param dim: the dimension across which to sum.
    :type dim: scalar

    :return y: 

    :rtype y: N-dimensional array

Examples
----------------

::

    x = seqa(1, 1, 24);

    dims = { 2, 3, 4 };
    x = areshape(x, dims);

    y = asum(x, 3);

*x* is a 2x3x4 array, such that:

::

    Plane [1,.,.]

       1.000    2.000    3.000    4.000
       5.000    6.000    7.000    8.000
       9.000   10.000   11.000   12.000

    Plane [2,.,.]

      13.000   14.000   15.000   16.000
      17.000   18.000   19.000   20.000
      21.000   22.000   23.000   24.000

and y is equal to:

::

    Plane [1,.,.]

      14.000   16.000   18.000   20.000
      22.000   24.000   26.000   28.000
      30.000   32.000   34.000   36.000

::

    y = asum(x,1);

Using the same array *x* as the above example, this example computes the sum across the first dimension. *y* will be a 2x3x1 array, such that:

::

    Plane [1,.,.]

      10.000
      26.000
      42.000

    Plane [2,.,.]

      58.000
      74.000
      90.000

Remarks
-------

The output *y*, will have the same sizes of dimensions as *x*, except that
the dimension indicated by *dim* will be collapsed to 1.

.. seealso:: Functions :func:`amean`
