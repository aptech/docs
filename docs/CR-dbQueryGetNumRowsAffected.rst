
dbQueryGetNumRowsAffected
==============================================

Purpose
----------------

Reports the number of rows affected by the result's SQL statement.

Format
----------------
.. function:: num_rows = dbQueryGetNumRowsAffected(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: **num_rows** (*scalar*) - the number of rows affected by the result's SQL statement, or
        a -1 if it cannot be determined or the query is not active.

Remarks
-------

Note that for ``SELECT`` statements, the value is undefined; use :func:`dbQueryRows` instead.


Examples
----------------

::

    // Create and prepare query
    qid = dbCreateQuery(db_id, "INSERT INTO
         PEOPLE (fname, lname) VALUES
         ('John', 'Doe');");

    // Print report of number of rows affected
    print dbQueryGetNumRowsAffected(qid) " row(s) were affected";

::

    1 row(s) were affected

.. seealso:: Functions :func:`dbQueryRows`, :func:`dbHasFeature`
