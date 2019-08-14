
dbCreateQuery
==============================================

Purpose
----------------

Process an SQL statement and prepare a query. If placeholders is present, these values are bound sequentially to ODBC style parameters.

Format
----------------
.. function:: qid = dbCreateQuery(db_id[, query[, placeholders]])

    :param db_id: database connection index number.
    :type db_id: scalar

    :param query: optional. database query to construct.
    :type query: string

    :param placeholders: optional. containing bind value(s).
    :type placeholders: string or string array

    :return qid: query id to be used for result retrieval.

    :type qid: scalar

Remarks
-------

If the *placeholders* parameter is passed in, the values are bound
sequentially to ODBC style parameters.

Examples
----------------

Example 1
+++++++++

::

    // Create and prepare query
    qid = dbCreateQuery("SELECT * FROM GDP
                        WHERE COUNTRY = ?", "USA");
    dbQueryExecPrepared(qid);

    // Results as a matrix
    results = dbQueryFetchAllM(qid);

Example 2
+++++++++

::

    // Create query
    qid = dbCreateQuery("INSERT INTO
                        PEOPLE(id, fname, lname) VALUES
                        (NULL, ?, ?);");

    // Set the placeholder
    dbQueryBindValue(qid, "Joe");

    // Set the placeholder
    dbQueryBindValue(qid, "Smith");

    // Execute query
    dbQueryExecPrepared(qid);

.. seealso:: :func:`dbQueryPrepare`
