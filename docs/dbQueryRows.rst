
dbQueryRows
==============================================

Purpose
----------------

Returns the size of the result (number of rows returned), or -1 if the size
cannot be determined or if the database does not support reporting information
about query sizes.

Format
----------------
.. function:: result_size = dbQueryRows(qid)

    :param qid: query number.
    :type qid: scalar

    :return result_size: number of rows in the current result set of the active query. If the number of rows cannot be determined a -1 is returned.

    :rtype result_size: scalar

Examples
----------------

::

    // Given a table with US States.
    qid = dbCreateQuery(db_id, "SELECT *
        FROM STATES");

    count = dbQueryRows(qid); // count = 50

Remarks
-------

Note that if the query is not active or if the query is not a ``SELECT``
statement, a -1 is returned. These properties can be checked with
:func:`dbQueryIsActive` or :func:`dbQueryIsSelect`.


