
strctoposix
==============================================

Purpose
----------------

Converts string dates to a matrix containing dates in POSIX date/time format, using the BSD strftime format specifiers.

Format
----------------
.. function:: d = strctoposix(x, fmt)

    :param x: dates
    :type x: NxK string array

    :param fmt: containing strftime date/time format characters.
    :type fmt: string or ExE conformable string array 

    :return d: displaying the date in the `fmt` format and containing the dates in POSIX format (seconds since the Jan 1, 1970).

    :rtype d: NxK date variable

Examples
----------------

Example 1
+++++++++
::

   print strctoposix("2012/06/23", "%Y/%m/%d");

produces the output:

::

              X1
      2012/06/23

To see the date in seconds since Jan 1, 1970, you can use the :func:`asmatrix` function.

::

    print asmatrix(strctoposix("2012/06/23", "%Y/%m/%d"));

::

    1340409600

Example 2
+++++++++

Convert a string to a date variable and then change the date format.

::

   dt = strctoposix("1945-11-22 18:36:29", "%Y-%m-%d %H:%M:%S");
   print dt;

produces the output:

::

                  X1 
    1945-11-22 18:36

Now change the date format that is printed.

::

    dt = asdate(dt, "%a, %b %d");
    print dt;

::

              X1 
     Thu, Nov 22

Now change the variable name:

::

    dt = asdf(dt, "day");
    print dt;

::

             day 
     Thu, Nov 22
    

Example 3
+++++++++
::

   print strctoposix("January 29, 1973 at  4:19 PM", "%B %d, %Y at %l:%M %p");

produces the output:

::

                              X1
    January 29, 1973 at  4:19 PM

Example 4
+++++++++
::

   ds = "Oct 23, 2007" $| "Feb 16, 2008";
   s = strctoposix(ds, "%b %d, %Y");

produces *s* equal to:

::

             X1
   Oct 23, 2007
   Feb 16, 2008

Example 5
+++++++++
::

   ds = "10/23/07 20:45:42" $| "02/16/08 14:32:22";
   s = strctoposix(ds, "%x %X");

produces *s* equal to:

::

                  X1
   10/23/07 20:45:42
   02/16/08 14:32:22

Remarks
-------

* To change the printed date format, use :func:`asdate`.
* To view the date in seconds since Jan 1, 1970, use :func:`asmatrix`.
* The following format specifiers are supported:

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
| %q              | The quarter, derived from the month. (1-4)          |
+-----------------+-----------------------------------------------------+
| %Z              | The time zone name, or by the empty string if this  |
|                 | is not determinable.                                |
+-----------------+-----------------------------------------------------+
| %%              | The '%' sign.                                       |
+-----------------+-----------------------------------------------------+


.. seealso:: Functions :func:`asdate`, :func:`asmatrix`, :func:`posixtostrc`, :func:`dttostrc`, :func:`strctodt`, :func:`dttostr`, :func:`strtodt`, :func:`dttoutc`, :func:`utctodt`

