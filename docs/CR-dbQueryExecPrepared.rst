
dbQueryExecPrepared
==============================================

Purpose
----------------

Executes a previously created and prepared query.

Format
----------------
.. function:: ret = dbQueryExecPrepared(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 for success and 0 for failure.

    :type ret: scalar

Examples
----------------

::

    // Prepare a query
    qid = dbCreateQuery(db_id);
    dbQueryPrepare(qid, "SELECT * FROM
         USERS WHERE ID = :id");

    // Set `:id` placeholder
    dbQueryBindValue(qid, ":id", "5");

    // Execute `qid` query
    dbQueryExecPrepared(qid);

    // Return results as a string array
    results = dbQueryFetchAllSA(qid);

    // Reset `:id` placeholder
    dbQueryBindValue(qid, ":id", "10");

    // Re-execute the query with new value
    dbQueryExecPrepared(qid);

    // Return new results as a string array
    results = dbQueryFetchAllSA(qid);
