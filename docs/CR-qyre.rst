
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

    :type qy: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :type r: KxP matrix

    :return e: permutation vector

    :type e: Px1 vector

.. DANGER:: fix equations

Remarks
-------

Given :math:`X[.,E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[.,E]` is zero below
its diagonal, i.e.,

.. math::

where :math:`R` is upper triangular. If we partition

.. math::

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

is the QR decomposition of :math:`X[.,E]`.

For most problems :math:`Q` or :math:`Q\ 1` is not what is required. Since :math:`Q` can be a
very large matrix, :func:`qyre` has been provided for the calculation of :math:`QY`,
where :math:`Y` is some NxL matrix, which will be a much smaller matrix.

If either :math:`Q'Y` or :math:`Q\ 1'Y` are required, see :func:`qtyre`.

If :math:`N < P`, the factorization assumes the form:

.. math::

where :math:`R\ 1` is a PxP upper triangular matrix and :math:`R\ 2` is Px(N-P). Thus :math:`Q`
is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R\ 1` and :math:`R\ 2`.

Source
------

qyr.src

.. seealso:: Functions :func:`qqr`, :func:`qre`, :func:`qyr`

