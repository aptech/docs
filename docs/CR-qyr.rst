
qyr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix :math:`X` and returns :math:`QY` and :math:`R`.

Format
----------------
.. function:: { qy, r } = qyr(y, x)

    :param y: data
    :type y: NxL matrix

    :param X: data
    :type X: NxP matrix

    :return qy: unitary matrix

    :rtype qy: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :rtype r: KxP matrix

.. DANGER:: fix equations

Remarks
-------

Given :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X` is zero below its diagonal, i.e.,

.. math::

where :math:`R` is upper triangular. If we partition

.. math::

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

is the QR decomposition of :math:`X`. If :math:`X` has linearly independent columns, :math:`R`
is also the Cholesky factorization of the moment matrix of :math:`X`, i.e., of :math:`X'X`.

For most problems :math:`Q` or :math:`Q\ 1` is not what is required. Since :math:`Q` can be a
very large matrix, :func:`qyr` has been provided for the calculation of :math:`QY`,
where :math:`Y` is some NxL matrix, which will be a much smaller matrix.

If either :math:`Q'Y` or :math:`Q\ 1'Y` are required, see :func:`qtyr`.

Source
------

qyr.src

.. seealso:: Functions :func:`qqr`, :func:`qyre`, :func:`qyrep`, :func:`olsqr`

