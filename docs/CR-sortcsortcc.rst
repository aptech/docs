
sortc, sortcc
==============================================

Purpose
----------------

Sorts a numeric matrix, character matrix or string array.

Format
----------------
.. function:: sortcc(x, c)

    :param x: or string array.
    :type x: NxK matrix

    :param c: 
    :type c: scalar specifying one column of x to sort on

    :returns: y (*NxK matrix*) equal to x and sorted on the column
        c.

Examples
----------------

Sort rows of a matrix based upon first column
+++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 4 7 3,
          1 3 2,
          3 4 8 };
    
    // Sort 'x' based upon the first row
    y = sortc(x,1);

The above example code produces, y equal to:

::

    1 3 2
    3 4 8
    4 7 3

Sort rows of a 5x1 string vector
++++++++++++++++++++++++++++++++

::

    // Create a 5x1 string array, using the string
    // vertical concatenation operator '$|'
    letters = "epsilon" $|
              "gamma" $|
              "beta" $|
              "alpha" $|
              "delta";
    
    // Sort 'letters'
    letters_s = sortc(letters,1);

The above example code produces, letters_s equal to:

::

    alpha
       beta
      delta
    epsilon
      gamma

Remarks
-------

-  These functions will sort the rows of a matrix with respect to a
   specified column. That is, they will sort the elements of a column
   and will arrange all rows of the matrix in the same order as the
   sorted column.
-  sortc assumes that the column to sort on is numeric. sortcc assumes
   that the column to sort on contains character data.
-  The matrix may contain both character and numeric data, but the sort
   column must be all of one type.
-  Missing values will sort as if their value is below -∞.
-  The sort will be in ascending order.
-  This function uses the Quicksort algorithm.
-  If you need to obtain the matrix sorted in descending order, you can
   use:

   ::

      rev(sortc(x, c))

.. seealso:: Functions :func:`rev`, :func:`sortind`, :func:`unique`
