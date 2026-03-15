
dbIsOpen
==============================================

Purpose
----------------

Reports whether a specified database connection is open.

Format
----------------
.. function:: ret = dbIsOpen(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return ret: 1 if the connection is open or 0 if it is closed.

    :rtype ret: scalar

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");
    dbSetDatabaseName(db_id, "mydb");

    // Open the connection
    dbOpen(db_id);

    // Check if the connection is open
    if dbIsOpen(db_id);
        print "Connection is open";
    endif;

