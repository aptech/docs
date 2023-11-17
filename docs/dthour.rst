
dtHour
==============================================

Purpose
----------------

Extracts the hour component from a date/time variable as a number (1-12 or 1-24).

Format
----------------
.. function:: hour = dtHour(X [, column, twenty_four])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get hours from.  Default = first column.
    :type column: Scalar or string

    :param twenty_four: Optional, indicator variable to specify twenty-four hour clock (0-23). Set to 1 to use 24-hr clock names. Default = 0.
    :type twenty_four: Scalar
    
    :return hour: The hour of the dates in the column specified by *column*.
    :rtype hour: Tx1 Vector
    

Examples
----------------

::

  // Load data
  date_df = asDate("2008-02-16 18:36:29", "%Y-%m-%d %H:%M:%S");

  // Get hours
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

