
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

Source
------

qyr.src

.. seealso:: Functions :func:`qqr`, :func:`qre`, :func:`qyr`
