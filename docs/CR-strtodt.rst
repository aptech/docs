
strtodt
==============================================

Purpose
----------------
Converts a string array of dates to a matrix in DT scalar format.

Format
----------------
.. function:: strtodt(sa, fmt)

    :param sa: 
    :type sa: NxK string array containing dates

    :param fmt: 
    :type fmt: string containing date/time format characters

    :returns: x (*TODO*), NxK matrix of dates in DT scalar format.

Examples
----------------

::

    x = strtodt("2012-07-12 10:18:32", "YYYY-MO-DD HH:MI:SS");
    print x;

produces:

::

    20120712101832.0

::

    x = strtodt("2012-07-12 10:18:32", "YYYY-MO-DD");
    print x;

produces:

::

    20120712000000.0

::

    x = strtodt("10:18:32", "HH:MI:SS");
    print x;

produces:

::

    101832.0

::

    x = strtodt("05-28-10", "MO-DD-YR");
    print x;

produces:

::

    20100528000000.0

.. seealso:: Functions :func:`dttostr`, :func:`dttoutc`, :func:`utctodt`
