
dbCommit
==============================================

Purpose
----------------

Commits a transaction to the database if the driver supports transactions and a :func:`dbTransaction` has been started.

Format
----------------
.. function:: dbCommit(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: ret (*scalar*), 1 for success or 0 for failure.

Examples
----------------

::

    db_id = dbAddDatabase("SQLITE");
    dbExecQuery(db_id, "INSERT INTO PEOPLE 
        (first, last) VALUES ('John', 'Doe');");
    dbCommit(db_id);
    dbClose(db_id);

Remarks
-------

Note: For some databases, the commit will fail and return 0 if there is
an active query using the database for a ``SELECT`` statement. Make the
query inactive before doing the commit to resolve this problem.

Call :func:`dbGetLastError` to get information about errors.

