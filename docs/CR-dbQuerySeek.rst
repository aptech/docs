
dbQuerySeek
==============================================

Purpose
----------------

Retrieves the record at a specified position, if available, and positions the query 
on the retrieved record. 

Format
----------------
.. function:: dbQuerySeek(qid, idx, idx_type) 
			  dbQuerySeek(qid, idx)

    :param qid: query number.
    :type qid: scalar

    :param idx: the index at which to place the cursor.
    :type idx: scalar

    :param idx_type: 1 for relative position or 0 for absolute positioning. If not specified, absolute positioning is used.
    :type idx_type: scalar

    :returns: ret (*scalar*), 1 if successful.



Remarks
-------

The first record is at position 1. Note that the query must be in an
active state before calling this function. The state of the query may be
verified with the function dbQueryIsSelect().

If idx_type is 0 (the default), the following rules apply:

If idx is negative, the result is positioned before the first record and
0 is returned. Otherwise, an attempt is made to move to the record at
position idx. If the record at position idx could not be retrieved, the
result is positioned after the last record and 0 is returned. If the
record is successfully retrieved, 1 is returned.

If idx_type is 1, the following rules apply:

If the result is currently positioned before the first record or on the
first record, and idx is negative, there is no change, and 0 is
returned.

If the result is currently located after the last record, and idx is
positive, there is no change, and 0 is returned. If the result is
currently located somewhere in the middle, and the relative offset idx
moves the result below zero, the result is positioned before the first
record and 0 is returned.

Otherwise, an attempt is made to move to the record idx records ahead of
the current record (or idx records behind the current record if idx is
negative).

If the record at offset idx could not be retrieved, the result is
positioned after the last record if idx >= 0, (or before the first
record if idx is negative), and 0 is returned. If the record is
successfully retrieved, 1 is returned.

