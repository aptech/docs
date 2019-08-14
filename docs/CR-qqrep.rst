
qqrep
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix *x*, such that: :math:`X[.,E] = Q1R`

.. DANGER:: fix equations. corrupted equations below have been left empty.

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

    :return q1: ``K = min(N,P)``.

    :type q1: NxK unitary matrix

    :return r: 

    :type r: KxP upper triangular matrix

    :return e: 

    :type e: Px1 permutation vector

Remarks
-------

Given :math:`X[.,E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[.,E]` is zero below its diagonal, i.e.,

.. math::

where :math:`R` is upper triangular. If we partition

.. math::

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

is the QR decomposition of :math:`X[.,E]`.

:func:`qqrep` allows you to control the pivoting. For example, suppose that *x* is
a data set with a column of ones in the first column. If there are
linear dependencies among the columns of *x*, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using *pvt*.

If you want only the :math:`R` matrix, see :func:`qrep`. Not computing :math:`Q\ 1` can produce
significant improvements in computing time and memory usage.

Source
------

qqr.src

.. seealso:: Functions :func:`qqr`, :func:`qre`, :func:`olsqr`

