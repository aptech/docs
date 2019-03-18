
rankindx
==============================================

Purpose
----------------
Returns the vector of ranks of a vector.

Format
----------------
.. function:: rankindx(x,  flag)

    :param x: Nx1 vector.
    :type x: TODO

    :param flag: 1 for numeric data or 0 for character data.
    :type flag: scalar

    :returns: y (*TODO*), Nx1 vector containing the ranks of x.
        That is, the rank of the largest element is N and the rank of the
        smallest is 1. (To get ranks in descending order, subtract y from N+1).

Examples
----------------

::

    x = { 12, 4, 15, 7, 8 };
    r = rankindx(x,1);

After the code above, r is equal to:

::

    4
        1
    r = 5
        2
        3

