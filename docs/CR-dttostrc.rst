
dttostrc
==============================================

Purpose
----------------

Converts a matrix containing dates in DT scalar format to a string array, using the BSD strftime format specifiers.

Format
----------------
.. function:: sa = dttostrc(x, fmt)

    :param x: Contains dates in DT scalar format.
    :type x: NxK matrix

    :param fmt: Contains strftime date/time format characters.
    :type fmt: string or ExE conformable string array.

    :return sa: Converted dates in string array form.

    :rtype sa: NxK string array

Remarks
-------

The DT scalar format is a double precision representation of the date
and time. In the DT scalar format, the number

::

   20180703105031

represents 10:50:31 or 10:50:31 AM on July 3, 2018. :func:`dttostrc` converts a
date in DT scalar format to a character string using the format string
in *fmt*.

The following formats are supported:

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
|                 | (0-23); single digits are preeded by a blank.       |
+-----------------+-----------------------------------------------------+
| %l              | The hour (12-hour clock) as a decimal number        |
|                 | (1-12); single digits are preeded by a blank.       |
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
| %Z              | The time zone name, or by the empty string if this  |
|                 | is not determinable.                                |
+-----------------+-----------------------------------------------------+
| %%              | The '%' sign.                                       |
+-----------------+-----------------------------------------------------+

A complete DT scalar format number will have 14 digits all to the left
of the decimal point. However, :func:`dttostrc` will accept numbers with fewer
digits. It will assume that the first four digits are the year, the next
two the month and so on.


Examples
----------------

Example 1
+++++++++

::

    dt = 20140317100312;

    // Generate date in format "%Y-%m-%d".
    print dttostrc(dt, "%F");

produces the output:

::

    2014-03-17

Example 2
+++++++++

::

    /*
    ** Print date including the full weekday name,
    ** the full month name, the date, and the year.
    */
    print dttostrc(20110117151218, "%A, %B %dth, %Y");

produces the output:

::

    Monday, January 17th, 2011

Example 3
+++++++++

::

    print dttostrc(19411207074801, "Pearl Harbor was attacked on %B %d, %Y at %R %p");

produces the output:

::

    Pearl Harbor was attacked on December 07, 1941 at 07:48 AM

Example 4
+++++++++

::

    x = { 19120317060424, 19370904010928, 19510221031129 };
    s = dttostrc(x, "%D");

produces *s* equal to:

::

    03/17/12
    09/04/37
    02/21/51

Continuing with the same *x* from above:

::

    fmt = "%A, %D" 
          $| "%a, %F" 
          $| "%v";

    s = dttostrc(x, fmt);

produces *s* equal to:

::

    Sunday, 03/17/12
     Sat, 1937-09-04
         21-FEB-1951

.. seealso:: Functions :func:`dttostr`, :func:`strctodt`, :func:`strtodt`, :func:`dttoutc`, :func:`posixtostrc`, :func:`strctoposix`, :func:`utctodt`
