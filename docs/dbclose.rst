
dbClose
==============================================

Purpose
----------------

Closes a database connection and destroys any remaining queries.

Format
----------------
.. function:: dbClose(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Configure and open the connection
    dbSetDatabaseName(db_id, "mydb");
    dbOpen(db_id);

    // Perform database operations...
    qid = dbExecQuery(db_id, "SELECT * FROM customers");

    // Close the connection when done
    dbClose(db_id);

Remarks
-------

:func:`dbClose` does not remove the database connection from the list of
available database connections. The connection can be opened again
without repeating the database initialization and setup steps.

