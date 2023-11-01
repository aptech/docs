
dtminute
==============================================

Purpose
----------------

Extracts the minute component from a date/time variable as a number (0-59).

Format
----------------
.. function:: minutes = dtMinute(X [, columns])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Optional, names or indices of the date variable in *X* to get minutes from.
    :type columns: Jx1 Vector or string array

    :return minutes: the minutes component of the dates contained in the Jx1 columns specified by *columns*.
    :rtype minutes: NxJ Vector
    

Examples
----------------

::

  // Load data
  date_df = asDate("2008-02-16 18:36:29", "%Y-%m-%d %H:%M:%S");

  // Get minutes
  dtMinute(date_df);

This extracts the minute component:

::

  36

.. seealso:: Functions :func:`dtHour`, :func:`dtSecond`

