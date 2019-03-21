
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

    :param what: the substring to be searched for in
        where.
    :type what: string or scalar

    :param start: the starting point of the search in  where for
        an occurrence of what.
        where will be searched from this point
        backward for what.
    :type start: scalar

    :returns: y (*scalar containing the index of the last occurrence of what*), within where, which is less than or equal to start. If
        no occurrence is found, it will be 0.

