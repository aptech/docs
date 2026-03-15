
dbQuerySeekPrevious
==============================================

Purpose
----------------
Retrieves the previous record in the result, if available, and positions the query on the retrieved record.

Format
----------------
.. function:: ret = dbQuerySeekPrevious(qid)

    :param qid: query number.
    :type qid: scalar

    :return ret: 1 if the record is successfully retrieved. If the record could not be retrieved, the result is positioned before the first record and 0 is returned.

    :rtype ret: scalar

Remarks
-------

Note that the result must be in the active state before calling this
function or it will do nothing and return false. The state of the query
can be verified with :func:`dbQueryIsSelect`.

The following rules apply:

    If the result is currently located before the first record, there is no
    change and 0 is returned.

    If the result is currently located after the last record, an attempt is
    made to retrieve the last record.

    If the result is somewhere in the middle, an attempt is made to retrieve
    the previous record.


Examples
----------------

::

    // Execute a query with bidirectional scrolling
    qid = dbExecQuery(db_id, "SELECT name, price FROM products");

    // Move to the first record
    dbQuerySeekNext(qid);

    // Move to the second record
    dbQuerySeekNext(qid);

    // Go back to the first record
    ret = dbQuerySeekPrevious(qid);

    if ret;
        name = dbQueryGetField(qid, 1);
        print name;
    endif;

.. seealso:: Functions :func:`dbQuerySeekFirst`, :func:`dbQuerySeekLast`, :func:`dbQuerySeekNext`, :func:`dbQuerySeek`, :func:`dbQueryGetPosition`
