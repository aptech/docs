
strctoposix
==============================================

Purpose
----------------

Converts string dates to a matrix containing dates in Posix date/time format, using the BSD strftime format specifiers.

Format
----------------
.. function:: strctoposix(x,  fmt)

    :param x: NxK string array containing dates.
    :type x: TODO

    :param fmt: or  ExE conformable string array containing strftime date/time format characters.
    :type fmt: string

    :returns: d (*TODO*), NxK matrix containing dates in Posix format (seconds since the Jan 1, 1970).

Examples
----------------

print strctoposix("2012/06/23", "%Y/%m/%d");
++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    1340409600

print strctoposix("1945-11-22 18:36:29", "%Y-%m-%d %H:%M:%S");
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    -760771411

print strctoposix("January 29, 1973 at  4:19 PM", "%B %d, %Y at %l:%M %p");
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    97172340

ds = "Oct 23, 2007" $| "Feb 16, 2008";
s = strctoposix(ds, "%b %d, %Y");
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces s equal to:

::

    1193097600
    1203120000

ds = "10/23/07 20:45:42" $| "02/16/08 14:32:22";
s = strctoposix(ds, "%x %X");
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces s equal to:

::

    1193172342
    1203172342

.. seealso:: Functions :func:`posixtostrc`, :func:`dttostrc`, :func:`strctodt`, :func:`dttostr`, :func:`strtodt`, :func:`dttoutc`, :func:`utctodt`
