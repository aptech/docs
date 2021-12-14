
dbExecQuery
==============================================

Purpose
----------------

Executes a SQL statement and creates a query.

Format
----------------
.. function:: qid = dbExecQuery(db_id, sql_statement[, placeholders])

    :param db_id: database connection index number.
    :type db_id: scalar

    :param sql_statement: Contains a valid SQL statement
    :type sql_statement: string

    :param placeholders: Contains bind value(s)
    :type placeholders: string or string array

    :return qid: query id to be used for result retrieval.

    :rtype qid: scalar

Examples
----------------

Example 1
+++++++++

In the examples below, *db_id* is a previously created database id.

::

    // Set SQL statement
    sql_statement = "SELECT * FROM GDP WHERE COUNTRY = ?";

    // Set bind value
    placeholders = "USA";

    // Execute query
    qid = dbExecQuery(db_id, sql_statement, placeholders);

    // Results as a matrix
    results = dbQueryFetchAllM(qid);

Example 2
+++++++++

::

    // Set SQL statement
    sql_statement = "INSERT INTO PEOPLE(id, fname, lname) VALUES (NULL, ?, ?);";

    // Set bind values
    placeholders = "Joe"$|"Smith";

    // Execute query
    qid = dbExecQuery(db_id, sql_statement, placeholders);


Example 3
+++++++++

::

    // Set SQL statement
    sql_statement = "SELECT * FROM PEOPLE p WHERE p.FNAME = ?";

    // Set bind value
    placeholders = "Joe";

    // Execute query
    qid = dbExecQuery(db_id, sql_statement, placeholders);

    // Results as a string array
    results = dbQueryFetchAllSA(qid);

.. seealso:: Functions :func:`dbCreateQuery`, :func:`dbExecQueries`

