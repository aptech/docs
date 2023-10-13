
getcategories
==============================================

Purpose
----------------

Returns the unique set of column labels for a categorical variable.

Format
----------------
.. function:: labels = getCategories(X [, columns])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Optional argument, Name or index of the categorical variable in *X* to get labels from. Must be specified if *X* contains more than one column. Default = 1.
    :type columns: scalar or string

    :return labels: Categorical labels assigned to variables specified by *columns*.
    :rtype labels: string array


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples/yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  labels = getCategories(yarn, "yarn_length");

  // Print results
  sprintf("%10s", "Labels");
  sprintf("%10s", labels);

The code above prints the following table:

::

      Labels

        high
        low
        med

.. seealso:: Functions :func:`getColLabels`

