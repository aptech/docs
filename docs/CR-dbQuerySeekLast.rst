
dbQuerySeekLast
==============================================

Purpose
----------------

Retrieves the last record in the result, if available, and positions the query
on the retrieved record.

Format
----------------
.. function:: ret = dbQuerySeekLast(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: returns 1 if successful. If unsuccessful the query position is set to an invalid position and 0 is returned.

    :rtype ret: scalar

Examples
----------------

::

    /*
    ** Given STATES is a table with all
    ** 50 states listed alphabetically
    */
    qid = dbExecQuery(db_id, "SELECT name FROM STATES");

    // Move to last state
    ret = dbQuerySeekLast(qid);

    // If 'ret' is equal to 0
    if not  ret;
       print  "dbQuerySeekLast failed";
    else;
       // Print last state: Wyoming
       print dbQueryFetchOneSA(qid);
    endif;

Remarks
-------

Note that the result must be in the active state and :func:`dbQueryIsSelect`
must return 1 before calling this function or it will do nothing and
return 0.


.. seealso:: Functions :func:`dbQuerySeekNext`, :func:`dbQuerySeekPrevious`, :func:`dbQuerySeekFirst`, :func:`dbQuerySeek`, :func:`dbQueryGetPosition`
