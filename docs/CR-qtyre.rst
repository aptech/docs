
qtyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X and returns :math:`Q'Y` and :math:`R`.


Format
----------------
.. function:: { qty, r, e } = qtyre(y, x)

    :param y: data
    :type y: NxL matrix

    :param x: data
    :type x: NxP matrix

    :return qty: unitary matrix

    :rtype qty: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :rtype r: KxP matrix

    :return e: permutation vector

    :rtype e: Px1 vector

Remarks
-------

Given :math:`X[., E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[., E]` is zero below
its diagonal, i.e.,

.. math::

    Q′X[ ., E ] = \begin{bmatrix}
        R \\
        0
        \end{bmatrix}

where :math:`R` is upper triangular. If we partition

.. math::

   Q⁢ = [Q_1\ Q_2⁢]

where :math:`Q_1` has :math:`P` columns, then

.. math::

  X[., E] = Q_1R

is the QR decomposition of :math:`X[., E]`.

If :math:`X` has rank :math:`P`, then the columns of :math:`X` will not be permuted. If :math:`X` has
rank :math:`M < P`, then the :math:`M` linearly independent columns are permuted to the
front of :math:`X` by :math:`E`. Partition the permuted :math:`X` in the following way:

.. math::

   X[.⁢, E] = [X1⁢  X2⁢]

where :math:`X_1` is NxM and :math:`X_2` is :math:`N \times (P-M)`. Further partition :math:`R` in the following way:

.. math::

    R = \begin{bmatrix}
      R_{11} & R_{12} \\
      0 & 0
      \end{bmatrix}

where :math:`R_{11}` is MxM and :math:`R_{12}` is :math:`M \times (P-M)`. Then

.. math::

    A = R_{11}^{-1}R_{12}

and

.. math::

    X_2 = X_1A

that is, :math:`A` is an :math:`M \times (P-N)` matrix defining the linear combinations of :math:`X_2`
with respect to :math:`X_1`.

For most problems :math:`Q` or :math:`Q_1` is not it is required. Rather, we require
:math:`Q'Y` or :math:`Q_1'Y` where :math:`Y` is an NxL matrix. Since :math:`Q` can be a very large
matrix, :func:`qtyre` has been provided for the calculation of :math:`Q'Y` which will be
a much smaller matrix. :math:`Q_1'Y` will be a submatrix of :math:`Q'Y`. In particular,

.. math::

    Q_1'Y = qty[1:P, .]

and :math:`Q_2'Y` is the remaining submatrix:

.. math::

    Q_2'Y = qty[P+1:N, .]

Suppose that :math:`X` is an NxK dataset of independent variables and :math:`Y` is an
Nx1 vector of dependent variables. Suppose further that :math:`X` contains
linearly dependent columns, i.e., :math:`X` has rank :math:`M < P`. Then define

.. math::

    C = Q_1'Y[1:M, .]\\
    A = R[1:M, 1:M]

and the vector (or matrix of :math:`L > 1`) of least squares coefficients of the
reduced, linearly independent problem is the solution of

.. math::

    Ab = C

To solve for *b* use :func:`qrsol`:

::

   b = qrsol(C, A);

If :math:`N < P`, the factorization assumes the form:

.. math::

    Q_1'X[.⁢, E] = [R_1 R_2]

where :math:`R_1` is a PxP upper triangular matrix and :math:`R_2` is :math:`P \times (N-P)`. Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R_1` and :math:`R_2`. This
type of factorization is useful for the solution of underdetermined systems. For the solution of

.. math::

    X[.⁢, E]b = Y

it can be shown that

::

   b = qrsol(Q'Y, R1)|zeros(N-P,1);

Source
------

qtyr.src

.. seealso:: Functions :func:`qqr`, :func:`qre`, :func:`qtyr`
