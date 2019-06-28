
dbGetLastErrorNum
==============================================

Purpose
----------------

Returns information about the last error that occurred on the database.

Format
----------------
.. function:: dbGetLastErrorNum(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: **last_error** (*scalar*) - number of last error on the specified database.
