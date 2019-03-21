
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

Remarks
-------

The rotation is performed horizontally within each row of the matrix. A
positive rotation value will cause the elements to move to the right. A
negative rotation value will cause the elements to move to the left. In
either case, the elements that are pushed off the end of the row will
wrap around to the opposite end of the same row.

If the rotation value is greater than or equal to the number of columns
in x, then the rotation value will be calculated using (r % cols(x)).


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
