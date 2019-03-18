
getRow
==============================================

Purpose
----------------

Returns a specified row from a matrix.

Format
----------------
.. function:: getRow(a,  row)

    :param a: NxK matrix
    :type a: TODO

    :param row: The row of the matrix to extract.
    :type row: TODO

    :returns: y (*TODO*), A 1xK row vector.

Examples
----------------
First create a matrix, a:

::

    a = rndn(10,10);

Now you can assign a variable y to be equal the third row of a with either
of the following statements.

::

    y = getRow(a,3);

or

::

    y = a[3,.];

While both statements will produce the same result, the first may make for code that is easier to read and interpret.

.. seealso:: Functions :func:`getTrRow`
