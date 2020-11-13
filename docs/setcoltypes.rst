
setcoltypes
==============================================

Purpose
----------------

Set columns in a matrix to have metadata types.

Format
----------------
.. function:: x_meta = setColTypes(x, types [, columns])

    :param x: data.
    :type x: NxK matrix

    :param types: Specifies types to be assigned to columns specified in *columns*. Valid options include: ``"string"``, ``"date"``, ``"numeric"``, and ``"category"``.
    :type types: Mx1 vector

    :param columns: Optional argument, specifies columns to be assigned types in *types*. Default = all columns.
    :type columns: Mx1 vector

    :return x_meta: Data with the types specified in *types* assigned to the columns specified in *columns*.
    :rtype x_meta: NxK matrix


Examples
----------------

::

  // Load exchange rate data
  // First column is ticker times
  // but is in POSIX time
  fname = getGAUSShome $+ "examples/usd_cad_2018.dat";
  usd_cad_2018 = loadd(fname);

  // Specify first column to be a date
  x_meta = setColTypes(usd_cad_2018, "date", 1);



.. seealso:: Functions :func:`setColNames`, :func:`setColLabels`, :func:`setColMetadata`, :func:`setColDateFormats`
