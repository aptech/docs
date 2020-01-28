
dbOpen
==============================================

Purpose
----------------

Opens a specified database connection using the current connection values.

Format
----------------
.. function:: ret = dbOpen(db_id[, user_name, password])

    :param db_id: database connection index number.
    :type db_id: scalar

    :param user_name: optional. user name for the database being connected to.
    :type user_name: string

    :param password: optional. password associated with the specified user name for this database.
    :type password: string

    :return ret: 1 for success.

    :rtype ret: scalar

Examples
----------------

Set driver and host

::

    // Adds "MYSQL"" to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set database connection's hostname
    dbSetHostName(db_id, "localhost");

then, either

::

    // Set database username
    dbSetUserName(db_id, "test");

    // Set database password
    dbSetPassword(db_id, "password");

    // Open database connection
    ret = dbOpen(db_id);

or

::

    /*
    ** Open database connection
    ** using optional username input `test`
    ** and optional password input `password`
    */
    ret = dbOpen(db_id, "test", "password");
