
dbQueryGetLastErrorText
==============================================

Purpose
----------------

Returns error information about the last error that occurred (if any) with the last executed query.

Format
----------------
.. function:: err_txt = dbQueryGetLastErrorText()

    :return err_txt: database and driver text of last error.

    :rtype err_txt: 2x1 string array

Remarks
-------

Because a failed query will not have a valid handle (*id*), this function
retrieves stored error information about the last executed query.

Examples
----------------

::

    // Execute a query
    qid = dbExecQuery(db_id, "SELECT * FROM nonexistent_table");

    // Get the error text for the last failed query
    err_txt = dbQueryGetLastErrorText();
    print err_txt;

.. seealso:: :func:`dbQueryGetLastErrorNum`
