
dbQueryIsActive
==============================================

Purpose
----------------

Returns 1 if the query is active.

Format
----------------
.. function:: ret = dbQueryIsActive(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 if the query is active or 0 if not.

    :rtype ret: scalar

Remarks
-------

An active query is one that has been :func:`dbQueryExecPrepared`'d
successfully, but not yet finished with. When you are finished with an
active query, you can make the query inactive by calling :func:`dbQueryFinish`
or :func:`dbQueryClear`.

.. note:: Of particular interest is an active query that is a ``SELECT``
    statement. For some databases that support transactions, an active query
    that is a ``SELECT`` statement can cause a :func:`dbCommit` or a :func:`dbRollback` to
    fail, so before committing or rolling back, you should make your active
    ``SELECT`` statement query inactive using one of the methods listed above.


Examples
----------------

::

    // Create query
    qid = dbCreateQuery(db_id);

    // Check if active
    dbQueryIsActive(qid); // False

    // Prepare query
    dbQueryPrepare(qid, "INSERT INTO TEST
         (foo, bar) VALUES (1, 2);");

    // Check if active
    dbQueryIsActive(qid); // False

    // Execute query
    dbQueryExecPrepared(qid);

    // Check if active
    dbQueryIsActive(qid); // True

    // Finish query
    dbQueryFinish(qid);

    // Check if active
    dbQueryIsActive(qid); // False
