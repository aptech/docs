
order
==============================================

Purpose
----------------

Reorder a matrix based on user-specified ordering. Relocates *columns* to the beginning of the dataset in the order in which the variables are specified.

Format
----------------
.. function:: X_new = order(X, columns)

    :param X: data. Must have metadata.
    :type X: NxK dataframe

    :param columns: Names or indices of variables in *X* to be moved to first *J* columns in the dataframe.
    :type columns: Jx1 vector or string array

    :return X_new: reordered data with the first *J* columns containing the columns in *columns*, in the order they are input.
    :rtype X_new: NxK dataframe


Examples
----------------

::

  // Create matrix
  x = reshape(seqa(1, 1, 100), 5, 20);

  // Order of columns
  columnlist = 5|3|1;

  // Reorder matrix
  x_new = order(x, columnlist);

  // Load NBA dataset
  fname = getGAUSSHome() $+ "examples/nba_ht_wt.xls";
  nba_ht_wt = loadd(fname, "str(Player) + cat(Pos) + Age + date(BDate) + Height");

  // Reorder column to show 'Age', 'Pos', and 'Height'
  // in column 1, 2, 3
  nba_new = order(nba_ht_wt, "Age"$|"Pos"$|"Height");

After the code above, the first five rows of *nba_new* looks like:

::

             Age    Pos           Height           Player            BDate 
       25.000000      C        83.000000   Vitor Faverani       1988-05-05 
       22.000000      G        74.000000    Avery Bradley       1990-11-26 
       33.000000      G        77.000000     Keith Bogans       1980-05-12 
       21.000000      F        81.000000  Jared Sullinger       1992-03-04 
       27.000000      F        81.000000       Jeff Green       1986-08-28


.. seealso:: Functions :func:`delcols`
