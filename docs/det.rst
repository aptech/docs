
det
==============================================

Purpose
----------------

Returns the determinant of a square matrix.

Format
----------------
.. function:: d = det(x)

    :param x: matrix or array used to find the determinant.
    :type x: NxN matrix or KxNxN array

    :return d: the determinant(s) of *x*.

    :rtype d: scalar or 1-dimensional array

Examples
----------------

::

    x = { 3 2 1,
          0 1 -2,
          1 3 4 };

    d = det(x);

    format /rd 3,0;
    print "The determinant of d =" d;

The code above, produces:

::

    The determinant of d = 25

Remarks
-------

*x* may be any valid expression that returns a square matrix (number of
rows equals number of columns) or a K-dimensional array where the last
two dimensions are of equal size.

If *x* is a K-dimensional array, the result will be a 1-dimensional
array containing the determinants of each 2-dimensional array described
by the two trailing dimensions of *x*. For example, for a 10x4x4 array,
the result will be a 1-dimensional array of 10 elements containing the
determinants of each of the 10 4x4 arrays contained in *x*.

:func:`det` computes an LU decomposition. For a real matrix, it returns 0
when a pivot is at or below ``crout_tol * min(1, largest absolute element)``,
or at or below the smallest normal double (about 2.2e-308) when
``crout_tol`` is at least that large. NaN elements are skipped when finding
the largest absolute element. The ``crout_tol`` tolerance is set by
:func:`sysstate`, case 13. This scaling allows a well-conditioned matrix
with small elements, such as ``1e-15*eye(2)``, to have a nonzero
determinant.

:func:`detl` can be much faster in many applications.


.. seealso:: Functions :func:`detl`
