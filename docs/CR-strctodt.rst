
strctodt
==============================================

Purpose
----------------

Converts string dates to a matrix containing dates in DT Scalar date/time format, using the BSD strftime format specifiers.

Format
----------------
.. function:: strctodt(x, fmt)

    :param x: 
    :type x: NxK string array containing dates

    :param fmt: or  ExE conformable string array containing strftime date/time format characters.
    :type fmt: string

    :returns: d (*NxK matrix*), containing dates in DT Scalar format (i.e. 200803170930).

Examples
----------------

print strctodt("2012/06/23", "%Y/%m/%d");
+++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    20120623000000

print strctodt("1945-11-22 18:36:29", "%Y-%m-%d %H:%M:%S");
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    19451122183629

print strctodt("January 29, 1973 at  4:19 PM", "%B %d, %Y at %l:%M %p");
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    19730129161900

ds = "Oct 23, 2007" $| "Feb 16, 2008";
s = strctodt(ds, "%b %d, %Y");
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces s equal to:

::

    20071023000000 
    20080216000000

ds = "10/23/07 20:45:42" $| "02/16/08 14:32:22";
s = strctodt(ds, "%x %X");
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces s equal to:

::

    20071023204542 
    20080216143222

.. seealso:: Functions :func:`posixtostrc`, :func:`dttostrc`, :func:`strtodt`, :func:`dttoutc`, :func:`utctodt`
