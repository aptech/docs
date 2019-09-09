
qtyrep
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X using a pivot vector and returns :math:`Q'Y` and :math:`R`.

.. DANGER:: fix equations

Format
----------------
.. function:: { qty, r, e } = qtyrep(y, x, pvt)

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

    :return qty: unitary matrix

    :rtype qty: NxL matrix

    :return r: upper triangular matrix. :math:`K = min(N,P)`.

    :rtype r: KxP matrix

    :return e: permutation vector

    :rtype e: Px1 vector

Remarks
-------

Given :math:`X[.,E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[.,E]` is zero below
its diagonal, i.e.,

::

where :math:`R` is upper triangular. If we partition

::

where :math:`Q\ 1` has :math:`P` columns, then

::

is the QR decomposition of :math:`X[.,E]`.

:func:`qtyrep` allows you to control the pivoting. For example, suppose that :math:`X`
is a dataset with a column of ones in the first column. If there are
linear dependencies among the columns of :math:`X`, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using *pvt*.

Source
------

qtyr.src

.. seealso:: Functions :func:`qrep`, :func:`qtyre`

