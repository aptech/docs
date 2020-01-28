
dbGetLastErrorText
==============================================

Purpose
----------------

Returns information about the last error that occurred on the database.

Format
----------------
.. function:: last_error = dbGetLastErrorText(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return last_error: details of last error on the specified database.

    :rtype last_error: string

