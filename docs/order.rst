
order
==============================================

Purpose
----------------

Reorder a matrix based on user-specified ordering. Relocates *columns* to the beginning of the dataset in the order in which the variables are specified.

Format
----------------
.. function:: x_new = order(X, column)

    :param X: data. Must have metadata.
    :type X: NxK dataframe

    :param columns: Names or indices of variables in *X* to be moved to first *J* columns in the dataframe.
    :type columns: Jx1 vector or string array

    :return x_meta: reordered data with the first J columns containing the columns in *columns*, in the order they are input.
    :rtype x_meta: NxK dataframe


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
  nba_ht_wt = loadd(fname, "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

  // Reorder column to show 'Age', 'Pos', and 'Height'
  // in column 1, 2, 3
  nba_new = order(nba_ht_wt, "Age"$|"Pos"$|"Height");

After the code above, the first five rows of *nba_new* looks like:

::

           Age              Pos           Height           Player           Weight           School            BDate
     25.000000                C        83.000000   Vitor Faverani        260.00000             None 05/05/1988 00:00
     22.000000                G        74.000000    Avery Bradley        180.00000            Texas 11/26/1990 00:00
     33.000000                G        77.000000     Keith Bogans        215.00000         Kentucky 05/12/1980 00:00
     21.000000                F        81.000000  Jared Sullinger        260.00000       Ohio State 03/04/1992 00:00
     27.000000                F        81.000000       Jeff Green        235.00000       Georgetown 08/28/1986 00:00



.. seealso:: Functions :func:`delcols`
