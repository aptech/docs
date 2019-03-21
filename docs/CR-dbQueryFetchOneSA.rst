
dbQueryFetchOneSA
==============================================

Purpose
----------------

Returns a single row as a string vector containing the field information for the current query. 

Format
----------------
.. function:: dbQueryFetchOneSA(qid[, columns])

    :param qid: query number.
    :type qid: scalar

    :param columns: specific columns to pull from the result matrix. Must be a subset of fields from the ``SELECT`` statement.
    :type columns: string or string array

    :returns: record (*string array*), if the query points to a valid row (:func:`dbQueryIsValid` returns
        true), the record is populated with the row's values. An empty record (:code:`scalmiss(record)` is true) is
        returned when there is no active query :func:`dbQueryIsActive` returns false).

Remarks
-------

This function is only useful in an iterative context. You can easily
retrieve all the results at once by using the :func:`dbQueryFetchAllM` and
:func:`dbQueryFetchAllSA` functions.

For numerical only results, using :func:`dbQueryFetchOneM` will return a
matrix instead of a string array.


Examples
----------------

::

    qid = dbExecQuery(db_id, "SELECT COUNTRY, 
        TOTAL FROM GDP");
    do while dbQuerySeekNext(qid);
        record = dbQueryFetchOneSA(qid);
        country = record[1];
        total = record[2];
    endo;

.. seealso:: Functions :func:`dbQueryFetchOneM`, :func:`dbQueryFetchAllM`, :func:`dbQueryFetchAllSA`, :func:`dbQueryGetField`

