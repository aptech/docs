
delcols
==============================================

Purpose
----------------

Returns a matrix with specified columns removed.

Format
----------------
.. function:: delcols(X, r_idx)

    :param X:
    :type X: Input matrix

    :param r_idx: or vector, index of columns to remove from *X*.
        Negative integers will start from the back. For example,
        -1 will indicate to remove the final column of *X*.
    :type r_idx: Scalar

    :returns: **X_trim** (*matrix*) - equal to input *X* without columns specified by
        input *r_idx*. If no rows remain, *X_trim* will be
        an empty matrix.

Examples
----------------

Example 1
+++++++++

::

    X = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the second column of 'X'
    X_trim = delcols(X, 2);

After the above code:

::

              1  3  4
    X_trim =  5  7  8
              9 11 12

Example 2
+++++++++

::

    X = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the second and fourth columns of 'X'
    r_idx = { 2, 4 };
    
    X_trim = delcols(X, r_idx);

After the above code:

::

              1  3
    X_trim =  5  7
              9 11


Example 3
+++++++++

::

    X = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the final column of 'X'
    X_trim = delcols(X, -1);

After the above code:

::

              1  2  3
    X_trim =  5  6  7
              9 10 11

.. seealso:: Functions :func:`delif`, :func:`delrows`, :func:`selif`
