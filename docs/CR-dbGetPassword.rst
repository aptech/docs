
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

    :returns: db_password (string), containing the password for the specified database connection or a null string.



Remarks
-------

dbGetPassword() will only return passwords set with dbSetPassword().

