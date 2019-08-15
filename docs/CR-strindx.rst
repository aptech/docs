
strindx
==============================================

Purpose
----------------
Finds the index of one string within another string.

Format
----------------
.. function:: y = strindx(where, what, start)

    :param where: the data to be searched.
    :type where: string or scalar

    :param what: the substring to be searched for in *where*.
    :type what: string or scalar

    :param start: the starting point of the search in *where* for an occurrence of *what*. 
        The index of the first character in a string is 1.
    :type start: scalar

    :return y: containing the index of the first occurrence of *what*, within *where*, 
        which is greater than or equal to *start*. If no occurrence is found, it will be 0.

    :rtype y: scalar

Remarks
-------

An example of the use of this function is the location of a name within a string of names:

::

   z = "nameagepaysex";
   x = "pay";
   y = strindx(z,x,1);

The above code will set *y* equal to:

::

   8.00

This function is used with :func:`strsect` for extracting substrings.

.. seealso:: Functions :func:`strrindx`, :func:`strlen`, :func:`strsect`, :func:`strput`, :func:`strreplace`

