
delrows
==============================================

Purpose
----------------

Deletes rows from a matrix. The second argument
contains the indices of the rows to be deleted.

Format
----------------
.. function:: y = delrows(x, r)

    :param x: data
    :type x: NxK matrix

    :param r: indices of rows to delete.
    :type r: Scalar or Mx1 vector

    :returns: **x_trim** (*PxK matrix*) - the remaining rows of *x*.
        If no rows remain, *x_trim* will be an empty matrix.

Remarks
-------

If *r* is an empty matrix, the result will be unchanged. Negative values
of *r* are counted from the end of the matrix, therefore:

::

   r = -1;

   x_trim = delrows(x, r);

will delete last row of *x* . The remaining rows of *x* will be assigned to *x_trim*.


Examples
----------------

::

    x = { 0 10 20,
         30 40 50,
         32 42 52,
         35 45 55,
         60 70 80 };

    // Delete the second and fourth rows
    r = { 2,
          4 };

    x_trim = delrows(x, r);

After the code above:

::

    x_trim =   0 10 20
              32 42 52
              60 70 80

.. seealso:: Functions :func:`delif`
