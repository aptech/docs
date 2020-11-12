
setColDateFormats
==============================================

Purpose
----------------

Specifies how GAUSS should display dates using the BSD strftime format specifiers. Note that this will also convert the type of the columns specified by *index* to *Date*.

Format
----------------
.. function:: x_date = setColDateFormats(x, fmt, index)

    :param x: data.
    :type x: NxK matrix

    :param fmt: contains strftime date/time format characters.
    :type format: Mx1 string array

    :param index: index of variable containing dates.
    :type index: Mx1 scalar or string

    :return x_date: contains metadata assigning the date display format specified by *fmt* to the variables in *x* specified by *index*.
    :rtype x_date: NxK matrix


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
