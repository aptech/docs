
qre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X[.,E] = Q_1R`

Format
----------------
.. function:: { r, e } = qre(x)

    :param x: data
    :type x: NxP matrix

    :return r: :math:`K = min(N,P)`.

    :rtype r: KxP upper triangular matrix

    :return e: permutation vector

    :rtype e: Px1 vector

Remarks
-------

:func:`qre` is the same as :func:`qqre` but doesn't return the :math:`Q_1` matrix. If :math:`Q_1` is
not wanted, :func:`qre` will save a significant amount of time and memory usage, especially for large problems.

Given :math:`X[.,E]`, where :math:`E` is a permutation vector that permutes the columns
of *x*, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[.,E]` is zero below its diagonal, i.e.,

.. math::

   Q′X[.,E] = \begin{bmatrix}
        R \\
        0
        \end{bmatrix}

where :math:`R` is upper triangular. If we partition

.. math::

   Q⁢ = [Q_1 Q_2⁢]

where :math:`Q_1` has :math:`P` columns, then

.. math::

   X[.,E] = Q_1R

is the QR decomposition of :math:`X[.,E]`.

:func:`qre` does not return the :math:`Q_1` matrix because in most cases it is not
required and can be very large. If you need the :math:`Q_1` matrix, see the
function :func:`qqre`. If you need the entire :math:`Q` matrix, call :func:`qyre` with :math:`Y` set to
a conformable identity matrix. For most problems :math:`Q'Y`, :math:`Q_1'Y`, or :math:`QY`,
:math:`Q_1\ Y`, for some *y*, are required. For these cases see :func:`qtyre` and :func:`qyre`.

If :math:`X` has rank :math:`P`, then the columns of :math:`X` will not be permuted. If :math:`X` has
rank :math:`M < P`, then the :math:`M` linearly independent columns are permuted to the
front of :math:`X` by :math:`E`. Partition the permuted :math:`X` in the following way:

.. math::

    X[ ., E ] = \begin{bmatrix}
      X_1 & X_2
      \end{bmatrix}

where :math:`X_1` is NxM and :math:`X_2` is Nx(P-M). Further partition :math:`R` in the following way:

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


that is, :math:`A` is an Mx(P-N) matrix defining the linear combinations of :math:`X_2` with respect to :math:`X_1`

If :math:`N < P` the factorization assumes the form:

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

   b = qrsol(Q'Y, R1)|zeros(N-P,1);

The explicit formation here of :math:`Q`, which can be a very large matrix, can be avoided by using the function :func:`qtyre`.

For further discussion of QR factorizations see the remarks under :func:`qqr`.

Source
------

qr.src

.. seealso:: Functions :func:`qqr`, :func:`olsqr`
