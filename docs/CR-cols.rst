
cols
==============================================

Purpose
----------------

Returns the number of columns in a matrix.

Format
----------------
.. function:: cols(x)

    :param x:
    :type x: NxK matrix or sparse matrix

    :returns: **n_cols** (*scalar*) - number of columns in *x*.

Remarks
-------

Use :func:`getorders` to return both the number of rows and columns in one call.
If *x* is an empty matrix, :code:`rows(x)` and :code:`cols(x)` both return 0.

Examples
----------------

::

    // Create a 100x3 matrix of uniform random numbers
    x = rndu(100, 3);

    // Find out how many columns are in 'x'
    n_cols = cols(x);

After the code above:

::

    n_cols = 3

.. seealso:: Functions :func:`rows`, :func:`colsf`, :func:`getorders`, :func:`show`
