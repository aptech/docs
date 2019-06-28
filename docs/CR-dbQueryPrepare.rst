
dbQueryPrepare
==============================================

Purpose
----------------

Prepares a SQL query for execution.

Format
----------------
.. function:: dbQueryPrepare(qid, query)

    :param qid: query index number.
    :type qid: scalar

    :param query: database query to prepare.
    :type query: string

    :returns: **ret** (*scalar*) - 1 for success and 0 for failure.

Examples
----------------

::

    // Add "MYSQL" database to list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Create query
    qid = dbCreateQuery(db_id);

    // Prepare query
    ret = dbQueryPrepare(qid, "SELECT *
        FROM STOCKS WHERE SYMBOL = :sym");

    // Set `:sym` placeholder
    dbQueryBindValue(qid, ":sym", "GOOG");

    // Execute query
    ret = dbQueryExecPrepared(qid);

Remarks
-------

The query may contain placeholders for binding values. Both Oracle style
colon-name (e.g., ``:surname``), and ODBC style (``?``) placeholders are
supported; but they cannot be mixed in the same query.

.. note:: Portability: Some databases choose to delay preparing a query until
    it is executed the first time. In this case, preparing a syntactically
    incorrect query succeeds, but every consecutive :func:`dbQueryExecPrepared`
    will fail.

For SQLite, the query string can contain only one statement at a time.
If more than one statement is given, the function returns 0.

See also
------------

.. seealso:: Function :func:`dbQueryBindValue`
