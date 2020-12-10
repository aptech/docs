
setcoltypes
==============================================

Purpose
----------------

Set columns in a matrix to have metadata types.

Format
----------------
.. function:: x_meta = setColTypes(X, types [, columns])

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

When a numeric column is set to type ``date`` with :func:`setcoltypes`: 

* The data from the column is interpreted as POSIX time (seconds since Jan 1, 1970).
* The default date format will be used. This can be changed with :func:`setcoldateformats`.

Categorical and String  Variables
++++++++++++++++++++++++++++++++++++

When a numeric column is set to type ``category``, or ``string``  with :func:`setcoltypes`: 

* Each value will be converted to an integer to create the keys. The labels will be the string version of the number.


Examples
----------------

Example 1: POSIX time numeric column to date column
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    secs_per_day = 24 * 60 * 60;

    // Create a 2x1 vector
    x = 0 | secs_per_day;

    // Set the numeric vector to be a date
    x = setcoltypes(x, "date", 1);
    print x;

Since the date vector is interpreted as seconds since Jan 1, 1970, the code above will print:

::

              X1 
      1970-01-01 
      1970-01-02



Example 2: Integer column to category 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 1,
          0,
          1,
          2 };

    // Make 'x' a dataframe and set its
    // only column to be a category
    x = setcoltypes(x, "category", 1);

After the above code, *x* will be a datframe as shown below:

::

    X1
     1
     0
     1
     2

We can get the categorical labels and key values like this:

::

    { labels, key_vals } = getcollabels(x, 1);

They will equal:

::

    labels = "0"   key_vals = 0
             "1"              1
             "2"              2

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


.. seealso:: Functions :func:`setColNames`, :func:`setColLabels`, :func:`setColMetadata`, :func:`setColDateFormats`
