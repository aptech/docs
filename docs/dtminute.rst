
dtMinute
==============================================

Purpose
----------------

Extracts the minute component from a date/time variable as a number (0-59).

Format
----------------
.. function:: minutes = dtMinute(X [, column])

    :param X: data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get minutes from.
    :type column: Scalar or string

    :return minutes: The minutes component of the dates contained in the column specified by *column*.
    :rtype minutes: Tx1 vector
    

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

