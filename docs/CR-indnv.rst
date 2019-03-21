
indnv
==============================================

Purpose
----------------

Checks one numeric vector against another and returns the indices of the elements of the first vector in the second vector.

Format
----------------
.. function:: indnv(what, where)

    :param what: 
    :type what: Nx1 numeric vector which contains the values to be found in vector  where

    :param where: 
    :type where: Mx1 numeric vector to be searched for matches to the values in  what

    :returns: z (*Nx1 vector of integers*), the indices of the corresponding elements of  what in  where.

Examples
----------------

::

    what = { 8, 7, 3 };
    where = { 2, 7, 8, 4, 3 };
    z = indnv(what,where);

::

    3
    z = 2
        5

.. seealso:: Functions :func:`contains`, :func:`ismember`, :func:`rowcontains`
