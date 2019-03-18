
dbQuerySeekPrevious
==============================================

Purpose
----------------
Retrieves the previous record in the result, if available, and positions the query on the retrieved record.

Format
----------------
.. function:: dbQuerySeekPrevious(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*scalar*), 1 if the record is successfully retrieved. If the record could not be retrieved, the result is positioned before the first record and 0 is returned.

