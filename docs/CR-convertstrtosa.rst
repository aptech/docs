
convertstrtosa
==============================================

Purpose
----------------

Converts a string to a 1x1 string array.

Format
----------------
.. function:: convertstrtosa(str)

    :param str: string.
    :type str: TODO

    :returns: sa (*1x1 string array*), str converted to a string array.

Examples
----------------

::

    str = "This is a string";
    z = convertstrtosa(str);

You can check the types of your variables by viewing them on the GAUSS data page, or by using the
show command. If the code above was executed at startup, running the show command would return:

::

    24 bytes     str          STRING                          16 char
    40 bytes     z            STRING ARRAY                     1,1

.. seealso:: Functions :func:`convertsatostr`
