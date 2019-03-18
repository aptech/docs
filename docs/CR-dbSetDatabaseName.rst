
dbSetDatabaseName
==============================================

Purpose
----------------
Sets the connection's database name to name. To have effect, the database name must be set before the connection is opened. Alternatively, you can dbClose() the connection, set the database name, and call dbOpen() again.

Format
----------------
.. function:: dbSetDatabaseName(db_id, database_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param database_name: database name to apply to specified database connection.
    :type database_name: string

