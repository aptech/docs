
sortmc
==============================================

Purpose
----------------

Sorts a matrix on multiple columns.

Format
----------------
.. function:: sortmc(x,  v)

    :param x: NxK matrix to be sorted.
    :type x: TODO

    :param v: in
        order, that are to be sorted. If an element is negative,
        that column will be interpreted as character data.
    :type v: Lx1 vector containing integers specifying the columns

    :returns: y (*TODO*), NxK sorted matrix.

Examples
----------------
sortmc

::

    x = { 9 2 5 6,
          3 6 1 9,
          3 7 4 1,
          1 2 8 9 };
    
    s1 = sortc(x,1);
    
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

In the output above, we see that the difference between s1 and sm is
that the second and third rows have been switched. This is because sortmc first sorted the matrix
based upon row one like sortc. Then sortmc sorted the rows in which
the first column was the same (in our example they are both threes), based upon the values in the second column.

Source
++++++

sortmc.src

.. seealso:: Functions :func:`sortd`, :func:`sortc`, :func:`sortcc`, :func:`sorthc`, :func:`sorthcc`
