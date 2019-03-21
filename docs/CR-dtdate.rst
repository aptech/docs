
dtdate
==============================================

Purpose
----------------

Creates a matrix in DT scalar format.

Format
----------------
.. function:: dtdate(year, month, day, hour, minute, second)

    :param year: 
    :type year: NxK matrix of years

    :param month: 1-12.
    :type month: NxK matrix of months

    :param day: 1-31.
    :type day: NxK matrix of days

    :param hour: 0-23.
    :type hour: NxK matrix of hours

    :param minute: 0-59.
    :type minute: NxK matrix of minutes

    :param second: 0-59.
    :type second: NxK matrix of seconds

    :returns: dt (*TODO*), NxK matrix of DT scalar format dates.



Remarks
-------

The arguments must be ExE conformable.



Source
------

time.src

