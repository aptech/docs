
getCategories
==============================================

Purpose
----------------

Returns the unique set of column labels for a categorical variable.

Format
----------------
.. function:: labels = getCategories(X [, columns])

    :param X: Data with metadata.
    :type X: NxK dataframe

    :param columns: Optional argument, name or index of the categorical variable in *X* to get labels from. Must be specified if *X* contains more than one column. Default = 1.
    :type columns: Scalar or string

    :return labels: Categorical labels assigned to variables specified by *columns*.
    :rtype labels: Dataframe


Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yarn.xlsx");
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  labels = getCategories(yarn, "yarn_length");

  print labels;


As we can see below, the variable name for the returned dataframe is *"categories"*.

::

    categories
          high
           low
           med

The returned dataframe contains both the string labels and the key values. Some functions need a string array as input. You can convert *labels* to a string array with :func:`ntos`:

::

    // Convert to a string array
    str_labels = ntos(labels);

    print str_labels;

::

          high
           low
           med


If you want to see the key values, you can use the :func:`asmatrix` function:

::

    // Convert to a numeric matrix
    // to see the key values
    numeric_keys = asmatrix(labels);
    
    print numeric_keys;

::

    0
    1
    2



.. seealso:: Functions :func:`dropcategories`, :func:`getColLabels`, :func:`setColLabels`

