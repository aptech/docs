
qrtsol
==============================================

Purpose
----------------

Computes the solution of :math:`R'x = b` where *R* is an upper triangular matrix.

Format
----------------
.. function:: x = qrtsol(b, R)

    :param b: data
    :type b: PxL matrix

    :param R: upper triangular matrix
    :type R: PxP matrix

    :returns: x (*PxL matrix*) 

Remarks
-------

:func:`qrtsol` applies a forward solve to :math:`R'x = b` to solve for *x*. Generally *R*
will be the *R* matrix from a QR factorization. :func:`qrtsol` may be used,
however, in any situation where *R* is upper triangular. If *R* is lower
triangular, transpose before calling :func:`qrtsol`.

If *R* is not transposed, use :func:`qrsol`.

Source
------

qrsol.src

.. seealso:: Functions :func:`qqr`, :func:`qr`, :func:`qtyr`, :func:`qrsol`

