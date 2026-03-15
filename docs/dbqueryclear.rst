
dbQueryClear
==============================================

Purpose
----------------

Clears the result set and releases any resources held by the query. Sets the query state to inactive.

Format
----------------
.. function:: dbQueryClear(qid)

    :param qid: query number.
    :type qid: scalar

Examples
----------------

::

    // Execute a query
    qid = dbExecQuery(db_id, "SELECT * FROM orders");

    // Process results...

    // Clear the result set and release resources
    dbQueryClear(qid);

Remarks
-------

You should rarely if ever need to call this function.

