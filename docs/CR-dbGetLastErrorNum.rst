
dbGetLastErrorNum
==============================================

Purpose
----------------

Returns information about the last error that occurred on the database.

Format
----------------
.. function:: last_error = dbGetLastErrorNum(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return last_error: number of last error on the specified database.

    :rtype last_error: scalar

