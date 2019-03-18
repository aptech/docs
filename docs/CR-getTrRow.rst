
getTrRow
==============================================

Purpose
----------------

Transposes a matrix and then returns a single row from it.

Format
----------------
.. function:: getTrRow(a,  row)

    :param a: NxK matrix
    :type a: TODO

    :param row: The row of the matrix to extract.
    :type row: TODO

    :returns: y (*TODO*), A 1xK row vector.

Examples
----------------

::

    a = rndn(10,10);
    y = getTrRow(a,3);

.. seealso:: Functions :func:`getRow`
