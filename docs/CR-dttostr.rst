
dttostr
==============================================

Purpose
----------------

Converts a matrix containing dates in DT scalar format to a string array.

Format
----------------
.. function:: dttostr(x, fmt)

    :param x: 
    :type x: NxK matrix containing dates in DT scalar format

    :param fmt: or  ExE conformable string array containing date/time format characters.
    :type fmt: string

    :returns: sa (*NxK string array*) .

Remarks
-------

For more formatting options, see :func:`dttostrc`.

The DT scalar format is a double precision representation of the date
and time. In the DT scalar format, the number

::

   20120703105031

represents 10:50:31 or 10:50:31 AM on July 3, 2012. :func:`dttostr` converts a
date in DT scalar format to a character string using the format string
in fmt.

The following formats are supported:

+-----------------+-----------------------------------------------------+
|    YYYY         | 4 digit year                                        |
+-----------------+-----------------------------------------------------+
|    YR           | Last two digits of year                             |
+-----------------+-----------------------------------------------------+
|    QQ           | Quarter of the year. This is calculated from the    |
|                 | month number.                                       |
+-----------------+-----------------------------------------------------+
|    MO           | Number of month, 01-12                              |
+-----------------+-----------------------------------------------------+
|    DD           | Day of month, 01-31                                 |
+-----------------+-----------------------------------------------------+
|    HH           | Hour of day, 00-23                                  |
+-----------------+-----------------------------------------------------+
|    MI           | Minute of hour, 00-59                               |
+-----------------+-----------------------------------------------------+
|    SS           | Second of minute, 00-59                             |
+-----------------+-----------------------------------------------------+

A complete DT scalar format number will have 14 digits all to the left
of the decimal point. However, dttostr will accept numbers with fewer
digits. It will assume that the first four digits are the year, the next
two the month and so on.


Examples
----------------

Example 1
+++++++++

::

    dt = 201202;
    print dttostr(dt, "QQ-YYYY");
    
    produces the output:

::

    Q1-2012


Example 2
+++++++++


::

    S0 = dttostr(utctodt(timeutc), "YYYY-MO-DD HH:MI:SS");
    print ("Date and Time are: " $+ s0);

produces the output:

::

    Date and time are: 2012-09-14 11:49:10

Example 3
+++++++++

::

    print dttostr(utctodt(timeutc), "Today is DD-MO-YR");

produces the output:

::

    Today is 14-09-12


Example 4
+++++++++

::

    x = { 19120317060424, 19370904010928, 19510221031129 };
    s = dttostr(x, "YYYY-MO-DD");

produces *s* equal to:

::

    1912-03-17
    1937-09-04
    1951-02-21

Using the same *x* from above:

::

    s = dttostr(x, "DD/MO/YYYY");

produces *s* equal to:

::

    03/17/1912
    09/04/1937
    02/21/1951

Continuing with the same *x* from above:

::

    string fmt = { "YYYY-QQ", "YYYY-QQ-DD", "DD/MO/YYYY" };
    s = dttostr(x, fmt);

produces *s* equal to:

::

    1912-Q1
    1937-Q3-04
    21/02/1951

.. seealso:: Functions :func:`dttostrc`, :func:`strtodt`, :func:`dttoutc`, :func:`utctodt`, :func:`posixtostrc`, :func:`strctoposix`

