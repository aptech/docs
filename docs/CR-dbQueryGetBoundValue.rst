
dbQueryGetBoundValue
==============================================

Purpose
----------------

Returns the value for a placeholder in a query.

Format
----------------
.. function:: dbQueryGetBoundValue(qid, placeholder)

    :param qid: query number.
    :type qid: scalar

    :param placeholder: Oracle style (:value_name) or index of ODBC style (?) placeholder.
    :type placeholder: string

    :returns: val (*string*), bound value if previously set.

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
    
    print "Name = ";; 
    print dbQueryGetBoundValue(qid, ":fname");; 
    print dbQueryGetBoundValue(qid, ":lname");

::

    db_id = dbAddDatabase("MYSQL");
    string args = { "John", "Doe" };
    qid = dbCreateQuery(db_id, "SELECT * FROM 
        PEOPLE WHERE FIRST = ? AND LAST = ?", args);
    
    print "Name = ";;  
    print dbQueryGetBoundValue(qid, 1);; 
    print dbQueryGetBoundValue(qid, 2);

results in

::

    Name = John Doe

