
qqr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X = Q1R`

.. DANGER:: fix all equations

Format
----------------
.. function:: { q1, r } = qqr(x)

    :param x: data
    :type x: NxP matrix

    :return q1: :math:`K = min(N,P)`.

    :type q1: NxK unitary matrix

    :return r: 

    :type r: KxP upper triangular matrix

Remarks
-------

Given :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'x` is zero below its diagonal, i.e.,

.. math::

   Q′X=[R0]

where :math:`R` is upper triangular. If we partition

.. math::

   Q⁢ = [ Q1Q2⁢]

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

   X⁢= Q1⁢ R

is the QR decomposition of :math:`X`. If :math:`X` has linearly independent columns, :math:`R`
is also the Cholesky factorization of the moment matrix of :math:`X`, i.e., of :math:`X'X`.

If you want only the :math:`R` matrix, see the function qr. Not computing :math:`Q\ 1`
can produce significant improvements in computing time and memory usage.

An unpivoted :math:`R` matrix can also be generated using :func:`cholup`:

::

   r = cholup(zeros(cols(x), cols(x)), x);

For linear equation or least squares problems, which require :math:`Q\ 2` for
computing residuals and residual sums of squares, see :func:`olsqr` and :func:`qtyr`.

For most problems an explicit copy of :math:`Q\ 1` or :math:`Q\ 2` is not required.
Instead one of the following, :math:`Q'Y`, :math:`QY`, :math:`Q\ 1'Y`, :math:`Q\ 1\ Y`, :math:`Q\ 2'Y`, or
:math:`Q\ 2\ Y`, for some :math:`Y`, is required. These cases are all handled by :func:`qtyr`
and :func:`qyr`. These functions are available because :math:`Q` and :math:`Q\ 1` are typically
very large matrices while their products with :math:`Y` are more manageable.

If :math:`N < P`, the factorization assumes the form:

.. math::

    Q'X = [R\ 1 | R\ 2]

where :math:`R\ 1` is a PxP upper triangular matrix and :math:`R\ 2` is :math:`Px(N-P)`. Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R\ 1` and :math:`R\ 2`. This
type of factorization is useful for the solution of underdetermined
systems. However, unless the linearly independent columns happen to be
the initial rows, such an analysis also requires pivoting (see :func:`qre` and
:func:`qrep`).

Source
------

qqr.src

.. seealso:: Functions :func:`qre`, :func:`qrep`, :func:`qtyr`, :func:`qtyre`, :func:`qtyrep`, :func:`qyr`, :func:`qyre`, :func:`qyrep`, :func:`olsqr`

