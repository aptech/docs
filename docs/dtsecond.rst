
dtSecond
==============================================

Purpose
----------------

Extracts the seconds component from a date/time variable as a number (0-59).

Format
----------------
.. function:: seconds = dtSecond(X [, column])

    :param X: Data with metadata.
    :type X: Txk dataframe

    :param column: Optional, name or index of the date variable in *X* to get seconds from. Default = first column.
    :type column: Scalar or string

    :return seconds: The seconds of the dates in the column specified by *column*.
    :rtype seconds: Tx1 vector
    

Examples
----------------

::

  // Create a date
  date_df = asDate("2008-02-16 18:36:29", "%Y-%m-%d %H:%M:%S");

  // Get seconds
  dtSecond(date_df);

This extracts the seconds:

::

  29


Remarks
----------
This function only works with dataframes. It does not work with DT Scalars.

.. seealso:: Functions :func:`dtHour`, :func:`dtMinute`

