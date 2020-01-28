
dbQueryIsValid
==============================================

Purpose
----------------

Reports whether the specified query is positioned on a valid record.

Format
----------------
.. function:: ret = dbQueryIsValid(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 if the query is positioned on a valid record or 0 otherwise.

    :rtype ret: scalar

Examples
----------------

::

    // Execute query
    qid = dbExecQuery(db_id, "SELECT * FROM
         PEOPLE");

    // Check if query is valid
    dbQueryIsValid(qid); // False

    // Give it a valid position
    dbQuerySeekFirst(qid);

    // Iterate until no longer valid.
    do while dbQueryIsValid(qid);
        // dbQueryIsValid = True
        dbQuerySeekNext(qid);
    endo;

    dbQueryIsValid(qid); // False
