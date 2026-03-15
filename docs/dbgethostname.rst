
dbGetHostName
==============================================

Purpose
----------------

Returns the database connection's host name

Format
----------------
.. function:: host_name = dbGetHostName(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return host_name: name of database connection.

    :rtype host_name: string

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set the host name
    dbSetHostName(db_id, "db.example.com");

    // Retrieve and print the host name
    host_name = dbGetHostName(db_id);
    print host_name;

