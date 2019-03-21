
rank
==============================================

Purpose
----------------
Computes the rank of a matrix, using the singular value decomposition.

Format
----------------
.. function:: rank(x)

    :param x: 
    :type x: NxP matrix

    :returns: k (*TODO*), an estimate of the rank of x. This
        equals the number of singular values of x
        that exceed a prespecified tolerance in absolute value.

