
dbExecQuery
==============================================

Purpose
----------------

Executes an SQL statement and creates a query.

Format
----------------
.. function:: dbExecQuery(db_id, sql_statement,placeholders)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param sql_statement: string containing a valid SQL statement.
    :type sql_statement: TODO

    :param placeholders: string (array) containing bind value(s).
    :type placeholders: TODO

    :returns: qid (*scalar*), query id to be used for result retrieval.

Examples
----------------
In the examples below, db_id is a previously created database id.

qid = dbExecQuery(db_id, "SELECT * FROM GDP 
     WHERE COUNTRY = ?", "USA");

// Results as a matrix
results = dbQueryFetchAllM(qid);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

bd_vals = "Joe"$|"Smith";
qid = dbExecQuery(db_id, "INSERT INTO PEOPLE(id, 
      fname, lname); VALUES (NULL, ?, ?);",bd_vals);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

qid = dbExecQuery("SELECT * FROM PEOPLE 
     p WHERE p.FNAME = ?", "Joe");
// Results as a string array
results = dbQueryFetchAllSA(qid);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

