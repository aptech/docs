
dbSetUserName
==============================================

Purpose
----------------

Sets the specified database connection's user name.

Format
----------------
.. function:: dbSetUserName(db_id, user_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param user_name: user name to apply to specified database connection.
    :type user_name: string

Remarks
-------

This function must be called before the connection is opened with
:func:`dbOpen` to have an effect.

.. seealso:: :func:`dbGetUserName`

