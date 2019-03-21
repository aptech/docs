
getPreviousTradingDay
==============================================

Purpose
----------------

Returns the previous trading day.

Format
----------------
.. function:: getPreviousTradingDay(a)

    :param a: date in DT scalar format.
    :type a: scalar

    :returns: n (*scalar*), previous trading day in DT scalar format.



Remarks
-------

A trading day is a weekday that is not a holiday as defined by the New
York Stock Exchange from 1888 through 2006. Holidays are defined in
holidays.asc. You may edit that file to modify or add holidays.

