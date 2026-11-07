
spEigv
==============================================

Purpose
----------------

Computes a specified number of eigenvalues and eigenvectors of a square, sparse matrix *a*.

Format
----------------
.. function:: { va, ve } = spEigv(a, nev, which, tol, maxit, ncv)

    :param a: NxN square, real sparse matrix.
    :type a: sparse matrix

    :param nev: number of eigenvalues to compute, a whole number from 1 to N-2.
    :type nev: scalar

    :param which: which eigenvalues to compute, in upper or lower case:

        .. list-table::
            :widths: auto

            * - "LM"
              - Largest magnitude (the default; 0 also selects it).
            * - "SM"
              - Smallest magnitude.
            * - "LR"
              - Largest real part.
            * - "SR"
              - Smallest real part.
            * - "LI"
              - Largest imaginary part, in absolute value.
            * - "SI"
              - Smallest imaginary part, in absolute value.

    :type which: string

    :param tol: relative accuracy of the eigenvalues, 0 or more. Default input 0 sets *tol* to 1e-15.
    :type tol: scalar

    :param maxit: maximum number of Arnoldi restarts, a whole number of 0 or more. Default input 0 sets *maxit* to :math:`nev * N * 100`.
    :type maxit: scalar

    :param ncv: number of Arnoldi vectors, a whole number of 0 or more. Default input 0 sets *ncv* to the larger of :math:`2 * nev + 1` and 20, but no more than N. Other values are raised to at least the larger of :math:`nev + 2` and 20, and lowered to at most N. See Remarks.
    :type ncv: scalar

    :return va: the eigenvalues, sorted by *which*: by magnitude for ``"LM"`` and ``"SM"``, by real part for ``"LR"`` and ``"SR"``, and by the absolute value of the imaginary part for ``"LI"`` and ``"SI"``, the wanted eigenvalues first. The two eigenvalues of a complex conjugate pair are next to each other, the one with the positive imaginary part first.

    :rtype va: nevx1 complex vector

    :return ve: the eigenvectors; column *i* belongs to ``va[i]``.

    :rtype ve: Nxnev complex matrix

Examples
----------------

Largest eigenvalues
+++++++++++++++++++

::

    // Set random seed
    rndseed 3456;

    // Declare sparse matrix a
    sparse matrix a;

    // Create random matrix x
    x = 10*rndn(5, 5);

    // Convert x to a sparse matrix, dropping elements smaller than 4 in magnitude
    a = densetosp(x, 4);

    // The 2 eigenvalues of largest magnitude, with the default settings
    { va, ve } = spEigv(a, 2, "LM", 0, 0, 0);

The results are:

::

    va = 22.243033
         1.2721326 + 19.674188i

    ve = -0.41242526   -0.053404520 + 0.024343329i
         -0.52805398     0.14690080 - 0.25069356i
         -0.22729706     0.58688261 + 0.012127271i
          0.19822788    0.076225392 + 0.53603640i
          0.67831125     0.51827223 + 0.076148155i

The second eigenvalue is one of a complex conjugate pair; its conjugate, ``1.2721326 - 19.674188i``, would come next with ``nev = 3``.
The first eigenvalue times its eigenvector equals the matrix times the eigenvector:

::

    va[1]*ve[.,1]      a*ve[.,1]
     -9.1735886       -9.1735886
     -11.745522       -11.745522
     -5.0557761       -5.0557761
      4.4091892        4.4091892
      15.087699        15.087699

Smallest eigenvalues
++++++++++++++++++++

::

    // 1-D Laplacian: 2 on the diagonal, -1 beside it
    n = 10000;
    i = seqa(1, 1, n);
    j = seqa(1, 1, n-1);
    p = (2*ones(n, 1)~i~i) | (-ones(n-1, 1)~j~(j+1)) | (-ones(n-1, 1)~(j+1)~j);
    sparse matrix a;
    a = packedToSp(n, n, p);

    // The 3 eigenvalues of smallest magnitude
    { va, ve } = spEigv(a, 3, "SM", 0, 0, 0);

::

    va = 9.8676307e-08
         3.9470522e-07
         8.8808670e-07

These equal the exact eigenvalues, :math:`2 - 2\cos(k \pi / (n+1))` for *k* = 1, 2, 3.

When the eigenvalues do not converge
++++++++++++++++++++++++++++++++++++

::

    trap 1;
    { va, ve } = spEigv(a, 6, "SR", 1e-14, 1, 0);
    trap 0;

    if scalmiss(va);
        print "spEigv failed, error " scalerr(va);
    endif;

::

    spEigv failed, error 580.00000

Remarks
-------

- ``"SM"`` factors *a* once with a sparse LU factorization and then works with the inverse of *a*. This
  finds the smallest eigenvalues much faster than the other settings, and needs memory for the LU factors.
  If *a* is singular or nearly singular, as a graph Laplacian is, :func:`spEigv` checks the results and, when
  needed, searches again without the factorization. The results are just as accurate, but this can be much
  slower.

- If not all *nev* eigenvalues converge within *maxit* restarts, :func:`spEigv` stops with error G0580,
  or G0590 if none converged. Other failures of the eigensolver stop with an error too. Under ``trap 1``,
  *va* and *ve* are instead scalar error codes holding the error number; test them with :func:`scalmiss`
  and read the number with :func:`scalerr`. To get convergence, raise *maxit* or *ncv*, or loosen *tol*.

- *nev*, *maxit* and *ncv* must be whole numbers, *tol* must be 0 or more, and *which* must be one of the
  six settings. Otherwise :func:`spEigv` stops with an error, whatever the ``trap`` setting.

- The ideal setting for input *ncv* is problem dependent and cannot be easily predicted ahead of time.
  Increasing *ncv* increases the memory used, about :math:`8 * N * ncv` bytes, and often reduces the number of
  restarts. For a large, sparse matrix, *ncv* should be small compared to N.

- When *nev* falls between the two eigenvalues of a complex conjugate pair, only the first of them, the one
  with the positive imaginary part, is returned.

- :func:`spEigv` starts from the same vector on every call, so repeating a call normally gives the same results.

- Calls to :func:`spEigv` from different threads run one at a time.

Technical Notes
----------------

:func:`spEigv` uses the implicitly restarted Arnoldi method from the ARPACK library. For ``"SM"`` it uses
the shift-invert mode of ARPACK, with the LU factorization from SuperLU.

.. seealso:: Functions :func:`eig`, :func:`eigv`
