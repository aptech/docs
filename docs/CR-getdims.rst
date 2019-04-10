
getdims
==============================================

Purpose
----------------

Gets the number of dimensions in an array, matrix, string array or other symbol.

Format
----------------
.. function:: getdims(a)

    :param a: N-dimensional array, matrix, string, string array or sparse matrix.
    :type a: any

    :returns: ndims (*scalar*), the number of dimensions in the symbol.

Examples
----------------

::

    //Create a 2x120x12 random normal array
    nelems = 2 * 120 * 12;
    a = areshape(rndn(nelems, 1), 2|120|12);
    
    //Find ut the number of dimensions in 'a'
    ndims = getdims(a);

The code above, assigns *ndims* to be equal to 3.

.. seealso:: Functions :func:`getorders`

