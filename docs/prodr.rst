
prodr
==============================================

Purpose
----------------

Computes the products of all elements in each row of a matrix, or array.

Format
----------------
.. function:: y = prodr(x)

    :param x: data
    :type x: NxK matrix

    :return y: contains the products of all elements in each row of *x*.

    :rtype y: Kx1 matrix

Examples
----------------

::

    x = { 1 2 3,
          4 5 6,
          7 8 9 };

    y = prodr(x);

The code above assigns *y* to be equal to:

::

          6
    y = 120 
        504

Remarks
-------

:func:`prodr` will run faster than :func:`prodc`, so if you can arrange your data for a row-wise multiplication it may speed up your program.

To find the products of all of the elements in a matrix, use the :func:`vecr`
function before applying :func:`prodr`.


.. seealso:: Functions :func:`cumsumc`, :func:`prodc`, :func:`sumc`
