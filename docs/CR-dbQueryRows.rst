
dbQueryRows
==============================================

Purpose
----------------

Returns the size of the result (number of rows returned), or -1 if the size 
cannot be determined or if the database does not support reporting information 
about query sizes.

Format
----------------
.. function:: dbQueryRows(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: result_size (*scalar*), number of rows in the current result set of the active query. If the number of rows cannot be determined a -1 is returned.

Examples
----------------

::

    // Given a table with US States.
    qid = dbCreateQuery(db_id, "SELECT * 
        FROM STATES");
    
    count = dbQueryRows(qid); // count = 50

