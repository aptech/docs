
lusol
==============================================

Purpose
----------------

Computes the solution of :math:`LUx = b` where *L* is a lower triangular
 matrix and *U* is an upper triangular matrix.

Format
----------------
.. function:: x = lusol(b, L, U)

    :param b: data
    :type b: PxK matrix

    :param L: lower triangular matrix
    :type L: PxP matrix

    :param U: upper triangular matrix
    :type U: PxP matrix

    :return x: solution of LUx = b.

    :rtype x: PxK matrix

Examples
--------------

::

    A = { 3 -1 5,
          -2 0 5,
          7 2 -2};

    b = { 6 -4,
          3 2,
          7 -5};

    // Lower decomposition
    {l, u } = lu(A);

    // Solve system of equations
    X = lusol(b, l, u);

::

    x =   0.87654  -1.00000
          1.38272   1.00000
          0.95062   0.00000

Remarks
-------

If *b* has more than one column, each column is solved for separately,
i.e., :func:`lusol` solves :math:`LUx[., i] = b[., i]`.
