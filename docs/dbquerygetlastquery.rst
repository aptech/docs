
dbQueryGetLastQuery
==============================================

Purpose
----------------

Returns the text of the current query being used.

Format
----------------
.. function:: query_string = dbQueryGetLastQuery(qid)

    :param qid: query number.
    :type qid: scalar

    :return query_string: text of the current query, or empty string if there is no current query.

    :rtype query_string: string

Examples
----------------

::

    // Execute a query
    qid = dbExecQuery(db_id, "SELECT name, price FROM products");

    // Retrieve the SQL text of the current query
    sql = dbQueryGetLastQuery(qid);

    // Prints: SELECT name, price FROM products
    print sql;

