
qqrep
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X[., E] = Q_1R`

Format
----------------
.. function:: { q1, r, e } = qqrep(x, pvt)

    :param x: data
    :type x: NxP matrix

    :param pvt: controls the selection of the pivot columns:

        .. csv-table::
            :widths: auto

            "if :math:`pvt[i] > 0`, :math:`x[i]` is an initial column"
            "if :math:`pvt[i] = 0`, :math:`x[i]` is a free column"
            "if :math:`pvt[i] < 0`, :math:`x[i]` is a final column"

        The initial columns are placed at the beginning of the matrix and the final columns are placedat the end. Only the free columns will be moved during the decomposition.

    :type pvt: Px1 vector

    :return q1: unitary matrix, ``K = min(N,P)``.

    :rtype q1: NxK unitary matrix

    :return r: upper triangular matrix

    :rtype r: KxP matrix

    :return e: permutation vector

    :rtype e: Px1 vector

Remarks
-------

Given :math:`X[., E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[., E]` is zero below its diagonal, i.e.,

.. math::

    Q′R[ ., E ] = \begin{bmatrix}
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

  X[ ., E ] = Q_1R

is the QR decomposition of :math:`X[., E]`.

:func:`qqrep` allows you to control the pivoting. For example, suppose that *x* is
a dataset with a column of ones in the first column. If there are
linear dependencies among the columns of *x*, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using *pvt*.

If you want only the :math:`R` matrix, see :func:`qrep`. Not computing :math:`Q_1` can produce
significant improvements in computing time and memory usage.

Source
------

qqr.src

.. seealso:: Functions :func:`qqr`, :func:`qre`, :func:`olsqr`
