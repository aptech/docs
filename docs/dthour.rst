
dthour
==============================================

Purpose
----------------

Extracts the hour component from a date/time variable as a number (1-12 or 1-24).

Format
----------------
.. function:: hour = dtHour(X [, columns, twenty_four])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Optional, names or indices of the date variable in *X* to get hours from.
    :type columns: Jx1 Vector or string array

    :param twenty_four: Optional, indicator variable to specify twenty-four clock (0-23). Set to 1 to use 24-hr clock names. Default = 0.
    :type twenty_four: Scalar
    
    :return hour: the hour component of the dates contained in the Jx1 columns specified by *columns*.
    :rtype hour: NxJ Vector
    

Examples
----------------

::

  // Load data
  date_df = asDate("2008-02-16 18:36:29", "%Y-%m-%d %H:%M:%S");

  // Get hour
  dtHour(date_df);

This extracts the hour using the default 12-hr clock:

::

  6

To use the 24-hr clock:

::

  // Load data
  date_df = asDate("2008-02-16 18:36:29", "%Y-%m-%d %H:%M:%S");

  // Get hour
  dtHour(date_df, 1, 1);

::

  18
    

.. seealso:: Functions :func:`dtSecond`, :func:`dtMinute`

