
dbQueryGetLastInsertID
==============================================

Purpose
----------------

Returns the object ID of the most recent inserted row if supported by the database.

Format
----------------
.. function:: last_insert = dbQueryGetLastInsertID(qid)

    :param qid: query number.
    :type qid: scalar

    :return last_insert: object id

    :rtype last_insert: scalar

Remarks
-------

If more than one row was touched by the insert, the behavior is undefined.

For MySQL databases the row's auto-increment field will be returned.

With a PSQL database, the table must contain OID's which were not
created by default. Check the *default_with_oids* configuration variable
to be sure.


Examples
----------------

::

    /*
    ** Given NAMES is an empty MySQL
    ** table with the *id* column
    ** auto-incrementing.
    */
    // Add `MYSQL` to list of database connections
    db_id = dbAddDatabase("MYSQL");

    // Create and prepare query
    qid = dbCreateQuery(db_id, "INSERT
        INTO NAMES (first, last) VALUES
        ('John', 'Doe');");

    /*
    ** Check if database supports ID of last
    ** inserted row
    */
    if dbHasFeature(db_id, "LastInsertId");

        // Get ID of last inserted row
        last_id = dbQueryGetLastInsertID(qid);
        
    endif;

.. seealso:: Functions :func:`dbHasFeature`
