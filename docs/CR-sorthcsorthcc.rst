
sorthc, sorthcc
==============================================

Purpose
----------------

Sorts a matrix of numeric or character data, or a string array.

Format
----------------
.. function:: y = sorthc(x, c)
              y = sorthcc(x, c)

    :param x: data
    :type x: NxK matrix or string array

    :param c: specifies one column of x to sort on
    :type c: scalar

    :return y: equal to *x* and sorted on the column *c*.

    :rtype y: NxK matrix or string array

Examples
----------------

::

    let x[3, 3] = 4 7 3
                1 3 2
                3 4 8;

    // Sort x based upon the values in the third column
    y = sorthc(x, 3);

This produces *y* equal to:

::

    1 3 2
    4 7 3
    3 4 8

Remarks
-------

These functions will sort the rows of a matrix or string array with
respect to a specified column. That is, they will sort the elements of a
column and will arrange all rows of the object in the same order as the
sorted column.

:func:`sorthc` assumes that the column to sort on is numeric. :func:`sorthcc` assumes
that the column to sort on contains character data.

If *x* is a matrix, it may contain both character and numeric data, but
the sort column must be all of one type. Missing values will sort as if
their value is below :math:`-\infty`.

The sort is in ascending order. This function uses the heap sort algorithm.

If you need to obtain the matrix sorted in descending order, you can use:

::

   rev(sorthc(x, c))


.. seealso:: Functions :func:`sortc`, :func:`rev`
