
dbGetPort
==============================================

Purpose
----------------

Returns the database connection's port number if it has been set.

Format
----------------
.. function:: db_port = dbGetPort(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return db_port: the port number of the specified database connection.

    :rtype db_port: scalar

Remarks
-------

:func:`dbGetPort` will only return the port number if it was previously set
with :func:`dbSetPort`.

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set the port number
    dbSetPort(db_id, 3306);

    // Retrieve and verify the port
    port = dbGetPort(db_id);
    print (port);
