
diagmat
==============================================

Purpose
----------------
Creates a diagonal or off-diagonal matrix from a vector.

Format
----------------
.. function:: D = diagmat(v[, k])

    :param v: the diagonal elements.
    :type v: Nx1 or 1xN vector

    :param k: Optional, the diagonal offset. ``k > 0`` places *v* on the *k*-th superdiagonal, ``k < 0`` places *v* on the \|\ *k*\ \|-th subdiagonal. Default = 0.
    :type k: scalar

    :return D: with *v* on the specified diagonal and zeros elsewhere. When *k* = 0, the result is NxN. When *k* ≠ 0, the result is (N + \|\ *k*\ \|) x (N + \|\ *k*\ \|).

    :rtype D: matrix

Examples
----------------

Basic diagonal matrix
++++++++++++++++++++++++++++++++++++++++++++

::

    v = { 1, 2, 3 };

    D = diagmat(v);

After the above code, ``D`` will equal:

::

    1 0 0
    0 2 0
    0 0 3

Superdiagonal (k = 1)
++++++++++++++++++++++++++++++++++++++++++++

::

    v = { 1, 2, 3 };

    D = diagmat(v, 1);

After the above code, ``D`` will equal:

::

    0 1 0 0
    0 0 2 0
    0 0 0 3
    0 0 0 0

Subdiagonal (k = -1)
++++++++++++++++++++++++++++++++++++++++++++

::

    v = { 4, 5, 6 };

    D = diagmat(v, -1);

After the above code, ``D`` will equal:

::

    0 0 0 0
    4 0 0 0
    0 5 0 0
    0 0 6 0

Round-trip with diag
++++++++++++++++++++++++++++++++++++++++++++

::

    v = { 5, 10, 15 };

    // Create diagonal matrix, then extract diagonal
    D = diagmat(v);
    v2 = diag(D);

After the above code, ``v2`` will equal ``v``.

Remarks
-------

.. versionadded:: 26.0.1

:func:`diagmat` creates a new diagonal matrix. To extract the diagonal of an existing matrix, use :func:`diag`. To replace the diagonal of an existing matrix, use :func:`diagrv`.

Off-diagonal matrices are useful for building companion matrices, shift operators, and tridiagonal systems::

    // Build a tridiagonal matrix
    main  = { 2, 2, 2 };
    upper = { -1, -1 };
    lower = { -1, -1 };

    T = diagmat(main) + diagmat(upper, 1) + diagmat(lower, -1);

.. seealso:: Functions :func:`diag`, :func:`diagrv`, :func:`bandrv`, :func:`eye`
