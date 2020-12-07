
getcollabels
==============================================

Purpose
----------------

Returns the unique set of column labels and corresponding key values for a categorical variable.

Format
----------------
.. function:: { labels, keyvalues } = getColLabels(x, columns)

    :param x: data with metadata.
    :type x: NxK dataframe

    :param columns: Categorical variable in *x* to get labels from.
    :type columns: scalar or string

    :return labels: Categorical labels assigned to variables specified by *columns*.
    :rtype labels: string array

    :return keyvalues: Key values corresponding to categorical labels assigned to the variables in *x* specified by *columns*.
    :rtype keyvalues: vector

Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples\\yarn.xlsx";
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
