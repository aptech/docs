
prodc
==============================================

Purpose
----------------

Computes the products of all elements in each column of a matrix.

Format
----------------
.. function:: prodc(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*TODO*), Kx1 matrix containing the products of all elements in each column of x.

Examples
----------------

::

    x = { 1 2 3,
          4 5 6,
          7 8 9 };
     
    y = prodc(x);

The code above assigns y to be equal to:

::

    28
    y =  80
        162

.. seealso:: Functions :func:`sumc`, :func:`meanc`, :func:`stdc`
