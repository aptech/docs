
setBaseCat
==============================================

Purpose
----------------

Assign the label *basecase* to be the base case for the categorical variable specified by *columns* .

Format
----------------
.. function:: x_meta = setBaseCat(x, basecase [, columns])

    :param x: data.
    :type x: NxK matrix

    :param basecase: category to be set to base case.
    :type basecase: Mx1 string array

    :param columns: Optional argument, indicates columns of categorical variables to set base case for. Default = all columns.
    :type columns: Mx1 scalar or string

    :return x_meta: contains data with categorical base cases set to the categories specified in *basecase* for the variables in *columns* .
    :rtype x_meta: NxK dataframe


Remarks
-------------

Use :func:`reordercatlabels` to change the order of all category labels.

Examples
----------------

::

    // Load yarn data file
    fname = getGAUSSHome() $+ "examples/yarn.xlsx";
    yarn = loadd(fname, "cat(yarn_length) + cycles");

    // Get categorical labels for 'yarn_length'
    print "Original categorical labels:";
    getColLabels(yarn, "yarn_length");

    // Change base case to 'low'
    yarn = setBaseCat(yarn, "low", "yarn_length");

    print "";
    print "Updated categorical labels:";
    getColLabels(yarn, "yarn_length");


The above code will print out:

::

    Original categorical labels:

            high
             low
             med

       0.0000000
       1.0000000
       2.0000000

    Updated categorical labels:

             low
            high
             med 

       0.0000000
       1.0000000
       2.0000000



.. seealso:: Functions :func:`setColTypes`, :func:`getColLabels`, :func:`setColLabels`
