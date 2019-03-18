
dbQueryFetchAllSA
==============================================

Purpose
----------------

		Returns the result set for the current query as a string array. 

Format
----------------
.. function:: dbQueryFetchAllSA(qid) 
			  dbQueryFetchAllSA(qid, columns)

    :param qid: query number.
    :type qid: scalar

    :param columns: specific columns to pull out from result matrix.
        Must be a subset of fields from SELECT statement.
    :type columns: string or string array

    :returns: result (*string array*), containing the result set for the current query. If the result set is empty, a scalar error code is returned.

Examples
----------------

::

    qid = dbExecQuery(db_id, "SELECT * FROM 
         PEOPLE WHERE COUNTRY = ?", "USA");
    
    // specify names as columns of interest
    names = dbQueryFetchAllSA(qid, 
         "FIRST_NAME"$|"LAST_NAME"); 
    
    // If 'names' is not a scalar error code
    if not scalmiss(names);
        print "People in the USA = " names;
    endif;

.. seealso:: Functions :func:`dbQueryFetchAllM`, :func:`dbQueryFetchNextSA`, :func:`dbQueryFetchNextM`
