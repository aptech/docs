
dbCreateQuery
==============================================

Purpose
----------------

Process an SQL statement and prepare a query. If placeholders is present, these values are bound sequentially to ODBC style parameters.

Format
----------------
.. function:: dbCreateQuery(db_id, query) 
			  dbCreateQuery(db_id, query, placeholders)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param query: database query to construct.
    :type query: string

    :param placeholders: or string array  containing bind value(s).
    :type placeholders: string

    :returns: qid (*scalar*), query id to be used for result retrieval.

Examples
----------------

qid = dbCreateQuery("SELECT * FROM GDP
     WHERE COUNTRY = ?", "USA");
dbQueryExecPrepared(qid); 

// Results as a matrix
results = dbQueryFetchAllM(qid);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

qid = dbCreateQuery("INSERT INTO 
     PEOPLE(id, fname, lname) VALUES 
     (NULL, ?, ?);");
dbQueryBindValue(qid, "Joe");
dbQueryBindValue(qid, "Smith");
dbQueryExecPrepared(qid);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Remarks
-------

If the placeholders parameter is passed in, the values are bound
sequentially to ODBC style parameters.

See also
++++++++

`dbQueryPrepare <#dbQueryPrepare>`__
