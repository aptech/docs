
sortmc
==============================================

Purpose
----------------

Sorts a matrix on multiple columns.

Format
----------------
.. function:: y = sortmc(x, v [, sort_order])

    :param x: data to be sorted
    :type x: NxK matrix

    :param v: contains integers specifying the columns in order, that are to be sorted.
        If an element is negative, that column will be interpreted as character data.
    :type v: Lx1 vector

    :param sort_order: Optional input, the sort order. 1 for ascending order, -1 for descending order. Default=1.
    :type sort_order: scalar.

    :return y: sorted matrix

    :rtype y: NxK matrix

Examples
----------------

:func:`sortmc` keeps all rows together. After it sorts on the first specified column,
it will continue to sort the rows of the matrix using the other specified columns ONLY
when there is a tie in the first column. For example:

::

    x = { 9 2 5 6,
          3 6 1 9,
          3 7 4 1,
          1 2 8 9 };

    s1 = sortc(x, 1);

    sm = sortmc(x, 1|2);

will return:

::

         1      2      8      9
    s1 = 3      7      4      1
         3      6      1      9
         9      2      5      6

         1      2      8      9
    sm = 3      6      1      9
         3      7      4      1
         9      2      5      6

In the output above, we see that the difference between *s1* and *sm* is
that the second and third rows have been switched. This is because :func:`sortmc`
first sorted the matrix based upon row one like :func:`sortc`. Then :func:`sortmc` sorted the
rows in which the first column was the same (in our example they are both threes),
based upon the values in the second column.

Sort in descending order
++++++++++++++++++++++++++++++++

::

    x = { 9 2 5 6,
          3 6 1 9,
          3 7 4 1,
          1 2 8 9 };

    // Sort 'x' in descending order on columns 1 and 2
    sm = sortmc(x, 1|2, -1);

will return:

::

         9      2      5      6
    sm = 3      7      4      1
         3      6      1      9
         1      2      8      9

In this example, the matrix is sorted in descending order. First by column 1,
then by column 2 when there are ties in column 1 (as with the two rows
containing 3 in the first column).

Remarks
-------

-  The sort will be in ascending order by default.
-  To sort in descending order, set the *sort_order* parameter to -1.

Source
------

sortmc.src

.. seealso:: Functions :func:`sortd`, :func:`sortc`, :func:`sortcc`, :func:`sorthc`, :func:`sorthcc`
