
convertsatostr
==============================================

Purpose
----------------

Converts a 1x1 string array to a string.

Format
----------------
.. function:: str = convertsatostr(sa)

    :param sa:
    :type sa: 1x1 string array

    :return str: *sa* converted to a string.

    :rtype str: string

Examples
----------------

::

    // Create a 1x1 string array
    string sa = { "hello" };

    // Convert to a string type
    s = convertsatostr(sa);
    print s;

The code above produces the following output:

::

    hello

.. seealso:: :func:`convertstrtosa`
