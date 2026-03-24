
dbQueryIsForwardOnly
==============================================

Purpose
----------------

Reports whether you can only scroll forward through a result set.

Format
----------------
.. function:: ret = dbQueryIsForwardOnly(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 if the result set can only be scrolled through forward, otherwise a 0.

    :rtype ret: scalar

Remarks
-------

Setting a query to "forward only" will usually improve performance. By
default, queries are created with "forward only" on.

Examples
----------------

::

    // Execute a query
    qid = dbExecQuery(db_id, "SELECT * FROM products");

    // Check if the result set is forward-only
    if dbQueryIsForwardOnly(qid);
        print "Forward-only mode is enabled";
    else;
        print "Bidirectional scrolling is allowed";
    endif;

.. seealso:: Functions :func:`dbQuerySetForwardOnly`, :func:`dbQuerySeekNext`
