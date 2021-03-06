
cholup
==============================================

Purpose
----------------

Performs a Cholesky update of one or more rows on an upper triangular matrix.

Format
----------------
.. function:: r = cholup(C, x)

    :param C: upper triangular matrix
    :type C: KxK matrix

    :param x: the rows to update *C* with.
    :type x: NxK matrix

    :return r: the updated matrix.

    :rtype r: KxK upper triangular matrix

Examples
----------------

::

    // Assign C matrix
    C = { 18.87055964 15.3229443  8.04947012,
                    0 9.30682813 -2.12009339,
                    0          0  7.62878355 };

    // Assign x matrix
    x = { 1.76644971 7.49445820 9.79114666,
          6.87691156 4.41961438 4.32476921 };

    // Call cholup
    r = cholup(C, x);

After the above code, `r` will equal:

::

        20.162100    16.505444    9.8667614
    r = 0.0000000    11.166015    2.9776167
        0.0000000    0.0000000    11.654961

Remarks
-------

*C* should be a Cholesky factorization.

:code:`cholup(C, x)` is equivalent to :code:`chol(C'C + x'x)`, but cholup is numerically
much more stable.

.. seealso:: Functions :func:`choldn`
