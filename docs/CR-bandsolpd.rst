
bandsolpd
==============================================

Purpose
----------------

Solves the system of equations :math:`Ax = b` for *x*, where *A* is a positive definite banded matrix.

Format
----------------
.. function:: bandsolpd(b, A)

    :param b:
    :type b: KxM matrix

    :param A:
    :type A: KxN compact form matrix

    :returns: x (*KxM matrix*)

Remarks
-------

*A* is a positive definite banded matrix in compact form. See :func:`band` for a
description of the format of *A*.

*b* can have more than one column. If so, :math:`Ax = b` is solved for each
column. That is,

.. math:: A*x[.,i] = b[.,i]

.. seealso:: Functions :func:`band`, :func:`bandchol`, :func:`bandcholsol`, :func:`bandltsol`, :func:`bandrv`
