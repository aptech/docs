
dbQueryBindValue
==============================================

Purpose
----------------

Set the placeholder placeholder to be bound to value val in the prepared statement. 
Note that the placeholder mark (e.g ``:``) must be included when specifying the placeholder name.

Format
----------------
.. function:: dbQueryBindValue(qid, placeholder, val)

    :param qid: query number.
    :type qid: scalar

    :param placeholder: Oracle style (``:value_name``) or index of ODBC style (``?``) placeholder.
    :type placeholder: string

    :param val: the value to be bound.
    :type val: valid type

Remarks
-------

Values cannot be bound to multiple locations in the query.


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
    dbQueryExecPrepared(qid);

