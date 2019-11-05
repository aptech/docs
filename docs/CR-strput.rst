
strput
==============================================

Purpose
----------------
Lays a substring over a string.

Format
----------------
.. function:: y = strput(substr, str, off)

    :param substr: the substring to be laid over the other string.
    :type substr: string

    :param str: the string to receive the substring.
    :type str: string

    :param off: the offset in *str* to place *substr*. The offset of the first byte is 1.
    :type off: scalar

    :return y: the new string.

    :rtype y: string

Examples
----------------

::

    // String receiving substring
    str = "max";

    // String to add
    sub = "imum";

    // Location to add new string
    loc = 4;

    // Build new string
    y = strput(sub, str, loc);
    print y;

::

    maximum

Source
------

strput.src
