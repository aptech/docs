
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

    :returns: y (*TODO*), scalar containing the exact length of the
        string x, or NxK matrix or string array containing the lengths of the
        elements in x.

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
