
getcolnames
==============================================

Purpose
----------------

Returns the column variable names.

Format
----------------
.. function:: variable_names = getColNames(x, index)

    :param x: data with metadata.
    :type x: NxK matrix,

    :param index: Specifies columns in *x* to get variable names of.
    :type index: scalar or string

    :return variable_names: Variables names in matrix *x* for the columns specified by *index*.
    :rtype variable_names: string array


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples\\yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  getColNames(yarn, 1|2);

The code above prints the following:

::

  yarn_length
  amplitude

.. seealso:: Functions :func:`setColNames`
