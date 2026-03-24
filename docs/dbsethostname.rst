
dbSetHostName
==============================================

Purpose
----------------

Sets the specified database connection's host name.

Format
----------------
.. function:: dbSetHostName(db_id, host_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param host_name: the name to assign to the connection's host name.
    :type host_name: string

Remarks
-------

For this function to have an effect, it must be called before the
database connection is opened with :func:`dbOpen`.

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set the host name before opening
    dbSetHostName(db_id, "db.example.com");

    // Configure remaining settings and open
    dbSetDatabaseName(db_id, "mydb");
    dbOpen(db_id);
