
dbSetPort
==============================================

Purpose
----------------

Sets the specified database connection's port number.

Format
----------------
.. function:: dbSetPort(db_id, port_num)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param port_num: port number for database connection to use.
    :type port_num: scalar

Remarks
-------

This function must be called before the connection is opened with
:func:`dbOpen` to have an effect.

.. seealso:: :func:`dbGetPort`

