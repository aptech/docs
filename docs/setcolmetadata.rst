
setcolmetadata
==============================================

Purpose
----------------

Set columns in a matrix to have variable names and types.

Format
----------------
.. function:: x_meta = setColMetadata(X, varnames, types)

    :param X: data.
    :type X: NxK matrix

    :param varnames: Names to apply to column in *X*.
    :type varnames: Kx1 vector

    :param types: Specifies types to be assigned to names in *varnames*. Valid options include: ``"string"``, ``"date"``, ``"numeric"``, and ``"category"``.
    :type types: Kx1 vector

    :return x_meta: Data with column names in *varnames* and types in *types* assigned to the columns.
    :rtype x_meta: NxK dataframe


Examples
----------------

::

  // Generate random data matrix
  x = rndn(150, 3);

  // Specify types
  types = "numeric"|"numeric"|"numeric";

  // Specify variable names
  varnames = "Planes"$|"Trains"$|"Automobiles";

  // Assign variable names to all three columns
  // and create new matrix x_meta
  x_meta = setColMetadata(x, varnames, types);



.. seealso:: Functions :func:`setColNames`, :func:`setColLabels`, :func:`setColtypes`, :func:`setColDateFormats`
