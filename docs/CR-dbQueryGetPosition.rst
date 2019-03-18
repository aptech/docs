
dbQueryGetPosition
==============================================

Purpose
----------------

Returns the current internal position of the query.

Format
----------------
.. function:: dbQueryGetPosition(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: index (*scalar*), query position

Examples
----------------

::

    qid = dbCreateQuery(db_id, "SELECT * 
        FROM PEOPLE");
    do while dbQuerySeekNext(qid);
        print "Current index = " 
        dbQueryGetPosition(qid);
    endo;

