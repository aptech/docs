
dbQueryFetchOneSA
==============================================

Purpose
----------------

			Returns a single row as a string vector containing the field information for the current query. 

Format
----------------
.. function:: dbQueryFetchOneSA(qid, columns)

    :param qid: query number.
    :type qid: scalar

    :param columns: specific columns to pull from the result matrix. Must be a subset of fields from the SELECT statement.
    :type columns: string or string array

    :returns: record (*string array*), if the query points to a valid row
        
        (dbQueryIsValid() returns
        true), the record is populated with the row's values. An empty
        
        record (scalmiss(record) is true) is
        returned when there is no active query dbQueryIsActive()
        
        returns false).

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
