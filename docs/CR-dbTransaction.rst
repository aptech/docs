
dbTransaction
==============================================

Purpose
----------------

Begins a transaction on the database.

Format
----------------
.. function:: ret = dbTransaction(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: **ret** (*scalar*) - 1 to indicate success and a 0 if the transaction fails.
    
Examples
----------------

::

    // If 'dbTransaction' succeeds
    if dbTransaction(db_id);
        // All queries must succeed, or all fail.
        if not dbExecQuery(db_id,
            "INSERT INTO TEST...");
            dbRollback(db_id);
            errorlog("Query 1 failed");
            end;
        endif;

        if not dbExecQuery(db_id,
            "INSERT INTO TEST...");
            dbRollback(db_id);
            errorlog("Query 2 failed");
            end;
        endif;

        dbCommit(db_id);
    endif;

Remarks
-------

This function can only be used with databases that support transactions.

.. seealso:: Functions :func:`dbCommit`, :func:`dbRollback`
