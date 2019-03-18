
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

