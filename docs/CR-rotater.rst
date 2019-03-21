
rotater
==============================================

Purpose
----------------

Rotates the rows of a matrix.

Format
----------------
.. function:: rotater(x, r)

    :param x: 
    :type x: NxK matrix to be rotated

    :param r: 
    :type r: Nx1 or 1x1 matrix specifying the amount of
        rotation

    :returns: y (*TODO*), NxK rotated matrix.

Examples
----------------

::

    y = rotater(x,r);

::

    1  2  3           1            3  1  2
    If x =          and r =     Then y =
           4  5  6          -1            5  6  4

::

    1  2  3           0            1  2  3
    
           4  5  6           1            6  4  5
    If x =          and r =     Then y =
           7  8  9           2            8  9  7
    
          10 11 12           3           10 11 12

.. seealso:: Functions :func:`shiftr`
