
dbRollback
==============================================

Purpose
----------------

Rolls back a transaction on the database.

Format
----------------
.. function:: dbRollback(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: ret (*scalar*), 1 to indicate success and a 0 if the rollback fails.

