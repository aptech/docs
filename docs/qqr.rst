
qqr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X = Q_1R`

Format
----------------
.. function:: { q1, r } = qqr(x)

    :param x: data
    :type x: NxP matrix

    :return q1: unitary matrix, :math:`K = min(N, P)`.

    :rtype q1: NxK matrix

    :return r: upper triangular matrix

    :rtype r: KxP matrix

Remarks
-------

Given :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'x` is zero below its diagonal, i.e.,

.. math::

   Q′X = \begin{bmatrix}
        R \\
        0
        \end{bmatrix}

where :math:`R` is upper triangular. If we partition

.. math::

   Q⁢ = \begin{bmatrix}
        Q_1 &
        Q_2
        \end{bmatrix}

where :math:`Q_1` has :math:`P` columns, then

.. math::

   X⁢= Q_1⁢R

is the QR decomposition of :math:`X`. If :math:`X` has linearly independent columns, :math:`R`
is also the Cholesky factorization of the moment matrix of :math:`X`, i.e., of :math:`X'X`.

If you want only the :math:`R` matrix, see the function :func:`qr`. Not computing :math:`Q_1`
can produce significant improvements in computing time and memory usage.

An unpivoted :math:`R` matrix can also be generated using :func:`cholup`:

::

   r = cholup(zeros(cols(x), cols(x)), x);

For linear equation or least squares problems, which require :math:`Q_2` for
computing residuals and residual sums of squares, see :func:`olsqr` and :func:`qtyr`.

For most problems an explicit copy of :math:`Q_1` or :math:`Q_2` is not required.
Instead one of the following, :math:`Q'Y`, :math:`QY`, :math:`Q_1Y`, :math:`Q_1'Y`, :math:`Q_2Y`, or
:math:`Q_2'Y`, for some :math:`Y`, is required. These cases are all handled by :func:`qtyr`
and :func:`qyr`. These functions are available because :math:`Q` and :math:`Q_1` are typically
very large matrices while their products with :math:`Y` are more manageable.

If :math:`N < P`, the factorization assumes the form:

.. math::

    Q'X = \begin{bmatrix}
         R_1 &
         R_2
         \end{bmatrix}


where :math:`R_1` is a PxP upper triangular matrix and :math:`R_2` is :math:`P \times (N-P)`. Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R_1` and :math:`R_2`. This
type of factorization is useful for the solution of underdetermined
systems. However, unless the linearly independent columns happen to be
the initial rows, such an analysis also requires pivoting (see :func:`qre` and
:func:`qrep`).

Examples
--------

::

    // Create a 3x2 matrix
    x = { 1 2,
          3 4,
          5 6 };

    // Compute Q1 and R
    { q1, r } = qqr(x);

    print "Q1 (orthogonal factor):";
    print q1;
    print "R (upper triangular):";
    print r;

    // Verify that Q1*R reconstructs x
    print "Q1*R (should equal x):";
    print (q1 * r);

The above code produces the following output:

::

    Q1 (orthogonal factor):

     -0.16903085       0.89708523
     -0.50709255       0.27602622
     -0.84515425      -0.34503278

    R (upper triangular):

      -5.9160798       -7.4373574
       0.0000000       0.82807867

    Q1*R (should equal x):

       1.0000000        2.0000000
       3.0000000        4.0000000
       5.0000000        6.0000000

Source
------

qqr.src

.. seealso:: Functions :func:`qre`, :func:`qrep`, :func:`qtyr`, :func:`qtyre`, :func:`qtyrep`, :func:`qyr`, :func:`qyre`, :func:`qyrep`, :func:`olsqr`
