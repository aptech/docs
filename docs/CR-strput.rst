
strput
==============================================

Purpose
----------------
Lays a substring over a string.

Format
----------------
.. function:: strput(substr, str, off)

    :param substr: the substring to be laid over the other
        string.
    :type substr: string

    :param str: the string to receive the substring.
    :type str: string

    :param off: the offset in str to place substr. The offset
        of the first byte is 1.
    :type off: scalar

    :returns: y (*string*), the new string.

Examples
----------------

::

    str = "max";
    sub = "imum";
    loc = 4;
    y = strput(sub,str,loc);
    print y;

::

    maximum

Source
------

strput.src

