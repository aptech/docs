
elapsedTradingDays
==============================================

Purpose
----------------

Computes number of trading days between two dates inclusively.

Format
----------------
.. function:: n_days = elapsedTradingDays(t_start, t_end)

    :param t_start: date in DT scalar format.
    :type t_start: scalar

    :param t_end: date in DT scalar format.
    :type t_end: scalar

    :return n_days: number of trading days between dates inclusively, that is,
        elapsed time includes the dates *t_start* and *t_end*.

    :rtype n_days: Scalar

Examples
----------------

::

    // September 10, 2015
    t_start = 20150910110231;

    // September 28, 2015
    t_end = 20150928080722;

    n_days = elapsedTradingDays(t_start, t_end);

::

    n_days = 12

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


`\_fin_holidays`

.. seealso:: Functions :func:`getNextTradingDay`, :func:`getPreviousTradingDay`, :func:`getNextWeekDay`, :func:`getPreviousWeekDay`
