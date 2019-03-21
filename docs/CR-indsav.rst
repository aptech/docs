
indsav
==============================================

Purpose
----------------

Checks one string array against another and returns the indices of the first string array in the second string array.

Format
----------------
.. function:: indsav(what, where)

    :param what: 
    :type what: Nx1 string array which contains the values to be found in vector  where

    :param where: 
    :type where: Mx1 string array to be searched for the corresponding elements of  what

    :returns: indx (*Nx1 vector of indices*), the values of  what in  where.



Remarks
-------

If no matches are found, those elements in the returned vector are set
to the GAUSS missing value code.

If there are duplicate elements in where, the index of the first match
will be returned.

