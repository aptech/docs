
dbQueryGetBoundValues
==============================================

Purpose
----------------

Returns an Nx2 string array containing the placeholders and their corresponding values in a query.

Format
----------------
.. function:: bound_values = dbQueryGetBoundValues(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: **bound_values** (*Nx2 string array*) - The first column contains the placeholders and the second column contains the corresponding values.

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

    // Print all `qid` placeholders
    print "Vars = " dbQueryGetBoundValues(qid);

will print

::

    Vars =
       :fname   John
       :lname   Doe
