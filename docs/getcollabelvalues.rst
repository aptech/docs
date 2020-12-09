
getcollabelvalues
==============================================

Purpose
----------------

Returns a string array of labels assigned to a categorical or string variable.

Format
----------------
.. function:: x_labels_sa = getColLabelValues(X [, columns])

    :param X: data with metadata.
    :type X: NxK dataframe

    :param columns: Optional argument, the names or indicies of the categorical or string variables in *X* to get labels from. Default = all columns.
    :type columns: Mx1 vector or string array

    :return x_labels_sa: labels assigned to the categorical or string variables in *X* specified by *columns*.
    :rtype x_labels_sa: NxM string array

Examples
----------------

::

  // Load 3 variables from an NBA data file into a dataframe 
  fname = getGAUSShome $+ "examples/nba_ht_wt.xls";
  nba_ht_wt = loadd(fname, "str(Player) + Age + str(School)");

  // Get player names and schools
  player_schools = getColLabelValues(nba_ht_wt, "Player"$|"School");


After the above code, *player_schools* will be a string array with two columns. Each column will contain all string labels from the
corresponding variable from the *nba_ht_wt* dataframe. The first few rows will look like this:

::

     Vitor Faverani         None
      Avery Bradley        Texas
       Keith Bogans     Kentucky
    Jared Sullinger   Ohio State

.. seealso:: Functions :func:`getColLabels`
