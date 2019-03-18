
sorthc, sorthcc
==============================================

Purpose
----------------

Sorts a matrix of numeric or character data, or a string array.

Format
----------------
.. function:: sorthcc(x, c)

    :param x: NxK matrix or string array.
    :type x: TODO

    :param c: scalar specifying one column of x to sort on.
    :type c: TODO

    :returns: y (*TODO*), NxK matrix or string array equal to x and sorted on the column c.

Examples
----------------

::

    let x[3,3]= 4 7 3
                1 3 2
                3 4 8;
    
    //Sort x based upon the values in the third column
    y = sorthc(x,3);

This produces y equal to:

::

    1 3 2
    4 7 3
    3 4 8

.. seealso:: Functions :func:`sortc`, :func:`rev`
