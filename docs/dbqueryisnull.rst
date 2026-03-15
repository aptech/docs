
dbQueryIsNull
==============================================

Purpose
----------------

Returns 1 if the query is active, positioned on a valid record and the
field is ``NULL``; otherwise returns 0.

Reports whether the current field pointed at by an active query positioned on
a valid record is ``NULL``.

Format
----------------
.. function:: ret = dbQueryIsNull(qid, field)

    :param qid: query number.
    :type qid: scalar

    :param field: index into result set.
    :type field: scalar

    :return ret: 1 if the field is ``NULL`` or 0 otherwise.

    :rtype ret: scalar

Remarks
-------

Note that for some drivers, :func:`dbQueryIsNull` will not return accurate
information until after an attempt is made to retrieve data.

Examples
----------------

::

    // Execute a query
    qid = dbExecQuery(db_id, "SELECT name, email FROM customers");

    // Move to the first record
    dbQuerySeekNext(qid);

    // Check if the second field (email) is NULL
    if dbQueryIsNull(qid, 2);
        print "Email field is NULL";
    endif;

.. seealso:: Functions :func:`dbQueryIsActive`, :func:`dbQueryIsValid`
