
reorderCatLabels
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
    :rtype x_new: NxK dataframe


Examples
----------------

::

    // Load data
    fname = getGAUSSHome $+ "examples/yarn.xlsx";
    yarn = loadd(fname, "cat(yarn_length) + cycles");
    
    // Get column labels for yarn_length
    { labels, keyvalues } = getColLabels(yarn, "yarn_length");
    
    // Print results
    print "Original yarn_length labels";
    print ntos(keyvalues)$~labels;
    
    
    // Reorder yarn_length variable from
    // 'low', 'med', and 'high'
    //  to 'high', 'med', 'low'
    yarn_recoded = reorderCatLabels(yarn, "high"$|"med"$|"low", "yarn_length");
    
    // Get column labels for yarn_length
    { labels, keyvalues } = getColLabels(yarn_recoded, "yarn_length");
    
    // Print results
    print "";
    print "Reordered yarn_length labels";
    print ntos(keyvalues)$~labels;


Remarks
----------

Use :func:`recodeCatLabels` to change the names of the category labels.


.. seealso:: Functions :func:`getColLabels`, :func:`setColLabels`, :func:`recodeCatLabels`, :func:`reclassify`
