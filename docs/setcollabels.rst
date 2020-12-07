
setcollabels
==============================================

Purpose
----------------

Set categorical variable labels.

Format
----------------
.. function:: x_meta = setColLabels(x, labels, values, columns)

    :param x: data.
    :type x: NxK matrix or dataframe

    :param labels: Categorical labels to assign to each value of *x[., columns]* specified in *values*.
    :type labels: Mx1 string array

    :param values: Values to assign labels to.
    :type values: Mx1 vector

    :param columns: Variables to assign the labels to.
    :type columns: scalar or string

    :return x_cat: Contains metadata assigning the categorical labels in *labels* to values specified in *values* for the variable specified by *columns*.
    :rtype x_cat: NxK dataframe


Examples
----------------

::

  // Generate random categorical variable
  x = rndi(100, 1, 1|5)~rndn(100, 3);

  // Define labels
  labels = "poor"$|"fair"$|"average"$|"good"$|"excellent";

  // Set labels
  // Note that this assigns metadata to x
  x_cat = setColLabels(x, labels, unique(x[., 1]), 1);

  // Get column labels for x_cat
  { labels, keyvalues } = getColLabels(x_cat, 1);

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
