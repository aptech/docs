
dbQueryIsActive
==============================================

Purpose
----------------

Returns 1 if the query is active.

Format
----------------
.. function:: dbQueryIsActive(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*scalar*), 1 if the query is active or 0 if not.

Examples
----------------

::

    qid = dbCreateQuery(db_id);
    
    dbQueryIsActive(qid); // False dbQueryPrepare(qid, "INSERT INTO TEST
         (foo, bar) VALUES (1, 2);");
    
    dbQueryIsActive(qid); // False dbQueryExecPrepared(qid);
    
    dbQueryIsActive(qid); // True dbQueryFinish(qid);
    
    dbQueryIsActive(qid); // False

