
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

Remarks
-------

An active query is one that has been dbQueryExecPrepared()'d
successfully, but not yet finished with. When you are finished with an
active query, you can make the query inactive by calling dbQueryFinish()
or dbQueryClear().

Note: Of particular interest is an active query that is a SELECT
statement. For some databases that support transactions, an active query
that is a SELECT statement can cause a dbCommit() or a dbRollback() to
fail, so before committing or rolling back, you should make your active
SELECT statement query inactive using one of the methods listed above.


Examples
----------------

::

    qid = dbCreateQuery(db_id);
    
    dbQueryIsActive(qid); // False dbQueryPrepare(qid, "INSERT INTO TEST
         (foo, bar) VALUES (1, 2);");
    
    dbQueryIsActive(qid); // False dbQueryExecPrepared(qid);
    
    dbQueryIsActive(qid); // True dbQueryFinish(qid);
    
    dbQueryIsActive(qid); // False

