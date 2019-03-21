
matalloc
==============================================

Purpose
----------------

Allocates a matrix with unspecified contents.

Format
----------------
.. function:: matalloc(r, c)

    :param r: rows.
    :type r: scalar

    :param c: columns.
    :type c: scalar

    :returns: y (*TODO*), r x c matrix.



Remarks
-------

The contents are unspecified. This function is used to allocate a matrix
that will be written to in sections using indexing or used with the
Foreign Language Interface as an output matrix for a function called
with dllcall.

