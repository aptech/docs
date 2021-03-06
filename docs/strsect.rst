
strsect
==============================================

Purpose
----------------
Extracts a substring of a string.

Format
----------------
.. function:: y = strsect(str, start, len)

    :param str: data from which the string segment is to be obtained.
    :type str: string or scalar

    :param start: the index of the substring in *str*. The index of the first character is 1.
    :type start: scalar

    :param len: the length of the substring.
    :type len: scalar

    :return y: the extracted substring, or a null string if
        *start* is greater than the length of *str*.

    :rtype y: string

Examples
----------------

::

    // String to search in 
    strng = "This is an example string.";

    // Remove section of string
    y = strsect(strng, 12, 7);

The above code assigns the variable *y* to be:

::

    example

Remarks
-------

If there are not enough characters in a string for the defined substring
to be extracted, then a short string or a null string will be returned.

If *str* is a matrix containing character data, it must be scalar.

.. seealso:: Functions :func:`strlen`, :func:`strindx`, :func:`strrindx`, :func:`strreplace`
