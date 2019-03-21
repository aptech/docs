
dbQuerySeekLast
==============================================

Purpose
----------------

Retrieves the last record in the result, if available, and positions the query 
on the retrieved record.

Format
----------------
.. function:: dbQuerySeekLast(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*scalar*), returns 1 if successful. If unsuccessful the query position is set to an invalid position and 0 is returned.

Remarks
-------

Note that the result must be in the active state and dbQueryIsSelect()
must return 1 before calling this function or it will do nothing and
return 0.


Examples
----------------

::

    // Given STATES is a table with all 
    // 50 states listed alphabetically
    qid = dbExecQuery(db_id, "SELECT name 
        FROM STATES");
    
    // Move to last state
    ret = dbQuerySeekLast(qid);
    
    //If 'ret' is equal to 0   
    if not  ret;
       print  "dbQuerySeekLast failed";
    else;
       // Print last state: Wyoming   
    print dbQueryFetchOneSA(qid);
    endif;

See also
++++++++

`dbQuerySeekNext <CR-dbQuerySeekNext.html#dbQuerySeekNext>`__\,\ `dbQuerySeekPrevious <CR-dbQuerySeekPrevious.html#dbQuerySeekPrevious>`__\,\ `dbQuerySeekFirst <CR-dbQuerySeekFirst.html#dbQuerySeekFirst>`__\,\ `dbQuerySeek <CR-dbQuerySeek.html#dbQuerySeek>`__\,\ `dbQueryGetPosition <CR-dbQueryGetPosition.html#dbQueryGetPosition>`__
