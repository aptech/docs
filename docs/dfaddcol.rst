
dfaddcol
==============================================

Purpose
----------------

Adds a new named column to a dataframe.

Format
----------------
.. function:: df_new = dfaddcol(df, name, data)

    :param df: The dataframe to add a column to.
    :type df: NxK Dataframe

    :param name: The name for the new column.
    :type name: String

    :param data: The data for the new column.
    :type data: Nx1 vector, string array, or dataframe

    :return df_new: The original dataframe with the new column appended on the right.

    :rtype df_new: Nx(K+1) Dataframe

Examples
----------------

Add a computed column
++++++++++++++++++++++++

::

    // Load dataset
    fname = getGAUSSHome("examples/auto2.dta");
    auto2 = loadd(fname);

    // Add a new column computed from an existing column
    auto2 = dfaddcol(auto2, "price_k", auto2[., "price"] ./ 1000);

    // Preview first 5 rows of selected columns
    head(auto2[., "make" "price" "price_k"]);

::

                  make            price          price_k
           AMC Concord         4099.000         4.099000
             AMC Pacer         4749.000         4.749000
            AMC Spirit         3799.000         3.799000
        Buick Century         4816.000         4.816000
        Buick Electra         7827.000         7.827000

Add a string column
++++++++++++++++++++++++

::

    // Create a small numeric dataframe
    x = asdf(100 | 200 | 300, "value");

    // Add a string column
    x = dfaddcol(x, "label", "low" $| "mid" $| "high");

::

    x =          value            label
           100.00000              low
           200.00000              mid
           300.00000             high

Remarks
----------------

* :func:`dfaddcol` always appends the new column to the right side of the dataframe. To insert a column at a specific position, use :func:`insertcols`.

* The *data* argument must have the same number of rows as *df*.

* This function is equivalent to ``df ~ asDF(data, name)`` but reads more clearly when adding computed columns.

.. seealso:: Functions :func:`asdf`, :func:`dfappend`, :func:`dfname`, :func:`insertcols`
