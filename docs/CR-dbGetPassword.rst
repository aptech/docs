
dbGetPassword
==============================================

Purpose
----------------

Returns a connection's password.

Format
----------------
.. function:: dbGetPassword(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: **db_password** (string) - Contains the password for the specified database connection or a null string.


Remarks
-------

:func:`dbGetPassword` will only return passwords set with :func:`dbSetPassword`.
