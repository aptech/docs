
choldn
==============================================

Purpose
----------------

Performs a Cholesky downdate of one or more rows on an upper triangular matrix.

Format
----------------
.. function:: choldn(C, x)

    :param C: KxK upper triangular matrix.
    :type C: TODO

    :param x: the rows to downdate  C with.
    :type x: NxK matrix

    :returns: r (*KxK upper triangular matrix*), the downdated matrix.

Examples
----------------

::

    let C[3,3] = 20.16210005 16.50544413 9.86676135
                           0 11.16601462 2.97761666
                           0 0 11.65496052;
    let x[2,3] = 1.76644971 7.49445820 9.79114666
                 6.87691156 4.41961438 4.32476921;
    r = choldn(C,x);
    
        18.8706  15.3229   8.0495
    r =  0.0000   9.3068  -2.1201
         0.0000   0.0000   7.6288

.. seealso:: Functions :func:`cholup`, :func:`chol`

cholesky downdate upper triangular matrix
