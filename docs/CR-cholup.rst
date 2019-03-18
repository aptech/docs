
cholup
==============================================

Purpose
----------------

Performs a Cholesky update of one or more rows on an upper triangular matrix.

Format
----------------
.. function:: cholup(C, x)

    :param C: KxK upper triangular matrix.
    :type C: TODO

    :param x: the rows to update  C with.
    :type x: NxK matrix

    :returns: r (*KxK upper triangular matrix*), the updated matrix.

Examples
----------------

::

    let C[3,3] = 18.87055964 15.3229443  8.04947012
                           0 9.30682813 -2.12009339
                           0 0           7.62878355;
    let x[2,3] = 1.76644971 7.49445820 9.79114666
                 6.87691156 4.41961438 4.32476921;
    r = cholup(C,x);
    
        20.162100    16.505444    9.8667614
    r = 0.0000000    11.166015    2.9776167
        0.0000000    0.0000000    11.654961

.. seealso:: Functions :func:`choldn`

cholesky update upper triangular matrix
