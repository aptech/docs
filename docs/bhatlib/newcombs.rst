newcombs
==============================================
Purpose
----------------
Generates new combinations for structured matrix multiplication.

Format
----------------
.. function:: { B, F, C, Bindx } = newcombs(a, m)

    :param a: Input matrix.
    :type a: matrix

    :param m: Combination size.
    :type m: scalar

    :return B: Combined values matrix.
    :rtype B: matrix

    :return F: Frequency matrix.
    :rtype F: matrix

    :return C: Count matrix.
    :rtype C: matrix

    :return Bindx: Index matrix.
    :rtype Bindx: matrix

Library
-------
bhatlib

Source
------
vecup.src