
getTrRow
==============================================

Purpose
----------------

Transposes a matrix and then returns a single row from it.

Format
----------------
.. function:: getTrRow(a, row)

    :param a: 
    :type a: NxK matrix

    :param row: 
    :type row: The row of the matrix to extract

    :returns: y (*1xK row vector*) .

Remarks
-------

getRow is designed to give an alternative access to rows in a matrix
than indexing the matrix by brackets.


Examples
----------------

::

    a = rndn(10,10);
    y = getTrRow(a,3);

.. seealso:: Functions :func:`getRow`
