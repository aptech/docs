
intrleavsa
==============================================

Purpose
----------------

Interleaves the rows of two string arrays that have been sorted on a common column.

Format
----------------
.. function:: intrleavsa(sa1, sa2, ikey)

    :param sa1: 
    :type sa1: NxK string array 1

    :param sa2: 
    :type sa2: MxK string array 2

    :param ikey: index of the key column the string arrays are sorted on.
    :type ikey: scalar integer

    :returns: y (*TODO*), LxK interleaved (combined) string array.



Remarks
-------

The two string arrays MUST have exactly the same number of columns AND
have been already sorted on a key column.

This procedure will combine them into one large string array, sorted by
the key column.



Source
------

sortd.src

