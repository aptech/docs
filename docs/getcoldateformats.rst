
getColDateFormats
==============================================

Purpose
----------------

Gets BSD strftime format specifiers for specified columns of a dataframe.

Format
----------------
.. function:: fmt_date = getColDateFormats(X [, columns])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Optional argument, The names or indices of the date columns to query. Default = all columns.
    :type columns: Mx1 scalar or string

    :return fmt_date: contains the strftime date/time format characters corresponding to the columns of *X* specified by *columns*.
    :rtype fmt_date: Mx1 string array


Examples
----------------

The dataset for this example has two variables, *TIMESTAMP* and *BIDPRICE*. It looks like this:

::

     TIMESTAMP  BIDPRICE
    1514826015   1.25505
    1514826196   1.25515
    1514826196   1.25518

The dates in the file are in POSIX time, seconds since Jan 1, 1970.

::

  // Load exchange rate data
  // First column is ticker times in POSIX format
  fname = getGAUSShome $+ "examples/usd_cad_2018.dat";
  usd_cad_2018 = loadd(fname);

  // Specify format to represent
  // Year-day-month Hour:Minute:Second
  fmt = "%Y-%m-%d %H:%M:%S";
  usd_cad_df = setColDateFormats(usd_cad_2018, fmt, "TIMESTAMP");

  // Get data format of "TIMESTAMP" variable
  fmt_timestamp = getColDateFormats(usd_cad_df, "TIMESTAMP");

.. note:: Column indices can also be used in place of the variable name like this, `getColDateFormats(usd_cad_df, 1)`

After the above code, the first few rows of *usd_cad_df* will look like this:

::

              TIMESTAMP   BIDPRICE
    2018-01-01 17:00:15    1.25505
    2018-01-01 17:03:16    1.25515
    2018-01-01 17:03:16    1.25518

and *fmt_time_stamp* will be equal to:

::

    %Y-%m-%d %H:%M:%S

.. seealso:: Functions :func:`dftype`, :func:`asdate`
