
getcolnames
==============================================

Purpose
----------------

Returns the column variable names.

Format
----------------
.. function:: varnames = getColNames(x, index)

    :param x: data with metadata.
    :type x: NxK matrix

    :param index: Specifies columns in *x* to get variable names of.
    :type index: Kx1 vector

    :return varnames: Variable names in matrix *x* for the columns specified by *index*.
    :rtype varnames: Kx1 string array


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples\\yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for first and second
  // column in yarn
  getColNames(yarn, 1|2);

The code above prints the following:

::

  yarn_length
  amplitude

.. seealso:: Functions :func:`setColNames`
