
hess
==============================================

Purpose
----------------

Computes the Hessenberg form of a square matrix.

Format
----------------
.. function:: { H, Z } = hess(A)

    :param A: data
    :type A: KxK real or complex matrix

    :returns: **H** (*KxK matrix*) - Hessenberg form.

    :returns: **Z** (*KxK matrix*) - transformation matrix.

Remarks
-------

:func:`hess` computes the Hessenberg form of a square matrix. The Hessenberg
form is an intermediate step in computing eigenvalues. It also is useful
for solving certain matrix equations that occur in control theory (see
*Van Loan, Charles F. "Using the Hessenberg Decomposition in Control
Theory". Algorithms* and *Theory in Filtering and Control. Sorenson, D.C.
and R.J. Wets, eds., Mathematical Programming Study No. 18, North
Holland, Amsterdam, 1982, 102-111*).

*Z* is an orthogonal matrix that transforms *A* into *H* and vice versa. Thus:

::

   H = Z'*A*Z

and since *Z* is orthogonal,

::

   A = Z*H*Z'

*A* is reduced to upper Hessenberg form using orthogonal similiarity
transformations. This preserves the Frobenious norm of the matrix and
the condition numbers of the eigenvalues.

Examples
----------------

::

    A = { 0.5 0.2 0.33,
          1.4 0.5 0.6,
          0.7 1.2 0.9 };

    { H, Z } = hess(A);

After the code above:

::

    H =  0.500   -0.326    0.206     Z = 1.000    0.000    0.000
        -1.565    1.300   -0.400         0.000   -0.894   -0.447
         0.000   -1.000    0.100         0.000   -0.447    0.894

.. seealso:: Functions :func:`eig`, :func:`qz`, :func:`schur`
