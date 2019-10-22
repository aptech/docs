
strtodt
==============================================

Purpose
----------------
Converts a string array of dates to a matrix in DT scalar format.

Format
----------------
.. function:: x = strtodt(sa, fmt)

    :param sa: dates
    :type sa: NxK string array

    :param fmt: date/time format characters
    :type fmt: string

    :return x: of dates in DT scalar format.

    :rtype x: NxK matrix

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

Remarks
-------

The DT scalar format is a double precision representation of the date
and time. In the DT scalar format, the number:

::

   20120921223505

represents 22:35:05 or 10:35:05 PM on September 21, 2012.

The following formats are supported:

+------+-------------------------+
| YYYY | Four digit year         |
+------+-------------------------+
| YR   | Last two digits of year |
+------+-------------------------+
| MO   | Number of month, 01-12  |
+------+-------------------------+
| DD   | Day of month, 01-31     |
+------+-------------------------+
| HH   | Hour of day, 00-23      |
+------+-------------------------+
| MI   | Minute of hour, 00-59   |
+------+-------------------------+
| SS   | Second of minute, 00-59 |
+------+-------------------------+


.. seealso:: Functions :func:`dttostr`, :func:`dttoutc`, :func:`utctodt`

