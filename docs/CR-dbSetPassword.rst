
dbSetPassword
==============================================

Purpose
----------------

Sets the database connection's password.

Format
----------------
.. function:: dbSetPassword(db_id, pswd)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param pswd: password for database.
    :type pswd: string



Remarks
-------

This function must be called before the connection is opened with
dbOpen() to have an effect.

