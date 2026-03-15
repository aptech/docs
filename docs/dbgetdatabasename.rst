
dbGetDatabaseName
==============================================

Purpose
----------------

Returns the name of the database.

Format
----------------
.. function:: db_name = dbGetDatabaseName(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return db_name: name of the database.

    :rtype db_name: string

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set the database name
    dbSetDatabaseName(db_id, "inventory");

    // Retrieve and print the database name
    db_name = dbGetDatabaseName(db_id);
    print db_name;

