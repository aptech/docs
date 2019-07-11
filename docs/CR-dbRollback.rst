
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

    :returns: **ret** (*scalar*) - 1 to indicate success and a 0 if the rollback fails.

Remarks
-------

A rollback is only possible if the SQL driver supports transactions and
a :func:`dbTransaction` has been started.

.. Note:: For some databases, the rollback will fail and return 0 if there is an active query using the database for a ``SELECT``. Make the query inactive before doing the rollback.

Call :func:`dbGetLastError` to get information about errors.
