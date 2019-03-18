
cols
==============================================

Purpose
----------------

Returns the number of columns in a matrix.

Format
----------------
.. function:: cols(x)

    :param x: NxK matrix or sparse matrix.
    :type x: TODO

    :returns: p (*TODO*), number of columns in x.

Examples
----------------

::

    //Create a 100x3 matrix of uniform random numbers
    x = rndu(100,3);
    
    //Find out how many columns are in 'x'
    p = cols(x);

After the code above:

::

    p = 3

.. seealso:: Functions :func:`rows`, :func:`colsf`, :func:`getorders`, :func:`show`
