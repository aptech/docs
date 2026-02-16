
transpose
==============================================

Purpose
----------------

Transposes a matrix, swapping rows and columns. For complex matrices, computes the conjugate transpose.

Format
----------------

::

    y = x'

Parameters
----------------

    :param x: Input matrix.
    :type x: MxN matrix

Returns
----------------

    :return y: Transposed matrix with rows and columns swapped.

    :rtype y: NxM matrix

Examples
----------------

::

    x = { 1 2 3,
          4 5 6 };
    y = x';

::

    y =    1.0000000    4.0000000
           2.0000000    5.0000000
           3.0000000    6.0000000

Vector Transpose
++++++++++++++++

::

    // Column to row vector
    x = { 1, 2, 3 };
    y = x';

::

    y =    1.0000000    2.0000000    3.0000000

Inner Product
+++++++++++++

::

    a = { 1, 2, 3 };
    b = { 4, 5, 6 };
    y = a' * b;

::

    y =   32.0000000

Remarks
-------

- For complex matrices, ``'`` computes the conjugate transpose (Hermitian transpose).
- For non-conjugate transpose of complex matrices, use ``.'`` (bookkeeping transpose).

.. seealso:: Operators :doc:`bookkeeping-transpose`, Functions :func:`atranspose`
