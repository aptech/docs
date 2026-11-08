
spChol
==============================================

Purpose
----------------
Computes the Cholesky factorization :math:`LL^{T}` of a sparse, symmetric, positive definite matrix *A*,
optionally after reordering its rows and columns to keep *L* sparse.

Format
----------------
.. function:: L = spChol(a)
              { L, p } = spChol(a, order)

    :param a: symmetric, positive definite matrix. Only the lower triangle is used.
    :type a: NxN sparse matrix

    :param order: Optional. How to order the rows and columns of *a* before factoring.

        .. list-table::
            :widths: auto

            * - "amd"
              - Approximate minimum degree: reorder to reduce the number of nonzeros in *L*. Recommended for large matrices.
            * - "natural"
              - No reordering: :math:`LL^{T} = a` and *p* is 1, 2, ..., N.

        Without *order*, *a* is factored in its own order and *p* is not returned.

    :type order: string

    :return L: lower-triangular matrix with :math:`LL^{T} = a`, or :math:`LL^{T} = a[p,p]` when *order* is given.

    :rtype L: NxN sparse matrix

    :return p: the permutation: :math:`LL^{T} = a[p,p]`. Returned only when *order* is given.

    :rtype p: Nx1 vector

Examples
----------------

Factor a small matrix
++++++++++++++++++++++++++++++++

::

    sparse matrix A;
    sparse matrix L;

    // Create a small, simple positive-definite matrix
    x = { 9.53984224e+001 -5.84272701e+000 1.99970335e+001,
         -5.84272701e+000  1.09765831e+002 2.52038945e+000,
          1.99970335e+001  2.52038945e+000 4.71834812e+000 };

    // Create the sparse matrix A from x, keeping all elements
    A = denseToSp(x, 0);

    // Create matrix factorization
    L = spChol(A);

    print spDenseSubmat(L, 0, 0);

::

       9.7672116        0.0000000        0.0000000
     -0.59819806        10.459827        0.0000000
       2.0473636       0.35804782       0.63123068

Factor a large matrix with order="amd"
+++++++++++++++++++++++++++++++++++++++

::

    // 2-D Laplacian on a 300 x 300 grid: 90,000 rows, 5 nonzeros per row
    g = 300;
    n = g*g;
    i = seqa(1, 1, n);
    right = selif(i, (i % g) ./= 0);
    down = selif(i, i .<= n - g);
    r = i | right | (right + 1) | down | (down + g);
    c = i | (right + 1) | right | (down + g) | down;
    v = 4*ones(n, 1) | -ones(2*rows(right) + 2*rows(down), 1);

    sparse matrix A;
    sparse matrix L;
    A = spCreate(n, n, v, r, c);

    { L, p } = spChol(A, order="amd");

    // The log determinant of A from the diagonal of L
    { lv, lr, lc } = spGetNZE(L);
    print "nonzeros in L: " spNumNZE(L);
    print "log determinant: " 2*sumc(ln(selif(lv, lr .== lc)));

::

    nonzeros in L:        2928059.0
    log determinant:        105130.00

Without ``order="amd"``, *L* for this matrix has 27 million nonzeros instead of 2.9 million.

Remarks
-------

- For large matrices, use ``order="amd"``. In the matrix's own order, *L* can have
  far more nonzeros than *a*, which takes more memory and time.
- To solve :math:`Ax = b`, use :func:`spSolPD`, which orders, factors and solves in one call.
- If *a* is banded, for example the precision matrix of a state-space or trend model,
  :func:`bandchol` (and :func:`bandcholsol` to solve) is much faster. It takes the matrix
  in compact band form, which :func:`band` makes from a dense matrix.
- If *a* is not positive definite, :func:`spChol` stops with error G0121, "Matrix not
  positive definite". With ``trap 1``, it returns error code 10 instead, as :func:`chol`
  does: *L* is a 1x1 sparse matrix and *p* a scalar, and :func:`scalerr` returns 10 for
  either.
- A row and column of *a* with no stored entries gives an empty column in *L*, so
  :func:`spChol` also factors a positive semidefinite *a* whose zero rows have no
  stored entries. With ``order="amd"`` those rows come last in *p*.
- :func:`spChol` does not check that *a* is symmetric. It uses only the lower triangle.

.. versionchanged:: 27.0
   Added the *order* argument and the *p* return. A matrix that is not positive
   definite now stops with error G0121 (or returns error code 10 under ``trap 1``);
   before, *L* held invalid values.

Technical Notes
----------------

``order="amd"`` uses the approximate minimum degree ordering of Amestoy, Davis and Duff
(1996), *An approximate minimum degree ordering algorithm*, SIAM Journal on Matrix
Analysis and Applications 17(4).

.. seealso:: Functions :func:`spLDL`, :func:`spSolPD`, :func:`chol`, :func:`spLU`, :func:`bandchol`
