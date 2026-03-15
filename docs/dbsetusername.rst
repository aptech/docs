
dbSetUserName
==============================================

Purpose
----------------

Sets the specified database connection's user name.

Format
----------------
.. function:: dbSetUserName(db_id, user_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param user_name: user name to apply to specified database connection.
    :type user_name: string

Remarks
-------

This function must be called before the connection is opened with
:func:`dbOpen` to have an effect.

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set the user name before opening
    dbSetUserName(db_id, "db_user");

    // Configure remaining settings and open
    dbSetDatabaseName(db_id, "mydb");
    dbSetPassword(db_id, "password");
    dbOpen(db_id);

.. seealso:: :func:`dbGetUserName`

