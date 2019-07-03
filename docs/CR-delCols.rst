
delcols
==============================================

Purpose
----------------

Returns a matrix with specified columns removed.

Format
----------------
.. function:: delcols(x, r_idx)

    :param x:
    :type x: Input matrix

    :param r_idx: or vector, index of columns to remove from *x*.
        Negative integers will start from the back. For example,
        -1 will indicate to remove the final column of *x*.
    :type r_idx: Scalar

    :returns: **x_trim** (*matrix*) - equal to input *x* without columns specified by
        input *r_idx*. If no rows remain, *x_trim* will be
        an empty matrix.

Examples
----------------

Example 1
+++++++++

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the second column of 'x'
    x_trim = delcols(x, 2);

After the above code:

::

              1  3  4
    x_trim =  5  7  8
              9 11 12

Example 2
+++++++++

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the second and fourth columns of 'x'
    r_idx = { 2, 4 };

    x_trim = delcols(x, r_idx);

After the above code:

::

              1  3
    x_trim =  5  7
              9 11


Example 3
+++++++++

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the final column of 'x'
    x_trim = delcols(x, -1);

After the above code:

::

              1  2  3
    x_trim =  5  6  7
              9 10 11

.. seealso:: Functions :func:`delif`, :func:`delrows`, :func:`selif`
