
dot
==============================================

Purpose
----------------

Returns a scalar dot product of the columns of two matrices.

Format
----------------
.. function:: z = dot(x, y)

    :param x: first matrix.
    :type x: Nx1 vector or NxK matrix

    :param y: second matrix, *y*.
    :type y: Nx1 vector or NxK matrix

    :return z: The dot product of *x* and *y*.

    :type z: scalar or Kx1

Remarks
----------

*x* and *y* must have the same number columns, or one of them must only have a single column.


Examples
----------------

Basic usage
+++++++++++

::

    // Create two 4x1 column vectors
    x = { 5,
          9,
          3,
          4 };

    y = { 9,
         -6,
          8,
          1  };

    // Compute dot product
    z = dot(x, y);

    print  "z = " z;

After the code above:

::

    z = 19

Dot product of an Nx1 vector and Nx2 matrix
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create 4x1 vector
    x = { 5,
          9,
          3,
          4 };

    // Create 4x2 matrix
    y = { 9  8,
         -6  4,
          8  3,
          1 -2 };

    // Compute dot product
    z = dot(x, y);

    print  "z = " z;

After the code above:

::

    z = 19
        77

Dot product of the corresponding columns of two matrices
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create two 4x2 matrices
    x = { 5 1,
          9 3,
          3 8,
          4 2 };

    y = { 9  8,
         -6  4,
          8  3,
          1 -2 };

    // Compute dot product
    z = dot(x, y);

    print  "z = " z;

After the code above:

::

    z = 19
        40

.. seealso:: Functions :func:`crossprd`, :func:`norm`
