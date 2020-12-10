
getcollabels
==============================================

Purpose
----------------

Returns the unique set of column labels and corresponding key values for a categorical variable.

Format
----------------
.. function:: { labels, keys } = getColLabels(X, columns)

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Name or index of the categorical variable in *X* to get labels from.
    :type columns: scalar or string

    :return labels: Categorical labels assigned to variables specified by *columns*.
    :rtype labels: string array

    :return keys: Integer key values corresponding to categorical labels assigned to the variables in *X* specified by *columns*.
    :rtype keys: vector

Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples/yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  { labels, keys } = getColLabels(yarn, "yarn_length");

  // Print results
  sprintf("%10s %10s", "Key", "Labels");
  sprintf("%10d %10s", keys, labels);

The code above prints the following table:

::

      Key     Labels

        0       high
        1        low
        2        med

.. seealso:: Functions :func:`setColLabels`
