
qqre
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X[ .,E ] = Q_1R`

Format
----------------
.. function:: { q1, r, e } = qqre(x)

    :param x: data
    :type x: NxP matrix

    :return q1: unitary matrix, :math:`K = min(N, P)`.

    :rtype q1: NxK matrix

    :return r: upper triangular matrix

    :rtype r: KxP matrix

    :return e: permutation vector

    :rtype e: Px1 vector

Remarks
-------

Given :math:`X[., E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[., E]` is zero below
its diagonal, i.e.,

.. math::

    Q′R[ ., E ] = \begin{bmatrix}
        R \\
        0
        \end{bmatrix}

where :math:`R` is upper triangular. If we partition

.. math::

   Q⁢ = [Q_1 Q_2⁢]

where :math:`Q_1` has :math:`P` columns, then

.. math::

  X[ ., E ] = Q_1R

is the QR decomposition of :math:`X[., E]`.

If you want only the :math:`R` matrix, see :func:`qre`. Not computing :math:`Q_1` can produce
significant improvements in computing time and memory usage.

If :math:`X` has rank :math:`P`, then the columns of :math:`X` will not be permuted. If :math:`X` has
rank :math:`M < P`, then the :math:`M` linearly independent columns are permuted to the
front of :math:`X` by :math:`E`. Partition the permuted :math:`X` in the following way:

.. math::

    X[ ., E ] = \begin{bmatrix}
      X_1 & X_2
      \end{bmatrix}

where :math:`X` is NxM and :math:`X_2` is :math:`N \times (P-M)`. Further partition :math:`R` in the following
way:

.. math::

    R = \begin{bmatrix}
      R_{11} & R_{12} \\
      0 & 0
      \end{bmatrix}

where :math:`R_{11}` is MxM and :math:`R_{12}` is Mx(P-M). Then

.. math::

    A = R_{11}^{-1}R_{12}

and

.. math::

    X_2 = X_1A

that is, :math:`A` is an :math:`M \times (P-N)` matrix defining the linear combinations of :math:`X_2` with respect to :math:`X_1`.

If :math:`N < P`, the factorization assumes the form:

.. math::

  Q'X = \begin{bmatrix}
    R_1 & R_2
    \end{bmatrix}

where :math:`R_1` is a PxP upper triangular matrix and :math:`R_2` is Px(N-P). Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R_1` and :math:`R_2`. This
type of factorization is useful for the solution of underdetermined systems. For the solution of

.. math::

    X[ ., E ]b = Y

it can be shown that

::

    b = qrsol(Q'Y, R1)|zeros(N-P, 1);

The explicit formation here of :math:`Q`, which can be a very large matrix, can
be avoided by using the function :func:`qtyre`.

For further discussion of QR factorizations see the remarks under :func:`qqr`.

Source
------

qqr.src

.. seealso:: Functions :func:`qtyre`, :func:`olsqr`, :func:`qqre`
