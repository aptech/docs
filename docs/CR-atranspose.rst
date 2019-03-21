
atranspose
==============================================

Purpose
----------------

Transposes an N-dimensional array.

Format
----------------
.. function:: atranspose(x, nd)

    :param x: 
    :type x: N-dimensional array

    :param nd: the new order of dimensions.
    :type nd: Nx1 vector

    :returns: y (N-dimensional array), transposed according to *nd*.

Remarks
-------

The vector of dimension indices must be a unique vector of integers,
*1-N*, where 1 corresponds to the first element of the vector of orders.

Examples
----------------

::

    x = seqa(1,1,24);
    x = areshape(x,2|3|4);
    nd = { 2,1,3 };
    y = atranspose(x,nd);

This example transposes the dimensions of *x* that correspond to the first and second elements of the vector of orders. *x* is a 2x3x4 array, such that:

::

    Plane [1,.,.]
    
       1.000    2.000    3.000    4.000
       5.000    6.000    7.000    8.000
       9.000   10.000   11.000   12.000
    
    Plane [2,.,.]
    
      13.000   14.000   15.000   16.000
      17.000   18.000   19.000   20.000
      21.000   22.000   23.000   24.000

*y* is a 3x2x4 array, such that:

::

    Plane [1,.,.]
    
       1.000    2.000    3.000    4.000
      13.000   14.000   15.000   16.000
    
    Plane [2,.,.]
    
       5.000    6.000    7.000    8.000
      17.000   18.000   19.000   20.000
    
    Plane [3,.,.]
    
       9.000   10.000   11.000   12.000
      21.000   22.000   23.000   24.000

::

    nd = { 2,3,1 };
    y = atranspose(x,nd);

Using the same array *x* as the example above, this example transposes all three dimensions of *x*, returning a 3x4x2 array *y*, such that:

::

    Plane [1,.,.]
    
       1.000   13.000
       2.000   14.000
       3.000   15.000
       4.000   16.000
    
    Plane [2,.,.]
    
       5.000   17.000
       6.000   18.000
       7.000   19.000
       8.000   20.000
    
    Plane [3,.,.]
    
       9.000   21.000
      10.000   22.000
      11.000   23.000
      12.000   24.000

.. seealso:: Functions :func:`areshape`, :func:`squeeze`

