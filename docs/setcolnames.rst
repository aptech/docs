
setcolnames
==============================================

Purpose
----------------

Set column variable names.

Format
----------------
.. function:: x_meta = setColNames(x, varnames, index)

    :param x: data with metadata.
    :type x: NxK matrix,

    :param varnames: Names to apply to columns specified in *index*.
    :type varnames: Vector

    :param index: Specifies columns to be assigned names in *varnames*.
    :type index: Vector

    :return x_meta: Data with column names in *varnames* assigned to the columns in *index*.
    :rtype x_meta: Matrix


Examples
----------------

::

  // Generate random data matrix
  x = rndn(150, 3);

  // Assign variable names to all three columns
  // and create new matrix x_meta
  x_meta = setcolnames(x, "Planes"$|"Trains"$|"Automobiles");

  // Change variables name for first column of x_meta
  x_meta = setcolnames(x_meta, "Airplanes", "Planes");



.. seealso:: Functions :func:`getColNames`
