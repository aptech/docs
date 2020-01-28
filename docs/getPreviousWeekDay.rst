
getPreviousWeekDay
==============================================

Purpose
----------------

Returns the previous day that is not on a weekend.

Format
----------------
.. function:: prev_weekday = getPreviousWeekDay(date)

    :param date: date in DT scalar format.
    :type date: scalar

    :return prev_weekday: previous weekday in DT scalar format.

    :rtype prev_weekday: scalar

Examples
----------------

::

  // Convert string to date to dt date
  dt_date = strtodt("2010-11-01", "YYYY-MO-DD");

  /*
  ** Get next trading day and print
  ** string form
  */
  dttostr(getPreviousWeekDay(dt_date), "YYYY-MO-DD");

This prints the previous trading weekday to the screen in string format

::

   2010-10-29


Source
------

finutils.src

.. seealso:: Functions :func:`getNextWeekDay`
