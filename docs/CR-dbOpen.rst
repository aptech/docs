
dbOpen
==============================================

Purpose
----------------

			Opens a specified database connection using the current connection values.

Format
----------------
.. function:: dbOpen(db_id, user_name, password) 
			  dbOpen(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param user_name: user name for the database being connected to.
    :type user_name: string

    :param password: password associated with the specified user name for this database.
    :type password: string

    :returns: ret (*scalar*), 1 for success.

Examples
----------------

::

    db_id = dbAddDatabase("MYSQL");
    dbSetHostName(db_id, "localhost");

::

    dbSetUserName(db_id, "test");
    dbSetPassword(db_id, "secret_passw0rd");
    ret = dbOpen(db_id);

or

::

    ret = dbOpen(db_id, "test", 
        "secret_passw0rd");

