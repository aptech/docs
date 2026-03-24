
qtyrep
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X using a pivot vector and returns :math:`Q'Y` and :math:`R`.


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

Given :math:`X[., E]`, where :math:`E` is a permutation vector that permutes the columns
of :math:`X`, there is an orthogonal matrix :math:`Q` such that :math:`Q'X[., E]` is zero below
its diagonal, i.e.,

.. math::

    Q′X[ ., E ] = \begin{bmatrix}
        R \\
        0
        \end{bmatrix}

where :math:`R` is upper triangular. If we partition

.. math::

   Q⁢ = [Q_1\ Q_2⁢]

where :math:`Q_1` has :math:`P` columns, then

.. math::

    X[., E] = Q_1R

is the QR decomposition of :math:`X[.,E]`.

:func:`qtyrep` allows you to control the pivoting. For example, suppose that :math:`X`
is a dataset with a column of ones in the first column. If there are
linear dependencies among the columns of :math:`X`, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using *pvt*.

Examples
--------

::

    // Create a 3x2 matrix
    x = { 1 2,
          3 4,
          5 6 };

    // Right-hand side vector
    y = { 1,
          0,
          0 };

    // Pivot vector: all columns are free
    pvt = { 0, 0 };

    // Compute Q'*Y, R, and permutation vector with controlled pivoting
    { qty, r, e } = qtyrep(y, x, pvt);

    print "Q'*Y:";
    print qty;
    print "R (upper triangular):";
    print r;
    print "Permutation vector E:";
    print e;

The above code produces the following output:

::

    Q'*Y:

     -0.26726124
      0.87287156
      0.40824829

    R (upper triangular):

      -7.4833148       -5.8797473
       0.0000000      -0.65465367

    Permutation vector E:

       2.0000000
       1.0000000

Source
------

qtyr.src

.. seealso:: Functions :func:`qrep`, :func:`qtyre`
