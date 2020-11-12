
setcoltypes
==============================================

Purpose
----------------

Set columns in a matrix to have metadata types.

Format
----------------
.. function:: x_meta = setcolmetadata(x, types, index)

    :param x: data.
    :type x: NxK matrix

    :param types: Specifies types to be assigned to columns specified in *index*. Valid options include: ``"str"``, ``"date"``, ``"num"``, and ``"cat"``.
    :type types: Mx1 vector

    :param index: Specifies columns to be assigned types in *types*.
    :type index: Mx1 vector

    :return x_meta: Data with the types specified in *types* assigned to the columns specified in *index*.
    :rtype x_meta: NxK matrix


Examples
----------------

::

  // Load exchange rate data
  // First column is ticker times
  // but is in POSIX time
  usd_cad_2018 = loadd("D:/svn/apps/rtl/examples/usd_cad_2018.dat");

  // Specify first column to be a date
  x_meta = setcoltypes(usd_cad_2018, "date", 1);



.. seealso:: Functions :func:`setColNames`, :func:`setColLabels`, :func:`setcolmetadata`, :func:`setColDateFormats`
