
hasimag
==============================================

Purpose
----------------

Tests whether the imaginary part of a complex matrix is negligible.

Format
----------------
.. function:: hasimag(x)

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*scalar*), 1 if the imaginary part of x has any nonzero elements, 0 if it consists entirely of 0's.

Examples
----------------

::

    x = { 1   2 3i,
          4-i 5 6i,
          7   8i 9 };
     
    if hasimag(x);
        //code path for complex case
    else;
        //code path for real case
    endif;

.. seealso:: Functions :func:`iscplx`
