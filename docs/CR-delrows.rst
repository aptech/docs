
delrows
==============================================

Purpose
----------------

Deletes rows from a matrix. The second argument
contains the indices of the rows to be deleted.

Format
----------------
.. function:: delrows(x, r)

    :param x: data 
    :type x: NxK matrix

    :param r: indices of rows to delete.
    :type r: Mx1 vector

    :returns: y (*PxK matrix contaning*) the remaining rows of *x*.
        If no rows remain, *y* will be an empty matrix.

Remarks
-------

If *r* is an empty matrix, the result will be unchanged. Negative values
of *r* are counted from the end of the matrix, therefore:

::

   r = -1;

   y = delrows(x, r);

will delete last row of *x* . The remaining rows of *x* will be assigned to *y*.


Examples
----------------

::

    x = { 0 10 20,
         30 40 50,
         32 42 52,
         35 45 55,
         60 70 80 };
    
    r = { 2,
          4 };
    
    y = delrows(x,r);

After the code above:

::

    y =   0 10 20
         32 42 52
         60 70 80

.. seealso:: Functions :func:`delif`

