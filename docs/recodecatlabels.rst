
recodeCatLabels
==============================================

Purpose
----------------

Change categorical variable labels.

Format
----------------
.. function:: x_new = recodeCatLabels(x, old_labels, new_labels [, column])

    :param x: data.
    :type x: NxK matrix

    :param old_labels: Categorical labels to be changed.
    :type old_labels: Mx1 string array

    :param new_labels: New labels use to replace the existing labels in *old_labels*.
    :type new_labels: Mx1 vector

    :param column: Optional argument, variables be recoded.
    :type column: scalar or string

    :return x_new: Data in *x* with categorical labels in *old_labels* replaced by those specified in *new_labels* for the variable specified by *column*.
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

  // Recode yarn_length variable from
  // 'low', 'medium', and 'high'
  //  to 'sm', 'md', 'lg'
  yarn_recoded = recodecatlabels(yarn, "low"$|"med"$|"high", "sm"$|"md"$|"lg", "yarn_length");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn_recoded, "yarn_length");

  // Print results
  print "Yarn recoded labels";

  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

.. seealso:: Functions :func:`getColLabels`, :func:`setColLabels`, :func:`reclassify` 
