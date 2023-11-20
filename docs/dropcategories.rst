
dropCategories
==============================================

Purpose
----------------

Removes categories and from dataframe. Resets the keyvalues and labels for the variable. 

Format
----------------
.. function:: df = dropCategories(X, categories, [, column])

    :param X: Data with metadata.
    :type X: NxK dataframe

    :param categories: The categories to be removed. 
    :type categories: String or string array
    
    :param column: Optional argument, name or index of the categorical variable in *X* which contains categories to be removed. Must be specified if *X* contains more than one column. Default = 1.
    :type column: Scalar or string

    :return df: Data with specified categories removed.
    :rtype df: NxK dataframe


Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yarn.xlsx");
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

Now, use :func:`dropCategories` to drop the `"high"` category and reprint labels.

::

  // Load data
  yarn = dropCategories(yarn, "high", "yarn_length");
  
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

