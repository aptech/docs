
annualTradingDays
==============================================

Purpose
----------------
Computes number of trading days in a given year.

Format
----------------
.. function:: n = annualTradingDays(a)

    :param a: year.
    :type a: scalar

    :returns: n (*scalar*), number of trading days in year.

Remarks
-------

A trading day is a weekday that is not a holiday as defined by the New
York Stock Exchange from 1888 through 2020. Holidays are defined in
`holidays.asc`. You may edit that file to modify or add holidays.

Globals
-------

.. data::  \_fin_annualTradingDays

.. data::  \_fin_holidays

Source
------

finutils.src

.. seealso:: Functions :func:`elapsedTradingDays`, :func:`getNextTradingDay`, :func:`getPreviousTradingDay`, :func:`getNextWeekDay`, :func:`getPreviousWeekday` 

