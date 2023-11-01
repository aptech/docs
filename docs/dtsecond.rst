
dtSecond
==============================================

Purpose
----------------

Extracts the seconds component from a date/time variable as a number (0-60).

Format
----------------
.. function:: seconds = dtSecond(X [, columns])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Optional, names or indices of the date variable in *X* to get seconds from.
    :type columns: Jx1 Vector or string array

    :return seconds: the seconds components of the dates contained in the Jx1 columns specified by *columns*.
    :rtype seconds: NxJ Vector
    

Examples
----------------

::

  // Load data
  date_df = asDate("2008-02-16 18:36:29", "%Y-%m-%d %H:%M:%S");

  // Get seconds
  dtSecond(date_df);

This extracts the hour using the default 12-hr clock:

::

  29

.. seealso:: Functions :func:`dtHour`, :func:`dtMinute`

