
dropCategories
==============================================

Purpose
----------------

Removes categories from a dataframe variable. Resets the keyvalues and labels for the variable.

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

  print labels;

The code above prints the following table of original labels:

::

    categories
          high
           low
           med

Using the :func:`frequency` function, we can see that the *yarn_length* column contains 9 observations of each category:

::

    print frequency(yarn, "yarn_length");

::

    Label      Count   Total %    Cum. %
     high          9     33.33     33.33
      low          9     33.33     66.67
      med          9     33.33       100
    Total         27       100        

Now, use :func:`dropCategories` to drop the `"high"` category and reprint the labels.

::

  // Drop the "high" category
  yarn = dropCategories(yarn, "high", "yarn_length");
 
  // Get updated column labels
  labels = getCategories(yarn, "yarn_length");

  print labels;

The code above prints the following table of updated labels:

::

    categories
           low
           med


Additionally, this time when we print the frequency report, we can see that the observations where *yarn_length* was equal to `"high"` have been removed.

::

    print frequency(yarn, "yarn_length");

::

    Label      Count   Total %    Cum. % 
      low          9        50        50 
      med          9        50       100 
    Total         18       100


.. seealso:: Functions :func:`dropunusedcategories`, :func:`getColLabels`, :func:`getCategories`, :func:`reordercatlabels`

