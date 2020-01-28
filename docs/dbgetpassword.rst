
dbGetPassword
==============================================

Purpose
----------------

Returns a connection's password.

Format
----------------
.. function:: db_password = dbGetPassword(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return db_password: Contains the password for the specified database connection or a null string.

    :rtype db_password: string

Remarks
-------

:func:`dbGetPassword` will only return passwords set with :func:`dbSetPassword`.
