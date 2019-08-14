
qyrep
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix :math:`X` using a pivot vector and returns :math:`QY` and :math:`R`.

Format
----------------
.. function:: { qy, r, e } = qyrep(y, x, pvt)

    :param y: data
    :type y: NxL matrix

    :param x: data
    :type x: NxP matrix

    :param pvt: controls the selection of the pivot columns:

        .. csv-table::
            :widths: auto
    
            "if :math:`pvt[i] > 0`, :math:`x[i]` is an initial column."
            "if :math:`pvt[i] = 0`, :math:`x[i]` is a free column."
            "if :math:`pvt[i] < 0`, :math:`x[i]` is a final column."
    
        The initial columns are placed at the beginning of the matrix and the final columns are placed at the end. Only the free columns will be moved during the decomposition.

    :type pvt: Px1 vector

    :return qy: unitary matrix

    :type qy: NxL matrix

    :return r: upper triangular matrix, :math:`K = min(N,P)`.

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

:func:`qyrep` allows you to control the pivoting. For example, suppose that :math:`X` is
a data set with a column of ones in the first column. If there are
linear dependencies among the columns of :math:`X`, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using *pvt*.

For most problems :math:`Q` or :math:`Q\ 1` is not what is required. Since :math:`Q` can be a
very large matrix, :func:`qyrep` has been provided for the calculation of :math:`QY`,
where :math:`Y` is some NxL matrix, which will be a much smaller matrix.

If either :math:`Q'Y` or :math:`Q\ 1'Y` are required, see :func:`qtyrep`.

If :math:`N < P`, the factorization assumes the form:

.. math::

where :math:`R\ 1` is a PxP upper triangular matrix and :math:`R\ 2` is
Px(N-P). Thus :math:`Q` is a PxP matrix and :math:`R` is a PxN matrix containing :math:`R\ 1` and :math:`R\ 2`.

Source
------

qyr.src

.. seealso:: Functions :func:`qr`, :func:`qqrep`, :func:`qrep`, :func:`qtyrep`

