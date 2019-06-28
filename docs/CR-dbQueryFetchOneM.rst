
dbQueryFetchOneM
==============================================

Purpose
----------------

Returns a single row as an Nx1 matrix where *N* is the column count of the ``SELECT`` statement containing the field information for the current query.

Format
----------------
.. function:: dbQueryFetchOneM(qid[, columns])

    :param qid: query number.
    :type qid: scalar

    :param columns: specific columns to pull from the result matrix. Must be a subset of fields from the ``SELECT`` statement.
    :type columns: string or string array

    :returns: **record** (*matrix*) - if the query points to a valid row (:func:`dbQueryIsValid` returns true), the record is populated with the row's values. An empty record (:code:`scalmiss(record)` is true) is returned when there is no active query (:func:`dbQueryIsActive` returns false).

Remarks
-------

This function is only useful in an iterative context. You can easily
retrieve all the results at once by using the :func:`dbQueryFetchAllM` and
:func:`dbQueryFetchAllSA` functions.

For string results, or to treat numerical results as a string, using
:func:`dbQueryFetchOneSA` will return a string array.


Examples
----------------

::

    // Execute `qid` query
    qid = dbExecQuery(db_id, "SELECT YTD,
         TOTAL FROM GDP");

    /*
    ** Iteratively retrieve single records
    ** and store as matrix
    */
    do while dbQuerySeekNext(qid);
       record = dbQueryFetchOneM(qid);
       ytd = record[1];
       total = record[2];
    endo;

.. seealso:: Functions :func:`dbQueryFetchOneSA`, :func:`dbQueryFetchAllM`, :func:`dbQueryFetchAllSA`, :func:`dbQueryGetField`
