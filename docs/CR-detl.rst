
detl
==============================================

Purpose
----------------

Returns the determinant of the last matrix that was passed to one of the intrinsic matrix decomposition routines.

Format
----------------
.. function:: detl

Remarks
-------

Whenever one of the intrinsic matrix decomposition routines is executed,
the determinant of the matrix is also computed and stored in a system
variable. This function will return the value of that determinant and,
because the value has been computed in a previous instruction, this will
require no computation.

The following functions will set the system variable used by detl:

+-----------------+-----------------------------------------------------+
| chol(x)         |                                                     |
+-----------------+-----------------------------------------------------+
| crout(x)        |                                                     |
+-----------------+-----------------------------------------------------+
| croutp(x)       |                                                     |
+-----------------+-----------------------------------------------------+
| det(x)          |                                                     |
+-----------------+-----------------------------------------------------+
| inv(x)          |                                                     |
+-----------------+-----------------------------------------------------+
| invpd(x)        |                                                     |
+-----------------+-----------------------------------------------------+
| solpd(y, x)     | determinant of x                                    |
+-----------------+-----------------------------------------------------+


Examples
----------------
If both the inverse and the determinant of the
matrix are needed, the following two commands will
return both with the minimum amount of computation:

::

    xi = inv(x);
    xd = detl;

The function det(x) returns the determinant of a
matrix using the Crout decomposition. If you only want the determinant of a positive definite matrix,
the following code will be the fastest for matrices larger than 10x10:

::

    //The 'call' keyword tells GAUSS to ignore the values
    //returned from chol
    call chol(x);
    xd = detl;

The Cholesky decomposition is computed and the
result from that is discarded. The determinant
saved during that instruction is retrieved using
detl. This can execute up to 2.5 times faster than
det(x) for large positive definite matrices.

.. seealso:: Functions :func:`det`, :func:`norm`

determinant matrix det decomposed
