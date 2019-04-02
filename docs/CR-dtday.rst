
dtday
==============================================

Purpose
----------------

Creates a matrix in DT scalar format containing only the year, month and day. Time of day information is zeroed out.

Format
----------------
.. function:: dtday(year, month, day)

    :param year: NxK matrix of years 
    :type year: matrix

    :param month: NxK matrix of months. 1-12.
    :type month: matrix

    :param day: NxK matrix of days. 1-31.
    :type day: matrix

    :returns: dt (*NxK matrix*) of DT scalar format dates.

Remarks
-------

This amounts to 00:00:00 or midnight on the given day. The arguments must be ExE conformable.

Source
------

time.src

.. seealso:: Functions :func:`dttime`, :func:`dtdate`, :func:`utctodt`, :func:`dttostr`

