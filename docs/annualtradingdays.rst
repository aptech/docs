
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

    :return n: number of trading days in year.

    :rtype n: scalar

Remarks
-------

A trading day is a weekday that is not a holiday as defined by the New
York Stock Exchange from 1888 through 2020. Holidays are defined in
``holidays.asc``. You may edit that file to modify or add holidays.

Globals
-------

.. data:: _fin_annualTradingDays

.. data:: _fin_holidays

Examples
--------

::

    // Get the number of NYSE trading days in 2023
    n = annualTradingDays(2023);
    print (n);

The above code sets *n* to 250.

::

    // Compare trading days across years
    for i (2020, 2024, 1);
        n = annualTradingDays(i);
        print i;; print " trading days: ";; print n;
    endfor;

Source
------

finutils.src

.. seealso:: Functions :func:`elapsedTradingDays`, :func:`getNextTradingDay`, :func:`getPreviousTradingDay`, :func:`getNextWeekDay`, :func:`getPreviousWeekday` 

