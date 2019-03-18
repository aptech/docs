
dbQueryFetchOneM
==============================================

Purpose
----------------

Returns a single row as an Nx1 matrix where N is the column count of the SELECT statement containing the field information for the current query. 

Format
----------------
.. function:: dbQueryFetchOneM(qid) 
			   
			  dbQueryFetchOneM(qid, columns)

    :param qid: query number.
    :type qid: scalar

    :param columns: specific columns to pull from the result matrix. Must be a subset of fields from the SELECT statement.
    :type columns: string or string array

    :returns: record (*matrix*), if the query points to a valid row (dbQueryIsValid() returns true), the record is populated with the row's values. An empty record (scalmiss(record) is true) is returned when there is no active query (dbQueryIsActive() returns false).

Examples
----------------

::

    qid = dbExecQuery(db_id, "SELECT YTD, 
         TOTAL FROM GDP");
    
    do while dbQuerySeekNext(qid);
       record = dbQueryFetchOneM(qid);
       ytd = record[1];
       total = record[2];
    endo;

.. seealso:: Functions :func:`dbQueryFetchOneSA`, :func:`dbQueryFetchAllM`, :func:`dbQueryFetchAllSA`, :func:`dbQueryGetField`
