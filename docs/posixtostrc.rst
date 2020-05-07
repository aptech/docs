
posixtostrc
==============================================

Purpose
----------------

Converts a matrix containing dates in POSIX date/time format to a string array, using the BSD strftime format specifiers.

Format
----------------
.. function:: sa = posixtostrc(x, fmt)

    :param x: dates in POSIX date/time format (seconds since January 1, 1970).
    :type x: NxK matrix

    :param fmt: contains strftime date/time format characters.
    :type fmt: string or ExE conformable string array

    :return sa: dates in POSIX date/time format found in *x* converted to a string array.
    :rtype sa: NxK string array

Examples
----------------

Example 1
+++++++++

::

    print posixtostrc(1340471401, "%Y/%m/%d");

produces the output:

::

    2012/06/23

Example 2
+++++++++

::

    print posixtostrc(-760771411, "%Y-%m-%d %H:%M:%S");

produces the output:

::

    1945-11-22 18:36:29

Example 3
+++++++++

::

    print posixtostrc(97172340, "%B %d, %Y at %l:%M %p");

produces the output:

::

    January 29, 1973 at  4:19 PM

Example 4
+++++++++

::

    d = { 1193172342, 1203172342 };
    s = posixtostrc(d, "%b %d, %Y");

produces *s* equal to:

::

    Oct 23, 2007
    Feb 16, 2008

Using the same *d* from above:

::

    s = posixtostrc(d, "%x %X");

produces *s* equal to:

::

    10/23/07 20:45:42
    02/16/08 14:32:22

Continuing with the same *x* from above:

::

    fmt = "Michael was born on %b %drd, %Y" $| "Jessica was born on %b %dth, %Y";
    s = posixtostrc(d, fmt);

produces *s* equal to:

::

    Michael was born on Oct 23rd, 2007
    Jessica was born on Feb 16th, 2008

Remarks
-------

The following format specifiers are supported:

+-----------------+-----------------------------------------------------+
| %A              | The full weekday name.                              |
+-----------------+-----------------------------------------------------+
| %a              | The abbreviated weekday name.                       |
+-----------------+-----------------------------------------------------+
| %B              | The full month name.                                |
+-----------------+-----------------------------------------------------+
| %b, or %h       | The abbreviated month name.                         |
+-----------------+-----------------------------------------------------+
| %C              | The century (a year divided by 100 and truncated to |
|                 | an integer) as a decimal number (00-99).            |
+-----------------+-----------------------------------------------------+
| %c              | The locale's appropriate date and time              |
|                 | representation.                                     |
+-----------------+-----------------------------------------------------+
| %D              | The date format "%m/%d/%y".                         |
+-----------------+-----------------------------------------------------+
| %d              | The day of month as a decimal number (01-31).       |
+-----------------+-----------------------------------------------------+
| %e              | The day of month as a decimal number (1-31); single |
|                 | digits are preceded by a blank.                     |
+-----------------+-----------------------------------------------------+
| %F              | The date format "%Y-%m-%d".                         |
+-----------------+-----------------------------------------------------+
| %G              | The ISO 8601 year with century as a decimal number. |
+-----------------+-----------------------------------------------------+
| %g              | The ISO 8601 year without century as a decimal      |
|                 | number (00-99).                                     |
+-----------------+-----------------------------------------------------+
| %H              | The hour (24-hour clock) as a decimal number        |
|                 | (00-23).                                            |
+-----------------+-----------------------------------------------------+
| %I              | The hour (12-hour clock) as a decimal number        |
|                 | (01-12).                                            |
+-----------------+-----------------------------------------------------+
| %j              | The day of the year as a decimal number (001-366).  |
+-----------------+-----------------------------------------------------+
| %k              | The hour (24-hour clock) as a decimal number        |
|                 | (0-23); single digits are preceded by a blank.      |
+-----------------+-----------------------------------------------------+
| %l              | The hour (12-hour clock) as a decimal number        |
|                 | (1-12); single digits are preceded by a blank.      |
+-----------------+-----------------------------------------------------+
| %M              | The minute as a decimal number (00-59).             |
+-----------------+-----------------------------------------------------+
| %m              | The month as a decimal number (01-12).              |
+-----------------+-----------------------------------------------------+
| %n              | A newline.                                          |
+-----------------+-----------------------------------------------------+
| %p              | The locale's equivalent of either “AM” or “PM”.     |
+-----------------+-----------------------------------------------------+
| %R              | The time in the format "%H:%M".                     |
+-----------------+-----------------------------------------------------+
| %r              | The locale's representation of 12-hour clock time   |
|                 | using AM/PM notation.                               |
+-----------------+-----------------------------------------------------+
| %S              | The second as a decimal number (00-60). The range   |
|                 | of seconds is (00-60) instead of (00-59) to allow   |
|                 | for the periodic occurrence of leap seconds.        |
+-----------------+-----------------------------------------------------+
| %s              | The number of seconds since the Epoch, UTC.         |
+-----------------+-----------------------------------------------------+
| %T              | The time in the format "%H:%M:%S".                  |
+-----------------+-----------------------------------------------------+
| %t              | A tab.                                              |
+-----------------+-----------------------------------------------------+
| %U              | The week number of the year (Sunday as the first    |
|                 | day of the week) as a decimal number (00-53).       |
+-----------------+-----------------------------------------------------+
| %u              | The weekday (Monday as the first day of the week)   |
|                 | as a decimal number (1-7).                          |
+-----------------+-----------------------------------------------------+
| %V              | The week number of the year (Monday as the first    |
|                 | day of the week) as a decimal number (01-53). If    |
|                 | the week containing January 1 has four or more days |
|                 | in the new year, then it is week 1; otherwise it is |
|                 | week 53 of the previous year, and the next week is  |
|                 | week 1.                                             |
+-----------------+-----------------------------------------------------+
| %v              | The date in the format "%e-%b-%Y".                  |
+-----------------+-----------------------------------------------------+
| %W              | The week number of the year (Monday as the first    |
|                 | day of the week) as a decimal number (00-53).       |
+-----------------+-----------------------------------------------------+
| %w              | The weekday (Sunday as the first day of the week)   |
|                 | as a decimal number (0-6).                          |
+-----------------+-----------------------------------------------------+
| %X              | The locale's appropriate time representation.       |
+-----------------+-----------------------------------------------------+
| %x              | The locale's appropriate date representation.       |
+-----------------+-----------------------------------------------------+
| %Y              | The year with century as a decimal number.          |
+-----------------+-----------------------------------------------------+
| %y              | The year without century as a decimal number        |
|                 | (00-99).                                            |
+-----------------+-----------------------------------------------------+
| %q              | The quarter of the year. (1-4)                      |
+-----------------+-----------------------------------------------------+
| %Z              | The time zone name, or by the empty string if this  |
|                 | is not determinable.                                |
+-----------------+-----------------------------------------------------+
| %%              | The '%' sign.                                       |
+-----------------+-----------------------------------------------------+


.. seealso:: Functions :func:`dttostrc`, :func:`strctodt`, :func:`strctoposix`, :func:`dttostr`, :func:`strtodt`, :func:`dttoutc`, :func:`utctodt`
