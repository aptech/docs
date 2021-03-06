
dbQueryGetPosition
==============================================

Purpose
----------------

Returns the current internal position of the query.

Format
----------------
.. function:: index = dbQueryGetPosition(qid)

    :param qid: query number.
    :type qid: scalar

    :return index: query position

    :rtype index: scalar

Examples
----------------

::

    // Create and prepare query
    qid = dbCreateQuery(db_id, "SELECT *
        FROM PEOPLE");

    // Print record positions
    do while dbQuerySeekNext(qid);
        print "Current index = "
        dbQueryGetPosition(qid);
    endo;

Remarks
-------

The first record is at position zero. If the position is invalid, the
function returns `DB_BEFORE_FIRST_ROW` (-1) or `DB_AFTER_LAST_ROW` (-2), which are
special negative values.


