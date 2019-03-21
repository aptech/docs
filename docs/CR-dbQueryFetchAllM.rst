
dbQueryFetchAllM
==============================================

Purpose
----------------

Returns the result set for the current query as a matrix. 

Format
----------------
.. function:: dbQueryFetchAllM(qid[, columns]) 

    :param qid: query number.
    :type qid: scalar

    :param columns: specific columns to pull out from result matrix. Must be a subset of fields from ``SELECT`` statement.
    :type columns: string or string array

    :returns: result (*matrix*), the result set; or if the result set is empty, a scalar error code.

Remarks
-------

For string results, or to treat numerical results as strings, use
:func:`dbQueryFetchAllSA` to return a string array.

This function retrieves all rows at once. You can process rows in an
iterative manner by using the :func:`dbQueryFetchOneM` and
:func:`dbQueryFetchOneSA` functions.


Examples
----------------

Example 1
+++++++++

..

    qid = dbExecQuery(db_id, "SELECT * FROM GDP");
    
    gdp = dbQueryFetchAllM(qid);
    				
    // If 'gdp' is a scalar error code    
    if scalmiss(gdp);
         print "No results";
    else;
         // do something with gdp
    endif;

Example 2
+++++++++

::

    qid = dbExecQuery(db_id, "SELECT * FROM 
         PEOPLE WHERE COUNTRY = ?", "USA");
    
    // specify zipcode as column of interest
    zipcodes = dbQueryFetchAllM(qid, "ZIPCODE"); 
    
    if not scalmiss(zipcodes);
        print "zip codes = " zipcodes;
    endif;

.. seealso:: Functions :func:`dbQueryFetchAllSA`, :func:`dbQueryFetchOneM`, :func:`dbQueryFetchOneSA`

