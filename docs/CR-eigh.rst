
eigh
==============================================

Purpose
----------------

Computes the eigenvalues of a complex hermitian or real symmetric matrix.

Format
----------------
.. function:: eigh(x)

    :param x: 
    :type x: NxN matrix or K-dimensional array where
        the last two dimensions are NxN

    :returns: va (*TODO*), Nx1 vector or K-dimensional array where
        the last two dimensions are Nx1, the eigenvalues of
        x.



Remarks
-------

If x is an array, the result will be an array containing the eigenvalues
of each 2-dimensional array described by the two trailing dimensions of
x. In other words, for a 10x4x4 array, the result will be a 10x4x1 array
containing the eigenvalues of each of the 10 4x4 arrays contained in x.

**Errors**
If the eigenvalues cannot all be determined, va[1] is set to an error
code. Passing va[1] to the scalerr function will return the index of the
eigenvalue that failed. The eigenvalues for indices 1 to
scalerr(va[1])-1 should be correct.

Error handling is controlled with the low bit of the trap flag.

+------------+--------------------------------------+
| **trap 0** | set va[1] and terminate with message |
+------------+--------------------------------------+
| **trap 1** | set va[1] and continue execution     |
+------------+--------------------------------------+

Invalid inputs, such as an infinity, missing value or Nan will cause an
error. If the **trap** is set to 1, va will be set to a scalar error
code and program execution will continue. Passing this scalar error code
to the scalerr function will return -1.

**Eigenvalue ordering**
The eigenvalues are in ascending order.

The eigenvalues of a complex hermitian or real symmetric matrix are
always real.

