
balance
==============================================

Purpose
----------------
Balances a square matrix.

Format
----------------
.. function:: { b, z } = balance(x)

    :param x:
    :type x: KxK matrix or N-dimensional array where the last two dimensions are KxK

    :return b: balanced matrix

    :rtype b: KxK matrix or N-dimensional array where the last two dimensions are KxK

    :return z: diagonal scale matrix

    :rtype z: KxK matrix or N-dimensional array where the last two dimensions are KxK

Remarks
---------------------

Returns a balanced matrix *b* and another matrix *z*
with scale factors in powers of two on its diagonal. *b* is balanced in the
sense that the absolute sums of the magnitudes of elements in corresponding
rows and columns are nearly equal.

:func:`balance` is most often used to scale matrices to improve the numerical
stability of the calculation of their eigenvalues. It is also useful in
the solution of matrix equations.

In particular,

.. math:: \mathit{b = \, z^{- 1}xz}

:func:`balance` uses the `BALANC` function from `EISPACK`

Examples
----------------

::

    x = { 100 200 300,
           40  50  60,
            7   8   9 };

    { b, z } = balance(x);

The above code will assign *b* and *z* as shown below.

::

    b = 100.0  100.0  37.5
         80.0   50.0  15.0
         56.0   32.0   9.0

    z = 4.0  0.0  0.0
        0.0  2.0  0.0
        0.0  0.0  0.5
