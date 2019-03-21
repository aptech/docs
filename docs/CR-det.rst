
det
==============================================

Purpose
----------------

Returns the determinant of a square matrix.

Format
----------------
.. function:: det(x)

    :param x: 
    :type x: NxN square matrix or K-dimensional array where the last two dimensions are NxN 

    :returns: y (*TODO*), scalar or [K-2]-dimensional array, the determinant(s) of x.

Examples
----------------

::

    x = { 3 2 1,
          0 1 -2,
          1 3 4 };
    y = det(x);
    
    format /rd 3,0;
    print "The determinant of y =" y;

The code above, produces:

::

    The determinant of y = 25

.. seealso:: Functions :func:`detl`

determinant square matrix det
