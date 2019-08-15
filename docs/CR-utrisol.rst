
utrisol
==============================================

Purpose
----------------

Computes the solution of :math:`Ux = b` where :math:`U` is an upper triangular matrix.

Format
----------------
.. function:: x = utrisol(b, U)

    :param b: data
    :type b: PxK matrix

    :param U: data
    :type U: PxP upper triangular matrix

    :return x: solution of :math:`Ux = b`.

    :rtype x: PxK matrix

Remarks
-------

:func:`utrisol` applies a back solve to :math:`Ux = b` to solve for :math:`x`. If :math:`b` has more
than one column, each column is solved for separately, i.e., :func:`utrisol` applies a back solve to :math:`U \* x[.,i] = b[.,i]`.

.. DANGER:: check equations

