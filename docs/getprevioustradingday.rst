
getPreviousTradingDay
==============================================

Purpose
----------------

Returns the previous trading day.

Format
----------------
.. function:: prev_date = getPreviousTradingDay(a)

    :param date: date in DT scalar format.
    :type date: scalar

    :return prev_date: previous trading day in DT scalar format.

    :rtype prev_date: scalar

Examples
----------------

::

    // Convert string to date to dt date
    dt_date = strtodt("2012-07-12", "YYYY-MO-DD");

    /*
    ** Get next trading day and print
    ** string form
    */
    dttostr(getPreviousTradingDay(dt_date), "YYYY-MO-DD");

This prints the previous trading day to the screen in string format

::

    2012-07-11

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

.. seealso:: Functions :func:`getNextTradingDay`
