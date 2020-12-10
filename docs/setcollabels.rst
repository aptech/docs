
setcollabels
==============================================

Purpose
----------------

Set categorical variable labels.

Format
----------------
.. function:: x_cat = setColLabels(X, labels, values, columns)

    :param X: data.
    :type X: NxK matrix or dataframe

    :param labels: Names or indices of the categorical variables in *X* to set labels for.
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

  x = { 3,
        2,
        0,
        4,
        2,
        1 };

  // Define labels
  labels = "poor"$|"fair"$|"average"$|"good"$|"excellent";

  /*
  ** Set labels
  */

  key_vals = { 0, 1, 2, 3, 4 };

  // Note that this makes 'x_cat' a dataframe
  // with a single categorical column
  x_cat = setColLabels(x, labels, key_vals, 1);

  print x_cat;


The code above prints the following:

::

              X1 
            good 
         average 
            poor 
       excellent 
         average 
            fair



.. seealso:: Functions :func:`getColLabels`, :func:`recodeCatLabels`, :func:`reorderCatLabels`
