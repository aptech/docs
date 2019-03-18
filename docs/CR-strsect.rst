
strsect
==============================================

Purpose
----------------
Extracts a substring of a string.

Format
----------------
.. function:: strsect(str,  start,  len)

    :param str: string or scalar from which the segment is
        to be obtained.
    :type str: TODO

    :param start: the index of the substring
        in  str. The index of the first character is 1.
    :type start: scalar

    :param len: the length of the substring.
    :type len: scalar

    :returns: y (*string*), the extracted substring, or a null string if
        start is greater than the length of  str.

Examples
----------------

::

    strng = "This is an example string.";
    y = strsect(strng,12,7);

The above code assigns the variable y to be:

::

    example

.. seealso:: Functions :func:`strlen`, :func:`strindx`, :func:`strrindx`, :func:`strreplace`
