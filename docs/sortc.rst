
sortc
==============================================

Purpose
----------------

Sorts a matrix, dataframe or string array.

Format
----------------
.. function:: y = sortc(x [, c])

    :param x: data
    :type x: NxK matrix, dataframe or string array.

    :param c: Optional input, specifies the column(s) of *x* to sort on. Default=1.
    :type c: scalar, column vector or string array.

    :return y: equal to *x* and sorted on the column(s) represented by *c*.

    :rtype y: NxK matrix, dataframe or string array.

Examples
----------------

Sort rows of a matrix based upon first column
+++++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 4 7 3,
          1 3 2,
          3 4 8 };

    // Sort 'x' based upon the first column
    y = sortc(x);

The above example code produces *y* equal to:

::

    1 3 2
    3 4 8
    4 7 3


Sort rows of a dataframe based on multiple columns
+++++++++++++++++++++++++++++++++++++++++++++++++++++

This example will demonstrate sorting a dataframe on a single column, and then on two combinations of two columns.

First we will load the data and print it out.

::

    // Get file name with full path
    fname = getGAUSSHome() $+ "examples/tips2.dta";

    // Load 3 variables from dataset
    tips = loadd(fname, "size + tip + sex");

    // Index the first 10 observations
    tips = tips[1:10,.];

    print "original = ";
    tips;

will print out:

::

    original

            size              tip              sex
       2.0000000        1.0100000           Female
       3.0000000        1.6600000             Male
       3.0000000        3.5000000             Male
       2.0000000        3.3100000             Male
       4.0000000        3.6100000           Female
       4.0000000        4.7100000             Male
       2.0000000        2.0000000             Male
       4.0000000        3.1200000             Male
       2.0000000        1.9600000             Male
       2.0000000        3.2300000             Male

Next we will sort the data based on the first column. We do not need to specify which column to sort on since the first column is the default.

::

    print "sorted on 1st column";
    sortc(tips);

will print out:

::

    sorted on 1st column

            size              tip              sex
       2.0000000        1.0100000           Female
       2.0000000        3.3100000             Male
       2.0000000        2.0000000             Male
       2.0000000        1.9600000             Male
       2.0000000        3.2300000             Male
       3.0000000        1.6600000             Male
       3.0000000        3.5000000             Male
       4.0000000        3.6100000           Female
       4.0000000        4.7100000             Male
       4.0000000        3.1200000             Male


This time we will sort the ``tips`` dataframe on ``size`` and then ``tip``.

::

    print "sorted on 1st column then 2nd column";
    sortc(tips, "size" $| "tip");


will print out the following. Notice that ``tip`` column is now sorted for every category of ``size``.

::

    sorted on 1st column then 2nd column

            size              tip              sex
       2.0000000        1.0100000           Female
       2.0000000        1.9600000             Male
       2.0000000        2.0000000             Male
       2.0000000        3.2300000             Male
       2.0000000        3.3100000             Male
       3.0000000        1.6600000             Male
       3.0000000        3.5000000             Male
       4.0000000        3.1200000             Male
       4.0000000        3.6100000           Female
       4.0000000        4.7100000             Male

Finally, we will reverse the order of the sort variables to make sure that behavior is clear.
::

    print "sorted on 2nd column then 1st column";
    sortc(tips, "tip" $| "size");


Notice that this time, all the ``tip`` observations are in sequential order. However, since there are no ties in the ``tip`` variable, this is the same result we would get if we only sorted on the ``tip`` column.

::

    sorted on 2nd column then 1st column

            size              tip              sex
       2.0000000        1.0100000           Female
       3.0000000        1.6600000             Male
       2.0000000        1.9600000             Male
       2.0000000        2.0000000             Male
       4.0000000        3.1200000             Male
       2.0000000        3.2300000             Male
       2.0000000        3.3100000             Male
       3.0000000        3.5000000             Male
       4.0000000        3.6100000           Female
       4.0000000        4.7100000             Male


Sorting on categorical variables
++++++++++++++++++++++++++++++++++++

By default categorical variables are sorted by their underlying key value. We will start by loading our data and taking a sample.

::

    // Get file name with full path
    fname = getGAUSSHome() $+ "examples/tips2.dta";

    // Load 2 variables from dataset
    tips = loadd(fname, "sex + size");

    // Take a repeatable random sample
    rndseed 72917;
    tips = sampleData(tips, 10);

    print tips;

::

             sex             size
            Male        2.0000000
            Male        2.0000000
          Female        2.0000000
          Female        3.0000000
            Male        2.0000000
            Male        2.0000000
          Female        1.0000000
          Female        2.0000000
            Male        2.0000000
          Female        3.0000000

Before we sort this data, let's get the categorical keys and compare them to the printed labels.

::

    { label, k } = getcollabels(tips, "sex");


Running the above code will show us the labels and their corresponding keys.

::

    label = Female    k = 0.0000
              Male        1.0000



Therefore when we sort the data on the ``sex`` variable:

::

    print "sorted on 1st column";
    sortc(tips);

we see that ``Female`` is first and ``Male`` is second. This is because the key for ``Female`` is zero, not because ``Female`` comes before ``Male`` alphabetically. See :func:`reordercatlabels` to see how to set the order for the categories.

::

             sex             size
          Female        2.0000000
          Female        3.0000000
          Female        1.0000000
          Female        2.0000000
          Female        3.0000000
            Male        2.0000000
            Male        2.0000000
            Male        2.0000000
            Male        2.0000000
            Male        2.0000000

Sort rows of a 5x1 string vector
++++++++++++++++++++++++++++++++

::

    // Create a 5x1 string array, using the string
    // vertical concatenation operator '$|'
    letters = "epsilon" $|
              "gamma" $|
              "beta" $|
              "alpha" $|
              "delta";

    // Sort 'letters'
    letters_s = sortc(letters, 1);

The above example code produces, *letters_s* equal to:

::

      alpha
       beta
      delta
    epsilon
      gamma


Remarks
-------

-  These functions will sort the rows of a matrix with respect to a
   specified column. That is, they will sort the elements of a column
   and will arrange all rows of the matrix in the same order as the
   sorted column.
-  Missing values will sort as if their value is below :math:`-\infty`.
-  The sort will be in ascending order.
-  This function uses the Quicksort algorithm.
-  If you need to obtain the matrix sorted in descending order, you can use:

   ::

      rev(sortc(x, c))

.. seealso:: Functions :func:`getcollabels`, :func:`reordercatlabels`, :func:`rev`, :func:`sortind`, :func:`unique`
