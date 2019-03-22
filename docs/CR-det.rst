
det
==============================================

Purpose
----------------

Returns the determinant of a square matrix.

Format
----------------
.. function:: det(x)

    :param x: NxN square matrix or K-dimensional array where the last two dimensions are NxN 
    :type x: matrix or array

    :returns: y (*scalar or [K-2]-dimensional array*) , the determinant(s) of *x*.

Remarks
-------

*x* may be any valid expression that returns a square matrix (number of
rows equals number of columns) or a K-dimensional array where the last
two dimensions are of equal size.

If *x* is a K-dimensional array, the result will be a [K-2]-dimensional
array containing the determinants of each 2-dimensional array described
by the two trailing dimensions of *x*. In other words, for a 10x4x4 array,
the result will be a 1-dimensional array of 10 elements containing the
determinants of each of the 10 4x4 arrays contained in *x*.

:func:`det` computes an LU decomposition.

:func:`detl` can be much faster in many applications.


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

