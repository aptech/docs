
ltrisol
==============================================

Purpose
----------------

Computes the solution of :math:`Lx = b` where *L* is a lower triangular matrix.

Format
----------------
.. function:: x = ltrisol(b, L)

    :param b: data
    :type b: PxK matrix

    :param L: lower triangular matrix
    :type L: PxP matrix

    :return x: soluion of :math:`Lx = b`.

    :rtype x: PxK matrix

Remarks
---------------

:func:`ltrisol` applies a forward solve to :math:`Lx = b` to solve for *x*. If *b* has more
than one column, each column will be solved for separately, 
i.e., :func:`ltrisol` will apply a forward solve to :math:`L*x[., i] = b[., i]`.

