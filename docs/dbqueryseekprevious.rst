
dbQuerySeekPrevious
==============================================

Purpose
----------------
Retrieves the previous record in the result, if available, and positions the query on the retrieved record.

Format
----------------
.. function:: ret = dbQuerySeekPrevious(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 if the record is successfully retrieved. If the record could not be retrieved, the result is positioned before the first record and 0 is returned.

    :rtype ret: scalar

Remarks
-------

Note that the result must be in the active state before calling this
function or it will do nothing and return false. The state of the query
can be verified with :func:`dbQueryIsSelect`.

The following rules apply:

    If the result is currently located before the first record, there is no
    change and 0 is returned.

    If the result is currently located after the last record, an attempt is
    made to retrieve the last record.

    If the result is somewhere in the middle, an attempt is made to retrieve
    the previous record.


.. seealso:: Functions :func:`dbQuerySeekFirst`, :func:`dbQuerySeekLast`, :func:`dbQuerySeekNext`, :func:`dbQuerySeek`, :func:`dbQueryGetPosition`
