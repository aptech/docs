
dbQueryGetBoundValues
==============================================

Purpose
----------------

Returns an Nx2 string array containing the placeholders and their corresponding values in a query.

Format
----------------
.. function:: dbQueryGetBoundValues(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: bound_values (*TODO*), Nx2 string array. The first column contains the placeholders and the second column contains the corresponding values.

Examples
----------------

::

    db_id = dbAddDatabase("MYSQL");
    qid = dbCreateQuery(db_id);
    dbQueryPrepare(qid, "SELECT * FROM
         PEOPLE WHERE FIRST = :fname AND
         LAST = :lname");
    dbQueryBindValue(qid, ":fname", "John");
    dbQueryBindValue(qid, ":lname", "Doe");
    
    print "Vars = " dbQueryGetBoundValues(qid);

will print

::

    Vars =
       :fname   John
       :lname   Doe

