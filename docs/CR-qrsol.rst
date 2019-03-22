
qrsol
==============================================

Purpose
----------------

Computes the solution of Rx = b where R is an
 upper triangular matrix.

Format
----------------
.. function:: qrsol(b, R)

    :param b: 
    :type b: PxL matrix

    :param R: 
    :type R: PxP upper triangular matrix

    :returns: x (*PxL matrix*) .



Remarks
-------

qrsol applies a backsolve to Rx = b to solve for x. Generally R will be
the R matrix from a QR factorization. qrsol may be used, however, in any
situation where R is upper triangular.



Source
------

qrsol.src

.. seealso:: Functions :func:`qqr`, :func:`qr`, :func:`qtyr`, :func:`qrtsol`
