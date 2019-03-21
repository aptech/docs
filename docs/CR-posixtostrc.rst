
posixtostrc
==============================================

Purpose
----------------

Converts a matrix containing dates in Posix date/time format to a string array, using the BSD strftime format specifiers.

Format
----------------
.. function:: posixtostrc(x, fmt)

    :param x: , 1970).
    :type x: NxK matrix containing dates in Posix date/time format (seconds since January 1

    :param fmt: or  ExE conformable string array containing strftime date/time format characters.
    :type fmt: string

    :returns: sa (*TODO*), NxK string array.

Examples
----------------

print posixtostrc(1340471401, "%Y/%m/%d");
++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    2012/06/23

print posixtostrc(-760771411, "%Y-%m-%d %H:%M:%S");
+++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    1945-11-22 18:36:29

print posixtostrc(97172340, "%B %d, %Y at %l:%M %p");
+++++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    January 29, 1973 at  4:19 PM

d = { 1193172342, 1203172342 };
s = posixtostrc(d, "%b %d, %Y");
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces s equal to:

::

    Oct 23, 2007
    Feb 16, 2008

Using the same d from above:

::

    s = posixtostrc(d, "%x %X");

produces s equal to:

::

    10/23/07 20:45:42
    02/16/08 14:32:22

Continuing with the same x from above:

::

    fmt = "Michael was born on %b %drd, %Y" $| "Jessica was born on %b %dth, %Y";
    s = posixtostrc(d, fmt);

produces s equal to:

::

    Michael was born on Oct 23rd, 2007
    Jessica was born on Feb 16th, 2008

.. seealso:: Functions :func:`dttostrc`, :func:`strctodt`, :func:`strctoposix`, :func:`dttostr`, :func:`strtodt`, :func:`dttoutc`, :func:`utctodt`
