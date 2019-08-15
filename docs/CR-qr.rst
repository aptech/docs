
qr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X = Q1R`

.. DANGER:: fix equations

Format
----------------
.. function:: r = qr(x)

    :param x: data
    :type x: NxP matrix

    :return r: :math:`K = min(N,P)`.

    :rtype r: KxP upper triangular matrix

Remarks
-------

:func:`qr` is the same as :func:`qqr` but doesn't return the :math:`Q\ 1` matrix. If :math:`Q\ 1` is not
wanted, :func:`qr` will save a significant amount of time and memory usage, especially for large problems.

Given :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X` is zero below its diagonal, i.e.,

.. math::

where :math:`R` is upper triangular. If we partition

.. math::

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

is the QR decomposition of :math:`X`. If :math:`X` has linearly independent columns, :math:`R`
is also the Cholesky factorization of the moment matrix of :math:`X`, i.e., of :math:`X'X`.

:func:`qr` does not return the :math:`Q\ 1` matrix because in most cases it is not
required and can be very large. If you need the :math:`Q\ 1` matrix, see the
function :func:`qqr`. If you need the entire :math:`Q` matrix, call :func:`qyr` with :math:`Y` set to a
conformable identity matrix.

For most problems :math:`Q'Y`, :math:`Q\ 1'Y`, or :math:`QY`, :math:`Q\ 1\ Y`, for some :math:`Y`, are required.
For these cases see :func:`qtyr` and :func:`qyr`.

For linear equation or least squares problems, which require :math:`Q\ 2` for
computing residuals and residual sums of squares, see :func:`olsqr`.

If :math:`N < P`, the factorization assumes the form:

.. math::

where :math:`R\ 1` is a PxP upper triangular matrix and :math:`R\ 2` is Px(N-P). Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R\ 1` and :math:`R\ 2`. This
type of factorization is useful for the solution of underdetermined
systems. However, unless the linearly independent columns happen to be
the initial rows, such an analysis also requires pivoting (see :func:`qre` and :func:`qrep`).

Source
------

qr.src

.. seealso:: Functions :func:`qqr`, :func:`qrep`, :func:`qtyre`

