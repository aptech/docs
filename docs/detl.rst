
detl
==============================================

Purpose
----------------

Returns the determinant of the last matrix that was passed to one of the intrinsic matrix decomposition routines.

Format
----------------
.. function:: y = detl()

Examples
----------------
If both the inverse and the determinant of the
matrix are needed, the following two commands will
return both with the minimum amount of computation:

::

    xi = inv(x);
    xd = detl;

The function :func:`det(x)` returns the determinant of a
matrix using the Crout decomposition. If you only want the determinant of a positive definite matrix,
the following code will be the fastest for matrices larger than 10x10:

::

    /*
    ** The 'call' keyword tells GAUSS to ignore the values
    ** returned from chol
    */
    call chol(x);
    xd = detl;

The Cholesky decomposition is computed and the
result from that is discarded. The determinant
saved during that instruction is retrieved using
:func:`detl`. This can execute up to 2.5 times faster than
:func:`det(x)` for large positive definite matrices.

Remarks
-------

Whenever one of the intrinsic matrix decomposition routines is executed,
the determinant of the matrix is also computed and stored in a system
variable. This function will return the value of that determinant and,
because the value has been computed in a previous instruction, this will
require no computation.

The following functions will set the system variable used by :func:`detl`:

+-------------------------+-----------------------------------------------------+
| :code:`chol(x)`         |                                                     |
+-------------------------+-----------------------------------------------------+
| :code:`crout(x)`        |                                                     |
+-------------------------+-----------------------------------------------------+
| :code:`croutp(x)`       |                                                     |
+-------------------------+-----------------------------------------------------+
| :code:`det(x)`          |                                                     |
+-------------------------+-----------------------------------------------------+
| :code:`inv(x)`          |                                                     |
+-------------------------+-----------------------------------------------------+
| :code:`invpd(x)`        |                                                     |
+-------------------------+-----------------------------------------------------+
| :code:`solpd(y, x)`     | determinant of x                                    |
+-------------------------+-----------------------------------------------------+


.. seealso:: Functions :func:`det`, :func:`norm`
