
qrep
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix :math:`X`, such that: :math:`X[.,E] = Q1R`

.. DANGER:: fix equations

Format
----------------
.. function:: { r, e } = qrep(X, pvt)

    :param X: data
    :type X: NxP matrix

    :param pvt: controls the selection of the pivot columns:

        .. csv-table::
            :widths: auto
    
            "if :math:`pvt[i] > 0`, :math:`X[i]` is an initial column."
            "if :math:`pvt[i] = 0`, :math:`X[i]` is a free column."
            "if :math:`pvt[i] < 0`, :math:`X[i]` is a final column."
    
        The initial columns are placed at the beginning of the matrix and the final columns are placed at 
        the end. Only the free columns will be moved during the decomposition.

    :type pvt: Px1 vector

    :return r: :math:`K = min(N,P)`.

    :rtype r: KxP upper triangular matrix

    :return e: 

    :rtype e: Px1 permutation vector

Remarks
-------

:func:`qrep` is the same as :func:`qqrep` but doesn't return the :math:`Q\ 1` matrix. If :math:`Q\ 1` is
not wanted, :func:`qrep` will save a significant amount of time and memory usage, especially for large problems.

Given :math:`X[.,E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[.,E]` is zero below its diagonal, i.e.,

.. math::

where :math:`R` is upper triangular. If we partition

.. math::

where :math:`Q\ 1` has :math:`P` columns, then

.. math::

is the QR decomposition of :math:`X[.,E]`.

:func:`qrep` does not return the :math:`Q\ 1` matrix because in most cases it is not
required and can be very large. If you need the :math:`Q\ 1` matrix, see the
function :func:`qqrep`. If you need the entire :math:`Q` matrix, call :func:`qyrep` with :math:`Y` set
to a conformable identity matrix. For most problems :math:`Q'Y`, :math:`Q\ 1'Y`, or :math:`QY`,
:math:`Q\ 1\ Y`, for some :math:`Y`, are required. For these cases see :func:`qtyrep` and :func:`qyrep`.

:func:`qrep` allows you to control the pivoting. For example, suppose that :math:`X` is
a dataset with a column of ones in the first column. If there are
linear dependencies among the columns of :math:`X`, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using *pvt*.

Source
------

qr.src

.. seealso:: Functions :func:`qr`, :func:`qre`, :func:`qqrep`

