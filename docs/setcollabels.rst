
setcollabels
==============================================

Purpose
----------------

Set categorical variable labels.

Format
----------------
.. function:: x_meta = setColLabels(x, labels, values, index)

    :param x: data.
    :type x: NxK matrix

    :param labels: Categorical labels to assign to each value in *values*.
    :type labels: Mx1 string array

    :param values: Values corresponding to the labels specified in *labels*.
    :type values: Mx1 vector

    :param index: Index of variable to assign labels to.
    :type index: scalar or string

    :return x_meta: Vector with metadata assigning the categorical labels in *labels* to values specified in *values*.
    :rtype labels: Nx1 vector


Examples
----------------

::

  // Generate random categorical variable
  cat_var = rndi(100, 1, 1|5);

  // Define labels
  labels = "poor"$|"fair"$|"average"$|"good"$|"excellent";

  // Set labels
  // Note that this assigns metadata to cat_var
  cat_var = setcollabels(cat_var, labels, unique(cat_var), 1);

  // Get column labels for cat_var
  { labels, keyvalues } = getColLabels(cat_var, 1);

  // Print results
  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

The code above prints the following table:

::

    Key     Labels

     1       poor
     2       fair
     3    average
     4       good
     5  excellent

.. seealso:: Functions :func:`getColLabels`
