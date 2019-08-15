
eigh
==============================================

Purpose
----------------

Computes the eigenvalues of a complex hermitian or real symmetric matrix.

Format
----------------
.. function:: va = eigh(x)

    :param x: data used to compute the eigenvalues.
    :type x: NxN matrix or KxNxN array

    :return va: the eigenvalues of *x*.

    :rtype va: Nx1 vector or KxNx1 array

Remarks
-------

If *x* is an array, *va* will be an array containing the eigenvalues
of each 2-dimensional array described by the two trailing dimensions of
*x*. For example, if *x* is a 10x4x4 array, *va* will be a 10x4x1 array
containing the eigenvalues of each of the 10 4x4 arrays contained in *x*.

**Errors**

If the eigenvalues cannot all be determined, *va[1]* is set to an error
code. Passing *va[1]* to the :func:`scalerr` function will return the index of the
eigenvalue that failed. The eigenvalues for indices :math:`1 \to scalerr(va[1])-1` should be correct.

Error handling is controlled with the low bit of the `trap` flag.

+----------------+----------------------------------------------+
| :code:`trap 0` | set *va[1]* and terminate with message       |
+----------------+----------------------------------------------+
| :code:`trap 1` | set *va[1]* and continue execution           |
+----------------+----------------------------------------------+

Invalid inputs, such as an :math:`\infty`, missing value or NaN will cause an
error. If the `trap` is set to 1, *va* will be set to a scalar error
code and program execution will continue. Passing this scalar error code
to the :func:`scalerr` function will return -1.

**Eigenvalue ordering**

The eigenvalues are in ascending order.

The eigenvalues of a complex hermitian or real symmetric matrix are
always real.

.. seealso:: Functions :func:`eig`, :func:`eighv`, :func:`eigv`
