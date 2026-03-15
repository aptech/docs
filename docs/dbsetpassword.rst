
dbSetPassword
==============================================

Purpose
----------------

Sets the database connection's password.

Format
----------------
.. function:: dbSetPassword(db_id, pswd)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param pswd: password for database.
    :type pswd: string

Remarks
-------

This function must be called before the connection is opened with
:func:`dbOpen` to have an effect.

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set connection credentials before opening
    dbSetUserName(db_id, "admin");
    dbSetPassword(db_id, "secretpass");

    // Open the connection
    dbSetDatabaseName(db_id, "mydb");
    dbOpen(db_id);

.. seealso:: :func:`dbGetPassword`

