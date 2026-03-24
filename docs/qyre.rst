
qyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix *x* and returns :math:`QY` and :math:`R`.

Format
----------------
.. function:: { qy, r, e } = qyre(y, x)

    :param y: data
    :type y: NxL matrix

    :param x: data
    :type x: NxP matrix

    :return qy: unitary matrix

    :rtype qy: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :rtype r: KxP matrix

    :return e: permutation vector

    :rtype e: Px1 vector


Remarks
-------

Given :math:`X[.,E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[.,E]` is zero below
its diagonal, i.e.,

.. math::

    Q′R[ ., E ] = \begin{bmatrix}
        R \\
        0
        \end{bmatrix}

where :math:`R` is upper triangular. If we partition

.. math::

      Q = [Q_1 Q_2]

where :math:`Q_1` has :math:`P` columns, then

.. math::

    X[ ., E ] = Q_1R

is the QR decomposition of :math:`X[., E]`.

For most problems :math:`Q` or :math:`Q_1` is not what is required. Since :math:`Q` can be a
very large matrix, :func:`qyre` has been provided for the calculation of :math:`QY`,
where :math:`Y` is some NxL matrix, which will be a much smaller matrix.

If either :math:`Q'Y` or :math:`Q_1'Y` are required, see :func:`qtyre`.

If :math:`N < P`, the factorization assumes the form:

.. math::

    Q′R[ ., E ] = [R_1 R_2]

where :math:`R_1` is a PxP upper triangular matrix and :math:`R_2` is :math:`P \times (N-P)``. Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R_1` and :math:`R_2`.

Examples
--------

::

    // Create a 3x2 matrix
    x = { 1 2,
          3 4,
          5 6 };

    // Set Y to identity to recover the full Q matrix
    y = eye(3);

    // Compute Q*Y, R, and permutation vector E
    { qy, r, e } = qyre(y, x);

    print "Q (full orthogonal matrix):";
    print qy;
    print "R (upper triangular):";
    print r;
    print "Permutation vector E:";
    print e;

The above code produces the following output:

::

    Q (full orthogonal matrix):

     -0.26726124       0.87287156       0.40824829
     -0.53452248       0.21821789      -0.81649658
     -0.80178373      -0.43643578       0.40824829

    R (upper triangular):

      -7.4833148       -5.8797473
       0.0000000      -0.65465367

    Permutation vector E:

       2.0000000
       1.0000000

Source
------

qyr.src

.. seealso:: Functions :func:`qqr`, :func:`qre`, :func:`qyr`
