
dbSetHostName
==============================================

Purpose
----------------

Sets the specified database connection's host name.

Format
----------------
.. function:: dbSetHostName(db_id, host_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param host_name: the name to assign to the connection's host name.
    :type host_name: string

Remarks
-------

For this function to have an effect, it must be called before the
database connection is opened with :func:`dbOpen`.
