
dttostrc
==============================================

Purpose
----------------

Converts a matrix containing dates in DT scalar format to a string array, using the BSD strftime format specifiers.

Format
----------------
.. function:: dttostrc(x, fmt)

    :param x: 
    :type x: NxK matrix containing dates in DT scalar format

    :param fmt: or  ExE conformable string array containing strftime date/time format characters.
    :type fmt: string

    :returns: sa (*TODO*), NxK string array.

Examples
----------------

dt = 20140317100312;
print dttostrc(dt, "%F");
++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    2014-03-17

print dttostrc(20110117151218, "%A, %B %dth, %Y");
++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    Monday, January 17th, 2011

print dttostrc(19411207074801, "Pearl Harbor was atacked on %B %d, %Y at %R %p");
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces the output:

::

    Pearl Harbor was atacked on December 07, 1941 at 07:48 AM

x = { 19120317060424, 19370904010928, 19510221031129 };
s = dttostrc(x, "%D");
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

produces s equal to:

::

    03/17/12
    09/04/37
    02/21/51

Continuing with the same x from above:

::

    fmt = "%A, %D" $| "%a, %F" $| "%v";
    s = dttostrc(x, fmt);

produces s equal to:

::

    Sunday, 03/17/12
     Sat, 1937-09-04
         21-FEB-1951

.. seealso:: Functions :func:`dttostr`, :func:`strctodt`, :func:`strtodt`, :func:`dttoutc`, :func:`posixtostrc`, :func:`strctoposix`, :func:`utctodt`
