
dbQueryIsSelect
==============================================

Purpose
----------------

Reports whether the specified query is a ``SELECT`` statement.

Format
----------------
.. function:: ret = dbQueryIsSelect(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 if the query is a ``SELECT`` statement or 0 otherwise.

    :type ret: scalar

Examples
----------------

::

    // Execute query
    qid = dbExecQuery(db_id, "SELECT *
        FROM PEOPLE");

    // Check whether `qid` query is a `SELECT` statement
    dbQueryIsSelect(qid); // True

    // Execute new query
    qid = dbExecQuery(db_id, "INSERT INTO
        PEOPLE (fname, lname) VALUES
        ('John', 'Doe');");

    // Re-check whether `qid` query is a `SELECT` statement
    dbQueryIsSelect(qid); // False
