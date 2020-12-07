
getColTypes
==============================================

Purpose
----------------

Returns the metadata type of matrix *x* by columns.

Format
----------------
.. function:: col_types = getColTypes(x [, columns])

    :param x: data with metadata.
    :type x: NxK dataframe

    :param columns: Optional argument, specifies columns in *x* to get type of. Default = all columns.
    :type columns: Jx1 vector or string array

    :return col_types: Type of *x* for the J columns specified by *columns*.
    :rtype col_types: Jx1 dataframe


Examples
----------------

::

  /*
  ** Import NBA data
  */
  fname = getGAUSSHome $+ "examples\\nba_ht_wt.xls";
  nba_ht_wt = loadd(fname,
                   "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

  // Check column type of Age, Position, and Height
  col_types = getColTypes(nba_ht_wt, "Age"$|"Pos"$|"Height");


.. seealso:: Functions :func:`setColTypes`, :func:`setColLabels`, :func:`getColLabels`
