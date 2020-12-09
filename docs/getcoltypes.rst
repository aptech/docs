
getColTypes
==============================================

Purpose
----------------

Returns the metadata type of dataframe *X* by columns.

Format
----------------
.. function:: col_types = getColTypes(X [, columns])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Optional argument, names or indices of the columns in *X* to get type of. Default = all columns.
    :type columns: Jx1 vector or string array

    :return col_types: Type of *X* for the J columns specified by *columns*.
    :rtype col_types: Jx1 dataframe


Examples
----------------

::

  /*
  ** Import NBA data
  */
  fname = getGAUSSHome $+ "examples/nba_ht_wt.xls";
  nba_ht_wt = loadd(fname, "str(Player) + cat(Pos) + Height + Weight + Age");

  // Check column type of 'Age', 'Position', and 'Height'
  col_types = getColTypes(nba_ht_wt, "Age"$|"Pos"$|"Height");

After the above code, *col_types* will be a 3x1 dataframe with the following contents:

::

          number 
        category 
          number


.. seealso:: Functions :func:`setColTypes`, :func:`setColLabels`, :func:`getColLabels`
