
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

    :type user_name: string

.. seealso:: Functions :func:`dbSetUserName`
