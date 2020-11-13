
setcolmetadata
==============================================

Purpose
----------------

Reorder a matrix based on user specified ordering. Relocates *column* to the beginning of the dataset in the order in which the variables are specified.

Format
----------------
.. function:: x_new = order(x, column)

    :param x: data. Must have metadata.
    :type x: NxK matrix

    :param column: variables to be moved to first J columns in the matrix.
    :type column: Jx1 vector or string array

    :return x_meta: reordered data with the first J columns containing the columns in *column*, in the order they are input.
    :rtype x_meta: NxK matrix


Examples
----------------

::

  /*
  ** First use sequential data
  ** and numeric indices to
  ** reorder
  */
  // Create matrix
  x = reshape(seqa(1, 1, 100), 5, 20);

  // Order of columns
  columnlist = 5|3|1;

  // Reorder matrix
  x_new = order(x, columnlist);

  /*
  ** Use data file
  ** and variables names
  ** to order the
  */
  nba_ht_wt = loadd("C:\\gauss21\\examples\\nba_ht_wt.xls", "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

  // Reorder column to show age,
  // position, and height
  // in column 1, 2, 3
  nba_new = order(nba_ht_wt, "Age"$|"Pos"$|"Height");



.. seealso:: Functions :func:`delcols`
