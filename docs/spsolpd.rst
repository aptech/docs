
spSolPD
==============================================

Purpose
----------------
Solves a system of linear equations :math:`Ax = b` for a sparse, symmetric matrix *A*.

Format
----------------
.. function:: x = spSolPD(b, A)

    :param b: the right-hand side. Each column is solved separately.
    :type b: NxK dense or sparse matrix

    :param A: symmetric matrix. Only the upper triangle is used.
    :type A: NxN sparse matrix

    :return x: the solution of :math:`Ax = b`.

    :rtype x: NxK dense matrix

Examples
----------------

Solve a positive definite system
++++++++++++++++++++++++++++++++

::

    // A sparse, symmetric positive definite matrix
    x = {  4  -1   0   0   0,
          -1   4  -1   0   0,
           0  -1   4  -1   0,
           0   0  -1   4  -1,
           0   0   0  -1   4 };

    sparse matrix A;
    A = denseToSp(x, 0);

    b = { 1, 2, 3, 4, 5 };

    // Solve A*x = b
    x = spSolPD(b, A);

    print x;

The code above prints:

::

      0.49615385
      0.98461538
       1.4423077
       1.7846154
       1.6961538

Solve a symmetric system that is not positive definite
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    sparse matrix S;
    S = denseToSp({ 0 2, 2 1 }, 0);

    x = spSolPD({ 4, 5 }, S);

    print x;

The code above prints:

::

       1.5000000
       2.0000000

Remarks
-------

-  :func:`spSolPD` is the fastest way to solve a large sparse system when
   *A* is symmetric, for example a finite-element or grid matrix, a
   covariance or precision matrix, or the :math:`X'X` of a sparse design.
   Use :func:`spSolPD` rather than ``b/A`` for such systems: ``b/A`` uses a
   general sparse LU solver, which can be very slow and use a lot of memory
   on large symmetric systems. On normal equations with 210,000 unknowns,
   ``b/A`` did not finish in 20 minutes and used more than 8.5 GB of memory,
   while :func:`spSolPD` took 0.6 seconds.

-  If *A* is banded and positive definite, for example the precision matrix
   of a state-space or trend model, :func:`bandchol` and :func:`bandcholsol`
   are much faster still. They take *A* in compact band form, which
   :func:`band` makes from a dense matrix.

-  *A* does not have to be positive definite. If it is not, the solve
   switches to a factorization that handles symmetric indefinite matrices,
   for example a saddle-point (KKT) system. Positive definite matrices are
   the fastest case.

-  Only the upper triangle of *A*, including the diagonal, is used. The
   lower triangle is not checked: a non-symmetric *A* is solved as the
   symmetric matrix that has the same upper triangle.

-  *b* can have more than one column. :func:`spSolPD` factors *A* once and
   solves for every column.

-  If *A* or *b* is complex, the system is solved with the general sparse
   solver that ``b/A`` uses.

-  Large systems are solved in parallel, using as many threads as the
   GAUSS matrix functions use. Small systems are solved on one thread.

-  :func:`spSolPD` stops with an error if:

   -  *A* is singular, including a row or column of zeros (``G0048``);
   -  the upper triangle of *A*, or *b*, contains a missing value, ``NaN``
      or ``INF`` (``G0674``);
   -  *b* does not have the same number of rows as *A*, or *A* is not
      square (``G0520``);
   -  *A* is not a sparse matrix (``G0587``).

Technical Notes
----------------

:func:`spSolPD` orders *A* with an approximate minimum degree ordering
to reduce fill-in, then computes a supernodal Cholesky factorization. If
*A* is not positive definite, it uses a Bunch-Kaufman :math:`LBL^{T}`
factorization and, if that is not accurate enough, an LU factorization
with partial pivoting. The solution is refined iteratively until its
backward error is at the level of machine precision, with up to two
refinement steps.

.. seealso:: Functions :func:`spChol`, :func:`spLDL`, :func:`spLU`, :func:`solpd`, :func:`bandchol`, :func:`bandcholsol`
