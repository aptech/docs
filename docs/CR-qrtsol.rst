
qrtsol
==============================================

Purpose
----------------

Computes the solution of R'x = b where R is an upper triangular matrix.

Format
----------------
.. function:: qrtsol(b, R)

    :param b: 
    :type b: PxL matrix

    :param R: 
    :type R: PxP upper triangular matrix

    :returns: x (*PxL matrix*) .



Remarks
-------

qrtsol applies a forward solve to R'x = b to solve for x. Generally R
will be the R matrix from a QR factorization. qrtsol may be used,
however, in any situation where R is upper triangular. If R is lower
triangular, transpose before calling qrtsol.

If R is not transposed, use qrsol.



Source
------

qrsol.src

.. seealso:: Functions 
