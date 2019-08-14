
lusol
==============================================

Purpose
----------------

Computes the solution of :math:`LUx = b` where *L* is a lower triangular
 matrix and *U* is an upper triangular matrix.

Format
----------------
.. function:: x = lusol(b, L, U)

    :param b: data
    :type b: PxK matrix

    :param L: lower triangular matrix
    :type L: PxP matrix

    :param U: upper triangular matrix
    :type U: PxP matrix

    :return x: solution of LUx = b.

    :type x: PxK matrix

Remarks
-------

If *b* has more than one column, each column is solved for separately,
i.e., :func:`lusol` solves :math:`LUx[., i] = b[., i]`.

