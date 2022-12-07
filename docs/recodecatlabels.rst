
recodeCatLabels
==============================================

Purpose
----------------

Change categorical variable labels.

Format
----------------
.. function:: X_new = recodeCatLabels(X, old_labels, new_labels [, column])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param old_labels: Categorical labels to be changed.
    :type old_labels: Mx1 string array

    :param new_labels: New labels use to replace the existing labels in *old_labels*.
    :type new_labels: Mx1 string array

    :param column: Optional argument, the name or index of the variable be recoded.
    :type column: scalar or string

    :return X_new: Data in *X* with categorical labels in *old_labels* replaced by those specified in *new_labels* for the variable specified by *column*.
    :rtype X_new: NxK dataframe



Remarks
-----------------

* To change the order of category labels, use :func:`reordercatlabels`.
* To set the base case, use :func:`setbasecat`. 
* The key -2147483648 is reserved, and usage could result in undefined behavior.

Examples
----------------

::

    // Load data
    fname = getGAUSSHome $+ "examples/yarn.xlsx";
    yarn = loadd(fname, "cat(yarn_length) + cycles");
    
    // Get column labels for yarn_length
    { labels, keys } = getColLabels(yarn, "yarn_length");
    
    // Print results
    print "Original yarn_length labels:";
    print ntos(keys)$~labels;
    
    // Recode yarn_length variable from
    // 'low', 'medium', and 'high'
    //  to 'sm', 'md', 'lg'
    yarn_recoded = recodecatlabels(yarn, "low"$|"med"$|"high", "sm"$|"md"$|"lg", "yarn_length");
    
    // Get column labels for yarn_length
    { labels, keys } = getColLabels(yarn_recoded, "yarn_length");
    
    // Print results
    print "";
    print "Recoded yarn labels";
    print ntos(keys)$~labels


the above code will print out the following:

::

     Original yarn_length labels:

               0             high 
               1              low 
               2              med 

     Recoded yarn labels:

               0               lg 
               1               sm 
               2               md 


.. seealso:: Functions :func:`getColLabels`, :func:`setColLabels`, :func:`reclassify`

