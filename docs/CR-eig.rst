
eig
==============================================

Purpose
----------------

Computes the eigenvalues of a general matrix.

Format
----------------
.. function:: eig(A)

    :param A: 
    :type A: NxN matrix or K-dimensional array where
        the last two dimensions are NxN

    :returns: lambda (*Nx1 vector or K-dimensional array*) where the last two dimensions are Nx1, the
        eigenvalues of A.

Examples
----------------

::

    A = {  0.5  1.2  0.3, 
           0.6  0.9  0.2, 
           0.8  1.5  0.0 };
     
    lambda = eig(A);

After the above code, lambda will equal:

::

    1.8626           
    -0.1871           
    -0.2754

To calculate eigenvalues and eigenvectors see eigv. To calculate generalized eigenvalues and eigenvectors, see lapgeig, or lapgeigv.

Remarks
-------

If A is an array, the result will be an array containing the eigenvalues
of each 2-dimensional array described by the two trailing dimensions of
A. In other words, for a 10x4x4 array, the result will be a 10x4x1 array
containing the eigenvalues of each of the 10 4x4 arrays contained in A.

**Errors**

If the eigenvalues cannot all be determined, lambda[1] is set to an
error code. Passing lambda[1] to the scalerr function will return the
index of the eigenvalue that failed. The eigenvalues for indices
scalerr(lambda[1])+1 to N should be correct.

Error handling is controlled with the low bit of the trap flag.

+------------+------------------------------------------+
| **trap 0** | set lambda[1] and terminate with message |
+------------+------------------------------------------+
| **trap 1** | set lambda[1] and continue execution     |
+------------+------------------------------------------+

Invalid inputs, such as an infinity, missing value or Nan will cause an
error. If the **trap** is set to 1, lambda will be set to a scalar error
code and program execution will continue. Passing this scalar error code
to the scalerr function will return -1.

**Eigenvalue ordering**

The eigenvalues are unordered except that complex conjugate pairs of
eigenvalues will appear consecutively with the eigenvalue having the
positive imaginary part first.

.. seealso:: Functions :func:`eigh`, :func:`eighv`, :func:`eigv`

eigenvalue matrix eigen
