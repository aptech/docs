
getNextTradingDay
==============================================

Purpose
----------------

Returns the next trading day.

Format
----------------
.. function:: getNextTradingDay(a)

    :param a: date in DT scalar format.
    :type a: scalar

    :returns: n (*scalar*), next trading day in DT scalar format.


Remarks
-------

A trading day is a weekday that is not a holiday as defined by the New
York Stock Exchange from 1888 through 2006. Holidays are defined in
``holidays.asc``. You may edit that file to modify or add holidays.


Source
------

finutils.src

Globals
-------

`_fin_holidays`

.. seealso:: Functions :func:`getPreviousTradingDay`, :func:`annualTradingDays`

