
dtday
==============================================

Purpose
----------------

Creates a matrix in DT scalar format containing only the year, month and day. Time of day information is zeroed out.

Format
----------------
.. function:: dtday(year, month, day)

    :param year: 
    :type year: NxK matrix of years

    :param month: 1-12.
    :type month: NxK matrix of months

    :param day: 1-31.
    :type day: NxK matrix of days

    :returns: dt (*NxK matrix*) of DT scalar format dates.



Remarks
-------

This amounts to 00:00:00 or midnight on the given day. The arguments
must be ExE conformable.



Source
------

time.src

