
getcollabelvalues
==============================================

Purpose
----------------

Returns a string array of labels assigned to a categorical or string variable.

Format
----------------
.. function:: x_labels_sa = getColLabelValues(x, index)

    :param x: data with metadata.
    :type x: NxK matrix

    :param index: categorical or string variables in *x* to get labels from.
    :type index: Vector or string array

    :return x_labels_sa: labels assigned to the categorical or string variables in *x* specified by *index*.
    :rtype x_labels_sa: string array

Examples
----------------

::

  // Load NBA data file
  // with metadata
  nba_ht_wt = loadd("C:\\gauss21\\examples\\nba_ht_wt.xls",
                    "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

  // Get player names
  player_schools = getcollabelvalues(nba_ht_wt, "Player"$|"School");


.. seealso:: Functions :func:`getColLabels`
