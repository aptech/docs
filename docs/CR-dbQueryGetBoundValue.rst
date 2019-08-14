
dbQueryGetBoundValue
==============================================

Purpose
----------------

Returns the value for a placeholder in a query.

Format
----------------
.. function:: val = dbQueryGetBoundValue(qid, placeholder)

    :param qid: query number.
    :type qid: scalar

    :param placeholder: Oracle style (``:value_name``) or index of ODBC style (``?``) placeholder.
    :type placeholder: string

    :returns: **val** (*string*) - bound value if previously set.

Examples
----------------

::

    // Add `MYSQL` to list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Create and prepare `qid` query
    qid = dbCreateQuery(db_id);
    dbQueryPrepare(qid, "SELECT * FROM
        PEOPLE WHERE FIRST = :fname AND
        LAST = :lname");

    // Set `:fname` placeholder
    dbQueryBindValue(qid, ":fname", "John");

    // Set `:lname` placeholder
    dbQueryBindValue(qid, ":lname", "Doe");

    /*
    ** Print placeholders for `:fname` and `:lname`
    ** using value names
    */
    print "Name = ";;
    print dbQueryGetBoundValue(qid, ":fname");
    print dbQueryGetBoundValue(qid, ":lname");

or

::

    // Add `MYSQL` to list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Create and prepare query
    string args = { "John", "Doe" };
    qid = dbCreateQuery(db_id, "SELECT * FROM
        PEOPLE WHERE FIRST = ? AND LAST = ?", args);

    /*
    ** Print placeholders for `:fname` and `:lname`
    ** using indices
    */
    print "Name = ";;
    print dbQueryGetBoundValue(qid, 1);
    print dbQueryGetBoundValue(qid, 2);

results in

::

    Name = John Doe
