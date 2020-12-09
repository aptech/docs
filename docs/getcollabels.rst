
getcollabels
==============================================

Purpose
----------------

Returns the unique set of column labels and corresponding key values for a categorical or string variables.

Format
----------------
.. function:: { labels, keyvalues } = getColLabels(X, columns)

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: The names or indices of the categorical or string columns to query.
    :type columns: scalar or string

    :return labels: Labels assigned to variables specified by *columns*.
    :rtype labels: string array

    :return keyvalues: Key values corresponding to labels assigned to the variables in *X* specified by *columns*.
    :rtype keyvalues: vector

Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples/yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn, "yarn_length");

  // Print results
  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

The code above prints the following table:

::

      Key     Labels

       0       high
       1        low
       2        med

.. seealso:: Functions :func:`setColLabels`
