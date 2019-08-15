
choldn
==============================================

Purpose
----------------

Performs a Cholesky downdate of one or more rows on an upper triangular matrix.

Format
----------------
.. function:: r = choldn(C, x)

    :param C: Upper triangular matrix to be operated on.
    :type C: KxK matrix

    :param x: the rows to downdate *C* with.
    :type x: NxK matrix

    :return r: the downdated matrix.

    :rtype r: KxK upper triangular matrix

Remarks
-------

If **trap 1** is set, :func:`choldn` returns scalar error code 60, otherwise it
terminates the program with an error message.

*C* should be a Cholesky factorization.

::

   choldn(C, x);

is equivalent to
::

   chol(C'C - x'x);

but :func:`choldn` is numerically much more stable.

.. WARNING:: it is possible to render a Cholesky factorization non-positive
    definite with choldn. You should keep an eye on the ratio of the largest
    diagonal element of *r* to the smallest. If it gets very large, *r* may no
    longer be positive definite. This ratio is a rough estimate of the
    condition number of the matrix.

Examples
----------------

::

    // Set C
    C = { 20.16210005 16.50544413 9.86676135,
                    0 11.16601462 2.97761666,
                    0           0 11.65496052 };

    // Set x
    x = { 1.76644971 7.49445820 9.79114666,
          6.87691156 4.41961438 4.32476921 };

   // Call choldn
   r = choldn(C, x);

After the above code, `r` will equal:

::

        18.8706  15.3229   8.0495
    r =  0.0000   9.3068  -2.1201
         0.0000   0.0000   7.6288

.. seealso:: Functions :func:`cholup`, :func:`chol`
