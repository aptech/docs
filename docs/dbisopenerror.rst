
dbIsOpenError
==============================================

Purpose
----------------

Reports whether an error occurred while attempting to open the database connection.

Format
----------------
.. function:: ret = dbIsOpenError(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return ret: 1 if there was an error or 0 if not.

    :rtype ret: scalar

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");
    dbSetDatabaseName(db_id, "mydb");

    // Attempt to open the connection
    dbOpen(db_id);

    // Check if an error occurred during open
    if dbIsOpenError(db_id);
        print "Error opening database connection";
    endif;

