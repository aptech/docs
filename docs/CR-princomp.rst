
princomp
==============================================

Purpose
----------------

Computes principal components of a data matrix.

Format
----------------
.. function:: princomp(x, j)

    :param x: N>K, full rank.
    :type x: NxK data matrix

    :param j: number of principal components to be computed (j <= K).
    :type j: scalar

    :returns: p (*TODO*), NxJ matrix of the first  j principal
        components of x in descending order of amount of
        variance explained.

    :returns: v (*TODO*), Jx1 vector of fractions of variance explained.

    :returns: a (*JxK matrix of factor loadings*), such that:
        
        x = p*a + error.

