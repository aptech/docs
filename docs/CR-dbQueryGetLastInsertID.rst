
dbQueryGetLastInsertID
==============================================

Purpose
----------------

Returns the object ID of the most recent inserted row if supported by the database.

Format
----------------
.. function:: dbQueryGetLastInsertID(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: last_insert (*scalar*), object id

Examples
----------------

::

    // Given NAMES is an empty MySQL 
    // table with the *id* column 
    // auto-incrementing.
    db_id = dbAddDatabase("MYSQL");
    qid = dbCreateQuery(db_id, "INSERT 
        INTO NAMES (first, last) VALUES 
        ('John', 'Doe');");
    
    if dbHasFeature(db_id, "LastInsertId");
        last_id = dbQueryGetLastInsertID(qid); 
    endif;

.. seealso:: Functions :func:`dbHasFeature`
