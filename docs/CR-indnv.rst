
indnv
==============================================

Purpose
----------------

Checks one numeric vector against another and returns the indices of the elements of the first vector in the second vector.

Format
----------------
.. function:: indnv(what, where)

    :param what: contains the values to be found in vector *where*
    :type what: Nx1 numeric vector

    :param where: searched for matches to the values in *what*
    :type where: Mx1 numeric vector

    :returns: z (*Nx1 vector of integers*), the indices of the corresponding elements of *what* in *where*.

Remarks
-------

If no matches are found for any of the elements in *what*, then those
elements in the returned vector are set to the GAUSS missing value code.

If there are duplicate elements in *where*, the index of the first match
will be returned.


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

