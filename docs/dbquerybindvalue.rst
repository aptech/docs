
dbQueryBindValue
==============================================

Purpose
----------------

Set the placeholder, *placeholder*, to be bound to value, *val*, in the prepared statement.
Note that the placeholder mark (e.g ``:``) must be included when specifying the placeholder name.

Format
----------------
.. function:: dbQueryBindValue(qid, placeholder, val)

    :param qid: query number.
    :type qid: scalar

    :param placeholder: Oracle style (``:value_name``) or index of ODBC style (``?``) placeholder.
    :type placeholder: matrix or string

    :param val: the value to be bound.
    :type val: matrix or string 

Examples
----------------

::

    // Adds "MYSQL"" to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Prepare a query
    qid = dbCreateQuery(db_id);
    dbQueryPrepare(qid, "SELECT * FROM
         PEOPLE WHERE FIRST = :fname AND
         LAST = :lname");

    // Set `:fname` placeholder
    dbQueryBindValue(qid, ":fname", "John");

    // Set `:lname` placeholder
    dbQueryBindValue(qid, ":lname", "Doe");

    // Prepare the SQL query for execution
    dbQueryExecPrepared(qid);

Remarks
-------

Values cannot be bound to multiple locations in the query.


