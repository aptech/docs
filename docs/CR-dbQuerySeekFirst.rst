
dbQuerySeekFirst
==============================================

Purpose
----------------

Retrieves the first record in the result, if available, and positions the query
on the retrieved record.

Format
----------------
.. function:: ret = dbQuerySeekFirst(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 if successful. If unsuccessful the query position is set to an invalid position and 0 is returned.

    :rtype ret: scalar

Examples
----------------

::

    // Create and prepare query
    qid = dbCreateQuery(db_id, "SELECT *
        FROM PEOPLE");

    do while dbQuerySeekNext(qid);
        // iterate over results
    endo;

    // set back to start
    dbQuerySeekFirst(qid);

    do while dbQuerySeekNext(qid);
        // iterate over results AGAIN
    endo;

Remarks
-------

Note that the result must be in the active state or it will do nothing
and return. This can be verified by calling the :func:`dbQueryIsSelect`
function.


