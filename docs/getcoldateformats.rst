
getColDateFormats
==============================================

Purpose
----------------

Gets  BSD strftime format specifiers for the columns in *x* specified by *index* .

Format
----------------
.. function:: fmt_date = getColDateFormats(x, index)

    :param x: data.
    :type x: NxK matrix

    :param index: index of variables containing dates.
    :type index: Mx1 scalar or string

    :return fmt_data: contains the strftime date/time format characters corresponding to the columns of *x* specified by *index*.
    :rtype fmt_data: Mx1 string array


Examples
----------------

::

  // Load exchange rate data
  // First column is ticker times
  // but is in POSIX time
  fname = getGAUSShome $+ "examples/usd_cad_2018.dat";
  usd_cad_2018 = loadd(fname);

  // Specify format to represent
  // Year-day-month Hour:Minute:Second
  fmt = "%Y-%m-%d %H:%M:%S";
  x_meta = setColDateFormats(usd_cad_2018, fmt, "TIMESTAMP");

  // Get data format of "TIMESTAMP" function
  fmt_timestamp = getColDateFormats(x_meta, "TIMESTAMP");

.. seealso:: Functions :func:`setColtypes`, :func:`getColDateFormats`
