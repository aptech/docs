
recodeCatLabels
==============================================

Purpose
----------------

Change the order of categorical variable labels.

Format
----------------
.. function:: x_new = reorderCatLabels(x, labels [, column])

    :param x: data with metadata.
    :type x: NxK dataframe

    :param labels: Category labels list in their desired order.
    :type labels: Mx1 string array

    :param column: Optional argument, variables be recoded.
    :type column: scalar or string

    :return x_new: Data in *x* with categorical labels for the variable specified by *column* in the order specified by *labels*.
    :rtype x_new: NxK matrix


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples\\yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn, "yarn_length");

  // Print results
  print "Yarn labels";

  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

  // Reorder yarn_length variable from
  // 'low', 'med', and 'high'
  //  to 'high', 'med', 'low'
  yarn_recoded = reorderCatLabels(yarn, "high"$|"med"$|"low", "yarn_length");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn_recoded, "yarn_length");

  // Print results
  print "Reordered yarn_length labels";

  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

.. seealso:: Functions :func:`getColLabels`, :func:`setColLabels`, :func:`recodeCatLabels`, :func:`reclassify`
