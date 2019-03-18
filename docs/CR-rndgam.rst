
rndgam
==============================================

Purpose
----------------

Computes pseudo-random numbers with gamma distribution. NOTE: rndgam is deprecated and should be replaced with rndGamma.

Format
----------------
.. function:: rndgam(r, c, alpha)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param alpha: ExE conformable with
        r x c resulting matrix, shape
        parameters for gamma distribution.
    :type alpha: MxN matrix

    :returns: x (*r x c matrix*), gamma
        distributed pseudo-random numbers.

