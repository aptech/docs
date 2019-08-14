
dbQuerySeekNext
==============================================

Purpose
----------------

Retrieves the next record in the result, if available, and positions the query
on the retrieved record.

Format
----------------
.. function:: ret = dbQuerySeekNext(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: **ret** (*scalar*) - if the record could not be retrieved, the result is positioned after the last record and 0 is returned. If the record is successfully retrieved, 1 is returned.

Remarks
-------

Note that the result must be in the active state before calling this
function or it will do nothing and return 0. You can verify the status
of the query with :func:`dbQueryIsSelect`.

The following rules apply:

.. csv-table::
    :widths: auto

    "**Result location**","**Action taken**"
    "Before the first record","An attempt is made to retrieve
    the first record."
    "After the last record","There is no
    change and 0 is returned."
    "Somewhere between first and last record", "An attempt is made to
    retrieve the next record."

Examples
----------------

::

    // Create and prepare query
    qid = dbCreateQuery(db_id, "SELECT * FROM PEOPLE");

    do while dbQuerySeekNext(qid);
        row = dbQueryFetchOneSA(qid);
        /*
        ** Or dbQueryFetchOneM(qid) if data
        ** is numeric
        */
    endo;

.. seealso:: Functions :func:`dbQuerySeekFirst`, :func:`dbQuerySeekLast`, :func:`dbQuerySeekPrevious`, :func:`dbQuerySeek`, :func:`dbQueryGetPosition`
