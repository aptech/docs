
dbGetUserName
==============================================

Purpose
----------------

Returns the database connection's user name.

Format
----------------
.. function:: user_name = dbGetUserName(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return user_name: containing the user name associated with the specified database connection.

    :rtype user_name: string

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Set the user name
    dbSetUserName(db_id, "admin");

    // Retrieve the user name
    user_name = dbGetUserName(db_id);
    print user_name;

.. seealso:: Functions :func:`dbSetUserName`
