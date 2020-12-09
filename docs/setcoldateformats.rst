
setColDateFormats
==============================================

Purpose
----------------

Specifies how GAUSS should display dates using the BSD strftime format specifiers. Note that this will also convert the type of the columns specified by *column* to *Date*.

Format
----------------
.. function:: x_date = setColDateFormats(X, fmt, columns)

    :param X: data.
    :type X: NxK matrix or dateframe

    :param fmt: contains strftime date/time format characters.
    :type fmt: Mx1 string array

    :param columns: The names or indices of the date columns in *X* to set format of.
    :type columns: Mx1 scalar or string

    :return x_date: contains metadata assigning the date display format specified by *fmt* to the variables in *x* specified by *columns*.
    :rtype x_date: NxK dataframe


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



.. seealso:: Functions :func:`setColtypes`, :func:`getColDateFormats`
