
dropCategory
==============================================

Purpose
----------------

Removes category from dataframe and category labels. Resets the keyvalues and labels for the variable, keeps the original keyvalue, label pairs from the full dataset. 

Format
----------------
.. function:: df = dropCategory(X, category, [, columns])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param category: The categories to be removed. 
    :type category: String or string array
    
    :param columns: Optional argument, Name or index of the categorical variable in *X* to get labels from. Must be specified if *X* contains more than one column. Default = 1.
    :type columns: scalar or string

    :return df: Data with specified category removed.
    :rtype df: NxK dataframe


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

The code above prints the following table of original labels:

::

      Labels

        high
         low
         med

Now, use :func:`dropCategory` to drop the high category and reprint labels.

::

  // Load data
  yarn = dropCategory(yarn, "high", "yarn_length");
  
  // Get column labels for yarn_length
  labels = getCategories(yarn, "yarn_length");

  // Print results
  sprintf("%10s", "Labels");
  sprintf("%10s", labels);

The code above prints the following table of updated labels:

::

      Labels

         low
         med


.. seealso:: Functions :func:`getColLabels`, :func:`getCategories`

