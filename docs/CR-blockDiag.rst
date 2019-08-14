
blockDiag
==============================================

Purpose
----------------

Creates a block-diagonal matrix from one or more input matrices.

Format
----------------
.. function:: d = blockDiag(A [, B, C ...])

    :param A:
    :type A: One or more matrices

    :returns: d (*matrix*), Diagonal matrix constructed from the input matrices.

Remarks
----------------
The input matrices may be square or rectangular. The matrices do not need to have the same dimensions.

Examples
----------------

Basic example
+++++++++++++

::

    a = { 0.5 1.1,
          2.0 0.3 };
    b = 0.8;
    c = { 0.2 1.0 0.7,
          1.3 0.6 1.4 };

    d = blockDiag(a, b, c);

After the above code, *d* should equal:

::

        0.5 1.1   0   0   0   0
        2.0 0.3   0   0   0   0
    d =   0   0 0.8   0   0   0
          0   0   0 0.2 1.0 0.7
          0   0   0 1.3 0.6 1.4
