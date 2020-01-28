
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
