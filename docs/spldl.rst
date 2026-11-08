
spLDL
==============================================

Purpose
----------------
Computes the :math:`LDL^{T}` decomposition of a symmetric sparse matrix *A*, optionally after
reordering its rows and columns to keep *L* sparse.

Format
----------------
.. function:: { l, d } = spLDL(a)
              { l, d, p } = spLDL(a, order)

    :param a: symmetric matrix. Only the lower triangle is used.
    :type a: NxN sparse matrix

    :param order: Optional. How to order the rows and columns of *a* before factoring.

        .. list-table::
            :widths: auto

            * - "amd"
              - Approximate minimum degree: reorder to reduce the number of nonzeros in *l*. Recommended for large matrices.
            * - "natural"
              - No reordering: :math:`l d l^{T} = a` and *p* is 1, 2, ..., N.

        Without *order*, *a* is factored in its own order and *p* is not returned.

    :type order: string

    :return l: unit lower-triangular matrix with :math:`l d l^{T} = a`, or :math:`l d l^{T} = a[p,p]` when *order* is given.

    :rtype l: NxN sparse matrix

    :return d: diagonal matrix.

    :rtype d: NxN sparse matrix

    :return p: the permutation: :math:`l d l^{T} = a[p,p]`. Returned only when *order* is given.

    :rtype p: Nx1 vector

Examples
----------------

::

    declare sparse matrix a, l, d;

    nz = { 142 13 56 57 0,
            13  0  0  0 0,
            56  0 94 47 0,
            57  0 47 35 0,
             0  0  0  0 0 };

    a = densetosp(nz, 0);

    { l, d } = spLDL(a);

    print spDenseSubmat(l, 0, 0);
    print diag(spDenseSubmat(d, 0, 0));

::

       1.0000000        0.0000000        0.0000000        0.0000000        0.0000000
     0.091549296        1.0000000        0.0000000        0.0000000        0.0000000
      0.39436620        4.3076923        1.0000000        0.0000000        0.0000000
      0.40140845        4.3846154       0.50000000        1.0000000        0.0000000
       0.0000000        0.0000000        0.0000000        0.0000000        0.0000000

       142.00000
      -1.1901408
       94.000000
       11.500000
       0.0000000

The last row and column of *a* have no entries, so the last column of *l* is empty and the last element of *d* is 0.

Remarks
-------

- :func:`spLDL` does not pivot. It factors symmetric indefinite matrices, with negative
  elements in *d*, as long as no pivot is exactly zero in the order used. A zero pivot
  stops with error G0062, "Zero pivot encountered". With ``trap 1``, it returns error code
  10 instead, as :func:`chol` does: *l* and *d* are 1x1 sparse matrices and *p* a scalar,
  and :func:`scalerr` returns 10 for each.
- ``order="amd"`` can meet a zero pivot that the matrix's own order does not: for the
  matrix in the example, it eliminates the second row, whose diagonal is 0, first. To
  solve a symmetric indefinite system, use :func:`spSolPD`, which pivots.
- For large matrices, use ``order="amd"``. In the matrix's own order, *l* can have far more
  nonzeros than *a*, which takes more memory and time.
- A row and column of *a* with no stored entries gives an empty column in *l* (with no 1 on
  the diagonal) and a 0 in *d*. With ``order="amd"`` those rows come last in *p*.
- :func:`spLDL` does not check that *a* is symmetric. It uses only the lower triangle.

.. versionchanged:: 27.0
   Added the *order* argument and the *p* return. A zero pivot now stops with error
   G0062 (or returns error code 10 under ``trap 1``); before, *l* and *d* held infinite
   values.

Technical Notes
----------------

``order="amd"`` uses the approximate minimum degree ordering of Amestoy, Davis and Duff
(1996), *An approximate minimum degree ordering algorithm*, SIAM Journal on Matrix
Analysis and Applications 17(4).

.. seealso:: Functions :func:`spChol`, :func:`spSolPD`, :func:`spLU`
