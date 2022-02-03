
sortcc
==============================================

Purpose
----------------

Deprecated: Sorts a character matrix.

Format
----------------
.. function:: y = sortcc(x, c)

    :param x: data
    :type x: NxK matrix

    :param c: specifies the column of *x* to sort on
    :type c: scalar

    :return y: equal to *x* and sorted on the column *c*.

    :rtype y: NxK matrix


Example
++++++++++++++

The use of character data is deprecated. You should use string arrays or dataframes.

::

    // Create a matrix with character data
    // in the first column
    x = { "alpha",
          "beta",
          "alpha",
          "alpha" };

    print $x;

::

    alpha
    beta
    alpha
    alpha

::

    // sort the vector based on the characters
    x_s = sortcc(x, 1);

    print $x_s;

::

    alpha
    alpha
    alpha
    beta
    


Remarks
-------

-  This function is deprecated. New code should use :func:`sortc`.
-  These functions will sort the rows of a matrix with respect to a
   specified column. That is, they will sort the elements of a column
   and will arrange all rows of the matrix in the same order as the
   sorted column.
-  :func:`sortcc` assumes that the column to sort on contains character data.
-  The matrix may contain both character and numeric data, but the sort
   column must be all of one type.
-  Missing values will sort as if their value is below :math:`-\infty`.
-  The sort will be in ascending order.
-  This function uses the Quicksort algorithm.
-  If you need to obtain the matrix sorted in descending order, you can use:

   ::

      rev(sortcc(x, c))

.. seealso:: Functions :func:`rev`, :func:`sortind`, :func:`sortc`, :func:`unique`
