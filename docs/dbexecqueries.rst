
dbExecQueries
==============================================

Purpose
----------------

Executes a SQL statement multiple times with values from each row in *placeholders*. Only supports INSERT statements as there is no return mechanism for multiple SELECTs in this manner.

Format
----------------
.. function:: qid = dbExecQueries(db_id, sql_statement[, placeholders])

    :param db_id: database connection index number.
    :type db_id: scalar

    :param sql_statement: Contains a valid 'INSERT' SQL statement
    :type sql_statement: string

    :param placeholders: Contains bind value(s)
    :type placeholders: string array. each row denotes the values used for each operation.

    :return qid: query id to be used for result retrieval.

    :rtype qid: scalar

Examples
----------------

In the examples below, *db_id* is a previously created database id.

Example 1
+++++++++

::

    // Set SQL statement
    sql_statement = "INSERT INTO PEOPLE(fname, lname) VALUES (?, ?);";

    // Set bind values
    placeholders = ("Joe"$~"Smith")$|
                   ("Alice"$~"Jones")$|
                   ("Bob"$~"Monroe")$|
                   ("Carly"$~"Armstrong");

    // Execute multiple insert statements.
    qid = dbExecQueries(db_id, sql_statement, placeholders);


Example 2: Full Example
+++++++++++++++++++++++

The following is a full SQLite-based example.

::

    string valus = { "Foo"   "3.5" "Steve"  "33", 
                     "Bar"   "6.5" "Dave"   "53", 
                     "Baz"   "9.5" "Mark"   "38",
                     "One"   "13"  "Bob"    "26",
                     "Two"   "15"  "Alice"  "21",
                     "Three" "17"  "Kelsey" "43",
                     "Four"  "19"  "Rob"    "29"
    };

	// Create in memory SQLITE db
	id = dbAddDatabase("SQLITE");

	call dbSetDatabaseName(id, ":memory:");

	// Open database
	if not dbOpen(id);
		print "Cannot open database";
		dbClose(id);
	endif;
    
    call dbExecQuery(id, "drop table if exists test;");
    call dbExecQuery(id, "create table test (id INTEGER PRIMARY KEY, data TEXT, num DOUBLE, name TEXT, age INTEGER);");
    
    // Create single query statement
    query = "INSERT INTO test (data, num, name, age) VALUES (" $+ strjoin(reshape("?", 1, cols(valus)), ", ") $+ ")";
    
    // Using transactions is optional, but can help immensely when inserting a lot of data.
    if not dbTransaction(id);
        print "Could not open transaction";
        dbClose(id);
        end;
    endif;
    
    // Perform the insert
    call dbExecQueries(id, query, valus);
    
    call dbCommit(id); // Only necessary for transactions
    
    // Fetch all the data we just inserted
    table_data = dbQueryFetchAllSA(dbExecQuery(id, "SELECT * FROM test"));
    
    dbClose(id);
    
.. seealso:: Functions :func:`dbCreateQuery`, :func:`dbExecQuery`

