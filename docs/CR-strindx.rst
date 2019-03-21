
strindx
==============================================

Purpose
----------------
Finds the index of one string within another string.

Format
----------------
.. function:: strindx(where, what, start)

    :param where: the data to be searched.
    :type where: string or scalar

    :param what: the substring to be searched for in
        where.
    :type what: string or scalar

    :param start: the starting point of the search in  where for
        an occurrence of  what. The index of the first character in a string
        is 1.
    :type start: scalar

    :returns: y (*scalar containing the index of the first occurrence of what*), within where, which is greater than or equal to start. If
        no occurrence is found, it will be 0.



Remarks
-------

An example of the use of this function is the location of a name within
a string of names:

::

   z = "nameagepaysex";
   x = "pay";
   y = strindx(z,x,1);

The above code will set y equal to:

::

   8.00

This function is used with strsect for extracting substrings.

