
delrows
==============================================

Purpose
----------------

Deletes rows from a matrix. The second argument
contains the indices of the rows to be deleted.

Format
----------------
.. function:: delrows(x, r)

    :param x: 
    :type x: NxK data matrix

    :param r: indices of rows to delete.
    :type r: Mx1 vector

    :returns: y (*TODO*), PxK matrix contaning the remaining rows of x.
        If no rows remain, y will be an empty matrix.

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
