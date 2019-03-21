
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

    :returns: dt (*TODO*), NxK matrix of DT scalar format dates.

