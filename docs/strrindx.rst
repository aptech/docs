
strrindx
==============================================

Purpose
----------------
Finds the index of one string within another string.
Searches from the end of the string to the beginning.

Format
----------------
.. function:: idx = strrindx(haystack, needle [, start])

    :param haystack: the string, string array or dataframe to be searched.
    :type haystack: string or scalar

    :param needle: the substring to be searched for in *haystack*.
    :type needle: string or scalar

    :param start: the starting point of the search in *haystack* for an occurrence of *needle*.
        *haystack* will be searched from this point backward for *needle*. Default is the end of the string
    :type start: scalar

    :return idx: contains the index of the last occurrence of *needle*, within *haystack*,
        which is less than or equal to *start*. If no occurrence is found, it will be 0.

    :rtype idx: scalar

Examples
-----------

::

    // Create a 3x1 string array
    state = "alaska" $|
            "alabama" $|
            "arkansas";

    // Find the first instance of the
    // letter 'a' starting from
    // the end of the string
    strrindx(state, "a");

Since the search starts from the back, the above code will print out:

::

       6.0000000
       7.0000000
       7.0000000

::

    // Find the first instance of the
    // letter 'a' starting from the
    // 5th character of the string
    strrindx(state, "a", 5);

This time, the search will start from the 5th character and continue searching towards the first character, resulting in:

::

       3.0000000
       5.0000000
       4.0000000


A negative value for *start* causes the search to begin at the end of the
string. An example of the use of :func:`strrindx` is extracting a file name from
a complete path specification:

::

   path = "/gauss/src/ols.src";
   ps = "/";
   pos = strrindx(path, ps, -1);
   if pos;
      name = strsect(path, pos+1, strlen(path)-pos);
   else;
      name = "";
   endif;

The above code makes the following assignments:

::

   pos = 11

   name = ols.src

.. seealso:: Functions :func:`strindx`, :func:`strlen`, :func:`strsect`, :func:`strput`
