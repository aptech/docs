
dbHasFeature
==============================================

Purpose
----------------

Returns a 1 if the database supports the specified feature.

Format
----------------
.. function:: ret = dbHasFeature(db_id, feature)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param feature: one of the following predefined scalars:

        .. list-table::
            :widths: auto
            :header-rows: 1

            * - Supported
              - Define
              - Description
            * - Yes
              - DB_TRANSACTIONS
              - Whether the driver supports SQL transactions.
            * - Yes
              - DB_QUERY_SIZE
              - Whether the database is capable of reporting the size of a query. Note that some databases do not support returning the size (i.e. number of rows returned) of a query. This can affect the performance when fetching results using functions like :func:`dbQueryFetchAllM` or :func:`dbQueryFetchAllSA`
            * - No
              - DB_BLOB
              - Whether the driver supports Binary Large Object fields.
            * - No
              - DB_UNICODE
              - Whether the driver supports Unicode strings if the database server does.
            * - Yes
              - DB_PREPARED_QUERIES
              - Whether the driver supports prepared query execution.
            * - Yes
              - DB_NAMED_PLACEHOLDERS
              - Whether the driver supports the use of named placeholders.
            * - Yes
              - DB_POSITIONAL_PLACEHOLDERS
              - Whether the driver supports the use of positional placeholders.
            * - Yes
              - DB_LAST_INSERT_ID
              - Whether the driver supports returning the Id of the last touched row.
            * - Yes
              - DB_BATCH_OPERATIONS
              - Whether the driver supports batched operations, see :func:`dbExecQueries`.
            * - Yes
              - DB_SIMPLE_LOCKING
              - Whether the driver disallows a write lock on a table while other queries have a read lock on it.
            * - Yes
              - DB_LOW_PRECISION_NUMBERS
              - Whether the driver allows fetching numerical values with low precision.
            * - No
              - DB_EVENT_NOTIFICATIONS
              - Whether the driver supports database event notifications.
            * - Yes
              - DB_FINISH_QUERY
              - Whether the driver can do any low-level resource cleanup when :func:`dbQueryFinish` is called.
            * - No
              - DB_MULTIPLE_RESULT_SETS
              - Whether the driver can access multiple result sets returned from batched statements or stored procedures.
            * - No
              - DB_CANCEL_QUERY
              - Whether the driver allows cancelling a running query.

    :type feature: scalar

    :return ret: 1 if the database supports the specified
        feature, or 0 if not.

    :rtype ret: scalar

Examples
----------------

::

    // Set database connection index number
    db_id = dbAddDatabase("MYSQL");

    // Create empty query
    qid = dbCreateQuery(db_id);

    /*
    ** Use dbHasFeature to set up a
    ** conditional query
    */
    if dbHasFeature(db_id, DB_NAMED_PLACEHOLDERS);
         dbQueryPrepare(qid, "SELECT * FROM GDP WHERE COUNTRY = :country");
         dbQueryBindValue(qid, ":country", "USA");
    else;
         dbQueryPrepare(qid, "SELECT * FROM GDP WHERE COUNTRY = ?");
         dbQueryAddBindValue(qid, "USA");
    endif;

    dbQueryExecPrepared(qid);

Remarks
-------

Note that some databases need to be opened with :func:`dbOpen` before this can
be determined.

