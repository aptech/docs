
getNextWeekDay
==============================================

Purpose
----------------

Returns the next day that is not on a weekend.

Format
----------------
.. function:: n = getNextWeekDay(a)

    :param a: date in DT scalar format.
    :type a: scalar

    :return next_week: next week day in DT scalar format.

    :rtype next_week: scalar

Examples
----------------

::

   // Convert string to date to dt date
   dt_date = strtodt("2010-10-29", "YYYY-MO-DD");

   /*
   ** Get next trading day and print
   ** string form
   */
   dttostr(getNextWeekDay(dt_date), "YYYY-MO-DD");

This prints the next trading weekday to the screen in string format

::

   2010-11-01

Source
------

finutils.src

.. seealso:: Functions :func:`getPreviousWeekDay`
