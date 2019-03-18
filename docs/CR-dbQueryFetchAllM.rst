
dbQueryFetchAllM
==============================================

Purpose
----------------

		Returns the result set for the current query as a matrix. 

Format
----------------
.. function:: dbQueryFetchAllM(qid) 
			   
			  dbQueryFetchAllM(qid, columns)

    :param qid: query number.
    :type qid: scalar

    :param columns: specific columns to pull out from result matrix.
        Must be a subset of fields from SELECT statement.
    :type columns: string or string array

    :returns: result (*matrix*), the result set; or if the result set is empty, a scalar error code.

Examples
----------------

qid = dbExecQuery(db_id, "SELECT * FROM GDP");

gdp = dbQueryFetchAllM(qid);
				
// If 'gdp' is a scalar error code    
if scalmiss(gdp);
     print "No results";
else;
     // do something with gdp
endif;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

qid = dbExecQuery(db_id, "SELECT * FROM 
     PEOPLE WHERE COUNTRY = ?", "USA");

// specify zipcode as column of interest
zipcodes = dbQueryFetchAllM(qid, "ZIPCODE"); 

if not scalmiss(zipcodes);
    print "zip codes = " zipcodes;
endif;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. seealso:: Functions :func:`dbQueryFetchAllSA`, :func:`dbQueryFetchOneM`, :func:`dbQueryFetchOneSA`
