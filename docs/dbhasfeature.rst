
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

    :param feature:
    :type feature: string

        - DB_TRANSACTIONS
        - DB_QUERY_SIZE
        - DB_BLOB
        - DB_UNICODE
        - DB_PREPARED_QUERIES
        - DB_NAMED_PLACEHOLDERS
        - DB_POSITIONAL_PLACEHOLDERS
        - DB_LAST_INSERT_ID
        - DB_BATCH_OPERATIONS
        - DB_SIMPLE_LOCKING
        - DB_LOW_PRECISION_NUMBERS
        - DB_EVENT_NOTIFICATIONS
        - DB_FINISH_QUERY
        - DB_MULTIPLE_RESULT_SETS

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
    if dbHasFeature(db_id, "NamedPlaceholders");
         dbQueryPrepare(qid, "SELECT * FROM GDP
                             WHERE COUNTRY = :country");
         dbQueryBindValue(qid, ":country", "USA");
    else;
         dbQueryPrepare(qid, "SELECT * FROM GDP
                             WHERE COUNTRY = ?");
         dbQueryAddBindValue(qid, "USA");
    endif;

    dbQueryExecPrepared(qid);

Remarks
-------

Note that some databases need to be opened with :func:`dbOpen` before this can
be determined.