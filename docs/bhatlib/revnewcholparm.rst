revnewcholparm
==============================================
Purpose
----------------
Computes the reverse mapping of new Cholesky parameterization to obtain the parameter vector from the Cholesky matrix.

Format
----------------
.. function:: sdoubstar = revnewcholparm(L)

    :param L: Cholesky factor matrix.
    :type L: matrix

    :return sdoubstar: Parameter vector recovered from L.
    :rtype sdoubstar: vector

Library
-------
bhatlib

Source
------
matgradient.src