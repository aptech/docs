
setcolmetadata
==============================================

Purpose
----------------

Set columns in a matrix to have variable names and types.

Format
----------------
.. function:: x_meta = setColMetadata(x, varnames, types)

    :param x: data.
    :type x: NxK matrix

    :param varnames: Names to apply to column in *x*.
    :type varnames: Kx1 vector

    :param types: Specifies types to be assigned to names in *varnames*. Valid options include: ``"str"``, ``"date"``, ``"num"``, and ``"cat"``.
    :type types: Kx1 vector

    :return x_meta: Data with column names in *varnames* and types in *types* assigned to the columns.
    :rtype x_meta: NxK matrix


Examples
----------------

::

  // Generate random data matrix
  x = rndn(150, 3);

  // Specify types
  types = "num"|"num"|"num";

  // Specify variable names
  varnames = "Planes"$|"Trains"$|"Automobiles";

  // Assign variable names to all three columns
  // and create new matrix x_meta
  x_meta = setColMetadata(x, varnames, types);



.. seealso:: Functions :func:`setColNames`, :func:`setColLabels`, :func:`setColtypes`, :func:`setColDateFormats`
