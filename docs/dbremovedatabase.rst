
dbRemoveDatabase
==============================================

Purpose
----------------

Removes a database connection from the list of open database connections. Frees all related resources.

Format
----------------
.. function:: dbRemoveDatabase(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");
    dbSetDatabaseName(db_id, "mydb");
    dbOpen(db_id);

    // Perform database operations...

    // Close and remove the connection entirely
    dbClose(db_id);
    dbRemoveDatabase(db_id);

