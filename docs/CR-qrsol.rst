
qrsol
==============================================

Purpose
----------------

Computes the solution of :math:`Rx = b` where :math:`R` is an upper triangular matrix.

Format
----------------
.. function:: x = qrsol(b, R)

    :param b: data
    :type b: PxL matrix

    :param R: upper triangular matrix
    :type R: PxP matrix

    :return x: 

    :type x: PxL matrix

Remarks
-------

:func:`qrsol` applies a backsolve to :math:`Rx = b` to solve for *x*. Generally *R* will be
the *R* matrix from a QR factorization. :func:`qrsol` may be used, however, in any situation 
where *R* is upper triangular.

Source
------

qrsol.src

.. seealso:: Functions :func:`qqr`, :func:`qr`, :func:`qtyr`, :func:`qrtsol`

