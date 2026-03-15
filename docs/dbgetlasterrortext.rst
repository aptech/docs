
dbGetLastErrorText
==============================================

Purpose
----------------

Returns information about the last error that occurred on the database.

Format
----------------
.. function:: last_error = dbGetLastErrorText(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return last_error: details of last error on the specified database.

    :rtype last_error: string

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");
    dbSetDatabaseName(db_id, "mydb");

    // Attempt to open the connection
    ret = dbOpen(db_id);

    // Check for errors if the open failed
    if ret == 0;
        err_text = dbGetLastErrorText(db_id);
        print err_text;
    endif;

