
eigv
==============================================

Purpose
----------------

Computes eigenvalues and eigenvectors of a general matrix.

Format
----------------
.. function:: { lambda, v } = eigv(x)

    :param x: data used to compute the eigenvalues and eigenvectors.
    :type x: NxN matrix or KxNxN array

    :return lambda: the eigenvalues of *x*.

    :rtype lambda: Nx1 vector or KxNx1 array

    :return v: the eigenvectors of *x*.

    :rtype v: NxN matrix or KxNxN array

Examples
----------------

::

    x = {  0.5  1.2  0.3,
           0.6  0.9  0.2,
           0.8  1.5  0.0 };

    { lambda, v } = eigv(x);

After the above code:

::

              1.8626          0.5044  -0.7122  -0.6152
    lambda = -0.1871     v =  0.4317   0.3520   0.1361
             -0.2754          0.5643   0.2234   1.0458

Remarks
-------

If *x* is an array, *lambda* will be an array containing the eigenvalues of
each 2-dimensional array described by the two trailing dimensions of *x*,
and *v* will be an array containing the corresponding eigenvectors. For example, if *x* is a 10x4x4 array, *lambda* will be a 10x4x1 array
containing the eigenvalues and *v* a 10x4x4 array containing the
eigenvectors of each of the 10 4x4 arrays contained in *x*.

**Errors**

If the eigenvalues cannot all be determined, *lambda[1]* is set to an
error code. Passing *lambda[1]* to the :func:`scalerr` function will return the
index of the eigenvalue that failed. The eigenvalues for indices
:code:`scalerr(lambda[1])+1` to :math:`N` should be correct. The eigenvectors are not
computed.

Error handling is controlled with the low bit of the `trap` flag.

+---------------------+-----------------------------------------------------+
| :code:`trap 0`      | set *lambda[1]* and terminate with message              |
+---------------------+-----------------------------------------------------+
| :code:`trap 1`      | set *lambda[1]* and continue execution                  |
+---------------------+-----------------------------------------------------+

Invalid inputs, such as an :math:`\infty`, missing value or Nan will cause an
error. If the `trap` is set to 1, *lambda* will be set to a scalar error
code and program execution will continue. Passing this scalar error code
to the :func:`scalerr` function will return -1.

**Eigenvalue ordering**

The eigenvalues are unordered except that complex conjugate pairs of
eigenvalues will appear consecutively with the eigenvalue having the
positive imaginary part first. The columns of *v* contain the eigenvectors
of *x* in the same order as the eigenvalues. The eigenvectors are not
normalized.

.. seealso:: Functions :func:`eig`, :func:`eigh`, :func:`eighv`
