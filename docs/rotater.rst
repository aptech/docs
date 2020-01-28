
rotater
==============================================

Purpose
----------------

Rotates the rows of a matrix.

Format
----------------
.. function:: y = rotater(x, r)

    :param x: data to be rotated
    :type x: NxK matrix

    :param r: Specifies the amount of rotation
    :type r: Nx1 matrix or scalar

    :return y: Rotated matrix

    :rtype y: NxK matrix

Examples
----------------

::

    // Create data matrix
    x = { 1 2 3,
        4 5 6 };

    // Rotation matrix
    r = { 1, -1 };

    // Rotate matrix x
    y = rotater(x, r);

::

           1  2  3                3  1  2
      x =                   y =
           4  5  6                5  6  4

::

      // Create data matrix
      x = { 1 2 3,
          4 5 6,
          7 8 9,
          10 11 12 };

      // Rotation matrix
      r = { 0, 1, 2, 3 };

      // Rotate matrix x
      y = rotater(x, r);

::

           1  2  3                        1  2  3

           4  5  6                        6  4  5
      x =                          y =
           7  8  9                        8  9  7

          10 11 12                       10 11 12

Remarks
-------

The rotation is performed horizontally within each row of the matrix. A
positive rotation value will cause the elements to move to the right. A
negative rotation value will cause the elements to move to the left. In
either case, the elements that are pushed off the end of the row will
wrap around to the opposite end of the same row.

If the rotation value is greater than or equal to the number of columns
in *x*, then the rotation value will be calculated using ``(r % cols(x))``.


.. seealso:: Functions :func:`shiftr`
