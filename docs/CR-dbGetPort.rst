
dbGetPort
==============================================

Purpose
----------------

Returns the database connection's port number if it has been set.

Format
----------------
.. function:: dbGetPort(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: **db_port** (*scalar*) - the port number of the specified database connection.

Remarks
-------

:func:`dbGetPort` will only return the port number if it was previously set
with :func:`dbSetPort`.
