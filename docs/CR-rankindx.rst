
rankindx
==============================================

Purpose
----------------
Returns the vector of ranks of a vector.

Format
----------------
.. function:: y = rankindx(x, flag)

    :param x: data
    :type x: Nx1 vector

    :param flag: 1 for numeric data or 0 for character data.
    :type flag: scalar

    :returns: y (*Nx1 vector*) containing the ranks of *x*.
        That is, the rank of the largest element is :math:`N` and the rank of the
        smallest is 1. (To get ranks in descending order, subtract *y* from N+1).

Remarks
-------

:func:`rankindx` assigns different ranks to elements that have equal values
(ties). Missing values are assigned the lowest ranks.


Examples
----------------

::

    x = { 12, 4, 15, 7, 8 };
    r = rankindx(x,1);

After the code above, *r* is equal to:

::

        4
        1
    r = 5
        2
        3

