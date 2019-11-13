
qr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X = Q_1R`

Format
----------------
.. function:: r = qr(x)

    :param x: data
    :type x: NxP matrix

    :return r: upper triangular matrix, :math:`K = min(N,P)`.

    :rtype r: KxP matrix

Remarks
-------

:func:`qr` is the same as :func:`qqr` but doesn't return the :math:`Q_1` matrix. If :math:`Q_1` is not
wanted, :func:`qr` will save a significant amount of time and memory usage, especially for large problems.

Given :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X` is zero below its diagonal, i.e.,

.. math::

   Q′X = \begin{bmatrix}
        R \\
        0
        \end{bmatrix}


where :math:`R` is upper triangular. If we partition

.. math::

   Q⁢ = [Q_1 Q_2⁢]

where :math:`Q_1` has :math:`P` columns, then

.. math::

   X⁢ = Q_1⁢R

is the QR decomposition of :math:`X`. If :math:`X` has linearly independent columns, :math:`R`
is also the Cholesky factorization of the moment matrix of :math:`X`, i.e., of :math:`X'X`.

:func:`qr` does not return the :math:`Q_1` matrix because in most cases it is not
required and can be very large. If you need the :math:`Q_1` matrix, see the
function :func:`qqr`. If you need the entire :math:`Q` matrix, call :func:`qyr` with :math:`Y` set to a
conformable identity matrix.

For most problems :math:`Q'Y`, :math:`Q_1'Y`, or :math:`QY`, :math:`Q_1Y`, for some :math:`Y`, are required.
For these cases see :func:`qtyr` and :func:`qyr`.

For linear equation or least squares problems, which require :math:`Q_2` for
computing residuals and residual sums of squares, see :func:`olsqr`.

If :math:`N < P`, the factorization assumes the form:

.. math::

    Q'X = [R_1 R_2]

where :math:`R_1` is a PxP upper triangular matrix and :math:`R_2` is :math:`P \times (N-P)`. Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R_1` and :math:`R_2`. This
type of factorization is useful for the solution of underdetermined
systems. However, unless the linearly independent columns happen to be
the initial rows, such an analysis also requires pivoting (see :func:`qre` and :func:`qrep`).

Source
------

qr.src

.. seealso:: Functions :func:`qqr`, :func:`qrep`, :func:`qtyre`
