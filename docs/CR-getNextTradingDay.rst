
getNextTradingDay
==============================================

Purpose
----------------

Returns the next trading day.

Format
----------------
.. function:: n = getNextTradingDay(a)

    :param a: date in DT scalar format.
    :type a: scalar

    :return next_day: next trading day in DT scalar format.

    :rtype next_day: scalar

Examples
----------------

::

    // Convert string to date to dt date
    dt_date = strtodt("2012-07-12", "YYYY-MO-DD");

    /*
    ** Get next trading day and print
    ** string form
    */
    dttostr(getNextTradingDay(dt_date), "YYYY-MO-DD");

This prints the next trading day to the screen in string format

::

    2012-07-13


Remarks
-------

A trading day is a weekday that is not a holiday as defined by the New
York Stock Exchange from 1888 through 2020. Holidays are defined in
:file:`holidays.asc`. You may edit that file to modify or add holidays.


Source
------

finutils.src

Globals
-------

`_fin_holidays`

.. seealso:: Functions :func:`getPreviousTradingDay`, :func:`annualTradingDays`
