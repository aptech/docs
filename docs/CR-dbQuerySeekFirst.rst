
dbQuerySeekFirst
==============================================

Purpose
----------------

Retrieves the first record in the result, if available, and positions the query 
on the retrieved record.

Format
----------------
.. function:: dbQuerySeekFirst(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*TODO*), 1 if successful. If unsuccessful the query position is set to an invalid position and 0 is returned.

Examples
----------------

::

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

