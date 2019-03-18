
amean
==============================================

Purpose
----------------

Computes the mean across one dimension of an N-dimensional array.

Format
----------------
.. function:: amean(x,  dim)

    :param x: N-dimensional array.
    :type x: TODO

    :param dim: number of dimension to compute the mean across.
    :type dim: scalar

    :returns: y (*TODO*), [N-1]-dimensional array.

Examples
----------------

::

    //Create an additive sequence from 1-24
    x = seqa(1,1,24);
    
    //'Reshape' this 24x1 vector into a 2x3x4 dimensional array
    x = areshape(x,2|3|4);
    
    y = amean(x,3);

x is a 2x3x4 array, such that:
[1,1,1] through [1,3,4] =

::

    1.0000000       2.0000000       3.0000000       4.0000000
    5.0000000       6.0000000       7.0000000       8.0000000
    9.0000000       10.000000       11.000000       12.000000

[2,1,1] through [2,3,4] =

::

    13.000000       14.000000       15.000000       16.000000
    17.000000       18.000000       19.000000       20.000000
    21.000000       22.000000       23.000000       24.000000

y will be a 1x3x4 array, such that:
[1,1,1] through [1,3,4] =

::

    7.0000000       8.0000000       9.0000000       10.000000
    11.000000       12.000000       13.000000       14.000000
    15.000000       16.000000       17.000000       18.000000

::

    y = amean(x,1);

Using the same array x as the above example, this example computes the mean across the first dimension. y will be a 2x3x1 array, such that:
[1,1,1] through [1,3,1] =

::

    2.5000000
    6.5000000
    10.500000

[2,1,1] through [2,3,1] =

::

    14.500000
    18.500000
    22.500000

.. seealso:: Functions :func:`asum`
