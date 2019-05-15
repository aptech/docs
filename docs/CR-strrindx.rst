
strrindx
==============================================

Purpose
----------------
Finds the index of one string within another string.
Searches from the end of the string to the beginning.

Format
----------------
.. function:: strrindx(where, what, start)

    :param where: the data to be searched.
    :type where: string or scalar

    :param what: the substring to be searched for in *where*.
    :type what: string or scalar

    :param start: the starting point of the search in *where* for an occurrence of *what*.
        *where* will be searched from this point backward for *what*.
    :type start: scalar

    :returns: y (*scalar*) containing the index of the last occurrence of *what*, within *where*, 
        which is less than or equal to *start*. If no occurrence is found, it will be 0.

Remarks
-------

A negative value for *start* causes the search to begin at the end of the
string. An example of the use of :func:`strrindx` is extracting a file name from
a complete path specification:

::

   path = "/gauss/src/ols.src";
   ps = "/";
   pos = strrindx(path,ps,-1);
   if pos;
      name = strsect(path,pos+1,strlen(path)-pos);
   else;
      name = "";
   endif;

The above code makes the following assignments:

::

   pos = 11

   name = ols.src

.. seealso:: Functions :func:`strindx`, :func:`strlen`, :func:`strsect`, :func:`strput`

