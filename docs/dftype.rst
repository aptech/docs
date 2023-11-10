
dftype
==============================================

Purpose
----------------

Set the types of columns in a matrix or dataframe.

Format
----------------
.. function:: x_meta = dfType(X, types [, columns])

    :param X: data.
    :type X: NxK matrix

    :param types: Specifies types to be assigned to columns specified in *columns*. Valid options include: ``"string"``, ``"date"``, ``"number"``, and ``"category"``.
    :type types: Mx1 vector

    :param columns: Optional argument, indices of columns in *X* to assign types to. Default = all columns.
    :type columns: Mx1 vector

    :return x_meta: Data with the types specified in *types* assigned to the columns specified in *columns*.
    :rtype x_meta: NxK dataframe


Remarks
------------------

Date Variables
++++++++++++++++

When a numeric column is set to type ``date`` with :func:`dftype`:

* The data from the column is interpreted as POSIX time (seconds since Jan 1, 1970).
* The default date format will be used. This can be changed with :func:`asdate`.

Categorical and String  Variables
++++++++++++++++++++++++++++++++++++

When a numeric column is set to type ``category``, or ``string``  with :func:`dftype`:

* The labels will be the string version of the number. The keys will be integers from 0 to ``n-1``, where ``n`` is the number of unique values in the original data. The keys will be assigned to the labels such that the original order is maintained.

When a categorical or string variable is converted to a numeric column;

* The updated column will contain the numeric keys associated with the string or category labels.


Examples
----------------

Example 1: POSIX time numeric column to date column
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    secs_per_day = 24 * 60 * 60;

    // Create a 2x1 vector
    x = 0 | secs_per_day;

    // Set the numeric vector to be a date
    x = dftype(x, "date", 1);
    print x;

Since the date vector is interpreted as seconds since Jan 1, 1970, the code above will print:

::

              X1
      1970-01-01
      1970-01-02


Example 2: Category to number
+++++++++++++++++++++++++++++++++++++

::

    // Load 'cycles' and load 'amplitude' as a categorical variable
    fname = getGAUSSHome("examples/yarn.xlsx");
    yarn = loadd(fname, "cat(amplitude) + cycles");

    // Set the first column to be a numeric column
    yarn_n = dftype(yarn, "number", 1);


After the above code, the first few rows look like this:

::

    yarn = amplitude   cycles   yarn_n = amplitude   cycles
                 low      674                    1      674
                 low      370                    1      370
                 low      292                    1      292
                 med      338                    2      338

Example 3: Integer column to category
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 4,
          1,
          4,
          6 };

    // Make 'x' a dataframe and set its
    // only column to be a category
    x = dftype(x, "category");

After the above code, *x* will be a datframe as shown below:

::

    X1
     4
     1
     4
     6

We can get the categorical labels and key values like this:

::

    { labels, keys } = getcollabels(x, 1);

They will equal:

::

    labels = "1"   keys = 0
             "4"          1
             "6"          2

We can set new labels with :func:`recodecatlabels` like this:

::

    // Set the labels for 0, 1, and 2 to be
    // alpha, beta and gamma
    x = recodecatlabels(x, labels, "alpha"$|"beta"$|"gamma", 1);

Now *x* will be the following dataframe:

::

              X1
            beta
           alpha
            beta
           gamma


.. seealso:: Functions :func:`dfName`, :func:`setColLabels`, :func:`asdf`, :func:`asDate`
