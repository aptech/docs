
getColTypes
==============================================

Purpose
----------------

Returns the metadata type of matrix *x* by columns.

Format
----------------
.. function:: col_types = getColTypes(x [, columns])

    :param x: data with metadata.
    :type x: NxK matrix

    :param columns: Optional argument, specifies columns in *x* to get type of. Default = all columns.
    :type columns: Jx1 string array or vector

    :return col_types: Type of *x* for the J columns specified by *columns*.
    :rtype col_types: Jx1 category vector


Examples
----------------

::

  /*
  ** Import NBA data
  */
  nba_ht_wt = loadd("C:\\gauss21\\examples\\nba_ht_wt.xls",
                   "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

  // Check column type of Player
  col_types = getColTypes(nba_new, "Age"$|"Pos"$|"Height");


.. seealso:: Functions :func:`setColTypes`, :func:`setColLabels`, :func:`getColLabels`
