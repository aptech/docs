
dbQueryFinish
==============================================

Purpose
----------------

Instructs the database driver that no more data will be fetched from this query until it is re-executed.

Format
----------------
.. function:: dbQueryFinish(qid)

    :param qid: query number.
    :type qid: scalar

Remarks
-------

There is normally no need to call this function, but it may be helpful
in order to free resources such as locks or cursors if you intend to
re-use the query at a later time.

Sets the query to inactive. Bound values retain their values.

Examples
----------------

::

    // Execute a query
    qid = dbExecQuery(db_id, "SELECT * FROM orders");

    // Process some results...
    dbQuerySeekNext(qid);
    val = dbQueryGetField(qid, 1);

    // Signal that no more data will be fetched for now
    dbQueryFinish(qid);

