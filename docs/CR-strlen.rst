
strlen
==============================================

Purpose
----------------
Returns the length of a string.

Format
----------------
.. function:: strlen(x)

    :param x: NxK matrix of character data, or NxK string array.
    :type x: string

    :returns: y (*scalar*) containing the exact length of the
        string x, or NxK matrix or string array containing the lengths of the
        elements in x.

Remarks
-------

The null character (ASCII 0) is a legal character within strings and so
embedded nulls will be counted in the length of strings. The final
terminating null byte is not counted, though.

For character matrices, the length is computed by counting the
characters (maximum of 8) up to the first null in each element of the
matrix. The null character, therefore, is not a valid character in
matrices containing character data and is not counted in the lengths of
the elements of those matrices.


Examples
----------------

::

    x1 = "How long?";
    x2 = "Classification";
    len1 = strlen(x1);
    len2 = strlen(x2);

After running the code above:

::

    len1 = 9
    
    len2 = 14

.. seealso:: Functions :func:`strsect`, :func:`strindx`, :func:`strrindx`
