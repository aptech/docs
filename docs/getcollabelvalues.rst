
getcollabelvalues
==============================================

Purpose
----------------

Returns a string array of labels assigned to a categorical or string variable.

Format
----------------
.. function:: x_labels_sa = getColLabelValues(x [, columns])

    :param x: data with metadata.
    :type x: NxK matrix

    :param columns: Optional argument, categorical or string variables in *x* to get labels from. Default = all columns.
    :type columns: Mx1 Vector or string array

    :return x_labels_sa: labels assigned to the categorical or string variables in *x* specified by *columns*.
    :rtype x_labels_sa: NxM string array

Examples
----------------

::

  // Load NBA data file
  // with metadata
  nba_ht_wt = loadd("C:\\gauss21\\examples\\nba_ht_wt.xls",
                    "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

  // Get player names
  player_schools = getColLabelValues(nba_ht_wt, "Player"$|"School");


.. seealso:: Functions :func:`getColLabels`
