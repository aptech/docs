
dbOpen
==============================================

Purpose
----------------

Opens a specified database connection using the current connection values.

Format
----------------
.. function:: dbOpen(db_id[, user_name, password])

    :param db_id: database connection index number.
    :type db_id: scalar

    :param user_name: optional. user name for the database being connected to.
    :type user_name: string

    :param password: optional. password associated with the specified user name for this database.
    :type password: string

    :returns: ret (*scalar*), 1 for success.

Examples
----------------

Set driver and host

::

    db_id = dbAddDatabase("MYSQL");
    dbSetHostName(db_id, "localhost");

then, either

::

    dbSetUserName(db_id, "test");
    dbSetPassword(db_id, "password");
    ret = dbOpen(db_id);

or

::

    ret = dbOpen(db_id, "test", "password");

