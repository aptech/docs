
setcolnames
==============================================

Purpose
----------------

Set column variable names.

Format
----------------
.. function:: x_meta = setColNames(x, varnames [, columns])

    :param x: data.
    :type x: NxK matrix,

    :param varnames: Names to apply to columns specified in *index*.
    :type varnames: Mx1 vector

    :param columns: Specifies columns to be assigned names in *varnames*.
    :type columns: Mx1 vector

    :return x_meta: Data with column names in *varnames* assigned to the columns in *columns*.
    :rtype x_meta: NxK matrix


Examples
----------------

::

  // Generate random data matrix
  x = rndn(150, 3);

  // Assign variable names to all three columns
  // and create new matrix x_meta
  x_meta = setColNames(x, "Planes"$|"Trains"$|"Automobiles");

  // Change variable name of first column of x_meta
  x_meta = setColNames(x_meta, "Airplanes", "Planes");

.. seealso:: Functions :func:`getColNames`
