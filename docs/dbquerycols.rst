
dbQueryCols
==============================================

Purpose
----------------

Returns the number of fields in the record.

Format
----------------
.. function:: num_fields = dbQueryCols(qid)

    :param qid: query number.
    :type qid: scalar

    :return num_fields: number of fields.

    :rtype num_fields: scalar

Examples
----------------

::

    // Execute a query
    qid = dbExecQuery(db_id, "SELECT id, name, price FROM products");

    // Get the number of fields in the result set
    num_fields = dbQueryCols(qid);

    // Should print 3
    print (num_fields);

