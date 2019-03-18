
dbQueryExecPrepared
==============================================

Purpose
----------------

Executes a previously created and prepared query.

Format
----------------
.. function:: dbQueryExecPrepared(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*scalar*), 1 for success and 0 for failure.

Examples
----------------

::

    qid = dbCreateQuery(db_id);
    dbQueryPrepare(qid, "SELECT * FROM 
         USERS WHERE ID = :id");
    dbQueryBindValue(qid, ":id", "5");
    dbQueryExecPrepared(qid);
    
    results = dbQueryFetchAllSA(qid);
    
    dbQueryBindValue(qid, ":id", "10");
    
    // Re-execute the query with new value
    dbQueryExecPrepared(qid);
    
    results = dbQueryFetchAllSA(qid);

