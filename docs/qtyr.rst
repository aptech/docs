
qtyr
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix :math:`X` and returns :math:`Q'Y` and :math:`R`.

Format
----------------
.. function:: { qty, r } = qtyr(y, X)

    :param y: data
    :type y: NxL matrix

    :param X: data
    :type X: NxP matrix

    :return qty: unitary matrix

    :rtype qty: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :rtype r: KxP matrix

Examples
----------------
The QR algorithm is the numerically superior method for the solution of least squares problems:

::

    loadm x, y;
    { qty, r } = qtyr(y, x);
    q1ty = qty[1:rows(r), .];
    q2ty = qty[rows(r)+1:rows(qty), .];

    // LS coefficients
    b = qrsol(q1ty, r);

    // Residual sums of squares
    s2 = sumc(q2ty^2);

Remarks
-------

Given :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X` is zero below its
diagonal, i.e.,

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

  X = Q_1R

is the QR decomposition of :math:`X`. If :math:`X` has linearly independent columns, :math:`R`
is also the Cholesky factorization of the moment matrix of :math:`X`, i.e., of
:math:`X'X`. For most problems :math:`Q` or :math:`Q_1` is not what is required. Rather, we
require :math:`Q'Y` or :math:`Q_1'Y` where :math:`Y` is an NxL matrix (if either :math:`QY` or :math:`Q_1Y`
are required, see :func:`qyr`). Since :math:`Q` can be a very large matrix, :func:`qtyr` has
been provided for the calculation of :math:`Q'Y` which will be a much smaller
matrix. :math:`Q_1'Y` will be a submatrix of :math:`Q'Y`. In particular,

.. math::

   G = Q_1'Y = \text{qty}[1:P, .]

and :math:`Q_2'Y` is the remaining submatrix:

.. math::

   H⁢ = Q_2'Y = \text{qty}[P+1:N, .]

Suppose that :math:`X` is an NxK dataset of independent variables, and :math:`Y` is an
Nx1 vector of dependent variables. Then it can be shown that

.. math::

   b = R^{-1}G

and

.. math::

   s_j= \sum_{i=1}^{N−P}⁢H_{i,j}\\
   ⁢j = 1,2,...L

where *b* is a PxL matrix of least squares coefficients and *s* is a 1xL
vector of residual sums of squares. Rather than invert :math:`R` directly,
however, it is better to apply :func:`qrsol` to

.. math::

   Rb⁢= Q_1′Y

For rank deficient least squares problems, see :func:`qtyre` and :func:`qtyrep`.

Source
------

qtyr.src

.. seealso:: Functions :func:`qqr`, :func:`qtyre`, :func:`qtyrep`, :func:`olsqr`
